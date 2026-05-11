def is_even(num):
    
    if num %2 == 0:
            return True
    else:
            return False
        
def test_even():
     assert is_even(4) == True
     assert is_even(5) == False