from flask import Flask, request, render_template, redirect, url_for
import smtplib

app = Flask(__name__)

# My actual email credentials {Classified}
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'mondli99zulu@gmail.com'
EMAIL_PASSWORD = '0712380500'

@app.route('/')
def index():
    return render_template('index.html')       # Render to my homepage (My Portfolio)

@app.route('/.netlify/functions/submit_form_endpoint', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']                  # Get 'name' from the form on homepage
        email = request.form['email']                # Get 'email' from the form on homepage
        message = request.form['message']            # Get 'message' from the form on homepage

        try:
            # Send an email with the form data
            subject = f'New Contact Form Submission from {name}'
            body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
            message = f'Subject: {subject}\n\n{body}'

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
            server.quit()

            return redirect(url_for('index'))          # Redirect to my homepage after submission
        except Exception as e:
            return f"An error occurred: {e}"           #Display an Error Message !

if __name__ == '__main__':
    app.run(debug=True)               # Run the Flask app in debug mode if this script is executed directly
