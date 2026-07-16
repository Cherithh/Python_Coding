import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin23")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Admin").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    expect(page.get_by_role("heading", name="/ User Management")).to_be_visible()
    page.get_by_role("banner").get_by_text("Elif Torun").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill(" ")
