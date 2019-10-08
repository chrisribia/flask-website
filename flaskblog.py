from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {"author": "christopher ribia",
    "title":"corrutpion",
    "date_posted":"02/08/2001",
    "content":"Me without weed"},
    {"author":"Busy signal",
     "date_posted":"02/08/2001",
    "title":"Man a galis defender",
    "content":"Nice flow and vocals"
    }
]

@app.route("/")
def hello():
    return render_template('home.html',posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',posts = posts)

if __name__ == '__main__':
    app.run(debug=True)