from playwright.sync_api import sync_playwright

def test_supabets():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Open new page
        page = context.new_page()

        # Navigate to Supabets website
        page.goto('https://www.supabets.co.za')

        # Define the selector you want to interact with
        sb_match = "plr_1.ng-binding"

        # Wait for the first element that matches the selector
        first_element = page.locator(sb_match).first()
        first_element.wait_for()

        # Get the text content of the first matching element
        text_content = first_element.text_content()
        print("Text Content:", text_content)

        # Optionally, take a screenshot of the page
        page.screenshot(path='supabets_screenshot.png')

        # Close browser
        browser.close()
