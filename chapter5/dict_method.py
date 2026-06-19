marks={
    "rahul": 67,
    "ramesh": 89,
    "sushil": 56,
    "anil": 78,
    "sunil": 90,
    "raju": 45

}
# print(marks.items()) # dict_items([('rahul', 67), ('ramesh', 89), ('sushil', 56), ('anil', 78), ('sunil', 90), ('raju', 45)])
# print(marks.keys()) # dict_keys(['rahul', 'ramesh', 'sushil', 'anil', 'sunil', 'raju'])
# print(marks.values()) # dict_values([67, 89, 56, 78, 90, 45])
# marks.update({"ramesh": 95, "vicky": 85}) # it will update the value of the key "ramesh" to 95 and "anil" to 85

# print(marks.get("ramesh")) # 89
# print(marks.get("vicky")) # None
# print(marks.clear()) # it will clear the dictionary and return None
# print(marks.pop("ramesh")) # 89
# print(marks.popitem()) # ('raju', 45)
# print(marks.setdefault("vicky", 85)) # 85
print(marks) # {'rahul': 67, 'ramesh': 89, 'sushil': 56, 'anil': 78, 'sunil': 90, 'raju': 45, 'vicky': 85}
