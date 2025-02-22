from service.my_class import MyClass
from service import OpenAIClient
from utils.session_manager import SessionManager
from flask import request
from flask import jsonify  
import asyncio
from functools import wraps
from service.tools.tool_function import ToolFunction

def async_route(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(f(*args, **kwargs))
        finally:
            loop.close()
    return wrapper


def setup_routes(app):
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/index')
    def index():
        my_instance = MyClass("Flask App")
        message = my_instance.greet()
        return message
        

    # write a route for update context and instruction which is a async function which is get function
    @app.route('/tool', methods=['GET'])
    @async_route
    async def tool_route():
        try:
            # /tool/:tool_name?prompt=
            tool_name = request.args.get('tool_name')
            prompt = request.args.get('prompt')
            print("Hello")
            tool_function = ToolFunction()
            result = tool_function.get_tool_function(tool_name, prompt)
            return jsonify({"result": result}), 200
        except Exception as e:
            print(f"Error updating context and instruction: {e}")
            return jsonify({"message": "Error updating context and instruction"}), 500
        