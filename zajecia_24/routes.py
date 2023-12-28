from flask import Blueprint, render_template, request
from accountant.manager import manager

paths = Blueprint("routes", __name__)

@paths.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        context = {
            "stan_konta": manager.saldo,
            "magazyn": manager.magazyn
        }

        return render_template("main.html", context=context)
    elif request.method == "POST":
        operacja = request.form.get("operacja")
        if operacja == "sprzedaz-produktu":
            #dzialanie odpowiadajace sprzedazy produtku
            pass
        pass
    #return render_template("main.html", stan_konta=manager.saldo)