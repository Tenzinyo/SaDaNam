from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from security import authenticate_user, detect_fraudulent_activity

app = Flask(__name__) #create an instance of this class 
app.secret_key = 'SaDaNam#2025'

# Sample in-memory user data for demo
users = {'lemo': 'Bunakha2025'}

#session-based user authentication
@app.route("/") #routh decorater to tell Flask what URL should trigger our function
def home():
    if 'username' in session: #check if key username is in current users session obj
        #if username, render the dashboard webpage and passes the username value for personalization
        return render_template('dashboard.html', username=session['username']) 
    #if not username, driect to login page
    return redirect(url_for('login'))

#login and redirect to home if successful
@app.route('/')
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password, users):
            session['username']=username
            return redirect(url_for('home'))
        else:
            return "Invalid login credentials", 401
    return render_template('login.html')

#route '/transaction' that only accepts POST requests
@app.route('/transaction', method=['POST'])
def transaction():
    #if username not in session, return a json response and http status 401, unauthorised
    if 'username' not in session:
        return jsonify({"error":"Authentication required"}), 401 
    #extract the JSON data sent in the request body and store it as data
    data = request.json
    #if detected fraud, return a json response and http status 403, forbidden
    if detect_fraudulent_activity(data):
        return jsonify({"error":"Fraudulent activity detected"}), 403
    return jsonify({"message":"Transaction accepted"}), 200

if __name__ in '__main__':
    app.run(debug=True)
    