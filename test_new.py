from playwright.sync_api import sync_playwright
from selectors import *
import time


bw_url = "https://betway.co.za"
sb_url = "https://supabets.co.za"

bws_hl = page.wait_for_selector("button#synapse_highlights")
sb_tl = page.wait_for_selector("a[data-istestfield="tabs-topleagues"]")

sb_site = "Supabets"
bw_site = "Betway"

sb_sport = page.wait_for_selector("li > a.sport")
bw_sport = page.wait_for_selector("span[data-translate-key="Sport"]")

sb_soccer = page.wait_for_selector("div[title="SOCCER"]")
bw_soccer = page.wait_for_selector("li[data-translate-key="Soccer"]")

bw_match = page.wait_for_selector("div.row.eventRow label.ellips.theOtherFont")
sb_match = page.wait_for_selector("div.TopLeagues div.plr_1.ng-binding")
sb_away = page.wait_for_selector("div.TopLeagues div.plr_2.ng-binding")


bw_event =

sb_yt = page.wait_for_selector("div", has_text="Yes (GG)")
sb_yv = page.wait_for_selector("div.oddValue:right-of(sb_yt)")
bw_yt = page.wait_for_selector("div[data-markettitle="Both Teams To Score"] span[data-translate-key="Yes"]")
bw_yv = page.wait_for_selector("div[data-markettitle="Both Teams To Score"]:right-of(bw_yt)")

sb_nt = page.wait_for_selector("div", has_text="No (NG)")
sb_nv = page.wait_for_selector("div.oddValue:right-of(sb_nt)")
bw_nt = page.wait_for_selector("div[data-markettitle="Both Teams To Score"] span[data-translate-key="No"]")
bw_nv = page.wait_for_selector("div[data-markettitle="Both Teams To Score"]:right-of(bw_nt)")

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
        sb_sport.click()
        #sb_live.click()
        sb_soccer.click()
        fixtures = sb_match.query_selector_all()
        sb = []
        for fixture in fixtures:           
            fixture.click()
            # assert sb_is_live
            #sb_qtrs.click()
            #qtrs_sb.click()
            game = Event(sb_site, sb_yv.inner_text(), sb_nv.inner_text())
            sb.append(fixture)
            print(fixture)
        return sb

        browser.close()
