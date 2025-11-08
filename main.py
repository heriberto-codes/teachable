from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from utils import filter_api_courses

import requests
import os

# load env files
load_dotenv()
API_KEY = os.getenv("TEACHABLEAPI")

# start flask instance 
app = Flask(__name__)

# routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/fetch_teachable_api") # type: ignore
def teachable_api():
    
    # api endpoint:
    url = "https://developers.teachable.com/v1/courses"
    
    headers = {
        "accept": "application/json",
        "apiKey": f"{API_KEY}"
    }
    
    # make the api call
    # I decided to do it in a try/except to handle potential errors gracefully.
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        cleaned_api_courses = filter_api_courses(data)
        # print(cleaned_api_courses)
        return jsonify(cleaned_api_courses)
    except requests.exceptions.Timeout:
        return jsonify({"error", "The request took to long"}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error", "Network Error, could not conntect to Teachable API"}), 503
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": f"HTTP error: {str(e)}"}), response.status_code # type: ignore for now (response will throw an error eventually)
    
if __name__ == '__main__':
    app.run(debug=True)