# Teachable Courses Dashboard

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/teachable_assessment.git
   cd teachable_assessment
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your Teachable API key:
   ```
   TEACHABLE_API_KEY=your_api_key_here
   ```
5. Run the Flask application:
   ```bash
   python -m flask --app main run --debug
   ```
6. Open your browser and navigate to `http://127.0.0.1:5000` to view the dashboard.

---

## Technology Stack

- **Python 3**  
- **Flask** – Web framework for UI and routing  
- **requests** – For making HTTP API calls  
- **pytest** – Unit testing framework  
- **python-dotenv** – For secure management of environment variables  
- **Bootstrap** – Frontend styling  

---

## Project Structure

```
/teachable_assessment/
│
├── main.py               # Flask app: routes, request handling, response rendering
├── utils.py              # Helper functions: data filtering, formatting, and processing
│
├── templates/            # HTML templates for Flask
│   └── index.html        # UI: button to fetch data, display courses and student info
│
├── tests/
│   └── test_api_client.py # Unit tests for API client and utils
│
├── .env                  # Environment variables (API key)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Application Flow

1. User accesses the Flask route (`/`) served by `main.py`.
2. Flask triggers a request to fetch course data from the Teachable Public API.
3. The raw JSON response is passed to utility functions in `utils.py`.
4. `utils.py` filters and cleans the data to extract relevant information.
5. Cleaned JSON data is returned to Flask.
6. Flask renders the final response using a Jinja2 template (`index.html`).
7. The UI displays the list of courses and enrolled students.
8. Add a loading state from button click to api call to response

---

## Example Output

```
Course: Python Basics
Heading: Learn Python from scratch
Students Enrolled:
- Alice Smith (alice@example.com)
- Bob Johnson (bob@example.com)

Course: Advanced Data Science
Heading: Deep dive into data analysis
Students Enrolled:
- Carol White (carol@example.com)
- Dave Brown (dave@example.com)
```

---

## Future Improvements
- Add integration tests to cover end-to-end application behavior.
- Implement pagination support for large numbers of courses or students.
- Enhance UI with better view of the emails and names
- Add error handling and user-friendly messages for API failures.
- Caching the response from the API call to prevent unnecessary API requests.
- Finish writing test

---

## Testing - Not done ❌

- Unit tests are located in the `tests/` directory.
- Run tests with:
  ```bash
  pytest
  ```
- Tests cover API client functionality and utility functions ensuring data is fetched and processed correctly.

## AI Usage
- I used ChatGPT to help with the proof reading of the readme file 