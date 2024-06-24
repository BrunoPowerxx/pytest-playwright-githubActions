from playwright.sync_api import sync_playwright
import time

bw_basket = "https://betway.co.za/sport/basketball"
event_title = "//div[@data-eventtile='Brazil']"
types = "//div[@data-translate-market='Winner']"
values = "//div[@class='outcome-pricedecimal']"

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(5)
        page.locator(event_title).click
        time.sleep(5)
        odd_t = page.wait_for_selector(types, timeout=50000)
        odd_v = page.wait_for_selector(values, timeout=50000)
        type = odd_t.inner_text()
        value = odd_v.inner_text()
        print(type)
        print(value)
        print("yeah motherfucker!!")

        browser.close()
