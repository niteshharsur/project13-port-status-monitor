from pox.core import core
import pox.openflow.libopenflow_01 as of
import datetime

log = core.getLogger()

class PortMonitor(object):

    def __init__(self):
        core.openflow.addListeners(self)
        self.port_state = {}

    def _handle_ConnectionUp(self, event):
        log.info("Switch Connected: %s", event.dpid)

    def _handle_ConnectionDown(self, event):
        log.info("Switch Disconnected: %s", event.dpid)

    def _handle_PortStatus(self, event):
        dpid = event.dpid
        port_no = event.ofp.desc.port_no
        reason = event.ofp.reason
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if reason == of.OFPPR_ADD:
            status = "PORT ADDED"

        elif reason == of.OFPPR_DELETE:
            status = "PORT DELETED"

        elif reason == of.OFPPR_MODIFY:
            if event.ofp.desc.state & of.OFPPS_LINK_DOWN:
                status = "DOWN"
            else:
                status = "UP"
        else:
            status = "UNKNOWN"

        self.port_state[(dpid, port_no)] = status

        log.info("[%s] Switch %s Port %s -> %s",
                 now, dpid, port_no, status)

        if status == "DOWN":
            log.warning("ALERT! Port %s on Switch %s is DOWN",
                        port_no, dpid)

        self.show_status()

    def show_status(self):
        print("\nCurrent Port Status")
        print("-" * 30)

        for (dpid, port), state in self.port_state.items():
            print("Switch %s Port %s : %s" % (dpid, port, state))

        print("-" * 30)

def launch():
    core.registerNew(PortMonitor)
