from surebets import *
from arbfunk import *
import pytest

def test_betbot(): # test
    all = arbs()
    for item in all:
       # base url to confirm site
       
       if item['event'] == "Supabets - BetUS - Palacebets":
           bet_sbp(item)
       if item['event'] == "Supabets - Palacebets - BetUS":
           bet_spb(item)
       if item['event'] == "BetUS - Palacebets - Supabets":
           bet_bps(item)
       if item['event'] == "BetUS - Supabets - Palacebets":
           bet_bsp(item)
       if item['event'] == "Palacebets - BetUS - Supabets":
           bet_pbs(item)
       if item['event'] == "Palacebets - Supabets - BetUS":
           bet_psb(item)
       else:
           print("could not bet")
