import os
import time
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load local index.html
        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)

        # Wait for page load
        page.wait_for_load_state('networkidle')

        # Test 1: Verify elements have role="button" and tabindex="0"
        cards = page.locator('.fc')
        count = cards.count()
        print(f"Found {count} floating cards.")

        for i in range(count):
            card = cards.nth(i)
            role = card.get_attribute('role')
            tabindex = card.get_attribute('tabindex')
            if role != 'button' or tabindex != '0':
                print(f"Error: Card {i} missing accessibility attributes.")
                return
        print("Test 1 Passed: All cards have correct base attributes.")

        # Test 2: Verify keyboard interaction
        # Focus the first card
        first_card = cards.nth(0)
        first_card.focus()
        time.sleep(1) # Let the focus visible style apply and stabilize

        # Take a screenshot to verify focus outline
        page.screenshot(path="focus_test.png")
        print("Captured screenshot of focused card.")

        # Press Enter
        page.keyboard.press('Enter')
        time.sleep(1)

        # Verify expanded state
        classes = first_card.get_attribute('class')
        aria_expanded = first_card.get_attribute('aria-expanded')
        if 'expanded' not in classes or aria_expanded != 'true':
            print("Error: Card did not expand on Enter keypress.")
            return

        print("Test 2 Passed: Card expanded on Enter.")

        # Press Space
        page.keyboard.press(' ')
        time.sleep(1)

        # Verify collapsed state
        classes = first_card.get_attribute('class')
        aria_expanded = first_card.get_attribute('aria-expanded')
        if 'expanded' in classes or aria_expanded != 'false':
            print("Error: Card did not collapse on Space keypress.")
            return

        print("Test 3 Passed: Card collapsed on Space.")

        browser.close()

if __name__ == "__main__":
    run()
