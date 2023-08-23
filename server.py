from flask import Flask
from flask_cors import CORS
from flask_app.controllers import users, languages, flashcards

app = Flask(__name__)
# CORS(app, supports_credentials=True)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, support_credentials=True)


if __name__ == "__main__":
    app.run(debug=True)