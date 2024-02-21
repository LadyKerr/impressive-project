# app.py
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        number = request.form.get('number')
        with open('data.json', 'w') as f:
            json.dump({'number': number}, f)
        return 'Number submitted successfully!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)