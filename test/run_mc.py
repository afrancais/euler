cid = '5eb55c2a-07eb-4ab1-985f-652211c11d46'

from lib.utils.dolead_utils import *
c = TechnoUtils.get_campaign(cid)
from domain.service.bidder.montecarlo import *
r = MonteCarloService(c, 30)
r.run()
