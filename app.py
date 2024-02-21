from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from predict import predict_type

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/disease_pred', methods=['POST'])
def disease():
    if request.method == 'POST':
        data = request.form.to_dict()
        form_values = [float(data[key]) for key in data]
        form_values = [form_values]
        result = predict_type(form_values)
        print(result)
        return jsonify({"result": result})

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(debug=True, port=5000)
