from playwright.sync_api import sync_playwright
import time

#General
bw_basket = "https://betway.co.za/sport/basketball"
sport = "//div[@id='navbar_sport']"

#Soccer
soccer = "//p[@data-translate-key='Soccer']"

#Basketball
basket = "//p[@data-translate-key='Basketball']"
highlights = "//button[@value='highlights']"
event = "//label[@data-translate-type='event' and @data-translate-set='Basketball']"

    #Basketball Highlights
qtrs = "//span[@data-translate-key='Quarters']"
    #1st Quarter
qoe_1 = "//span[@data-translate-key='1StQuarterOddEven']"
    #1st Quarter - Odd
#qoe1_ot = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ov = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Odd'] ~ div.outcome-pricedecimal"
    #1st Quarter  - Even
#qoe1_et = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ev = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Even'] ~ div.outcome-pricedecimal"

#qoe1_ot = "//span[@data-translate-key='1StQuarterOddEven']//span[data-translate-key='Odd']"
#qoe1_v = "//span[@data-translate-key='1StQuarterOddEven']//div[@class='outcome-pricedecimal']"
testing = "//div[@class='outcome-pricedecimal']"
#qoe1_et = "//span[@data-translate-key='1StQuarterOddEven']/span[data-translate-key='Even']"
#qoe1_ev = "//span[@data-translate-key='1StQuarterOddEven']//div[@class='outcome-pricedecimal'][2]"

#    qoe_2 = "//span[@data-translate-key='2NdQuarterOddEven']"
#qoe2_ot =
#    qoe2_ov =
#    qoe2_et =
#    qoe2_ev =
#qoe_3 = "//span[@data-translate-key='3RQuarterOddEven']"
#    #    qoe3_ot =
#    #    qoe3_ov =
#    #    qoe3_et =
#    #    qoe3_ev =
#qoe_4 = "//span[@data-translate-key='4ThQuarterOddEven']"
#     #   qoe4_ot =
#     #   qoe4_ov =
#    #  qoe4_et =
#     #   qoe4_ev =

    #    types = "//div[@data-translate-market='Winner']"
    #    values = "//div[@class='outcome-pricedecimal']"

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(3)
        page.screenshot(path='shot_one.png', full_page=True)
        sport_tab = page.locator(sport)
        sport_tab.highlight()
        page.screenshot(path='shot_two.png', full_page=True)
        sport_tab.click()
        time.sleep(3)
        basket_tab = page.locator(basket)
        basket_tab.highlight()
        page.screenshot(path='shot_three.png', full_page=True)
        basket_tab.click()
        time.sleep(3)
        hilites_tab = page.locator(highlights)
        hilites_tab.highlight()
        page.screenshot(path='shot_four.png', full_page=True)
        hilites_tab.click()
        time.sleep(3)
        page.screenshot(path='shot_five.png', full_page=True)
        events = page.locator(event)
        events.highlight()
        page.screenshot(path='shot_six.png', full_page=True)
        #quarters = []
        events.nth(0).click()
        
        time.sleep(3)
        page.screenshot(path='shot_seven.png', full_page=True)
        qtrs_acc = page.locator(qtrs)
        qtrs_acc.highlight()
        page.screenshot(path='shot_eight.png', full_page=True)
        qtrs_acc.click()
        time.sleep(3)
        #page.locator(qoe_1).click()
        #time.sleep(3)
       # qoe1_vs = page.query_selector_all(qoe1_v)
      #  qoe1_ov = qoe1_vs[0]
      #  qoe1_ev = qoe1_vs[1]
      #  qoe1_odd_value = qoe1_ov.inner_text()
      #  qoe1_even_value = qoe1_ev.inner_text()
     #   qoe1_odds = {
   #         'Q1 Odd': qoe1_odd_value,
   #         'Q1 Even': qoe1_even_value
   #     }
        page.screenshot(path='shot_nine.png', full_page=True)
        tests = page.locator(testing)
        tests.highlight()
        #for test in tests:
        test = tests[0]
        test.highlight()
        test_text = test.inner_text()
        print(test_text)
        print("yeah motherfucker")

        browser.close()
