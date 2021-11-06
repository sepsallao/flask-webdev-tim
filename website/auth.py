from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    return render_template("sign_up.html")


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('passwrod')
        confirm_password = request.form.get('confirmPassword')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('Email must be greater than 1 characters.', category='error')
        elif password != confirm_password:
            flash('Passwords doesn\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to the database
            flash('Account created!', category='success')

    return render_template("sign_up.html")
