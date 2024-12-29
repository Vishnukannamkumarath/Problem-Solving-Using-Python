n=int(input("Enter Limit: "))
list=[];req_list=[];j=0
for i in range(n):
    list.append(int(input(f"Number{i}: ")))
list.sort()
while(j<len(list)-j-1):
    req_list.append(list[len(list)-j-1])
    req_list.append(list[j])
    j+=1
print(req_list)
