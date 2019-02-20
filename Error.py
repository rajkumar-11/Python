class Error(Exception):
    pass
class TrasitionError(Error):
    def __init__(self,prev,nex,msg):
        self.prev=prev
        self.next=nex
        self.msg=msg
try:
    raise(TrasitionError(2,3*2,"Not Allowed"))
except TrasitionError as error:
    print("Exception occured",error.msg)