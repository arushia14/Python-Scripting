
# Python program to change the mac address of the device

import subprocess   # For using terminal commands
import optparse     # For passing arguments in the terminals


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter the interface to change the MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        parser.error("Please enter an interface. Use --help for more information.")
    elif not options.new_mac:
        parser.error("Please enter the new MAC address. Use --help for more information.")
    return options


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print(f'Changed the mac address of {interface} to {new_mac}')


options = get_args()
change_mac(options.interface, options.new_mac)


