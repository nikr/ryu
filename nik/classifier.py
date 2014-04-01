
from ryu.controller.controller import Datapath
from ryu.lib.dpid import dpid_to_str

import logging


LOG = logging.getLogger('nik.classifier')

class OFClassifier(object):
    """ This class is used to manage which messages are sent to which controller."""

    def __init__(self):
        pass

    def classify_from_switch(self, message, dp):
        if not isinstance(dp, Datapath):
            raise TypeError("dp is not a Datapath.")
        self._lookup_dpid(dp.id)

    def _lookup_dpid(self, dpid):
        """ 
        checks to see if there is a flow/port associated with this dpid that needs 
        to be sent to the AC
        
        returns true iff there is. 
        TODO: lookup dpid. 
        """
        if dpid :
            LOG.debug("Looking up DPID: %s", dpid_to_str(dpid))
        else :
            LOG.debug("DPID is none.",)
        
