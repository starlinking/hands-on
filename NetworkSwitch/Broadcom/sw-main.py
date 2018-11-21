#!/usr/bin/env python
#title           :sw-main.py
#description     :A script is used for network automation with Broadcom-like switch
#author          :Star Chang (star@starlinking.com)
#date            :2018.11.15
#version         :0.1
#usage           :python sw-main.py
#notes           :
#python_version  :2.7.5 (Paramiko 2.4.2, Netmiko 2.3.0)  
#==================================================================================
fname = "sw-cfg.txt"
# Import the modules needed to run the script
from netmiko import ConnectHandler
# Use -O(Optimized) to disable debug logging, e.g. python -O sw-main.py 
if __debug__:
    import logging
    logging.basicConfig(filename='sw-debug.log', level=logging.DEBUG)
    logger = logging.getLogger("netmiko")

with open(fname, 'r') as f:
    cmds_to_send = f.read()

a1105 = {
    'device_type': 'ubiquiti_edge', # Broadcom-like Switch
    'ip': '192.168.1.10',           # switch default IP from serviceport
    'username': 'dp',               # default user for DataPlane switch 
    'password': 'live',             # default password for dp account
    'port' : 22,                    # optional, defaults to 22
    'secret':'',                    # no password needed for privilege exec mode
    'fast_cli': 'True',             # Provide a way to optimize for performance
}
net_connect = ConnectHandler(**a1105)
# User EXEC by default
#print(net_connect.find_prompt())
#stdout = net_connect.send_command('show serviceport')
# User EXEC to Privileged EXEC command mode
#net_connect.enable()
#print(net_connect.find_prompt())
#stdout = net_connect.send_command('show ip ssh')
#stdout = net_connect.send_command_timing('show port all')
#if '--More-- or (q)uit' in stdout:
#    stdout += net_connect.send_command_timing('y')
# send_command_timing as the router/switch prompt is not returned
#stdout = net_connect.send_command_timing('show port all', strip_command=False, strip_prompt=False)
#if "confirm" in stdout:
#    stdout += net_connect.send_command_timing(" ", strip_command=False, strip_prompt=False)
# Privileged EXEC to Global Configuration command mode
#stdout = net_connect.send_config_set('snmp-server location QALab')
#stdout = net_connect.send_config_set(['interface 1/0/16','switchport access vlan 100'], exit_config_mode=False)
# issue switch commands based on configuraiton file 
stdout = net_connect.send_command_expect(cmds_to_send)
#stdout = net_connect.send_command_expect(cmds_to_send, delay_factor=3)
print(stdout)
net_connect.disconnect()
