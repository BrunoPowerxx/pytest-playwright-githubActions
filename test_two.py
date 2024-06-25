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
qoe_1 = "//span[@data-translate-key='1StQuarterOddEven']"
qoe1_ot = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
qoe1_ov = "//span[@data-translate-key='1StQuarterOddEven']"
     #   qoe1_et =
      #  qoe1_ev =
      #  qoe1_ov =
      #  qoe1_et =
      #  qoe1_ev =
qoe_2 = "//span[@data-translate-key='2NdQuarterOddEven']"
    #    qoe2_ot =
     #   qoe2_ov =
      #  qoe2_et =
       # qoe2_ev =
qoe_3 = "//span[@data-translate-key='3RQuarterOddEven']"
    #    qoe3_ot =
    #    qoe3_ov =
    #    qoe3_et =
    #    qoe3_ev =
qoe_4 = "//span[@data-translate-key='4ThQuarterOddEven']"
     #   qoe4_ot =
     #   qoe4_ov =
    #  qoe4_et =
     #   qoe4_ev =

    #    types = "//div[@data-translate-market='Winner']"
    #    values = "//div[@class='outcome-pricedecimal']"

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(3)
        page.locator(sport).click()
        time.sleep(3)
        page.locator(basket).click()
        time.sleep(3)
        page.locator(highlights).click()
        time.sleep(3)
        page.locator(event).click()
        time.sleep(3)
        page.locator(qtrs).click()
        time.sleep(3)
        page.locator(qoe_1).click()
        time.sleep(3)
        
        
      #  for i in games:
      #  game.click()
      #  time.sleep(3)
            
        odd_t = page.locator(qoe1_ot)
        odd_v = page.locator(qoe1_ov)
        type = odd_t.inner_text()
        value = odd_v.inner_text()
            
        print(type)
        print(value)
        print("yeah motherfucker!!")

        browser.close()
