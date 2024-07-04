import os
import time
from datetime import datetime
from playwright.sync_api import sync_playwright

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
screenshot_directory = "screenshots"  # New directory to store screenshots

if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

def test_web1():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://za.indeed.com/")
        screenshot_path = os.path.join(screenshot_directory, f"screenshot_{timestamp}.png")
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()

        # Optionally, you can commit the screenshot to version control if needed
        # Example of committing the screenshot file
        commit_screenshot(screenshot_path)
        

def commit_screenshot(filepath):
    # Perform git commands to add and commit the screenshot file
    os.system(f"git add {filepath}")
    os.system(f"git commit -m 'Added screenshot {os.path.basename(filepath)}'")
    os.system("git push")

# Run the test function





#page.get_by_placeholder("Job title, keywords, or").fill("kill all leftists")        
#page.get_by_placeholder("City, state, zip code, or \"").fill("upington")
#page.get_by_role("button", name="Find jobs").click()
#page.goto("https://za.indeed.com/")
