def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("Sorry ! you are dividing by zero")
    else:
        print("yeah! your answer is :",result)
    finally:
        print("I'm finally Clause,Always Raised!!")

divide(3,0)