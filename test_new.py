from playwright.sync_api import sync_playwright
from collections import namedtuple
#from selectors import *
import time

bw_url = "https://betway.co.za"
sb_url = "https://supabets.co.za"

bws_hl = "button#synapse_highlights"
sb_tl = "a[data-istestfield='tabs-topleagues']"

sb_site = "Supabets"
bw_site = "Betway"

sb_sport = "li > a.sport"
bw_sport = "span[data-translate-key='Sport']"

sb_soccer = "div[title='SOCCER']"
bw_soccer = "li[data-translate-key='Soccer']"

bw_match = "div.row.eventRow label.ellips.theOtherFont"
sb_match = "div.plr_1.ng-binding"
sb_away = "div.plr_2.ng-binding"

#bw_event =
#sb_yt = ("div", has_text="Yes (GG)")
sb_yv = "div.oddValue:right-of(div[has_text='Yes (GG)'])"

bw_yt = "div[data-markettitle='Both Teams To Score'] span[data-translate-key='Yes']"
bw_yv = "div[data-markettitle='Both Teams To Score']:right-of(bw_yt)"

#sb_nt = ("div", has_text="No (NG)")
sb_nv = "div.oddValue:right-of(div[has_text='No (NG)'])"

bw_nt = "div[data-markettitle='Both Teams To Score'] span[data-translate-key='No']"
bw_nv = "div[data-markettitle='Both Teams To Score']:right-of(bw_nt)"

# takes inner text of odds as input
# calculates odds %% distribution
# percentages tuple in weight var 
# weight = ( , , )
Event = namedtuple('Event', ['site', 'GG', 'NG'])

def test_sb():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        #page.screenshot(path='shot_one.png', full_page=True)
        page.wait_for_selector(sb_sport).click()
        #sb_live.click()
        page.wait_for_selector(sb_soccer).click()
        page.wait_for_selector(sb_tl).click()
        fixtures = page.wait_for_selector(sb_match).query_selector_all()
        sb = []
        for fixture in fixtures:           
            fixture.click()
            # assert sb_is_live
            #sb_qtrs.click()
            #qtrs_sb.click()
            yes_val = page.wait_for_selector(sb_yv).inner_text()
            no_val = page.wait_for_selector(sb_nv).inner_text()
            game = Event(sb_site, yes_val, no_val)
            sb.append(fixture)
            print(fixture)
        return sb

        browser.close()
