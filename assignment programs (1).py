1) Python example for ascii value of single char

a=input('enter a char:')
print(a,'=',ord(a))

2) Python program to print ascii value of total characters in a string

a=input('enter a str:')
for i in a:
    print(i,'=',ord(i))

3) Python program to concatenate strings

a=input('enter a str:')
b=input('enter a str:')
for i in b:
    a+=i
print(a)

4) Python program to convert string to upper case

a=input('enter a str:')
b=''
for i in a:
    if 'a'<=i<='z':
        b+=chr(ord(i)-32)
    else:
        b+=i
print(b)

5) Python program to convert string to lowercase

a=input('enter a str:')
b=''
for i in a:
    if 'A'<=i<='Z':
        b+=chr(ord(i)+32)
    else:
        b+=i
print(b)

6) Python program to copy a string

a=input('enter a str:')
b=''
for i in a:
    b+=i
print(b)

7) Python program to count occurance of a char in a string

a=input('enter a str:')
b=input('enter a char:')
c=0
for i in a:
    if i==b:
        c+=1
print(c)

8) Python program to count total characters in a string

a=input('enter a str:')
c=0
for i in a:
    c+=1
print(c)

9) Python program to count total words in a string

a=input('enter a str:')
c=1
for i in a:
    if i==' ':
        c+=1
print(c)

10) Python program to count vowels in a string

a=input('enter a str:')
c=0
for i in a:
    if i in 'aeiouAEIOU':
        c+=1
print(c)

11) Python program to count vowels and consonants in a string

a=input('Enter a str :')
v=0
c=0
for i in a:
    if i in 'aeiouAEIOU':
        v+=1
    else:
        c+=1
print(v)
print(c)

12) Python program to Count Alphabets, Digits and Special Characters in a String

st=input('enter the str:')
uc=0
lc=0
dig=0
sc=0
for i in st:
    if 'A'<=i<='Z':
        uc+=1
    elif 'a'<=i<='z':
        lc+=1
    elif '0'<=i<='9':
        dig+=1
    else:
        sc+=1
print('count of uppercase:',uc)
print('count of lowercase:',lc)
print('count of digits:',dig)
print('count of special character:',sc)

13) Python program to check Palindrome or Not

st=input('enter the str:')
s=''
for i in st:
    s=i+s
if st==s:
    print(st,'is palindrome')
else:
    print(st,'is not palondrome')

14) Python program to Print Characters in a String

st=input('enter the str:')
for i in st:
    print(i)

15) Python program to Replace Blank Space with Hyphen in a String

st=input('enter the str:')
s=''
for i in st:
  if i==' ':
    s+='-'
  else:
    s+=i
print(s)

16) Python program to Replace Characters in a String

st=input('enter the str:')
ch=input('enter the char to be replaced:')
c=input('enter the new char:')
s=''
for i in st:
  if i==ch:
    s+=c
  else:
    s+=i
print(s)

17) Python program to Remove Odd Characters in a String

st=input('enter the str:')
s=''
for i in st:
    if ord(i)%2==0:
        s+=i
print(s)

18) Python program to Remove Odd Index Characters in a String

st=input('enter the str:')
s=''
for i in range(len(st)):
    if i%2==0:
       s+=st[i] 
print(s)

19) Python program to Reverse a String

st=input('enter the str:')
s=''
for i in st:
    s=i+s
print(s)

20) Python program to find String Length

st=input('enter the str:')
c=0
for i in st:
    c+=1
print(c)

21) Python program to Toggle Characters Case in a String

st=input('enter the str:')
s=''
for i in st:
    if 'A'<=i<='Z':
        s+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        s+=chr(ord(i)-32)
    else:
        s+=i
print(s)

22) Python program to find the sum of Natural Numbers

n=int(input('Enter a num :'))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

23) Python program to find the sum of even numbers

n=int(input('Enter a num :'))
sum=0
for i in range(0,n+1,2):
    sum+=i
print(sum)

24) Python program to find the sum of odd numbers

n=int(input('Enter a num :'))
sum=0
for i in range(1,n+1,2):
    sum+=i
print(sum)

25) Python program to find the sum and average of Natural Numbers

n=int(input('Enter a num :'))
sum=0
for i in range(1,n+1):
    sum+=i
avg=sum//n
print(sum)
print(avg)

26) Python program to find the sum of even and odd numbers

n=int(input('Enter a num :'))
odd=0
even=0
for i in range(1,n+1):
    if i%2==0:
        even+=i
    elif i%2==1:
        odd+=i
