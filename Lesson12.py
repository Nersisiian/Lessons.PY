mylist = [10, -7, 6, -9, -150, 8, 35, -1]

neg_indices = {i for i, v in enumerate(mylist) if v < 0}
positives = [v for v in mylist if v >= 0]

result = []
p = 0  

for i in range(len(mylist)):
    if i in neg_indices:
        result.append(mylist[i])  
    else:
        result.append(positives[p])  
        p += 1

print("Исходный  :", mylist)
print("Результат :", result)