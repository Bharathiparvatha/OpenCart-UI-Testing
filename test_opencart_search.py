import pytest
from playwright.sync_api import sync_playwright

def test_opencart_product_search():
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 1. Navigate to OpenCart Demo Portal
        page.goto("https://opencart.com")
        
        # 2. Locate Search Bar, type product name and search
        search_input = page.locator("input[name='search']")
        search_input.fill("MacBook")
        page.locator("button.btn-light.btn-lg").click()
        
        # 3. Assertion: Verify search result loads matching products
        assert page.locator("h2:has-text('Products meeting the search criteria')").is_visible()
        assert page.locator(".product-thumb").count() > 0
        
        browser.close()

def test_opencart_invalid_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.goto("https://opencart.com")
        
        # Search for a non-existing item
        search_input = page.locator("input[name='search']")
        search_input.fill("InvalidProduct123")
        page.locator("button.btn-light.btn-lg").click()
        
        # 4. Assertion: Verify 'No product' message is displayed
        no_product_msg = page.locator("p:has-text('There is no product that matches the search criteria.')")
        assert no_product_msg.is_visible()
        
        browser.close()
