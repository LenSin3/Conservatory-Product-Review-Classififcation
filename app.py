# Flask App
# Import dependencies
from flask import Flask, render_template, jsonify, redirect, url_for, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

# import and load saved transformer and model
transformer_path = f'model/text3_lsvc.pkl'
model_path = f'model/grid3_lsvc.pkl'

text_transformer = pickle.load(open(transformer_path, 'rb'))
lsvc_model = pickle.load(open(model_path, 'rb'))



app = Flask(__name__)

# create route that renders index.html template
@app.route("/", methods=['GET', 'POST'])
def index():
    """Returns the homepage"""
    if request.method == 'GET':


        return render_template('index.html')
    
    if request.method == 'POST':

        message = request.form['text']
        data = [message]
        data_transform = text_transformer.transform(data)
        prediction = lsvc_model.predict(data_transform)
    return render_template('index.html', output_prediction = prediction)
	

if __name__ == "__main__":

    app.run(debug=True)
