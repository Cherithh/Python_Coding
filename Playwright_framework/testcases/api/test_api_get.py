from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    request = playwright.request.new_context()
    response = request.get("https://reqres.in/api")

    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["name"] == "ReqRes API"

    request.dispose()
    print("Test completed successfully")