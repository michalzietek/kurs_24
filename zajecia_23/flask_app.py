from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_list = [
    {
        "email": "michalzietkowski@gmail.com",
        "password": "123456"
    },
    {
        "email": "jannowak@gmail.com",
        "password": "abcdefg"
    }
]


@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/hello2/")
def hello_2():
    return "Hello2"


@app.route("/welcome_page/")
def welcome_page():
    return render_template("welcome_page.html")


@app.route("/hello/", defaults={"name": None})
@app.route("/hello/<name>")
def hello_name(name):
    if name:
        return render_template("hello.html", rendered_name=name.capitalize())
    return render_template("hello.html", rendered_name=name)


@app.route("/users/")
def show_users():
    return render_template("users_list.html", users=users_list)

@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("create_user_2.html")
    else:
        email_address = request.form.get("email_address")
        password = request.form.get("password")
        users_list.append({
            "email": email_address,
            "password": password
        })
        print(users_list)
        #return "Zarejestrowałeś użytkownika"
        return redirect(url_for("show_users"))



if __name__ == "__main__":
    app.run(debug=True)