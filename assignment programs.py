#1.WAP to print 10 natural numbers

i=1
while i<=10:
    print(i)
    i=i+1   

#2.WAP to print first 10 natural numebrs along with its cube

i=1
while i<=10:
    print(i,i**3)
    i=i+1

#3.WAP to print first 10 natural numbers in reverse order

i=10
while i<=10:
    print(i)
    i-=1

#4.WAP to print sum of first 10 natural numbers

i=1
s=0
while i<=10:
    s=s+i
    i+=1
print(s)

#5.WAP to print characters present in the given string

st=input('enter string')
i=0
while i<len(st):
    print(st[i])
    i+=1

#6.WAP to print the values present in given heterogenous list collection

l=[2,'a',[3],True,8+5j]
i=0
while i<len(l):
    print(l[i])
    i+=1

#7.WAP to copy characters present in one str to another str

st=input('enter string')
s=''
i=0
while i<len(st):
    s+=st[i]
    i+=1
print(s)

#8.WAP to copy characters present in one lsit to another list

l=[2,'a',[3],True,8+5j]
l1=[]
i=0
while i<len(l):
    l1+=[l[i]]
    i+=1
print(l1)

#9.WAP to print good morning exactly at 5 times 

s='good morning'
i=1
while i<=5:
    print(s)
    i+=1

#10.WAP to print all even numbers from range 1 to 50

i=1
while i<=50:
    if i%2==0:
        print(i)
    i+=1

#or

i=2
while i<=50:
    print(i)
    i+=2

#11. WAP to print the table of the given number 

n=int(input('enter number'))
i=1
while 1<=10:
    print(n,'*',i,'=',n*i)
    i+=1

#12.WAP to print all characters present at even index

st=input('enter string')
i=0
while i<len(st):
    if i%2==0:
        print(st[i])
    i+=1

#13.WAP to extract all the lower case alhpa present in given string 

st=input('enter string')
s=''
i=0
while i<len(st):
    if 'a'<=st[i]<='z':
        s+=st[i]
    print(s)
    i+=1

#14.WAP to print those numbers divisible by 5 & 7 ranges from 1500 to 2700 
 
i=1500
while i<=2700:
    if i%5==0 and i%7==0:
        print(i)
    i+=1

#15.WAP to extract all the specal char present at odd index from string

st=input('enter str: ')
s=''
i=0
while i<len(st):
    if not('A'<=st[i]<='Z' or 'a'<st[i]<='z' or '0'<=st[i]<='9'):
        if i%2==1:
            s+=st[i]
            print(s)
    i+=1
    #or
i=1
while i<len(st):
    if not('A'<=st[i]<='Z' or 'a'<st[i]<='z' or '0'<=st[i]<='9'):
        s+=st[i]
        print(s)
    i+=2

#16.WAP to print cube of all numbers upto n

n=int(input('enter num: '))
i=0
while i<=n:
    print(n**3)
    i+=1

#17.WAP to print sum of individual digits of given integer number

n=int(input('enter number'))
s=0
while n>0:
    rem = n%10
    s+=rem
    n=n//10
print(s)

#18.WAP to print factorial of given integer number

n=int(input('enter number'))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

#19.WAP to check whether the given integer is palindrome or not

n=int(input('enter num'))
a=n
p=0
while n>0:
    rem=n%10
    p=p*10+rem
    n=n//10
if a==p:
    print('palindrome')
else:
    print('not a palindrome')

#20.WAP to seperate all the different characters present in given string to different variables

st=input('enter string')
u=''
l=''
n=''
s=''
i=0
while i<len(st):
    if 'A'<=st[i]<='Z':
        u+=st[i]
    elif 'a'<=st[i]<='z':
        l+=st[i]
    elif '0'<=st[i]<='9':
        n+=st[i]
    else:
        s+=st[i]
    i+=1
print('Upper=',u,'\nLower=',l,'\nNum=',n,'\nSpecial=',s)

