from app import sum_something,sub_somthing

def test_sum_something():
    a,b = 1,2

    assert sum_something(a,b)==3

def test_sub_somthing():
    a,b=1,2

    assert sub_somthing(1,2)==-1