from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates') # We have to write template_folder='templates' because we have created a separate folder for templates. If we don't specify this, Flask will look for templates in the default 'templates' folder in the same directory as the app.py file.


# --- CUSTOM JINJA FILTERS ---

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])


# --- ROUTES ---

@app.route('/')
def index():
    my_list = [10, 20, 30, 40, 50]
    return render_template('index.html', my_list=my_list)


@app.route('/other')
def other():
    return render_template('other.html', text_val="hello world")


@app.route('/redirect-me')
def redirect_endpoint():
    # Dynamic Redirect to 'other' view function
    return redirect(url_for('other'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)