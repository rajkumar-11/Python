from _ast import Name

try:
    a=4
    if a < 4:
        b=a/(a-3)
    print("value of b=",b)

except(ZeroDivisionError,NameError):
     print("error occured and handled",NameError)