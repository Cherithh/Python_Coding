from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage


def test_add_admin_user(page : Page):

    login = LoginPage(page)
    dashboard = DashboardPage(page)
    admin = AdminPage(page)
    add_user = AddUserPage(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php")

    login.login("Admin", "admin123")

    dashboard.click_admin()

    admin.click_add()

    add_user.add_user(
        "ram",
        "Cherith007",
        "Cherith@007"
    )

    dashboard.logout()