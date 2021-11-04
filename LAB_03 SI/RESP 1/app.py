from flask import Flask, jsonify, request, render_template
from products import products
import random as ra

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/JSON"
# Testing Route
@app.route('/im_data', methods=['GET'])
def im_data():
    file = request.files["data"]
    new_product = {
        '/im_data': request.json['data'],
    }
    file.append(new_product)
    return jsonify({'data': products})

if __name__ == '__main__':
    app.run(debug=True)