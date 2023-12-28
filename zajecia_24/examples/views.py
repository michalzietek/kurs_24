from flask_classful import FlaskView, route


class DummyView(FlaskView):
    def __init__(self):
        pass

    def index(self):
        return "Hello World"

    @route("/say-hi/<name>")
    def say_hi(self, name):
        return f"Hi {name}"
