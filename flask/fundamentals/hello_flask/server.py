from flask import Flask 
app= Flask(__name__)
@app.route('/')
def hello_world():
    return'Hello World'
@app.route('/user/<float:id>')
def call_user(id) :
    print(id)
    return "Hichem"


if __name__=="__main__" : 
    app.run(debug=True)