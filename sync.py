from playwright.sync_api import sync_playwright
import pytest

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://whatsmyuseragent.org/")
    page.screenshot(path="demo.png")
    browser.close()
