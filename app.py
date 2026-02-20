import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # For now, we just print the form; you can integrate email later
        print(f"Contact Form: {name}, {email}, {message}")
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        car_model = request.form['car_model']
        car_year = request.form['car_year']
        coverage = request.form['coverage']
        print(f"Quote Request: {car_model}, {car_year}, {coverage}")
        return render_template('quote.html', submitted=True)
    return render_template('quote.html')

@app.route('/location')
def location():
    # Example: embedding Google Maps
    return render_template('location.html')


if __name__ == "__main__":
    # Use Render-provided port, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)