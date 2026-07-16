import re
from playwright.sync_api import Page
from pages.login_page import LoginPage
from Playwright_framework.pages.dashboard_page import HomePage
from pages.admin_page import A

def test_admin(page: Page) -> None:
    login_page = LoginPage(page)
    home_page = HomePage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php")
    login_page.login("Admin","admin123")
    home_page.check_dashboard_visibility()