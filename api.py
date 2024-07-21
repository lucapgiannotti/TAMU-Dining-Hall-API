from flask import Flask, jsonify
import subprocess
from web_scraper import breakfast_menu, lunch_menu, dinner_menu

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "This is the TAMU Dining Hall API!"

@app.route('/test', methods=['GET'])
def get_test():
    result = "hello world!"
    return jsonify({'test': result.strip()})

@app.route('/breakfast_menu', methods=['GET'])
def get_breakfast_menu():
    result = breakfast_menu()
    return jsonify({'menu_items': result})

@app.route('/lunch_menu', methods=['GET'])
def get_lunch_menu():
    result = lunch_menu()
    return jsonify({'menu_items': result})

@app.route('/dinner_menu', methods=['GET'])
def get_dinner_menu():
    result = dinner_menu()
    return jsonify({'menu_items': result})

if __name__ == '__main__':
    app.run()