from flask import Flask
from routes import setup_routes
import os
from dotenv import load_dotenv
from routes import register_socketio_handlers
from flask_socketio import SocketIO
from utils.session_manager import SessionManager
import sys
import signal
from flask_cors import CORS
from utils.event_manager import EventManager

load_dotenv('./.env') #Load env from .env

app = Flask(__name__)
CORS(app, resources={
    r"/*": {  # Change from specific route to all routes
        "origins": ["http://localhost:8000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

app.session_manager = SessionManager()
# Initialize MongoDB when app starts
# mongo_uri = os.getenv("MONGO_URI")
# db = None # Initialize db outside try block for broader scope
# try:
#     db = MongoDB(mongo_uri) # Initialize MongoDB instance
#     app.mongo_client = db # Attach db to app instance for access in routes
#     print(f"MongoDB connected")
# except Exception as e:
#     print(f"Failed to initialize MongoDB in app: {e}")
#     # Handle initialization failure appropriately, maybe exit or disable DB features

# def init_app(app):
#     with app.app_context():
#         context_and_instructions.start(app)

# @app.teardown_appcontext
# def stop_background_tasks(exception=None):
#     context_and_instructions.stop()


# setting up routes
setup_routes(app)




# Registering socket options
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    try:
        # init_app(app)
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error running app: {e}")
        # Ensure cleanup runs even if startup fails
        signal_handler(signal.SIGTERM, None)