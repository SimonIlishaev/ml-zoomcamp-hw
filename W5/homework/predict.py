import pickle
from flask import Flask
from flask import request
from flask import jsonify

input_file_one = "dv.bin"
input_file_two = "model2.bin"

with open(input_file_one, 'rb') as f_in: 
    dv = pickle.load(f_in)
with open(input_file_two, 'rb') as f_in: 
    model = pickle.load(f_in)

app = Flask("Score")

@app.route("/predict", methods=["POST"])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    result = {"score": float(y_pred)}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
