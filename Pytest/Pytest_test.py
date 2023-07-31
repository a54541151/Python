
#輸入pytest Pytest_test.py執行


"""

def test_file1_method1():
	x=5
	y=6
	assert x+1 == y,"True1"
	# assert x == y,"failed1" #
def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"True2" 

"""


"""

import pytest

def add(x,y):
	return x+y

@pytest.mark.parametrize(
	"x,y,z",
	[
		(1,1,2),
		(2,2,3)  #
	]
)

def test_add(x,y,z):
	assert add(x,y)==z

"""

"""

import pytest

@pytest.mark.A1
def test1():
    pass

@pytest.mark.A1
def test2():
    pass

@pytest.mark.A2
def test6():
    pass

#輸入pytest -m A1 等於只執行所有A1

"""