#21.WAP to check whether given string is palindrome or not without using slicing

s=input('enter the str: ')
p=''
i=0
while i<len(s):
    p=s[i]+p
    i+=1
if s==p:
    print('palindrome')
else:
    print('not a palindrome')

#22.WAP to toggle the given input string

st=input('enter string')
i=0
o=''
while i<len(st):
    if 'A'<=st[i]<='Z':
        o+=chr(ord(st[i])+32)
    elif 'a'<=st[i]<='z':
        o+=chr(ord(st[i])-32)
    else:
        o+=st[i]
    i+=1
print(o)

#23.WAP to print product of given individual digits of given integer

n=int(input('enter num'))
p=1
while n>0:
    r=n%10
    p*=r
    n//10
print(p)

#24.WAP to extract all the complex data items present in heterogenous list collection. If legnth of output is >=3 then print output else print
# input list 

l=[1,2+3j,4,5j,7j]
i=0
out=[]
while i<len(l):
    if type(l[i])==complex:
        out+=[l[i]]
    i+=1
if len(out)>=3:
    print(out)
else:
    print(l)

#25.WAP to find sum of ascii value of all lower case alpha present at even index from string only if string is odd

s=input('enter string')
i=0
st=0
if len(s)%2==1:
    while i<len(s):
        if 'a'<=s[i]<='z':
            st+=ord(s[i])
        i+=2
    print(st)
else:
    print('string is even')

#26.WAP to print following series -> 10,20,30,40,..,200.
 
n=10
while n<=200:
    if n==200:
        print(n,end='.')
    else:
        print(n,end=',')
    n+=10
    #or
n=10
s=''
while n<=200:
    if n==200:
        s+=str(n)+'.'
    else:
        s+=str(n)+','
    n+=10
print(s)

#27.WAP to print the following output
#input -> 'roses are red'
#output -> ['sesor',3,'der']

s=input('enter string')
l=s.split()
i=0
out=[]
while i<len(l):
    if i%2==0:
        out+=[l[i][::-1]]
    else:
        out+=[len(l[i])]
    i+=1
print(out)


#28.WAP to print the following output
#input -> 'i am a fan of vijay'
#output -> {'i':1, 'am':2, 'a':1, 'fan':3, 'of':2, 'vijay':5}

s=input('enter string')
l=s.split()
i=0
d={}
while i<len(l):
    d[l[i]]=len(l[i])
    i+=1
print(d)

#29.WAP to print the following output
#input -> 'i am a fan of vijay'
#output -> {'i':1, 'am':1, 'a':1, 'fan':1, 'of':1, 'vijay':2}

st=input('enter string ')
s=st.split()
d={}
i=0
while i<len(s):
    if len(s[i])<5:
        d[s[i]]=1
    else:
        d[s[i]]=len(s[i])
    i+=1
print(d)

#30.WAP to print the following output
#input -> 'i am a fan of vijay'
#output -> {'i':'a', 'am':'ma', 'a':'a', 'fan':'naf', 'of':'fo', 'vijay':'jyajiv'}

s=input('enter string')
l=s.split()
i=0
d={}
while i<len(l):
    d[l[i]]=d[l[i][::-1]]
    i+=1
print(d)

#31.WAP to extract all even integers numbers present at odd index from given heter list collection

l=[1,3,4j,6,'a']
i=1
n=[]
while i<len(l):
    if type(l[i])==int and l[i]%2==0:
        n+=[l[i]]
    i+=2
print(n)

#32.WAP to remove all duplicate values present in the given list collection

l=[1,6,4j,6,'a','a']
d=[]
i=0
while i<len(l):
    if l[i] not in d:
        d+=[l[i]]
    i+=1
print(d)

#33.WAP to remove odd index char from string

s=input('enter string')
i=0
s1=''
while i<len(s):
    s1+=s[i]
    i+=2
print(s1)

#34.WAP to print following series -> 105,98,91,...,7.

