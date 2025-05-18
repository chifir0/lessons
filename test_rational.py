import rational as r

a = r.create(-1,2)
b = r.create(1,0)
c = r.create(14,7)

assert r.add(a,c) == [3,2]
assert r.add([0,1], [2,-2]) == [-1,1]
assert r.add([0,1], [0,1]) == [0,1]

assert r.sub(a,c) == [-5,2]
assert r.sub(c,a) == [5,2]
assert r.sub([1,1], [0,1]) == [1,1]
assert r.sub([0,1], [1,-1]) == [1,1]
assert r.sub([1,2], [5,12]) == [1,12]

assert r.mul(a,c) == [-1,1]
assert r.mul(c,a) == [-1,1]
assert r.mul([124,1203], [0,1]) == [0,1]
assert r.mul([1,2], [-1,-3]) == [1,6]

assert r.div([1,2], [0,1]) == 'Cannot divide by zero'
assert r.div(a,c) == [-1,4]
assert r.div(c,a) == [-4,1]
assert r.div([2,1], [-2,-4]) == [4,1]

assert r.power(a,2) == [1,4]
assert r.power(a,-2) == [4,1]
assert r.power(c,-1) == [1,2]
assert r.power(a,1) == [-1,2]
assert r.power([0,1], 10000) == [0,1]
assert r.power([123,100], 0) == [1,1]

assert r.compare(a,c) == -1
assert r.compare(c,a) == 1
assert r.compare(a,a) == 0
assert r.compare([0,1], [-1,1]) == 1
assert r.compare([123,124], [123,123]) == -1
assert r.compare([0,1], [0,1]) == 0
assert r.compare([-1,2], [-1,3]) == -1

assert r.to_int(a) == -1
assert r.to_int(c) == 2
assert r.to_int([21,12]) == 1
assert r.to_int([0,1]) == 0

assert r.to_float(a) == -0.5
assert r.to_float(c) == 2.0
assert r.to_float([7,12]) == 7/12
assert r.to_float([0,1]) == 0.0

assert r.to_str(a) == '-1/2'
assert r.to_str(c) == '2/1'
assert r.to_str([3,2]) == '3/2'

assert r.compare(r.add(c,a), r.sub(c,a)) == -1
assert r.to_str(r.mul(r.power(a,2), c)) == '1/2'
assert r.compare(a, r.div(r.mul(a,c), c)) == 0




