'''
Created on 18/02/2014

@author: Niklas Rehfeld
'''
from ryu.base.app_manager import RyuApp
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER, CONFIG_DISPATCHER, HANDSHAKE_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3, ofproto_v1_4, ofproto_v1_0
from ryu.lib.dpid import dpid_to_str



class ControllerProxy(RyuApp):
    '''
    Forwards all of the OpenFlow packets to another Controller.
    '''

    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION,
                    ofproto_v1_3.OFP_VERSION,
                    ofproto_v1_4.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(ControllerProxy, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPHello, HANDSHAKE_DISPATCHER)
    def handshake_handler(self, event):
        ''' Handles Hello (Handshake) messages. '''
        print "Hello\n"
#        print event.msg.__dict__
#        print "DPID %s" % event.msg.datapath.id

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def features_handler(self, event):
        '''
        This will only have traffic in OF v1.3+ I think, as older
        versions just send a PacketIn.
        '''
#        print event.msg.__dict__
        print "Switch Features"
        print "Message Type %s " % event.msg.msg_type
        print "Protocol %s" % event.msg.datapath.ofproto
        print "dpid %s \n" % event.msg.datapath.id
        
    @set_ev_cls(ofp_event.EventOFPStateChange,
                [CONFIG_DISPATCHER, DEAD_DISPATCHER, MAIN_DISPATCHER])
    def state_change_handler(self, event):
        """
        handles OFPStateCHange packets in DEAD and CONFIG states.
        """
        print "State Change"
        dp = event.datapath.id
        print "state: %s" % event.datapath.state
        if dp != None:
            print "DPID %s \n" % dpid_to_str(event.datapath.id)
        else:
            print "DPID %s \n" % event.datapath.id,
#        print event.datapath.__dict__

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, event):
        """
        Handles PacketIn Events.
        """
        print "PacketIn from %s\n" % event.msg.datapath.id
