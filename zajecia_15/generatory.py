import sys

def show_users(users):
    for user in users:
        return user

def show_users_generator(users):
    for user in users:
        yield user


users_list = ["Michal", "Andrzej", "Adam", "Jacek", "Mateusz"]

# for user in show_users(users_list):
#     print(user)
#
for user in show_users_generator(users_list):
    print(user)

# user_normal = show_users(users_list)
# print(user_normal)
#
# user_generator = show_users_generator(users_list)
# print(next(user_generator))
# print(next(user_generator))
# print(next(user_generator))
# print(next(user_generator))
# print(next(user_generator))
# print(next(user_generator))
#
# users = show_users_generator(users_list)

def data_generator(size):
    for item in range(size):
        yield item


def data_list(size):
    return [item for item in range(size)]

def memory_usage(object):
    return sys.getsizeof(object)


data_size = 1000000

generator = data_generator(data_size)

list_comprehension = data_list(data_size)


print(f"Memory usage generatora: {memory_usage(generator)}")

print(f"Memory usage funkcji z list comprehension: {memory_usage(list_comprehension)}")

