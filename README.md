# TEMPLATE PUSHER

This project was create with an intent of pushing templates to several network devices at once and save time for setting up new configuration.
This will save a lot of repetitive remote access connections to copy and paste the same config. Ita can also be used on a recurring basis to keep configuration consistency.

## Getting Started

This folder is structured as following:

backup - Will host all configuration backup taken before committing any changes to any device.

config - 

templates - 

TEMPLATE


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
   git clone https://github.com/diegogsoares/ISE-API-SCRIPTS.git
   cd ISE-API-SCRIPTS
```

## Deployment

Edit the config file inside config folder with proper ISE IP/Hostname and Credentials.

```
ise_host = "10.10.10.10"
ise_username = "iseUsername"
ise_password = "isePassword"
```

## Running Template Pusher

Use -h option on each script to be presented with help.

Template option is a requid
```
Give an example
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

