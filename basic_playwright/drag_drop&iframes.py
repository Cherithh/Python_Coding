from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://jqueryui.com/droppable/")
    frame = page.frame_locator("//iframe[@class='demo-frame']")
    drag = frame.locator("//div[@id='draggable']")
    drop = frame.locator("//div[@id='droppable']")

    drag.drag_to(drop)
    page.wait_for_timeout(3000)
    # drag.hover()
    # page.mouse.down()
    # drop.hover()
    # page.mouse.up()
    # page.wait_for_timeout(3000)

    browser.close()