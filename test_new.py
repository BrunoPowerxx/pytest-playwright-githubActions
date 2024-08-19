from playwright.sync_api import sync_playwright
from selectors import *
import time


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
