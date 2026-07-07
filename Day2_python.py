# c = input("Enter your word : ")
# print(c)
# a = c.lower()
# print(a)
# b = a[::-1]
# print(b)
# if a == b :
#     print("Given word is palindrome")
# else :
#     print("Given word is not palindrome")

# a = input("Enter your sentence : ")
# b = a.split()
# count = 0
# for ch in b:
#     count += 1
# print(count)

# a = []
# for i in range(5):
#     b = int(input("Enter your number : "))
#     a.append(b)
# # a = [22,1,45,7,8]
# largest = a[0]
# for n in a[1:]:
#     if n > largest:
#         largest = n
# print(largest)

# a = []
# for i in range(5):
#     b = int(input("Enter your number : "))
#     a.append(b)
# # a = [22,1,45,7,8,1]
# unique = []
# for item in a :
#     if item not in unique :
#         unique.append(item)
# print(a)
# print(unique)

# while True :
#     print("\n Menu : ")
#     print("1. Say hello ")
#     print("2. Show today's topic")
#     print("3. Exit")

#     choice = input("Enter your choice : ")

#     if choice == "1" :
#         print("Say Hello")
#     elif choice == "2" :
#         print("Today's topic - Python")
#     elif choice == "3" :
#         print("Exting menu ")
#         break
#     else :
#         print("Invalid choice")

# n = int(input("Enter your number : "))
# for i in range(1,11) :
#     print(n, "x", i, "=",n * i)   
 

#     b = int(input("Enter your number : "))    
# a = (1,2,3,4,5,6,7,8,9)
# count = 0
# for i in a :
#     if i % 2 == 0 :
#         count += i
#         print(count)
# print("sum", count)

# a = []
# for i in range(0,8) : 
#     b = int(input("Enter your numbers"))
#     a.append(b)
# print(a)
# p_count = 0
# n_count = 0
# z_count = 0

# for num in a:
#     if num < 0:
#         n_count += 1
#     elif num == 0:
#         z_count += 1
#     else:
#         p_count += 1

# print("Negative numbers:", n_count)
# print("Zeroes:", z_count)
# print("Positive numbers:", p_count)

# a = "s e r w q t y"
# b = a.replace(" ","-")
# print(a)
# print(b)

# n = int(input("Enter avg number : "))
# nums = []
# for i in range(n):
#     b = int(input("Enter your number : "))
#     nums.append(b)
# print(nums)
# total = sum(nums)
# avg = total/n
# print(n)
# print(avg)