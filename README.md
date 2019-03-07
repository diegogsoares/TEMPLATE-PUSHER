# TEMPLATE PUSHER

This project was create with an intent of pushing templates to several network devices at once and save time for setting up new configuration.
This will save remote access connections and time to copy and paste the same config over and over. It can also be used on a recurring basis to keep configuration consistency.

## Getting Started

This folder is structured as following:

backup - Will host all configuration backup taken before committing any changes to any device.

config - Where configuration and inventory files are

templates - Where configuration templates are stored



### Prerequisites

   - MAC, Linux (not supported on Windows)
   - python 3.x
   - pip package manager (https://pip.pypa.io/en/stable/installing/)
```bash
   If already installed, make sure that pip / setuptools are upto date (commands may vary)
   
   pip install --upgrade pip
   
   Ubuntu: sudo pip install --upgrade setuptools
```
   - virtualenv (recommended)
```bash
   Ubuntu: sudo apt-get install python-virtualenv
   Fedora: sudo dnf install python-virtualenv
   MAC: sudo pip install virtualenv
```

### Installing

Clone git repository
```bash
   git clone https://github.com/diegogsoares/TEMPLATE-PUSHER.git
   cd TEMPLATE-PUSHER
   python3 -m pip install -r requirements.txt 
   
```

## Deployment

Edit the config file inside config folder with proper Credentials, Remote Access port numbers and inventory file.

NOTE: all file references should consider the base folder being TEMPLATE-PUSHER. (Ex: config file is config/config.py)
```
device_inventory = "config/inventory.yml"
net_username = "admin"
net_password = "Cisco"
ssh_port = "22"
```

## Running Template Pusher

Use -h option on each script to be presented with help.

Template option is a required option
```
python3 template-pusher.py -t templates/basic-system-settings.cfg
```
You can select a different Inventory file.
```
python3 template-pusher.py -t templates/basic-system-settings.cfg -i config/new-inventory.yml
```
You can select a different Username and Password.
```
python3 template-pusher.py -t templates/basic-system-settings.cfg -u NEW_USER -p NEW_PASSWORD
```
You can select a specific device.

NOTE: If you don't use the -u and -p option the default credentials from the config file will be used.
```
python3 template-pusher.py -t templates/basic-system-settings.cfg -d 10.1.1.1
```

## Built With

* [PyCharm CE](https://www.jetbrains.com/pycharm/) - Python IDE

## Contributing

none

## Authors

* **Diego Soares** - *Initial work* - [diegogsoares](https://github.com/diegogsoares)

See also the list of [contributors] who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* BIG THANK YOU to all my CISCO customers that challenged me with use cases.

