from service.my_class import MyClass
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
    @app.route('/api/tool/<tool_name>', methods=['POST'])
    @async_route
    async def tool_route(tool_name):
        try:
            print(f"tool_name: {tool_name}")
            print(f"Received raw data: {request.get_data()}")
            data = request.get_json()
            print(f"data: {data}")
            parameters = data.get('parameters', {})
            print(f"parameters: {parameters}")
            tool_function = ToolFunction()
            result = await tool_function.get_tool_function(tool_name, parameters)
            print(f"result: {result}")
            return jsonify({"result": result}), 200
        except Exception as e:
            print(f"Error processing tool request: {e}")
            return jsonify({"error": str(e)}), 500
        