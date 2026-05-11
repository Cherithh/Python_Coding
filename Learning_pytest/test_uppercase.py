def uppercase(data=str):
    return data.lower()

def test_uppercase():
    assert uppercase("PYTHON") == "python"