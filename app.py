from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

# Change to use on another pc
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'user'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


@app.route('/employeelogin/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return redirect(url_for('home'))
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)


@app.route('/employeelogin/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/create_customer_screen')
def create_customer():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('create_customer_screen.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/update_customer_screen')
def update_customer():
    # Check if user is loggedin
    if 'loggedin' in session:
        # need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('update_customer_screen.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/create_accnt_screen')
def create_accnt():
    # Check if user is loggedin
    if 'loggedin' in session:
        # need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('create_accnt_screen.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/customer_status_screen')
def customer_status():
    # Check if user is loggedin
    if 'loggedin' in session:
        # need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('customer_status_screen.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/employeelogin/accnt_status_screen')
def accnt_status():
    # Check if user is loggedin
    if 'loggedin' in session:
        # need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userstore WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('accnt_status_screen.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