n=105
while n>=7:
    if n==7:
        print(n,end='.')
    else:
        print(n,end=',')
    n-=7

#35.WAP to find sum of all numbers which are divisble by 5 from range of 1 to 100

n=1
s=0
while n<=100:
    if n%5==0:
        s+=n
    n+=1
print(s)

#36.WAP to find sum of all numbers which are div by 7 and should present at even index from hetero tuple collection

t=(1,2,'a',5,6j)
s=0
i=0
while i<len(t):
    if type(t[i])==int and t[i]%7==0:
        s+=t[i]
    i+=2
print(s)

#37.WAP to store ascii value of all the lower case alpha present in string only if it is odd

s=input('enter string ')
st=[]
i=0
while i<len(s):
    if 'a'<=s[i]<='z' and ord(s[i])%2==1:
        st+=[ord(s[i])]
    i+=1
print(st)

#38.WAP to extract all alphabet whose ascii value is even from string

s=input('enter string ')
st=''
i=0
while i<len(s):
    if ord(s[i])%2==0:
        st+=s[i]
    i+=1
print(st)

#39.WAP to check the given integer number is prime or not

n=int(input('enter num '))
i=2
c=0
while i<n:
    if n%i==0:
        c+=1
    i+=1

if c==0:
    print('prime')
else:
    print('not prime')

#40.WAP to check the given integer number is perfect or not

n=int(input('enter num '))
s=0
i=1
while i<n:
    if n%i==0:
        s+=i
    i+=1
if s==n:
    print('perfect')
else:
    print('not perfect')

#41.WAP to check the given number is armstrong or not

n=int(input('enter num '))
a=n
l=len(str(n))
s=0
while n>0:
    r=n%10
    s+=r**l
    n=n//10
if a==s:
    print('armstrong')
else:
    print('not armstrong')

#42.WAP to split the given heterogenous list to SVDT and MVDT

l=[52,4,True,[5,3],6j,{1:4}]
i=0
s=[]
m=[]
while i<len(l):
    if type(l[i]) in [int,float,bool,complex]:
        s+=[l[i]]
    else:
        m+=[l[i]]
    i+=1
print(s)
print(m)

#43.WAP to check the given string is having one special char or not

s=input('enter string')
i=0
st=''
while i<len(s):
    if not('A'<=s[i]<='Z' or 'a'<=s[i]<='z' or '0'<=s[i]<='9'):
        st+=s[i]
    i+=1
if s==st:
    print('spcl char')
else:
    print('not spcl char')


#------------------------------------Assignment Questions------------------------------------#

#1.Python example for ASCII value of a single character

c=input('enter a character')
print(ord(c))

#2.Python program to print ASCII value of total characters in string

s=input('enter a string')
i=0
while i<len(s):
    print(ord(s[i]))
    i+=1

#3.Python program to concatenate strings

s1=input('enter a string')
s2=input('enter a string')
s3=s1+s2
print(s3)

#4.Python program to convert string to upper case

s=input('enter a string')
print(s.upper())
    #or
s=input('enter a string')
i=0
u=''
while i<len(s):
    if 'a'<=s[i]<='z':
        u+=chr(ord(s[i])-32)
    else:
        u+=s[i]
    i+=1
print(u)

#5.Python program to convert string to lower case
s=input('enter a string')
print(s.lower())
    #or
s=input('enter a string')
i=0
u=''
while i<len(s):
    if 'A'<=s[i]<='Z':
        u+=chr(ord(s[i])+32)
    else:
        u+=s[i]
    i+=1
print(u)

#6.Python program to copy a string

s1=input('enter a string')
s2=''
i=0
while i<len(s1):
    s2+=s1[i]
    i+=1
print(s2)

#7.Python program to count occurance of a character in a string
st=input('enter string')
i=0
count=0
c=input('enter string to be count')
while i<len(st):
    if st[i]==c:
        count+=1
    i+=1
print(count)

#8.Python program to count total characters in a string

