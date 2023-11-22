from flask import Flask, render_template

app = Flask(__name__)

@app.route('/static.css')
def style():
    return render_template('static.css', pagetitle="Checkerboard")

@app.route('/')
def index():
    return render_template('index.html', pagetitle="Chekerboard")

@app.route('/<int:num>')
def index1(num):
    return render_template('index1.html', num=num)

# @app.route('/<int:x, y>')
# def index2(x, y):
#     return render_template('index2.html', x=x, y=y)

@app.route('/<int:x>/<int:y>')
def index2(x, y):
    return render_template('index2.html', rows=x, cols=y)


if __name__ == '__main__':
    app.run(debug=True, port=5000)


