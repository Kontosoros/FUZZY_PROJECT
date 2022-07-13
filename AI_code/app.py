from flask import Flask, flash, request, url_for, jsonify
from flask_cors import CORS
from production import  use_the_model
import sys
import time
from fuzzy_code import Fuzzy
app = Flask(__name__)
CORS(app)

fuzzy = Fuzzy()

ALLOWED_EXTENSIONS = set(['tiff', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/results', methods=['POST'])
def results():
    time.sleep(2)
    if 'image' not in request.files:
        return 'there is no image in form!'
    image = request.files['image']
    if image.filename == '':
         return 'No selected file'
    if not image:
        return "Image is null"
    elif not allowed_file(image.filename):
        return "uploaded file is not an image"
    res = use_the_model(image)
    image.close()
    return jsonify(res)

@app.route('/recommendations', methods=['POST'])
def results_recommendations():
    data = request.json
    result = fuzzy.compute(data['age'], data['Cigarettes'], data['Exercise'], data['Eating unhealthy'], data['Anxiety'])
    print(str(round(result)))
    return str(round(result))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
    