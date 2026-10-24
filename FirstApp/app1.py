from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

# 2. Static Route
@app.route('/hello')
def hello_static():
    return "Hello World Static"

# 3. Dynamic URL Processor (String Parameter)
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

# 4. Dynamic URL Processor with Data Type (Integer Parameter)
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

# 5. Handling Query Parameters (http://127.0.0.1:5555/handle_url_params?greeting=hi&name=sameer)
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args and 'name' in request.args:
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting} {name}"
    else:
        return "Some parameters are missing", 400

# 6. Handling Methods (GET & POST) and Returning Custom Response
@app.route('/api/data', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_data():
    if request.method == 'GET':
        return "You made a GET request\n"
    elif request.method == 'POST':
        # Custom Response crafting
        response = make_response("You made a POST request\n")
        response.status_code = 202
        response.headers['Content-Type'] = 'text/plain'
        return response
    elif request.method == 'PUT':
        return "You made a PUT request\n"
    elif request.method == 'DELETE':
        return "You made a DELETE request\n"
    else:
        return "Method not allowed", 405

# Server Start Section
if __name__ == '__main__':
    # host='0.0.0.0' allows localhost and local network IP
    # port=5555 sets custom port
    # debug=True enables auto-reload on code change
    app.run(host='0.0.0.0', port=5555, debug=True)
    



