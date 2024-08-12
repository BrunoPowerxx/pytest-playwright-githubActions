from playwright_sync_api import sync_playwright

def sb_home(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        # navigate to sport
        sb_sport.click()
        sb_live.click()
        sb_basket.click()
        # assert event name
        event = page.wait_for_locator(sb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert sb_is_live
        sb_is_live.has_text("Live")
        # assert quarter
        sb_qtrs.has_text(item.quarter).click()
        qtrs_sb.click()
        # assert home odds
        sb1.has_value(item.home).click()
        # type stakes into betslip
        # round the amount first
        # factor profit into round
        sb_stake.fill(item.stake1)
        # assert typed stakes
        sb_stake.has_text(item.stake1)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        sb_go.click()
        # 2nd screenshot
        page.screenshot()
        # assert bet placement
        print("Supabets home ✓")
        
        # note time to end of qtr
        
        browser.close()
        
        
def sb_draw(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        # navigate to sport
        sb_sport.click()
        sb_live.click()
        sb_basket.click()
        # assert event name
        event = page.wait_for_locator(sb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert sb_is_live
        sb_is_live.has_text("Live")
        # assert quarter
        sb_qtrs.has_text(item.quarter).click()
        qtrs_sb.click()
        # assert draw odds
        sbx.has_value(item.draw).click()
        # type stakes into betslip
        sb_stake.type(item.stakex)
        # assert typed stakes
        sb_stake.has_text(item.stakex)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        sb_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Supabets draw ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def sb_away(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(sb_url)
        # navigate to sport
        sb_sport.click()
        sb_live.click()
        sb_basket.click()
        # assert event name
        event = page.wait_for_locator(sb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert sb_is_live
        sb_is_live.has_text("Live")
        # assert quarter
        sb_qtrs.has_text(item.quarter).click()
        qtrs_sb.click()
        # assert away odds
        sb2.has_value(item.away).click()
        # type stakes into betslip
        sb_stake.type(item.stake2)
        # assert typed stakes
        sb_stake.has_text(item.stake2)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        sb_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Supabets away ✓")

        # note time to end of qtr
        
        browser.close()


def pb_home(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(pb_url)
        # navigate to sport
        pb_sport.click()
        pb_live.click()
        pb_basket.click()
        # assert event name
        event = page.wait_for_locator(pb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert pb_is_live
        pb_is_live.has_text("Live")
        # assert quarter
        pb_qtrs.has_text(item.quarter).click()
        qtrs_pb.click()
        # assert home odds
        pb1.has_value(item.home).click()
        # type stakes into betslip
        pb_stake.type(item.stake1)
        # assert typed stakes
        pb_stake.has_text(item.stake1)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        pb_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Palacebet home √")
        
        # note time to end of qtr
        
        browser.close()
        
        
def pb_draw(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(pb_url)
        # navigate to sport
        pb_sport.click()
        pb_live.click()
        pb_basket.click()
        # assert event name
        event = page.wait_for_locator(pb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert pb_is_live
        pb_is_live.has_text("Live")
        # assert quarter
        pb_qtrs.has_text(item.quarter).click()
        qtrs_pb.click()
        # assert draw odds
        pbx.has_value(item.draw).click()
        # type stakes into betslip
        pb_stake.type(item.stakex)
        # assert typed stakes
        pb_stake.has_text(item.stakex)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        pb_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Palacebet draw ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def pb_away(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(pb_url)
        # navigate to sport
        pb_sport.click()
        pb_live.click()
        pb_basket.click()
        # assert event name
        event = page.wait_for_locator(pb_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert pb_is_live
        pb_is_live.has_text("Live")
        # assert quarter
        pb_qtrs.has_text(item.quarter).click()
        qtrs_pb.click()
        # assert away odds
        pb2.has_value(item.away).click()
        # type stakes into betslip
        pb_stake.type(item.stake2)
        # assert typed stakes
        pb_stake.has_text(item.stake2)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        pb_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Palacebet away ✓")
        
        # note time to end of qtr
        
        browser.close()

        
def bu_home(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bu_url)
        # navigate to sport
        bu_sport.click()
        bu_live.click()
        bu_basket.click()
        # assert event name
        event = page.wait_for_locator(bu_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bu_is_live
        bu_is_live.has_text("Live")
        # assert quarter
        bu_qtrs.has_text(item.quarter).click()
        qtrs_bu.click()
        # assert home odds
        bu1.has_value(item.home).click()
        # type stakes into betslip
        bu_stake.type(item.stake1)
        # assert typed stakes
        bu_stake.has_text(item.stake1)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bu_go.click()
        # 2nd screenshot
        page.screenshot()
        print("BetUS home ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def bu_draw(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bu_url)
        # navigate to sport
        bu_sport.click()
        bu_live.click()
        bu_basket.click()
        # assert event name
        event = page.wait_for_locator(bu_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bu_is_live
        bu_is_live.has_text("Live")
        # assert quarter
        bu_qtrs.has_text(item.quarter).click()
        qtrs_bu.click()
        # assert draw odds
        bux.has_value(item.draw).click()
        # type stakes into betslip
        bu_stake.type(item.stakex)
        # assert typed stakes
        bu_stake.has_text(item.stakex)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bu_go.click()
        # 2nd screenshot
        page.screenshot()
        print("BetUS draw ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def bu_away(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bu_url)
        # navigate to sport
        bu_sport.click()
        bu_live.click()
        bu_basket.click()
        # assert event name
        event = page.wait_for_locator(bu_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bu_is_live
        bu_is_live.has_text("Live")
        # assert quarter
        bu_qtrs.has_text(item.quarter).click()
        qtrs_bu.click()
        # assert away odds
        bu2.has_value(item.away).click()
        # type stakes into betslip
        bu_stake.type(item.stake2)
        # assert typed stakes
        bu_stake.has_text(item.stake2)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bu_go.click()
        # 2nd screenshot
        page.screenshot()
        print("BetUS away ✓")
        
        # note time to end of qtr
        
        browser.close()

def bw_home(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_url)
        # navigate to sport
        bw_sport.click()
        bw_live.click()
        bw_basket.click()
        # assert event name
        event = page.wait_for_locator(bw_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bw_is_live
        bw_is_live.has_text("Live")
        # assert quarter
        bw_qtrs.has_text(item.quarter).click()
        qtrs_bw.click()
        # assert home odds
        bw1.has_value(item.home).click()
        # type stakes into betslip
        bw_stake.type(item.stake1)
        # assert typed stakes
        bw_stake.has_text(item.stake1)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bw_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Betway home ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def bw_draw(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_url)
        # navigate to sport
        bw_sport.click()
        bw_live.click()
        bw_basket.click()
        # assert event name
        event = page.wait_for_locator(bw_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bu_is_live
        bw_is_live.has_text("Live")
        # assert quarter
        bw_qtrs.has_text(item.quarter).click()
        qtrs_bw.click()
        # assert draw odds
        bwx.has_value(item.draw).click()
        # type stakes into betslip
        bw_stake.type(item.stakex)
        # assert typed stakes
        bw_stake.has_text(item.stakex)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bw_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Betway draw ✓")
        
        # note time to end of qtr
        
        browser.close()
        
def bw_away(item):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_url)
        # navigate to sport
        bw_sport.click()
        bw_live.click()
        bw_basket.click()
        # assert event name
        event = page.wait_for_locator(bw_match)
        event.has_text(item.event).click()
        # assert event again
        eventId.has_text(item.eventId)
        # assert bw_is_live
        bw_is_live.has_text("Live")
        # assert quarter
        bw_qtrs.has_text(item.quarter).click()
        qtrs_bw.click()
        # assert away odds
        bw2.has_value(item.away).click()
        # type stakes into betslip
        bw_stake.type(item.stake2)
        # assert typed stakes
        bw_stake.has_text(item.stake2)
        # take a screenshot
        page.screenshot()
        # confirm bet placement
        bw_go.click()
        # 2nd screenshot
        page.screenshot()
        print("Betway away ✓")
        
        # note time to end of qtr
        
        browser.close()