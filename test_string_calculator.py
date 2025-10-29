@ pytest.mark.params([("",0),("1,0",1),("1,2",3),("1,2,3,4,5",15),("1,2\n3",6)])

def test_add_empty_string():
    assert add("") == 0
def test_add_1_number():
    assert add("1") == 1

def test_add_2_numbers():
    assert add("1,2") == 3
def test_add_5_numbers():
    assert add("1,2,3,4,5") == 15

def test_add_with_newline_separator():
    assert add("1,2\n3") == 6
