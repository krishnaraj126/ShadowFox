friends = ["Krishna","Neeraj","Meenagayathri","Raja Venkat","Subhash","AdithyaKrishna"]

result = []

for i in friends:
    info = (i,len(i))
    result.append(info)

print("List of Tuples (Name , Length) :")
print(result)