st=input('enter string')
i=0
count=0
while i<len(st):
    count+=1
    i+=1
print(count)

#9.Python program to count total number of words in a string

st=input('enter string')
i=0
count=1
while i<len(st):
    if st[i]==' ':
        count+=1
    i+=1
print(count)

#10.Python program to count vowels in a string 

st=input('enter string')
i=0
count=0
while i<len(st):
    if st[i] in 'aeiouAEIOU':
        count+=1
    i+=1
print(count)

#11.Python program to count vowels and consonant in a string

st=input('enter string')
c1=0
c2=0
i=0
while i<len(st):
    if st[i] in 'aeiouAEIOU':
        c1+=1
    else:
        c2+=1
    i+=1
print('vowels',c1)
print('consonant',c2)

#12.Python program to count alpha digit and special chars in a string

st=input('enter string')
c1=0
c2=0
c3=0
i=0
while i<len(st):
    if 'A'<=st[i]<='Z' or 'a'<=st[i]<='z':
        c1+=1
    elif '0'<=st[i]<='9':
        c2+=1
    else:
        c3+=1
    i+=1
print('alpha',c1)
print('digits',c2)
print('special chars',c3)

#13.Python program to print first occurance of a character in a string

st=input('enter string')
c=input('emter char')
i=0
while i<len(st):
    if st[i]==c:
        print(c,'ind',i)
        break
    i+=1

#14.Python program to print last occurance of a character in a string

st=input('enter string')
c=input('emter char')
i=len(st)-1
while i>=0:
    if st[i]==c:
        print(c,'ind',i)
        break
    i-=1

#15.Python program to check palindrome or not

n=int(input('enter num'))
p=0
a=n
while n>0:
    r=n%10
    p=p*10+r
    n=n//10
if a==p:
    print('palindrome')
else:
    print('not a palindrome')

#16.Python program to print characters in a string

st=input('enter string')
i=0
while i<len(st):
    print(st[i])
    i+=1

#17.Python program to replace blank space with hyphen in a string

st=input('enter string')
i=0
s=''
while i<len(st):
    if st[i]==' ':
        s+='-'
    else:
        s+=st[i]
    i+=1
print(s)
    #or
st=input('enter string')
s=st.replace(' ','-')
print(s)

#18.Python program to replace characters in a string

st=input('enter string')
c=input('enter char to replace')
ch=input('emter new char')
s=''
i=0
while i<len(st):
    if st[i]==c:
        s=ch
    else:
        s+=st[i]
    i+=1
print(st)

#19.Python program to remove odd characters in a string

st=input('enter string')
i=0
while i<len(st):
    if i%2==1:
        print(st[i],end='')
    i+=1

#20.Python program to remove odd index characters in a string

st=input('enter string')
i=0
while i<len(st):
    if i%2==0:
        print(st[i],end='')
    i+=2

#21.Python program to remove first occurance of a character in a string

s=input('enter string ')
i=0
st=input('enter char')
o=''
while i<len(s):
    if s[i]==st:
        o+=''
    else:
        o+=s[i]
    i+=1
print(o)

#22.Python program to remove last occurance of a character in a string

s=input('enter string ')
i=len(s)-1
st=input('enter char')
o=''
while i>=0:
    if s[i]==st:
        o+=''
    else:
        o=s[i]+o
    i-=1
print(o)

#23.Python program to reverse a string

s=input('enter string ')
st=''
i=0
while i<len(s):
    st=s[i]+st
    i+=1
print(st)
    #or
s=input('enter string ')
st=''
i=len(s)-1
while i>=0:
    st+=s[i]
    i-=1
print(st)

#24.Python program to find length of a string using while loop

s=input('enter string ')
i=0
c=0
while i<len(s):
    c+=1
    i+=1
print(c)
    #or
s=input('enter string ')
print(len(s))

#25.Python program to find total occurance of a character in a string

s=input('enter string ')
st=input('enter char')
c=0
i=0
while i<len(s):
    if s[i]==st:
        c+=1
    i+=1
