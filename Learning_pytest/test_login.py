def login(username,password):
    if username == "Admin":
        if password == "Admin123":
            return "Login Successful!"
        else:
            return "Login Unsuccessful"
    return "Invalid username"
        

def test_login():
    assert login("Admin","Admin123") == "Login Successful!"