# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False


# even_numbers = []

# for i in range(4):
#     n = int(input("enter a number: "))
#     if is_even(n):
#         even_numbers.append(n)

# print("all even numbers:", even_numbers)

# TODO
# all_students = ["artin", "hira","rastin", "farham","armin", "sara"]
"""
برنامه ای بنویس که اسم هایی که دارای کاراکتر
t 
هستند زا از لیست بالا نمایش دهد
و همینطور تعداد آن ها را نیز نمایش دهد
با
for
"""


# import random


# n1,n2,n3,n4,n5,n6 = (0,)*6

# for i in range(100):
#     face = random.randint(1,6)
#     if face == 1:
#         n1 += 1
#     elif face == 2:
#         n2 += 1
#     elif face == 3:
#         n3 += 1
#     elif face == 4:
#         n4 += 1


# print(f'# of 1 : {n1}')
# print(f'# of 2 : {n2}')
# print(f'# of 3 : {n3}')
# print(f'# of 4 : {n4}')



favorite_sports = {
    "hira":"handball",
    "arya":"football",
    "sara":"tennis"
}

print(f"hira likes {favorite_sports['hira']}")
print(f"arya likes {favorite_sports['arya']}")
print(f"sara likes {favorite_sports['sara']}")

favorite_sports["saman"] = "football"
print(f"saman likes {favorite_sports['saman']}")
print(favorite_sports)
del favorite_sports["saman"]
print(favorite_sports)