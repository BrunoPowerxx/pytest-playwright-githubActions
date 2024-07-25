from playwright.sync_api import sync_playwright
import time

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://betway.co.za/sport/basketball")
        time.sleep(3)
        
        # Wait for the page to load completely
        page.wait_for_load_state('networkidle')
        
        # Take a screenshot of the initial state
        page.screenshot(path='shot1.png', full_page=True)
        
        # Check for and close any modal dialog
        try:
            modal_close_button = page.wait_for_selector('div.modal.fade.in.toast button.close', timeout=5000)
            modal_close_button.click()
            time.sleep(1)
        except:
            print("No modal dialog appeared")
        
        # Wait for the event element and click it
        event = page.wait_for_selector('div.league-group-items label.ellips.theOtherFont')
        event.click()
        
        # Wait for the page to load completely again
        page.wait_for_load_state('networkidle')
        
        # Take a screenshot after clicking the event
        page.screenshot(path='shot2.png', full_page=True)
        
        browser.close()
