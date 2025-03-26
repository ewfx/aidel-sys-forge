from flask import Flask, jsonify, request, Response
from dotenv import load_dotenv
from openai import OpenAI
import requests
import os
from parsers.structured_parser import parse_structured

app = Flask(__name__)


def init(debug=False):
    load_dotenv()
    app.run(debug=debug)

@app.route('/help')
def help():
    return Response("Help will always be given at Hogwards, for those who ask for it", 200)

@app.route('/calculate/risk')
def calculate_risk():
    response = create_response()
    return jsonify(response), 200

@app.route('/structured/risk', methods=['GET', 'POST'])
def structured_risk():
    if request.method == 'POST':
        if 'data' not in request.files:
            return Response("Invalid request, Include structured file", status=400)
        file_contents = request.files['data'].read().decode('utf-8')
        contents = parse_structured(file_contents)
        return jsonify(contents), 200

def get_info(symbol):
    url = f"https://financialmodelingprep.com/stable/analyst-estimates?symbol={symbol}&apikey={os.environ.get('FINMODEL_API_KEY')}"
    response = requests.get(url)
    print(response.json())
    print(response.text)
    print(response.status_code)

def create_response():
    response = {}
    response['Transaction ID'] = "<Transaction ID>"
    response['Extracted Entity'] = ['<Entity One>', '<Entity Two>']
    response['Entity Type'] = ['Shell Company', 'NGO']
    response['Risk Score'] = 0.87
    response['Supporting Evidence'] = ['Panama Papers Db', 'Sanctions List'],
    response['Confidence Score'] = 0.89
    response['Reason'] = "Sample Reason why the risk is assigned"
    return response

if __name__ == "__main__":
    init(debug=True)