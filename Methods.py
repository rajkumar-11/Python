import math
def decorate_message(fun):
    def addWelcome(site_name):
        return "Welcome to "+fun(site_name)

    return addWelcome
@decorate_message
def site(site_name):
    return site_name
print(site("geeksforgeeks"))

flag=False
if(flag==False):
    pass
else:
    print("shouldnt have come here")

def fun():
    str="rajkumar"
    x=20
    return [str,x];
str,x=fun()
print(str)
print(x)
z=3.435
print(math.trunc(z))
print(math.ceil(z))
print(math.floor(z))
print('%0.2f'%z)
print("{0:.3f}".format(z))
print(round(z,4))

def testify(arg1,*argv):
    print("first argument",arg1)
    for arg in argv:
        print("next argument is ",arg)

testify('hello')


def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    innerFunction()


if __name__ == '__main__':
    outerFunction('Hey!')

def outerFunction(text):
    text=text
    def innerFunction():
        print(text)

    return innerFunction
myFunction=outerFunction("Monika!")

myFunction()


def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


corou = print_name("Dear")
corou.__next__()
corou.send("Atul")
corou.send("Dear Atul")
corou.close()





































