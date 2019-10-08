from flask import Flask,render_template
app = Flask(__name__)

posts = [
    {"author": "christopher ribia",
    "title":"corrutpion",
    "Content": "Me without weed"},
    {"author":"Busy signal",
    "title":"Man a galis defender",
    "Content":"Nice flow and vocals"
    }
]

@app.route("/")
def hello():
    return "domie wairimu!! chris loves you so much busy signal "

@app.route("/about")
def about():
    return render_template('home.html',posts = posts)

if __name__ == '__main__':
    app.run(debug=True)