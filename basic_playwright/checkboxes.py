from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://getcssscan.com/css-checkboxes-examples")
    page.locator("//label[@for='example-1']").check()
    page.locator("//input[@class='sc-gJwTLC ikxBAC']").check()
    page.get_by_text("Morning").check()
    page.wait_for_timeout(3000)
    page.locator("//label[@for='example-1']").uncheck()
    verify = page.get_by_text("Morning").is_checked()
    if verify == True:
        print("Yes its selected")
    else:
        print("Nope, not selected")
    page.wait_for_timeout(3000)
    browser.close()