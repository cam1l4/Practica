from playwright.sync_api import Page  #Libreria
import pytest

#@pytest.mark.only_browser("chromium") #Hacer la ejecucion en un solo browser
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

#@pytest.mark.only_browser("chromium")
def test_inventory_page(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."