print(c)

#26.Python program to toggle characters case in a string

s=input('enter string ')
i=0
st=''
while i<len(s):
    if 'A'<=s[i]<='Z':
        st+=chr(ord(s[i])+32)
    elif 'a'<=s[i]<='z':
        st+=chr(ord(s[i])-32)
    else:
        st+=s[i]
    i+=1
print(st)

#27.Python program to find sum of natural numbers

n=int(input('enter num '))
i=1
s=0
while i<=n:
    s+=i
    i+=1
print(s)

#28.Python program to sun the even numbers

n=int(input('enter numb '))
i=0
s=0
while i<=n:
    if i%2==0:
        s+=i
    i+=2
print(s)

#29.Python example to find sum and avg of natural numbers 

n=int(input('enter num '))
i=1
s=0
while i<=n:
    s+=i
    i+=1
print('sum=',s)
print('avg=',s/i)

#30.Python example to find sum of odd numbers

n=int(input('enter numb '))
i=1
s=0
while i<=n:
    if i%2==1:
        s+=i
    i+=2
print(s)

#31.Python example to find sum of even and odd numbers

n=int(input('enter nu m '))
e=0
o=0
i=0
while i<=n:
    if i%2==0:
        e+=i
    else:
        o+=i
    i+=1
print('even sum=',e)
print('odd sum=',o)

#32.Python example to access list index and value

l=[2,4,5j,True]
i=0
while i<len(l):
    print('list index',i,'list values',l[i])
    i+=1

#33.Python program to add two list

l1=[2,4,6,True]
l2=[5j,[4,5],7]
print('l3=',l1+l2)
    #or 
l1=[2,4,6,True]
l2=[5j,[4,5],7]
l3=[]
i=0
j=0
while i<len(l2):
    while j<len(l1):
        l3+=[l1[j]]
        j+=1
    l3+=[l2[i]]
    i+=1
print(l3)

#34.Python example for arithemetic operations on lists

l1=[10,20,30,40]
l2=[20,40,20,50]
i=0
r=[]
while i<len(l1) and i<len(l2):
    add=l1[i]+l2[i]
    sub=l1[i]-l2[i]
    mul=l1[i]*l2[i]
    if l2[i]!=0:
        div=l1[i]/l2[i]
        fdiv=l1[i]//l2[i]
        mod=l1[i]%l2[i]
    else:
        print('div by zero')
    print(l1[i],'+',l2[i],'=',add)
    print(l1[i],'-',l2[i],'=',sub)
    print(l1[i],'*',l2[i],'=',mul)
    print(l1[i],'/',l2[i],'=',div)
    print(l1[i],'//',l2[i],'=',fdiv)
    print(l1[i],'%',l2[i],'=',mod)
    print('-'*20)
    i+=1

#35.Python program to check list is empty or not

l=[2,3,5j]
if l==[]:
    print('list is empty')
else:
    print('list is not empty')

#36.Python example to clone or copy the list

l=[2,3,5j]
l1=[]
i=0
while i<len(l):
    l1+=[l[i]]
    i+=1
print(l1)
    #or
l=[2,3,5j]
l1=[]
if l not in l1:
    l1+=l
print(l1)

#37.Python program to count even and odd numbers in a list

l=[1,2,3,4,5,6,7,8,9,10]
i=0
e=0
o=0
while i<len(l):
    if l[i]%2==0:
        e+=1
    else:
        o+=1
    i+=1
print('even',e)
print('odd',o)

#38.Python program to count positive and negative numbers in a list

l=[1,2,3,4,5,6,7,8,9,10]
i=0
p=0
n=0
while i<len(l):
    if l[i]>0:
        p+=1
    else:
        n+=1
    i+=1
print('positive',p)
print('negative',n)

#39.Python program to print largest number in a list 

l=[1,2,3,4,5,6,7,8,9,10]
i=0
m=l[0]
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)

