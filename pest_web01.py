from playwright.sync_api import sync_playwright
import time


def supabets_quarters_odd_even():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://supabets.co.za")
        
        # Wait for the soccer tab to appear and click on it
        def supa_qts():
            sb_odd = []
            sb_even = []
            for i in games:
                games[i].click()
                odd = {
                    'home': hometeam,
                    'away': awayteam,
                    'odd': odd,
                    'time': time
                }
                even = {
                    'home': hometeam,
                    'away': awayteam,
                    'even': even,
                    'time': time
                }
                sb_odd.append(odd)
                sb_even.append(even)
            supa = [odd, even]
        def supabets_palace_qts(supa_qts, palace_qts):
            supa_home = supa[0]['home']
            supa_away = supa[1]['away']
            palace_home = palace[0]['home']
            palace_away = palace[1]['away']
            supa_qts_odd = supa[0][odd]
            supa_qts_even = supa[1][even]
            palace_qts_odds = palace[1][odd]
            palace_qts_even = palace[0][even]
            for x in supa[0]:
                for y in palace[1]:
                    if fuzz.ratio(supa_home, palace_away) => 90 
                    and fuzz.ratio(palace_home, supa_away) => 90:
                    supa_palace_all = []
                    supa_palace['home'] = supa_home or palace_home
                    supa_palace['away'] = supa_away or palace_away
                    supa_palace['odd'] =  supa_qts_odd
                    supa_palace['even'] = palace_qts_even
                    supa_palace['tip'] = 1 / supa_palace['odd'] + supa_palace['even'] * 100
                    supa_palace_all.append(supa_palace)
                    SbPb = sorted(supa_palace_all)
                
            
        browser.close()
