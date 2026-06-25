from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.flipkart.com/")
    page.locator("//div[@class='_1psv1zeb9 _1o6mltljs _1psv1ze9x _1psv1ze7o _1psv1ze2u _1psv1ze53 _7dzyg23 _1psv1ze29 _1psv1ze53 _1psv1zee3']//div[@class='_1psv1zeb9 _1psv1ze0 _1psv1zedi']//div//img[@alt='Image']").click()
    page.wait_for_timeout(3000)
    browser.close()