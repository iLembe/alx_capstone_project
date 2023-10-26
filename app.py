from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'  # Configuring SQLite database
db = SQLAlchemy(app)                                             # Initialize SQLAlchemy
Migrate=Migrate(app, db)

# A python class Defining a model for the form data(represents the structure of the table to store data)
class FormData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')       # Render to my homepage (My Portfolio)

@app.route('/submit_form_endpoint', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a new FormData object with form data
        form_data = FormData(name=name, email=email, message=message)

        # Add the object to the session and commit it to the database
        db.session.add(form_data)
        db.session.commit()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode if executed directly