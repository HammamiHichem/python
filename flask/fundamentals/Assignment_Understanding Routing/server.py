from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "have it say 'Dojo!'"

@app.route('/say/flask')
def say():
    return "have it say 'Hi Flask'"

@app.route('/say/<name>')
def say_michael():
    return  "have it say "

@app.route('/repeat/<int:num>/<string:name>')
def repeat_name(name, num):
    return f"Have it say {name * num}"

@app.errorhandler(404)
def page_not_found(error):
    return "Désolé ! Pas de réponse. Réessayez.", 404

if __name__ == "__main__" :
    app.run(debug=True)