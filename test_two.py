from playwright.sync_api import sync_playwright
import time

#General
bw_basket = "https://betway.co.za/sport/basketball"
#sport = "//div[@id='navbar_sport']"

#Soccer
#soccer = "//p[@data-translate-key='Soccer']"

#Basketball
#basket = "//p[@data-translate-key='Basketball']"
#highlights = "//button[@value='highlights']"
#event = "//label[@data-translate-type='event' and @data-translate-set='Basketball']"

    #Basketball Highlights
#qtrs = "//span[@data-translate-key='Quarters']"

    #1st Quarter
#qoe_1 = "//span[@data-translate-key='1StQuarterOddEven']"
    #1st Quarter - Odd
#qoe1_ot = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ov = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Odd'] ~ div.outcome-pricedecimal"
    #1st Quarter  - Even
#qoe1_et = "//span[@data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
#qoe1_ev = "div.outcome-title.doublechance > span[data-translate-market='1st Quarter - Odd/Even'][data-translate-key='Even'] ~ div.outcome-pricedecimal"

#qoe1_ot = "//span[@data-translate-key='1StQuarterOddEven']//span[data-translate-key='Odd']"
#qoe1_ov = "//span[@data-translate-key='1StQuarterOddEven']//div[@class='outcome-pricedecimal']"
# testing = "//div[@class='outcome-pricedecimal']"
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
        page.screenshot(path='shot1.png', full_page=True)
        event = page.locator('label').filter(data_translate_type='event', data_translate_set='Basketball')
        quarters = []
        event.click()
        time.sleep(3)
        page.screenshot(path='shot2.png', full_page=True)
        qtrs = page.locator('span').filter(data_translate_key='Quarters')
        qtrs.click()
        page.screenshot(path='shot3.png', full_page=True)
        time.sleep(3)
        qoe1 = page.locator('span').filter(data_translate_key='1StQuarterOddEven')
        qoe1.click()
        page.screenshot(path='shot4.png', full_page=True)
        ov_ch_1 = page.locator('div').filter(class_name='outcome-pricedecimal')
        ov_1 = page.get_by_role('span').filter(has=ov_ch_1)
        odd_value = ov_1.inner_text()
        print(odd_value)
        browser.close()
