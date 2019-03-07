import napalm
import sys
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from optparse import OptionParser
from datetime import datetime

sys.path.append('../')

from config import config

########################################################################

#####################################
######## Read inventory file
#####################################
def read_inventory(file_path):

    data_loader = DataLoader()
    inventory = InventoryManager(loader = data_loader, sources=[file_path])

    devices = inventory.list_hosts()

    return (devices)


#####################################
######## Push configuration to the network
#####################################
def push_config (configuration,net_device,username,password):

    # Use the appropriate network driver to connect to the device:
    driver = napalm.get_network_driver('ios')
    # Define device connection:
    device = driver(hostname=str(net_device), username=username, password=password, optional_args={'port': config.ssh_port})
    # Open connection
    print('Opening '+str(net_device)+' ...')
    device.open()

    # Backing Up Config
    print('Backing UP Config ...')
    backup = device.get_config(retrieve=u'running')
    file_date = datetime.now().strftime("%Y-%m-%d_%H-%M")
    f = open("backup/"+str(net_device)+"-backup-"+file_date+".cfg", "w")
    f.write(str(backup['running']))
    f.close
    # Push config to candidate config
    device.load_merge_candidate(filename=configuration)

    # Note that the changes have not been applied yet. Before applying the configuration you can check the changes:
    print('\nDiff:')
    print(device.compare_config())

    # You can commit or discard the candidate changes.
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice.lower() == 'y' or choice.lower() == 'yes':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()

    # close the session with the device.
    device.close()
    print('Done.')



    return


#####################################
######## MAIN Function
#####################################
def main ():

    parser = OptionParser(usage="usage: %prog -t [template file] [options]", version="%prog 1.0")
    parser.add_option("-t", "--template",action="store", dest="template", default=False, help="Specify Template file to push.")
    parser.add_option("-i", "--inventory", action="store", dest="inventory", default=False, help="Specify Inventory file to use. Default is inventory defined in config file")
    parser.add_option("-d", "--device", action="store", dest="device", default=False, help="Specify Device IP/Hostname to connect.")
    parser.add_option("-u", "--user", action="store", dest="user", default=False, help="Specify Username for device connection.")
    parser.add_option("-p", "--password", action="store", dest="password", default=False, help="Specify Password for device connection.")
    parser.add_option("-m", "--module", action="store", dest="module", default=False, help="Specify module to use. If unsure use keyword \"LIST\" to list available modules.")

    options, args = parser.parse_args()

    if not options.template:
        parser.error("Required arguments have not been supplied.\tUse -h to get more information.\n")
        sys.exit()
####
    if not options.inventory:
        devices = read_inventory(config.device_inventory)
    else:
        devices = read_inventory(options.inventory)
####
    if not options.user:
        username = config.net_username
    else:
        username = options.user
####
    if not options.password:
        password = config.net_password
    else:
        password = options.password
####
    if options.device:
        device = options.device
        push_config(options.template,device,username,password)
    else:
        for device in devices:
            push_config(options.template, device, username, password)


    return


#####################################
######## BEGINNING
#####################################
if __name__ == '__main__':
    main()