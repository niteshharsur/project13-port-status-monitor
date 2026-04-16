# Project 13: Port Status Monitoring Tool using SDN

## Objective
To monitor and detect switch port UP/DOWN status changes using Mininet and POX controller.

## Tools Used
- Ubuntu WSL
- Mininet
- Open vSwitch
- POX Controller
- OpenFlow Protocol

## Topology
- 1 Switch (s1)
- 3 Hosts (h1, h2, h3)

## Commands Used

### Start Controller

cd ~/pox  
python3 pox.py openflow.of_01 forwarding.l2_learning port_monitor

### Start Mininet

sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633

### Test Connectivity

pingall

### Simulate Port Down

link s1 h1 down

### Restore Port

link s1 h1 up

## Results
- Connectivity successful
- Port down detected automatically
- Alert generated when port goes down
- Port up restored successfully
- Current port status displayed

## Conclusion
Successfully implemented port status monitoring in SDN using Mininet and custom POX controller.
