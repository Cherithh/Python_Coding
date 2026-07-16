import re
from playwright.sync_api import Page,expect


class AdminPage:

    def __init__(self, page : Page):
        self.page = page

    def click_add(self):
        self.page.get_by_role("button", name="Add").click()

    def check_admin_page_visibility(self):
        expect(self.page.locator("div").filter(has_text=re.compile(r"^Admin$"))).to_be_visible()