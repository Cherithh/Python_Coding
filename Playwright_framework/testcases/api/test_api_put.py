from playwright.sync_api import sync_playwright

def test_get_api():
    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.get("https://reqres.in/api")

        print("Status Code:", response.status)

        json_data = response.json()

        print(json_data)

        assert response.ok  
        assert json_data["name"]=="ReqRes API"

        response = request.get("https://reqres.in/api/users/2")

        assert isinstance(json_data["name"], str)
        assert isinstance(json_data["description"], int)


        request.dispose()