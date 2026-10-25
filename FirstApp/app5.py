from flask import Flask, render_template, request, session, make_response, flash

app = Flask(__name__)

app.secret_key = 'super_secret_key_123'


@app.route('/')
def index():
    return render_template('index.html', message="Welcome to Session & Cookie Demo")


# --- 1. SESSION ROUTES (Server-side) ---

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'
    return render_template('index.html', message="Session Data Set!")


@app.route('/get_data')
def get_data():
    if 'name' in session and 'other' in session:
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f"Name: {name} | Other: {other}")
    return render_template('index.html', message="No Session Found!")


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message="Session Cleared!")


# --- 2. COOKIE ROUTES (Client-side) ---

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message="Cookie Set!"))
    response.set_cookie('cookie_name', 'cookie_value')
    return response


@app.route('/get_cookie')
def get_cookie():
    val = request.cookies.get('cookie_name')
    if val:
        return render_template('index.html', message=f"Cookie Value: {val}")
    return render_template('index.html', message="No Cookie Found!")


@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message="Cookie Removed!"))
    response.set_cookie('cookie_name', '', expires=0)
    return response


# --- 3. LOGIN & FLASHING ROUTE ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'neural9' and password == '12345':
            flash('Successful Login!')
            return render_template('index.html', message="Logged In!")
        else:
            flash('Login Failed! Wrong credentials.')
            return render_template('index.html', message="Login Failed!")

    return render_template('index.html', message="Please submit login form below")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)