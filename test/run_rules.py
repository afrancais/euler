cid = '118ea716-0a26-4b68-b0d9-d7a0027714f9'
import logging

from lib.utils.dolead_utils import *
c = TechnoUtils.get_campaign(cid)
from domain.algorithm.bidder import RuleBasedBidder
r = RuleBasedBidder(c)
r.run()
