list1 = [{'array1':10}]

list2 = []

list2.extend(list1)

print(list2)

list1.append({'array2':20})
list2.extend(list1)

print(list2)
