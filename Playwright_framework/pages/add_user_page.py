import re
from playwright.sync_api import Page,expect

class AddUserPage:

    def __init__(self, page : Page):
        self.page = page

    def add_user(self, employee, username, password):

        self.page.locator(".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow").first.click()
        self.page.get_by_role("option", name="Admin").click()

        self.page.get_by_role("textbox", name="Type for hints...").fill(employee)
        self.page.get_by_role("option", name="Chandramohan Moorthy").click()

        self.page.locator(
            "div:nth-child(3) > .oxd-input-group > div:nth-child(2)"
            " > .oxd-select-wrapper > .oxd-select-text"
            " > .oxd-select-text--after > .oxd-icon"
        ).click()

        self.page.get_by_role("option", name="Enabled").click()

        self.page.get_by_role("textbox").nth(2).fill(username)
        self.page.get_by_role("textbox").nth(3).fill(password)
        self.page.get_by_role("textbox").nth(4).fill(password)

        self.page.get_by_role("button", name="Save").click()