from flask import Flask,render_template,url_for, flash, redirect
from forms import LoginForm, RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '3ce72bb271c6adc396e4f8dd600610b0'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)