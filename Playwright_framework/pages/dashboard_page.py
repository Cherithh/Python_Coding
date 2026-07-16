from playwright.sync_api import Page,expect


class DashboardPage:

    def __init__(self, page : Page):
        self.page = page

    def click_admin(self):
        self.page.get_by_role("link", name="Admin").click()

    def logout(self):
        self.page.get_by_role("listitem").filter(has_text="NewFirstName NewLastName").locator("i").click()
        self.page.get_by_role("menuitem", name="Logout").click()