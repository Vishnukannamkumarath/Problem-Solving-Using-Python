list1=[];req_list=[];j=0;str_list=[]
n=int(input())
numbers=input()
str_list=numbers.split(' ')
list1=list(map(int,str_list))
while(j<=len(list1)-j-1):
    if(j==len(list1)-j-1):
        req_list.append(list1[len(list1)-j-1])
        break
    else:
        req_list.append(list1[len(list1)-j-1])
        req_list.append(list1[j])
        j+=1
print(*req_list)
