from flask import Flask, render_template, request, redirect, url_for, send_file

app = Flask(__name__)

# Hardcoded login credentials
USERNAME = "admin"
PASSWORD = "flipkart123"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/download')
def download_report():
    return send_file('sales_report.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
