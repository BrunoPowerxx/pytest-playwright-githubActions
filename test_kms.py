from playwright.sync_api import sync_playwright
import time

def test_web1():
    bw_basket = "https://betway.co.za/sport/basketball"

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(bw_basket)
        time.sleep(3)
        page.screenshot(path='shot1.png', full_page=True)

        # Locate the span containing 'Odd' under specific attributes using XPath
        odd_xpath = "//span[@data-translate-type='outcome' and @data-translate-set='Basketball' and @data-translate-market='1st Quarter - Odd/Even' and @data-translate-key='Odd']"
        odd_element = page.locator('xpath=' + odd_xpath)
        odd_element.click()  # Assuming you need to interact with this element
        time.sleep(3)
        page.screenshot(path='shot2.png', full_page=True)

        # Find the odds value under the div with class 'outcome-pricedecimal' using CSS selector
        odds_css = ".outcome-pricedecimal"
        odds_element = page.locator(odds_css)
        odds_value = odds_element.inner_text()
        print(f"Odds value: {odds_value}")

        browser.close()

