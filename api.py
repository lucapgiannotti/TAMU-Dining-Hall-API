from flask import Flask, jsonify
import subprocess
from web_scraper import get_menu

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

@app.route('/test', methods=['GET'])
def get_test():
    result = "hello world!"
    return jsonify({'test': result.strip()})

@app.route('/breakfast_menu', methods=['GET'])
def get_breakfast_menu():
    result = get_menu()
    return jsonify({'menu_items': result})

if __name__ == '__main__':
    app.run()