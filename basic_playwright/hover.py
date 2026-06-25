from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://prismic.io/blog/css-hover-effects")
    page.locator("//span[@class='transition-colors duration-300 flex items-center py-2 px-3 rounded-lg group-data-[state=open]:bg-gray-F7 group-data-[state=open]:text-gray-15'][normalize-space()='Product']").hover()
    page.wait_for_timeout(3000)
    browser.close()