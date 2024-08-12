from playwright.sync_api import sync_playwright
from locators import *
import time


# takes inner text of odds as input
# calculates odds %% distribution
# percentages tuple in weight var 
# weight = ( , , )
Event = namedtuple('Event', ['site', 'event', 'time', 'quarter', 'period', 'home', 'draw', 'away'])

def supabets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        page.screenshot(path='shot_one.png', full_page=True)
        sb_sport.click()
        sb_live.click()
        sb_basket.click()
        events = page.wait_for_locator(sb_match).query_selector_all()
        sb = []
        for event in events:           
            event.click()
            # assert sb_is_live
            sb_qtrs.click()
            qtrs_sb.click()
            game = Event(sb_site.inner_text(), sb_event.inner_text(), sb_time.inner_text(), sbq_num.inner_text(), sb_period.inner_text(), sb_home.inner(), sb_draw.inner_text(), sb_away.inner_text())
            sb.append(game)
        return sb

        browser.close()

def palacebets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(pb_url)
        page.screenshot(path='shot_one.png', full_page=True)
        pb_sport.click()
        pb_live.click()
        pb_basket.click()
        events = page.wait_for_locator(pb_match).query_selector_all()
        pb = []
        for event in events:           
            pb_event.click()
            pb_qtrs.click()
            qtrs_pb.click()
            game = (pb_site.inner_text(), pb_event.inner_text(), pb_time.inner_text(), pbq_num.inner_text(), pb_period.inner_text(), pb_home.inner_text(), pb_draw.inner_text(), pb_away.inner_text())
            pb.append(game)
        return pb
    
        browser.close()

def betUS():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bu_url)
        page.screenshot(path='shot_one.png', full_page=True)
        bu_sport.click()
        bu_live.click()
        bu_basket.click()
        events = page.wait_for_locator(bu_match).query_selector_all()
        bu = []
        for event in events:           
            bu_event.click()
            bu_qtrs.click()
            qtrs_bu.click()
            game = (bu_site.inner_text(), bu_event.inner_text(), bu_time.inner_text(), buq_num.inner_text(), bu_period.inner_text(), bu_home.inner_text(), bu_draw.inner_text(), bu_away.inner_text())
            bu.append(game)
        return bu

        browser.close()

def betway():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_url)
        page.screenshot(path='shot_one.png', full_page=True)
        bw_sport.click()
        bw_live.click()
        bw_basket.click()
        events = page.wait_for_locator(bw_match).query_selector_all()
        bw = []
        for event in events:           
            bw_event.click()
            bw_qtrs.click()
            qtrs_bw.click()
            game = (bw_site.inner_text(), bw_event.inner_text(), bw_time.inner_text(), bwq_num.inner_text(), bw_period.inner_text(), bw_home.inner_text(), bw_draw.inner_text(), bw_away.inner_text())
            bw.append(game)
        return bw

        browser.close()


def hollywoodbets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(hb_url)
        page.screenshot(path='shot_one.png', full_page=True)
        hb_sport.click()
        hb_live.click()
        hb_basket.click()
        events = page.wait_for_locator(hb_match).query_selector_all()
        hb = []
        for event in events:           
            hb_event.click()
            hb_qtrs.click()
            qtrs_hb.click()
            game = (hb_site.inner_text(), hb_event.inner_text(), time.inner_text(), hbq_num.inner_text(), hb_period.inner_text(), hb_home.inner_text(), hb_draw.inner_text(), hb_away.inner_text())
            hb.append(game)
        return hb

        browser.close()
        
def allgames():
    sb = supabets()
    pb = palacebets()
    bu = betUS()
    bw = betway()
    hb = hollywoodbets()
    games_list = sb, pb, bu, bw, hb
    
    return games_list