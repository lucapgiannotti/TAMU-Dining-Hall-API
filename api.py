from flask import Flask, jsonify, request, abort
from store_menu import breakfast_menu, lunch_menu, dinner_menu

def dining_hall_exists(dining_hall):
    available_dining_halls = ['commons', 'sbisa', 'duncan']
    return dining_hall.lower() in available_dining_halls

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the TAMU Dining Hall API!", 200


@app.route('/<dining_hall>/breakfast_menu', methods=['GET'])
def get_hall_breakfast_menu(dining_hall):
    if not dining_hall_exists(dining_hall):
        return jsonify({'error': 'Dining hall not found'}), 404
    try:
        result = breakfast_menu(dining_hall)
        return jsonify({'breakfast_menu_items': result}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/<dining_hall>/lunch_menu', methods=['GET'])
def get_hall_lunch_menu(dining_hall):
    if not dining_hall_exists(dining_hall):
        return jsonify({'error': 'Dining hall not found'}), 404
    try:
        result = lunch_menu(dining_hall)
        return jsonify({'lunch_menu_items': result}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/<dining_hall>/dinner_menu', methods=['GET'])
def get_hall_dinner_menu(dining_hall):
    if not dining_hall_exists(dining_hall):  
        return jsonify({'error': 'Dining hall not found'}), 404
    try:
        result = dinner_menu(dining_hall)
        return jsonify({'dinner_menu_items': result}), 200
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500
    
    
if __name__ == '__main__':
    app.run()