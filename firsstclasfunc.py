
def sqaures(x):
    return x*x

def mapper(this_func,myArgs):
    result = []
    for i in range(myArgs):
        result.append(this_func(i))
    return result

    Square_result = mapper(square,[2,3,4,5,6])
    print(Square_result)




