class User:

    user_counter = 0

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        User.user_counter += 1

    @staticmethod
    def calculate_user_weight_in_lbs(weight):
        return round(weight / 0.45, 2)

    def show_my_name(self):
        return self.name

    @classmethod
    def change_user_counter(cls, counter):
        cls.user_counter = counter


User.change_user_counter(counter=100)
user = User(name="Michal", surname="Zietkowski", email="michalzietkowski@gmail.com")
print(user.user_counter)
user_2 = User(name="Jan", surname="Nowak", email="jan.nowak@gmail.com")
print(user_2.user_counter)
print(User.user_counter)
print(user.calculate_user_weight_in_lbs(100))
print(user_2.calculate_user_weight_in_lbs(200))