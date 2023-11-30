class Car:
    def __init__(self, tire, gearbox, steering_wheel):
        self.tire = tire
        self.gearbox = gearbox
        self.steering_wheel = steering_wheel
        self.speed = 0

    def change_tire(self, new_tire):
        self.tire = new_tire

    def change_steering_wheel(self, new_steering_wheel):
        self.steering_wheel = new_steering_wheel

    def run_car(self, new_gear, starting_speed):
        self.change_gearbox(new_gear)
        self.accelerate(starting_speed)

    def change_gearbox(self, new_gear):
        self.gearbox = new_gear

    def accelerate(self, speed):
        self.speed = speed


audi = Car("michelin", 0, "sports_wheel")
audi.run_car(1, 10)

users = [{
        "id": 0,
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "email": "jan.kowalski@gmail.com"
    },
    {
        "id": 1,
        "imie": "Michal",
        "nazwisko": "Nowak",
        "email": "michal.nowak@gmail.com"
    }]


def find_user_in_users(user_id):
    for user in users:
        if user_id == user.get("id"):
            return user
    return None


def change_users_email(new_email, user_id):
    for user in users:
        if user.get('id') == user_id:
            user["email"] = new_email

def change_user_email(new_email, user_id):
    user_in_dict = find_user_in_users(user_id)
    users[user_id]["email"] = new_email if user_in_dict else None


change_users_email("michalnowak@interia.pl", 2)
change_user_email("adam.kowalski@gmail.com", 0)
print(users)