# # # ********with argument*******
# # def func(a):
# #     print(a)
# # func(3)
# # # ********without argument*******
# # def func():
# #     print("a")
# # func()
# # # ***************
# def func():
#     a=5
#     return a
# x=func()
# print(x)

# # ******************************
# def func(a):
#     return a
# x=func(3)
# print(x)

# wap to find prime and composite
def decision(x):
    b=0
    for a in range(1,x+1):
        if x % a==0:
            b=b+1
    if b==2 or b==1:
        print("number is prime")
    else:
        print("num is composite")

Num=int(input("enter any integer number"))
decision(Num)

# # to find palindrome
# def func(string):
    
    