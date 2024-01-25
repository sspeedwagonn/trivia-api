from flask import Flask, jsonify, request
import random
import os
import json

app = Flask(__name__)

def get_data_path(category):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    category_file = f'{category.lower().replace(" ", "_")}.json'
    return os.path.join(data_dir, category_file)

@app.route('/categories', methods=['GET'])
def get_categories():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    categories = [file.replace(".json", "").replace("_", " ").title() for file in os.listdir(data_dir) if file.endswith(".json")]
    return jsonify(categories)

@app.route('/questions', methods='GET')
def get_questions():
    category = request.args.get('category')
    data_path = get_data_path(category)
    
    if os.path.exists(data_path):
        with open(data_path, 'r') as file:
            questions = json.load(file)
            random_question = random.choice(questions)
            return jsonify(random_question)
    else:
        return jsonify({"Error": "Category not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)