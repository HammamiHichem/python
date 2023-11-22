from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Check if a session exists
    if 'actual_visits' not in session:
        # If not, initialize the session with the actual visit counter
        session['actual_visits'] = 0

    # Increment the actual visit counter
    session['actual_visits'] += 1

    # Check if a session exists for the custom counter
    if 'custom_counter' not in session:
        # If not, initialize the session with a custom visit counter
        session['custom_counter'] = 0

    # Render the template with both visit counters
    return render_template('index.html', actual_visits=session['actual_visits'], custom_counter=session['custom_counter'])

@app.route('/increment', methods=['POST'])
def increment():
    # Increment the custom visit counter by 1
    session['custom_counter'] += 1

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/increment_by_2', methods=['POST'])
def increment_by_2():
    # Increment the custom visit counter by 2
    session['custom_counter'] += 2

    # Redirect to the home page
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    # Clear the session
    session.clear()

    # Redirect to the home page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
