from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        last = request.form.get("last")
        email = request.form.get("email")
        birthdate = request.form.get("birthdate")
        

        # Here you could save data or process it
        return render_template("form.html", submitted=True, name=name)

    return render_template("form.html", submitted=False)


if __name__ == "__main__":
    app.run(debug=True)