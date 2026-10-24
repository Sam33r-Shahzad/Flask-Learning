import os
import uuid
import pandas as pd
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

app = Flask(__name__, template_folder='templates')


# --- 1. INDEX & LOGIN FORM ROUTE ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'sameer' and password == 'ucantcme':
            return "Success"
        else:
            return "Failure"


# --- FILE UPLOAD & VIEW CONTENT ROUTE ---
@app.route(rule='/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()

# --- 3. DIRECT CSV DOWNLOAD ROUTE ---
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    uploaded_file = request.files.get('file')
    df = pd.read_excel(uploaded_file)
    
    csv_data = df.to_csv(index=False)
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=result.csv"}
    )

# --- 4. CSV CONVERSION WITH DOWNLOAD PAGE REDIRECT ---
@app.route('/convert_csv_2', methods=['POST'])
def convert_csv_2():
    uploaded_file = request.files.get('file')
    df = pd.read_excel(uploaded_file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    unique_filename = f"{uuid.uuid4()}.csv"
    file_path = os.path.join('downloads', unique_filename)
    df.to_csv(file_path, index=False)

    return render_template('download.html', file_name=unique_filename)


# --- 5. SERVE FILE FROM SERVER DIRECTORY ---
@app.route('/download/<file_name>')
def download_file(file_name):
    return send_from_directory('downloads', file_name, download_name="result.csv")


# --- 6. HANDLE JAVASCRIPT FETCH POST REQUEST ---
@app.route('/handle_post', methods=['POST'])
def handle_post():
    data = request.json
    greeting = data.get('greeting')
    name = data.get('name')

    with open('file.txt', 'w') as f:
        f.write(f"{greeting} {name}")

    return jsonify({"message": "Successfully written to file.txt"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)