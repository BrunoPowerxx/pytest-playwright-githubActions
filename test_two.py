from playwright.sync_api import sync_playwright
import time

bw_basket = "https://betway.co.za/sport/basketball"
event_title = "//div[@data-eventtile='Brazil']"
types = "//div[ contains(@data-translate-market)]"
values = "//div[ contains(@data-pd)]"

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(5)
        page.locator(event_tile).click
        time.sleep(5)
        odd_t = page.query_selector(types)
        odd_v = page.query_selector(values)
        type = odd_t.inner_text()
        value = odd_v.inner_text()
        print(type)
        print(value)
        print("yeah motherfucker!!")

        browser.close()
