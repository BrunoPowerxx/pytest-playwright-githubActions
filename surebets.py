from fetch_odds import *
from thefuzz import fuzz

def arbs():
    sb, pb, bu, bw, hb = games_list()
    for a in sb:
        for b in pb:
            for c in bu:          
                x = fuzz.ratio(a.event, b.event)
                y = fuzz.ratio(b.event, c.event)
                if x > 90 and y > 90:
                    
                    sbp = {
                    'sites': a.site + " - " + c.site +         " - " + b.site,
                    'event': a.event,
                    'home': a.home,
                    'draw': c.draw,
                    'away': b.away,
                    }
                
                    spb = {
                    'sites': a.site + " - " + b.site +         " - " + c.site,
                    'event': a.event,
                    'home': a.home,
                    'draw': b.draw,
                    'away': c.away,
                    }
                
                    pbs = {
                    'sites': b.site + " - " + c.site +         " - " + a.site,
                    'event': b.event,
                    'home': b.home,
                    'draw': c.draw,
                    'away': a.away,
                    }
                
                    psb = {
                    'sites': b.site + " - " + a.site +         " - " + c.site,
                    'event': b.event,
                    'home': b.home,
                    'draw': a.draw,
                    'away': c.away,
                    }
                
                    bsp = {
                    'sites': c.site + " - " + a.site +         " - " + b.site,
                    'event': c.event,
                    'home': c.home,
                    'draw': a.draw,
                    'away': b.away,
                    }
                
                    bps = {
                    'sites': c.site + " - " + b.site +         " - " + a.site,
                    'event': c.event,
                    'home': c.home,
                    'draw': b.draw,
                    'away': a.away,
                    }
                    # write this shit into a file
                    # so you don't have to be
                    # frustrated by any bs
                    all = []
                    alles = [sbp, spb, pbs, psb, bsp, bps]
                    for item in alles:
                        if ((1/item['home']) + (1/item['draw']) + (1/item['away'])) <= 1.00:
                            all.append(item)
                    
    return all

# arbs()