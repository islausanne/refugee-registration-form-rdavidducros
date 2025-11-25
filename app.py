from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration form page
@app.route('/register')
def register():
    return render_template('register.html')

# Handle form submission (students will add JSON save code here)

# Display stored registrations (students will add JSON reading code here)
@app.route('/view')
def view_registrations():
    # TODO: Read data from registrations.json and send to template (worksheet Part 2)

    return render_template('view.html', registrations=[])


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    country = request.form['country']
    age = request.form['age']
    email = request.form['email']
    gender = request.form['gender']
    phone = request.form['phone']

    if not name:
        flash('Please enter your first name.')
    elif not country:
        flash('Please enter your country.')
    elif not age:
        flash('Please enter your age.')
    elif not email:
        flash('Please enter your email.')
    elif not gender:
        flash('Please enter your gender.')
    elif not phone:
        flash('Please enter your phone.')
    else:
        flash('These fields are required!')




    # Check if file exists
    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)
    else:
        data = []

    # Add the new registration
    data.append({'name': name, 'country': country, 'age': age, 'email': email, 'gender': gender, 'phone': phone})

    # Save all registrations back to the file
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)

    flash('Registration submitted successfully!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)