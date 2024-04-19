from flask import Flask, render_template

app = Flask(__name__, template_folder="templates/")

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html", title="Portfolio Homepage")

@app.get("/aboutme")
def about_me():
    return render_template("about_me.html", title="About me")

@app.get("/projects")
def projects():
    return render_template("projects.html", title="Portfolio Projects")

@app.get("/contact")
def contact():
    return render_template("contact.html", title="Contact Me")

if __name__ == "__main__":
    app.run(debug=True)