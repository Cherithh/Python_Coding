from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.amazon.in/")

    page.get_by_role(
        "searchbox",
        name="Search Amazon.in"
    ).fill("Books")

    page.locator("//input[@type='submit']").click()

    third_book = page.locator(
        "//div[@data-component-type='s-search-result']"
    ).nth(2)

    third_book.scroll_into_view_if_needed()

    with page.expect_popup() as popup_info:
        third_book.locator("a").first.click()

    new_page = popup_info.value

    new_page.wait_for_load_state()

    print(new_page.title())
    print(new_page.url)

    new_page.locator("#add-to-cart-button").click()
    page.bring_to_front()

    page.wait_for_timeout(5000)