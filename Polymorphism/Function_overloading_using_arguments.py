def add (*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        result = args[0]
        for arg in args[1:]:
            result += arg
        return result
    
print(add(1,2,3))
print(add(1))
print(add())
    