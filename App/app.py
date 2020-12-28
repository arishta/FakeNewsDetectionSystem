from flask import Flask, abort, jsonify, request, render_template
import joblib
from feature import *
import json

pipeline = joblib.load('./pipeline.sav')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api',methods=['POST'])
def get_delay():
    result=request.form
    title = result['title']
    author = result['author']
    text = result['maintext']
    query = get_all_query(title, author,text)
    user_input = {'query':query}
    pred = pipeline.predict(query)
    print("ans:",pred)
    output="The news article is REAL!"
    if pred==0: 
        output="The news article is FAKE!"
    return render_template('index1.html',output=output)
    
if __name__ == '__main__':
    app.run(port=8080, debug=True)
