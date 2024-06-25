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
#qoe_1 = "//span[@data-translate-key='1StQuarterOddEven']"
    #1st Quarter - Odd
#qoe1_ot = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ov = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Odd'] ~ div.outcome-pricedecimal"
    #1st Quarter  - Even
#qoe1_et = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ev = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Even'] ~ div.outcome-pricedecimal"

qoe1_ot = "//span[@data-translate-key='1StQuarterOddEven']//span[data-translate-key='Odd']"
qoe1_ov = "//span[@data-translate-key='1StQuarterOddEven']//div[@class='outcome-pricedecimal'][1]"

qoe1_et = "//span[@data-translate-key='1StQuarterOddEven']//span[data-translate-key='Even']"
qoe1_ev = "//span[@data-translate-key='1StQuarterOddEven']//div[@class='outcome-pricedecimal'][2]"

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
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(3)
        page.locator(sport).click()
        time.sleep(3)
        page.locator(basket).click()
        time.sleep(3)
        page.locator(highlights).click()
        time.sleep(3)
        events = page.locator(event)
        #quarters = []
        events.nth(0).click()
        
        time.sleep(3)
        page.locator(qtrs).click()
        time.sleep(3)
        page.locator(qoe_1).click()
        time.sleep(3)
        qoe1_odd_value = page.locator(qoe1_ov)
        qoe1_even_value = page.locator(qoe1_ev)
        qoe1_odds = {
            'Q1 Odd': qoe1_odd_value.inner_text(),
            'Q1 Even': qoe1_even_value.inner_text()
        }
   
        print(qoe1_odds)
        print("yeah motherfucker!!")

        browser.close()
