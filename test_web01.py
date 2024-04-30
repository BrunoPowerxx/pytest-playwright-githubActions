from playwright.sync_api import sync_playwright


def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://vshkodin.com/")
        pagetitle == page.title()
        assert "Vladimir Shkodin" == page.title()
        # page.fill("locator", "text")
        # page.click("locator")
        # time.sleep(5)
        # page.screenshot(path="screenshot.png")
        # head = page.query_selector("div[class='rows text-center'] h1");
        # print(head.inner_html(), str(currentDT))
        # page.goto("https://dateandage.com/date/how-long-july-8-2021")
        # head = page.query_selector('[id="time"]')
        print(pagetitle)
        browser.close()
