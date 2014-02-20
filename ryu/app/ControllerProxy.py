'''
Created on 18/02/2014

@author: Niklas Rehfeld
'''
from ryu.base.app_manager import RyuApp
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER, CONFIG_DISPATCHER, HANDSHAKE_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3, ofproto_v1_4
from ryu.lib.dpid import dpid_to_str



class ControllerProxy(RyuApp):
    '''
    Forwards all of the OpenFlow packets to another Controller.
    '''

    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION, ofproto_v1_4.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(ControllerProxy, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPHello, HANDSHAKE_DISPATCHER)
    def handshake_handler(self, event):
        ''' Handles Hello (Handshake) messages. '''
        print "Hello"
        print event.msg
        print "DPID %s" % event.msg.datapath.id

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def features_handler(self, event):
        '''
        This will only have traffic in OF v1.3+ I think, as older
        versions just send a PacketIn.
        '''
        print "Switch Features"
        print event.msg.msg_type
        print "Protocol %s" % event.msg.datapath.ofproto
        print "dpid %s " % event.msg.datapath.id
        
