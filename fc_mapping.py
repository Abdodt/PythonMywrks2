
def sqaures(x):
    return x*x

def cube(x):
    return x*x*x

def mapper(this_func,myArgs):
    result = []
    for i in myArgs:
        result.append(this_func(i))
    return result

Square_result = mapper(sqaures,[2,3,4,5,6]) #we input values into (this_fun = squares) 
print(Square_result)

Cube_result = mapper(cube,[2,3,4,5,6])
print(Cube_result)



