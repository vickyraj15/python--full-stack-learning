s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(s) # {20, '20'} it will return a set with the unique values of the list because 20 and 20.0 are considered equal in Python
