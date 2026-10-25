from flask import Flask, render_template

# Configuring static_folder and static_url_path
app = Flask(
    __name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/'
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)