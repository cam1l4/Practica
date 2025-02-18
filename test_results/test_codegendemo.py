import re
from playwright.sync_api import Page, expect
import pytest


def test_example2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.pause()
    
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    #actualizacion de script v1
