import openai
from distutils.log import debug
from fileinput import filename
from flask import *
from flask_cors import CORS
import config


app = Flask(__name__)
CORS(app) 

def fetch_answer(question,docs):
# Text completion API
    openai.api_key = config.API_KEY
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{docs}\n\nQ: {question}\nA:",
    max_tokens=100,
    temperature=0
    )
    print(question)
    return response.choices[0].text.strip()
    

@app.route('/fileupload', methods=['POST'])
def upload_file():
    file = request.files['file']
    question = request.form['question']
    answer = fetch_answer(question,file)
    return {'answer' : answer}

if __name__ == '__main__':
    app.run(debug=True)