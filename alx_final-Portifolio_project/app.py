from flask import Flask, render_template, request

app = Flask(__name__)


# Function to calculate the total cost based on room type and number of nights
def calculate_total_cost(room_type, nights):
    if room_type == 'standard':
        return 75 * nights
    elif room_type == 'deluxe':
        return 175 * nights
    elif room_type == 'suite':
        return 400 * nights
    return 0


# Route to serve your main site (if needed)
@app.route('/')
def index():
    return render_template('index.html')  # Render your main homepage


# Route to serve about page
@app.route('/about.html')
def about():
    return render_template('about.html')  # Render your main homepage


# Route to serve service.html
@app.route('/service.html')
def service():
    return render_template('service.html')  # Render your main homepage


# Route to serve service.html
@app.route('/room.html')
def room():
    return render_template('room.html')  # Render your main homepageroom.html


# Route to serve service.html
@app.route('/team.html')
def team():
    return render_template('team.html')  # Render your main homepageroom.html


# Route to serve service.html
@app.route('/contact.html')
def contact():  # Render your main homepageroom.html
    return render_template('contact.html')


# Route to serve the booking page
@app.route('/booking.html')
def booking_page():
    return render_template('booking.html')  # Render your existing booking page


# Route to serve the booking page
@app.route('/testimonial.html')
def testimonial():  # Render your existing booking page
    return render_template('testimonial.html')

# Route to serve the policy page
@app.route('/policy.html')
def policy():  # Render your existing policy page
    return render_template('policy.html')


# Route to handle booking form submission
@app.route('/confirmation.html', methods=['POST'])
def reserve():
    # Get the form data from your existing booking form
    name = request.form['name']
    occupants = int(request.form['occupants'])
    sex = request.form['sex']
    email = request.form['email']
    room_type = request.form['room_type']
    nights = int(request.form['nights'])

    # Calculate the total cost of the stay
    total_cost = calculate_total_cost(room_type, nights)

    # Render a confirmation page
    # (You can create a new one or display a message)
    return render_template('confirmation.html', name=name, occupants=occupants,
                           sex=sex, email=email, room_type=room_type,
                           nights=nights, total_cost=total_cost)


if __name__ == '__main__':
    app.run(debug=True)
