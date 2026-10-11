list=[]
count=0
nlist=[]
for i in range(1,11):
    value=list.append(int(input(f"enter number {i} to check:")))
for k in list:
    rev=0
    temp=k
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
        
    if k==rev:
        print(f"valid palindrome found:{k}")
        nlist.append(k)
        count+=1
print(f"total number of palindrome at end:{count}")
print(f"total palindromes are:{nlist}")
print(f"original list is:{list}")