def get_user_info():
    name = "Alice"
    age = 25
    return name, age  # 实际上返回的是 ("Alice", 25)

user = get_user_info()
# print(type(user))  # 输出: <class 'tuple'>

# name, age = user
# print(name)
# print(age)

# print(user[0])

# print(user)

# for i in list(range(10)):
#     print(i)

# for i in range(1,8,2):
#     print(i)

# def func(x, y=5):
#     return x + y

# # print(func(1))
# print(func())


# x = 10

# def func():
#     # global x
#     x = 20
#     print(x)
#     return x

# x = func()

# print(x)

# for i in range(1,4):
#     # print(i)
#     for j in range(i):
#         print(i, end=" ")

# for i in range(1,4):
#     print(i, end=" ")

i = 0
for j in range(i):
    print(i, end=" ")

i = 1
for j in range(i):
    print(i, end=" ")

i = 2
for j in range(i):
    print(i, end=" ")

i = 3
for j in range(i):
    print(i, end=" ")

# a = range(1)
# print(a)
