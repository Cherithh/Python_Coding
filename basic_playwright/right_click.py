from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.guru99.com/test/simple_context_menu.html")
    page.get_by_text("right click me").click(button='right')
    page.wait_for_timeout(3000)
    page.locator("//li[@class='context-menu-item context-menu-icon context-menu-icon-quit']").click()
    page.wait_for_timeout(3000)
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Double-Click Me To See Alert").dblclick()
    page.wait_for_timeout(3000)
    page.on("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(3000)
    browser.close()