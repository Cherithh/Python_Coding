from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")
    page.locator("//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select").select_option("IND")
    country = page.locator("//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select").input_value()
    print(country)
    page.wait_for_timeout(3000)
    browser.close()