#!/bin/bash
#################################################################################
#
# This script is for setting route for the 5G labkit, and should be run after the 
# core is deployed
#
################################################################################

# Add the route for imcoming packets going to 5G network (12.1.1.X) to the UPF container (192.168.70.134)
sudo route add -net 12.1.1.0/24 gw 192.168.70.134


# Add the route for outgoing packets that go to the 10.200.X.X/8 LAN to the enps06 interface (10.200.0.10) 
#sudo route add -net 10.200.0.0/8 gw 10.200.0.10 metric 10

# Block the firewall in order to allow ip forwarding
sudo  sysctl net.ipv4.conf.all.forwarding=1
sudo iptables -P FORWARD ACCEPT
