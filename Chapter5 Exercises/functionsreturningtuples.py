# 5.6 (Functions Returning Tuples) Define a function rotate that receives three arguments
# and returns a tuple in which the first argument is at index 1, the second argument
# is at index 2 and the third argument is at index 0. Define variables a, b and c containing
# 'Doug', 22 and 1984. Then call the function three times. For each call, unpack its result
# into a, b and c, then display their values.


def rotate(arg1, arg2, arg3):
    return arg3, arg1, arg2


a, b, c = 'Doug', 22, 1984

result = a, b, c = rotate(a, b, c)
print(result)
result = a, b, c = rotate(a, b, c)
print(result)
result = a, b, c = rotate(a, b, c)
print(result)