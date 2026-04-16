# Project 13: Port Status Monitoring Tool using SDN

## Objective
To monitor switch port UP/DOWN status using Mininet and POX controller.

## Tools Used
- Ubuntu WSL
- Mininet
- Open vSwitch
- POX Controller

## Topology
- 1 Switch
- 3 Hosts

## Commands Used

### Start Controller
python3 pox.py forwarding.l2_learning

### Start Mininet
sudo mn --topo single,3 --controller remote,ip=127.0.0.1,port=6633

### Test Connectivity
pingall

### Port Down
link s1 h1 down
sh ovs-ofctl show s1

### Port Up
link s1 h1 up
sh ovs-ofctl show s1

## Results
- Connectivity successful
- Port down detected
- Port up restored

## Conclusion
Successfully implemented port status monitoring in SDN.# Project 13: Port Status Monitoring Tool using SDN

## Objective
To monitor and detect switch port status changes (UP/DOWN) in a Software Defined Network using Mininet and POX controller.

---

## Tools Used
- Ubuntu WSL
- Mininet
- Open vSwitch
- POX Controller
- OpenFlow Protocol

---

## Topology Used
- 1 Switch (s1)
- 3 Hosts (h1, h2, h3)

---

## Steps to Run

### Start POX Controller

```bash
cd ~/pox
python3 pox.py forwarding.l2_learning
