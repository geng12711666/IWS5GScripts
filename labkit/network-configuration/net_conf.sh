#!/bin/bash
#################################################################################
#
# This script is for setting network configuration, including ip and  route for 
# the 5G labkit, and should be run after the core is deployed
#
################################################################################

# Turn off the NetworkManager to avoid ip assign conflict
#sudo systemctl stop NetworkManager

### Assign IP for three interfaces (2 sfp port and 1 ethernet port) ###
# sfp port 0 (right port of labkit) for data transmission
sudo ifconfig enp1s0f0 192.168.20.1 netmask 255.255.255.0 mtu 9000 up

# sfp port 1 (right port of labkit) for USRP management
sudo ifconfig enp1s0f1 192.168.30.1 netmask 255.255.255.0 up

# ethernet port for LAN network in the lab (will be connected to the PNI router in the future)
sudo ifconfig enp6s0 10.200.0.10 netmask 255.0.0.0 up


### Routing ###
# Add the route for USRP management data
#sudo route add -net 192.168.30.0/24 dev enp1s0f1

# Add the route for imcoming packets going to 5G network (12.1.1.X) to the UPF container (192.168.70.134)
sudo route add -net 12.1.1.0/24 gw 192.168.70.134


# Add the route for outgoing packets that go to the 10.200.X.X/8 LAN to the enps06 interface (10.200.0.10) 
sudo route add -net 10.0.0.0/8 dev enp6s0

# Block the firewall in order to allow ip forwarding
sudo  sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
