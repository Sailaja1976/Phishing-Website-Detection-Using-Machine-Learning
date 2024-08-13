import webbrowser
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# List of safe protocols
safe_protocols = ["http", "https", "ftp", "sftp"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        url = request.form['url']
        protocol = request.form['protocol']

        # Check if the protocol is considered safe
        if protocol.lower() in safe_protocols:
            prediction = 'good'
        else:
            prediction = 'bad'

        return jsonify({'url': url, 'protocol': protocol, 'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/openurl', methods=['POST'])
def open_url():
    try:
        url = request.form['url']
        protocol = request.form['protocol']
        prediction = request.form['prediction']

        if prediction == 'good':
            # Open URL in default browser
            webbrowser.open(url)
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'skipped'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
