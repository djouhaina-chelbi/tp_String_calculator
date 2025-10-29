@ pytest.mark.params([("",0),(1,0,1),(1,2,3)])

def test_add_empty_string():
    assert add("") == 0
def test_add_1_number():
    assert add("1") == 1

def test_add_2_numbers():
    assert add("1,2") == 3