#40.Python program to print largest and smallest number 

l=[1,2,3,4,5,6,7,8,9,10]
i=0
m=l[0]
s=l[0]
while i<len(l):
    if l[i]>m:
        m=l[i]
    if l[i]<s:
        s=l[i]
    i+=1
print('largest',m)
print('smallest',s)

#1

s=input('enter a character')
print(ord(s))

#2

st=input('enter a string')
i=0
while i<len(st):
    print(ord(st[i]))
    i+=1

#3

st1=input('enter a string')
st2=input('enter a string')
print(st1+st2)

#4

st=input('enter a string')
i=0
U=''
while i<len(st):
    if 'A'<=st[i]<='Z':
        U+=st[i]
    else:
         U+=chr(ord(st[i])-32)
    i+=1
print(U)

#5

st=input('enter a string')
i=0
L=''
while i<len(st):
    if 'a'<=st[i]<='z':
        L+=st[i]
    else:
         L+=chr(ord(st[i])+32)
    i+=1
print(L)

#6

st1=input('enter a string')
st2=''
i=0
while i<len(st1):
    st2+=st1[i]
    i+=1
print(st2)

#7

st=input('enter string')
i=0
cnt=0
char=input('enter string to be count')
while i<len(st):
    if st[i]==char:
        cnt+=1
    i+=1
print(cnt)

#8

st=input('enter string')
i=0
cnt=0
while i<len(st):
    cnt+=1
    i+=1
print(cnt)

#9

st=input('enter string')
i=0
cnt=1
while i<len(st):
    if st[i]==' ':
        cnt+=1
    i+=1
print(cnt)

#10

st=input('enter string')
i=0
cnt=0
while i<len(st):
    if st[i] in 'AEIOUaeiou':
        cnt+=1
    i+=1
print(cnt)

#11
st=input('enter the string')
vcnt=0
ccnt=0
i=0
while i<len(st):
    if st[i] in 'AEIOUaeiou':
        vcnt+=1
    else:
        ccnt+=1
    i+=1
print('vowel count is',vcnt)
print('consonent count is',ccnt)

#12

st=input('enter the str')
U=0
L=0
N=0
S=0
i=0
while i<len(st):
    if 'A'<=st[i]<='Z':
        U+=1
    elif 'a'<=st[i]<='z':
        L+=1
    elif '0'<=st[i]<='9':
        N+=1
    else:
        S+=1
    i+=1
print('cnt of upper:',U)
print('cnt of lower:',L)
print('cnt of number:',N)
print('cnt of special char:',S)

#13

st=input('enter the string')
ch=input('enter char to  be searched')
i=0
while i<len(st):
    if st[i]==ch:
        print('1st accurence of',ch,'is',i)
        break
    i+=1

#14

st=input('enter the string')
ch=input('enter char to  be searched')
i=len(st)-1
while i>=0:
    if st[i]==ch:
        print('1st accurence of',ch,'is',i)
        break
    i-=1


#15

st=input('enter the string')
s=''
i=0
while i<len(st):
    s=st[i]+s
    i+=1
if st==s:
    print(st,'is palindrome')
else:
    print(st,'is not palondrome')

#16

st=input('enter the string')
i=0
while i<len(st):
    print(st[i])
    i+=1

#17

st=input('enter the string')
out=''
i=0
while i<len(st):
  if st[i]==' ':
    out+='-'
  else:
    out+=st[i]
  i+=1
print(out)

#18

st=input('enter the str')
ch=input('enter the char to be reolaced')
re=input('enter the new char')
s=''
i=0
while i<len(st):
  if st[i]==ch:
    s+=re
  else:
    s+=st[i]
  i+=1
print(s)

#19

st=input('enter the str')
s=''
i=1
while i<len(st):
  s+=st[i]
  i+=2
print(s)

#20

st=input('enter the str')
s=''
i=1
while i<len(st):
  s+=st[i]
  i+=2
print(s)'''
    
