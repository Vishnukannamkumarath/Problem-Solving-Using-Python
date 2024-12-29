mob_list=[];i=0;count=0
while(1):
    user=input()
    if(user=='q' or user=='Q'):
        break
    else:
        mob_list.append(user)
    i+=1
if(i!=5):
    print("INPUT LIMIT IS 5")
    exit(0)
for i in mob_list:
    if(len(i)==10 and i.isdigit()):
        count+=1
print(count)