class PrintingObject:
     def __init__(self,a,b):
         self.a=a
         self.b=b
     def __repr__(self):
         return "Test a:%s b:%s" % (self.a, self.b)
     # def __str__(self):
     #    return "From str method of Test : a is %s, b is %s" %(self.a,self.b)

t=PrintingObject(1234,5678)
print((t))
print([t])