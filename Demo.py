# # a=100
# # b=20
# # print (a)
# # print (b)
# # print (a+b)
# # print (a-b)
# # _ = 10 
# # import keyword
# # print (keyword.kwlist)
# # Import = 2
# # s = "somesh"
# # print (s[::-1])
# # print (s[0::-1])
# # print (s[1::-1])
# # print (s[2::-1])
# # print (s[3::-1])
# # print (s[1::2])
# # t=("a b c")
# # print (type(t))
# # t=("abc")
# # print (type(t))
# # t=("a b c",)
# # print (type(t))
# # t=("a b c",)
# # print (type(t))
# # q=["a b c", 12]
# # print (type(q))
# # q=["a b c", ]
# # print (type(q))
# # q="a b c", 12
# # print (type(q))
# # q=["a b c", 12]
# # print (q[::-1])
# # q=["a b c", 12]
# # print (q[::-2])
# # q={"a b c", 12}
# # print (type(q))
# # q={ }
# # print (type(q))
# # print (-17//2)
# # print (12%145)
# # print (2**3**2)


# # s1 = [10, 12, 3.5, "abc"]
# # s2 = [0, 13, 4.8, "efg"]
# # print (s1+s2)

# # T1 = [10, 12, 3.5,]
# # T2 = ["efg",]
# # print (T1+T2)

# # d1 ={1:"s"}
# # d2 ={11:"r"}
# # print (d1+d2)

# # d1 ={1:"s"}
# # d2 ={11:"r"}
# # print (d1-d2)

# # d1 ={s:23}
# # d2 ={r:3}
# # print (d1-d2)

# # s1="a"
# # print (s1*0)

# print (int(8.9))
# print (int(-8.9))
# print (int(True))
# print (int(False))
# # print (int(0j))
# # print (int("abc"))
# print (int("10"))
# # print (int("abc"))
# print (float("10.5"))
# # print (int("abc"))
# print (int[10])

# print (float(6))
# print (float(-6))
# print (float(True))
# print (float(False))
# # print (float(5+7j))
# # print (float("a"))
# print (bool(0.000001))
# print (bool(5+1j))
# print (bool("a"))
# print (bool("n12"))
# print (bool("0.0"))

# print(set["q", [1], True])

# L=("XY", ((11, 15), "LO"), [["n"], nah], {True, 15}, {3:100, 2:200})
# print(dict(L))

# print (9 or 11)
# s = "space between words SPACE BETWEEN WORDS"
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize() )

# L=[12, 4.7, "na"]
# print(L.append(12.0))
# print(L)

# L=[12, 4.7, "na"]
# L.insert(4, "Somesh")
# print(L)

# L=[12, 4.7, "na"]
# L.insert(-6, "Somesh")
# print(L)

# L=[12, 4.7, "na"]
# L.extend("Somesh")
# print(L)

# L=[12, 4.7, "na"]
# L.clear()
# print(L)

# L=[12, 4.7, "na"]
# del(L)
# print(L)

# L=[12, 4.7, "na"]
# print(L.reverse())
# print(L)

# print("hello", sep="#")
# print("14 feb")
# print("is on friday")

# num1= float(input("Enter num1 = "))
# num2= float(input("Enter num2 = "))
# print(num1+num2)

# num= input("Enter your data = ")
# print(f"num+num")

# s="Somesh"
# for i in s:
#     print(i)
#     print(len(i))
# print("come in")

# s="Somesh"
# for char in s:
#     print(char*5)
# print(char)

# s = "Somesh"
# for i in range(-1,-7,-1) :
#     print(s[i])


# s = "Somesh"
# for i in range(len(s)5,-7,-1) :
#     print(s[i])

# s = "Rampure"
# rev = ""
# for i in range(len(s)-1,-8,-1) :
#     rev = rev + s[i] 
#     print(rev)

#     s = [10, "Somesh", 30]
# for i in range(len(s)-1,-4,-1) :
#     print(s[i])

# i=1
# while i <=5:
#     print("Somesh")
#     i += 1 

# num = 150

# # Loop to divide the number by 2 until it is less than 1
# while num >= 1:
#     print(num)
#     num //= 2


# class Company:
#     Cname = 'KPIT'
#     loc = 'Phase 3'
#     website = 'www.KPIT.com'
#     CEO = 'Kishor Patil'
#     def __init__(self, name, addr, cid, field):
#         self.name = name
#         self.addr = addr
#         self.cid = cid
#         self.field = field
# st1 = Company('Somesh','Pune',146, 'Tester')
# st2 = Company('Sakshi', 'Bangalore', 384, 'Dev')

# print (st1.name, st1.addr, st1.cid, st1.field) 
# print (st2.name, st2.addr, st2.cid, st2.field)

# class School:
#     __sname="JES"
#     __loc="Bangalore"
#     def __init__(self,stdname,rollno,phno):
#         self.__stdname=stdname
#         self.__rollno=rollno
#         self.__phno=phno
#     def getter(self):
#         return self.__stdname
#     def setter(self,new):
#         self.__stdname = new
# std1=School("Somesh",21,987612345)
# print (std1.getter())
# std1.setter("Prakash")
# print (std1.getter())

# from abc import ABC, abstractmethod
# class Calculator:
#     @abstractmethod
#     def add(a,b):
#         pass

# class Digital_Calculator(Calculator):
#     @staticmethod
#     def add (a,b):
#         print(a+b)
#     @staticmethod
#     def sub (a,b):
#         print(a-b)
# user = Digital_Calculator()
# user.add(10,20)
# user.sub(100,50)

# def vowel (str):
#     if str[0] in 'aeiouAEIOU':
#         return True
#     else :
#         return False
# print (vowel('Enter'))

# def add(a, b):
#     return a+b
# print(add(2,4))


# str = 'mapple'
# if str == str [::-1]:
#     print (str)
# else:
#     print (str [::-1])

# palindrome = lambda s:s if s == s[::-1] else s[::-1]
# print(palindrome('Apple'))

# cube = lambda i:(i,i**3)
# res = map(cube,range(1,6))
# print(dict(res))

# s = "qwerty mmmnb asdf zxcv yuiop hjkl 1234"
# out = s.split()
# a = lambda i:(i,i[::-1])
# res = map(a, out)
# print(dict(res))

# t = [22, 4, 2, 8]
# res = lambda i:i**2 type(i)==int and i%2==0
# print

# def fb(func):
#     def inner(*args, **kwargs):
#         print('www.fb.com')
#         print('Signup')
#         print('Log in')
#         func(*args, *kwargs)
#         print('Logout')
#     return inner
# @fb
# def A():
#     print('Upload the post')
#     print('Likes and Comments')
# A()

# import time
# def fb (func) :
#     def inner (*args, **kwargs) :
#         st = time.time()
#         print('Aooji')
#         func(*args, *kwargs)
#         et = time.time()
#         print('Jaoji')
#         print('Kitna hua = ', et)
#     return inner
# @timer 
# def record():
#     print('Kab khatam hoga...')
#     time.sleep(5)
# record()

# def demo(s):
#     for i in s:
#         if 'A'<=i<="Z":
#             yield i, i.lower()
#         elif 'a'<=i<='z':
#             yield i, i.lower()
#         else:
#             yield i,i
# print(dict(demo('APPLE')))
            
# a = open(r"C:\Users\someshk1\OneDrive - KPIT Technologies Ltd\Desktop\File Handling\File1.txt", 'w')
# data = ['1\n','10\n','100\n', '1000\n']
# a = a.writelines(data)

# with open('File1.txt','w') as a:
#     data='breakup'
#     a.write(data)

