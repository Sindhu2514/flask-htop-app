from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    processes = [{p.pid: p.info} for p in psutil.process_iter(['name', 'cpu_percent', 'memory_info'])]
    return jsonify(processes)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
