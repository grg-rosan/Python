# num=float(input("enter  number "))
# if isinstance(num,float):
#     if num % 2==0:
#         print("number is even")
#     else:
#         print("number is odd")
# else:
#     print("number is float")

import random
spin=random.randint(17,24)
print(spin)
dict1={17:9,19:7,24:2}
if spin in dict1:
        snake=dict1.get(spin)
        print("snake got you")
        print(snake)