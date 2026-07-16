from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    try:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.get_by_role("textbox", name="Username").fill("Admin")
        page.get_by_role("textbox", name="Password").fill("admin123")
        page.get_by_role("button", name="Login").click()

        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

        page.get_by_role("link", name="Performance").click()
        expect(page.get_by_role("heading", name="Performance")).to_be_visible()

        page.get_by_role("link", name="Dashboard").click()
        expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

    finally:
        page.context.tracing.stop(path="test-results/trace.zip")