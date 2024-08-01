# class student:
#     name="pandit"
#     age=1500
#     grade="f"
#     marks=2
#     print(name)
# A=student()
# print(A.name)
# # B=student()
# # B.name="puri"
# A.name=input("enter name")
# print(A.name)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

A=student("amit",20)
print(A.name)
print(A.age)
B=student("roshan",20)
print(B.name)
print(B.age)