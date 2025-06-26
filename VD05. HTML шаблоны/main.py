from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_header(response):
    """
    Отключаем кэширование в браузере.
    """
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response

@app.route("/")
def films():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()