def number_of_evens(numbers):
    return 0

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected,actual)


def test_not_equal(a,b):
    assert a != b, "Did not expect {0} but got {1}".format(a,b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection,item)
    
def test_not_in(collection,item):
    assert item not in collection, "{0} contains {1}".format(collection,item)

def test_between(number,lower,upper):
    assert number>= lower and number<=upper, "{0} is not between {1} and {2}".format(number,lower,upper)
    

#test_not_equal(1,1)
#test_is_in([1,2,3,4], 5)
#test_not_in([1,2,3,4,5], 5)
test_between(2,7,12)
# test_are_equal(number_of_evens([1,2,3]),2)


    