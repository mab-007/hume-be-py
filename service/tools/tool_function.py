from service.vendor.gemini_client import GeminiClient

class ToolFunction:
    def __init__(self):
        self.gemini_client = GeminiClient()

    

    async def get_tool_function(self, tool_name, body):
        print("get_tool_function")
        print(f"tool_name: {tool_name}")
        if tool_name == "web_search":
            return await self.web_search(body)
        elif tool_name == "get_current_weather":
            return "37 F"
        else:
            return None

    async def web_search(self, body):
        try:
            print(f"body: {body}")
            prompt = body.get("prompt")
            return self.gemini_client.grounding_google(prompt)
        except Exception as e:
            print(f"Error grounding google: {e}")
            return "Something went wrong!"