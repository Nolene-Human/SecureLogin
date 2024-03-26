from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Add your authentication logic here
        
        if username == 'admin' and password == 'password':
            return redirect('/authorised')
        else:
            return render_template('unauthorised.html', error='Invalid credentials')
    
    return render_template('simple_login.html')

@app.route('/authorised')
def dashboard():
    return 'Welcome to the dashboard!'

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)