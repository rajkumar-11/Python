names=['rajkumar','dharm','prachi', 'anu']
names2=['gru','dave','stuart']
names.extend(names2)
names.remove('gru')
names.sort()
print(names,len(names),names[-3:2])