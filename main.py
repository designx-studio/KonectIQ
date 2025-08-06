from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')  # Flask looks in the 'templates/' folder by default

if __name__ == '__main__':
    app.run(debug=True)