print(odd)
print(even)

27) Python example to access list index and values

l=[10,'abc',6+7j,False]
for i in range(len(l)):
    print('index :',i, 'value :',l[i])

28) Python example to add two lists

l=[10,'abc',6+7j,False]
li=[20,'def',7+8j,True]
lis=[]
for i in range(len(l)):
    lis+=[l[i]+li[i]]
print(lis)

29) Python program to clone or copy a list

l=[10,20]
li=[]
for i in l:
    li+=[i]
print(li)

30) Python program to count even and odd numbers in a list

l=[10,15,20,25,30]
even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

31) Python example to check if the list is empty or not

l=[10,'abc',6+7j,False]
count=0
for i in l:
    count+=1
if count==0:
    print(l,'is empty')
else:
    print(l,'is not empty')

32) Python program to print the largest number in a list

l=[10,20,30,40,100]
lar=0
for i in l:
    if i>lar:
        lar=i
print(lar)

33) Python program to print the smallest number in a list

l=[65,54,1,4,5,2]
small=l[0]
for i in l:
    if i<small:
        small=i
print(small)

34) Python program to print the second largest number in a list

l=[80,65,40,39,34,60,25,67]
large=0
sec_large=0
for i in l:
    if i>large:
        sec_large=large
        large=i
    elif i<large and i>sec_large:
        sec_large=i
print(sec_large)

35) Python program to find the length of the list

l=[65,54,1,4,5,2]
count=0
for i in l:
    count+=1
print(count)

36) Python program to count positive and negative numbers in a list

l=[65,-54,-1,4,5,2,-32]
pos=0
neg=0
for i in l:
    if type(i)==int:
        if i>0:
            pos+=1
        else:
            neg+=1
print('count of positive number:',pos)
print('count of negative number:',neg)

37) Python program to print the largest and smallest number in a list

l=[10,20,30,40,100]
lar=0
small=l[0]
for i in l:
    if i>lar:
        lar=i
    elif i<small:
        small=i     
print('largest number is:',lar)
print('smallest number is:',small)

38) Python list multiplicaton program

l=[10,20,30,40]
li=[12,35,45,55]
lis=[]
for i in range(len(l)):
    lis+=[l[i]*li[i]]
print(lis)

39) Python program to print the elements in the list

l=[10,20,30,40]
lis=[]
for i in l:
    lis+=[i]
print(lis)

40) Python program to print the list difference

l=[10,20,30,40]
li=[12,35,45,55]
lis=[]
for i in range(len(l)):
    lis+=[li[i]-l[i]]
print(lis)

41) Python programs to print even numbers in a list

l=[10,5j,8.4,]
lis=[]
for i in l:
    if type(i)==int:
        if i%2==0:
            lis+=[i]
print(lis)

42) Python programs to print odd list numbers in a list

l=[10,5j,8.4,9]
lis=[]
for i in l:
    if type(i)==int:
        if i%2==1:
            lis+=[i]
print(lis)

43) Python program to print positive numbers in a list

l=[10,5j,8.4,9]
lis=[]
for i in l:
    if type(i)==int:
        if i>0:
            lis+=[i]
print(lis)

44) Python program to print negative numbers in a list

l=[10,5j,-4,-19,9]
lis=[]
for i in l:
    if type(i)==int:
        if i<0:
            lis+=[i]
print(lis)

45) Python program to put even and odd numbers in a seperate list

l=[10,5j,-4,-19,9]
even=[]
odd=[]
for i in l:
    if type(i)==int:
        if i%2==0:
            even+=[i]
        else:
            odd+=[i]
print(even)
print(odd)

46) Python program to put positive and negative numbers in a seperate list

l=[10,5j,-4,-19,9]
pos=[]
neg=[]
for i in l:
    if type(i)==int:
        if i>0:
            pos+=[i]
        else:
            neg+=[i]
print(pos)
print(neg)

47) Python program to remove duplicates from the list

l=[10,'a',20,'a',10,67.9,False]
dup=[]
for i in l:
    if i not in dup:
        dup+=[i]    
print(dup)

48) Python program to remove even numbers from the list

l=[10,20.6,'a',9,67.9,False,True]
dup=[]
for i in l:
    if type(i)==int:
        if i%2==1:
            dup+=[i]    
print(dup)

49) python program to reverse the list items

l=[10,'a',67.9,False]
dup=[]
for i in l:
    dup=[i]+dup
print(dup)

50) Python program to sort elements in ascending order






