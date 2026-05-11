def password(data):
    if len(data) > 7:
        return "Valid"
    else:
        return "Invalid"

def test_pwd():
    assert password("Cherith123") == "Valid" 