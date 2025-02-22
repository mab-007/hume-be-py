from service.vendor.gemini_client import GeminiClient

class ToolFunction:
    def __init__(self):
        self.gemini_client = GeminiClient()

    async def get_tool_function(self, tool_name, body):
        if tool_name == "web_search":
            return await self.grounding_google(body)
        elif tool_name == "get_current_weather":
            return "37 F"
        else:
            return None

    async def grounding_google(self, body):
        try:
            prompt = body.get("prompt")
            print(f"prompt: {prompt}")
            result = self.gemini_client.grounding_google(prompt)
            print(f"result: {result}")  
            return result
        except Exception as e:
            print(f"Error grounding google: {e}")
            return "Something went wrong!"