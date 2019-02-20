import decimal

a=decimal.Decimal(4.5).ln()
b=decimal.Decimal(4.5).log10()

print("The exponent of decimal number is :",end="")

print(a)

print(" The square root of decimal is ",end="")

print(b)

x=decimal.Decimal(9.53)

y=decimal.Decimal(-9.56)

print(x.compare(y))

print(x.compare_total_mag(y))