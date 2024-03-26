

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password are valid
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect('/authorised')
        else:
            return render_template('session_login.html', error='Invalid username or password')
    
    return render_template('session_login.html')

@app.route('/authorised')
def dashboard():
    if 'username' in session:
        return render_template('authorised.html', username=session['username'])
    else:
        return redirect('/logout')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)