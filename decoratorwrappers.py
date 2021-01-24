
def decorator_func(argumentRecieve_func):
    def execution_func():
        print("This function will be displayed before {} because this is executed first!!".format(argumentRecieve_func))
        argumentRecieve_func()  #this needs to be a function because it's being treated as such.
    return execution_func


@decorator_func #This basically calls the decarotor function I.e it is same as :Decorator = decorator_func(randomparafun())
def randomparafun():
    print("This is a random sentence that will be diplayed:")
    
randomparafun()


# """
# def randomparafun():
#     print("This is a random sentence that will be diplayed:")

# Decorator = decorator_func(randomparafun())
# Decorator()

# The command you can see ^here above can be wriiten as I've shown below as well
# """



# def afuncfordecoration(theinsidearg):
#     def container():
#         print "This is also inside the arg"
#         return theinsidearg()
#     return container

# @afuncfordecoration
# def printthisforinsidearg():
#     print("This is what you are printing from outside into the container!!!!!")
# printthisforinsidearg()

    




















