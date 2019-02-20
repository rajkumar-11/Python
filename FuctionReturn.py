def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_18=create_adder(15)
print(add_18(10))