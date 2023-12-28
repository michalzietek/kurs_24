from flask import Flask
from routes import paths
from views import DummyView

app = Flask(__name__)
app.register_blueprint(paths)
DummyView.register(app)



if __name__ == "__main__":
    app.run(debug=True)
