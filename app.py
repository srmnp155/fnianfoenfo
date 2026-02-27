from flask import Flask, request, render_template, redirect, url_for
import csv
from io import TextIOWrapper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    csv_data = None
    headers = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        if file:
            wrapper = TextIOWrapper(file, encoding='utf-8')
            reader = csv.reader(wrapper)
            csv_data = list(reader)
            if csv_data:
                headers = csv_data[0]
                csv_data = csv_data[1:]
    return render_template('index.html', csv_data=csv_data, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
