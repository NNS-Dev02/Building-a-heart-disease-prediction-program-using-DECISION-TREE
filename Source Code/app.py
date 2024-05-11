import os
import subprocess
import time
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

last_modified = 0

@app.route('/')
def show_index():
    return render_template('index.html')

@app.route('/show_result')
def show_result():
    result = read_result()
    return render_template('result.html', result=result)


@app.route('/write_params', methods=['POST'])
def write_params():
    params = [request.form[f'param{i+1}'] for i in range(13)]
    params_str = ', '.join(params)

    with open('params.txt', 'w') as file:
        file.write(params_str)

    subprocess.Popen(["python", "program.py"])

    return 'OK', 200

@app.route('/check_program', methods=['GET'])
def check_program():
    global last_modified
    try:
        if os.path.getmtime('params.txt') > last_modified:
            last_modified = os.path.getmtime('params.txt')
            return 'File params.txt đã được cập nhật, chương trình program.py sẽ được chạy.'
        else:
            return 'File params.txt chưa có sự thay đổi.'
    except FileNotFoundError:
        return 'File params.txt không tồn tại.'

@app.route('/upload', methods=['POST'])
def upload_file():
    request.files['file'].save('params.txt')
    subprocess.Popen(["python", "program.py"])
    return 'File đã được lưu và chương trình program.py đang chạy'

def read_result():
    try:
        with open('result.txt', 'r') as file:
            result = file.read().strip()
            return result
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    app.run(debug=True)