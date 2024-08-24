from main import Calculator

obj=Calculator()
def test_add():
    assert obj.add(1,2)==3

def test_sub():
    assert obj.sub(2,1)==1

def test_multiply():
    assert obj.multiply(2,2)==4

def test_div():
    assert obj.divide(5,2)==2.5
