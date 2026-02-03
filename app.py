from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote')
def get_quote():
    try:
        # Using a reliable, free quote API
        response = requests.get("https://api.quotable.io/random", verify=False)
        data = response.json()
        return jsonify({
            'quote': data['content'],
            'author': data['author']
        })
    except:
        return jsonify({
            'quote': "The best way to predict the future is to create it.",
            'author': "Peter Drucker"
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
