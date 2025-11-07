## Setup
1. Clone this repo
2. Create and activate a virtual environment
3. Run `pip install -r requirements.txt`
4. Create a `.env` file with your Teachable API key
5. Run `python main.py`


## Requirements 
As a creator on Teachable’s platform, you’d like to see some information about your published
courses. Using the endpoints provided by the Public API, at a minimum, fetch and output a list
of published courses within your school, including the following information for each course:
- Course name
- Course heading
- A list of the names and emails of students actively enrolled in the course

## Stack 
```Language```
- Python 3

```Libraries```
- Flask ➡️ UI Entry point
- requests ➡️ API calls
- pandas ➡️ tabular output
- pytest ➡️ unit tests
- dotenv ➡️ secure API management
- tailwind.css ➡️ utility-first CSS framework

## Folder Structure
```
/teachable_assessment/
│
├── main.py               # Application layer (Flask app + routes)
├── api_client.py         # Integration layer (handles Teachable API requests)
├── utils.py              # Logic layer (filtering, formatting, helper logic)
│
├── templates/            # Flask looks here by default for HTML templates
│   └── index.html        # Contains your UI button + JS fetch logic
│
├── static/               # (optional) for CSS or JS files if you separate them
│   └── style.css
│
├── tests/
│   └── test_api_client.py
│
├── .env                  # Contains TEACHABLE_API_KEY=your_key_here
├── requirements.txt
└── README.md
```

## Flow Control
1️⃣ User clicks button (Frontend)
     ↓
2️⃣ JS sends GET request to /fetch_courses (Backend)
     ↓
3️⃣ Flask receives request and calls fetch_courses() in api_client.py
     ↓
4️⃣ api_client.py calls Teachable API and gets data
     ↓
5️⃣ Flask formats it and sends it back as JSON
     ↓
6️⃣ Frontend receives JSON and updates the page dynamically
