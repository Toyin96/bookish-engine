# 5.7 (Duplicate Elimination) Create a function that receives a list and returns a (possibly
# shorter) list containing only the unique values in sorted order. Test your function with
# a list of numbers and a list of strings.

def duplicate_searcher(arg1):
    """Removes duplicate elements in a sequence"""
    new_arg1 = []
    for i in arg1:
        if arg1.count(i) == 1:
            new_arg1.append(i)
    return new_arg1


toyin = [1, 2, 3, 4, 5, 6, 1, 2, 9, 8, 8]

print(duplicate_searcher(toyin))