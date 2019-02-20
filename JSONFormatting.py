import json
from io import StringIO

fileObj=StringIO()
json.dump(["Hello","Geeks"],fileObj)
print("using json .dump():"+str(fileObj.getvalue()))

class TypeEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,type):
            return str(obj)

print("Using json.dumps():"+str(json.dumps(type(str),cls=TypeEncoder)))
print("using json.JSONEncoder().encode"+str(TypeEncoder().encode(type(list))))
print("using json.JSONEncoder().iteraencaode"+str(list(TypeEncoder().iterencode(type(dict)))))