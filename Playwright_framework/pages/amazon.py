from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Amazon
    page.goto("https://www.amazon.in")

    # Search for books
    page.locator("#twotabsearchtextbox").fill("Books")
    page.locator("#nav-search-submit-button").click()

    # Wait for search results
    page.wait_for_selector("h2 a")

    books = page.locator("[data-component-type='s-search-result']")

    third_book = books.nth(2)

    print(third_book.locator("h2").text_content())

    third_book.locator("h2 a").click()

    page.wait_for_timeout(5000)
    browser.close()