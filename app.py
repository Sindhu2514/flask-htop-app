from flask import Flask
import os
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "Your Full Name"  # Replace with your actual name

    # Get system username
    username = getpass.getuser()

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Get 'top' command output
    top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout

    # Format output as HTML
    return f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time in IST:</b> {server_time}</p>
    <h2>Top Command Output:</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
