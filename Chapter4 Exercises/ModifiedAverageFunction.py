def average(arg1, *args):
    """Returns the average of the argument(s) passed""" 
    return (arg1 + sum(args)) / (1 + len(args))

        
    
print(average(20, 2))