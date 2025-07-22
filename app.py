from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (not persistent)
registrations = []

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        
        # Save the registration FIRST
        user = {'name': name, 'email': email, 'event': event}
        registrations.append(user)

        # THEN pass the list to the success page
        return render_template('success.html', name=name, event=event, registrations=registrations)
    
    return render_template('register.html')
if __name__ == '__main__':
    app.run(debug=True)
