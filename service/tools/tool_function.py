from vendor.gemini_client import GeminiClient

class ToolFunction:
    def __init__(self):
        self.gemini_client = GeminiClient()



    def get_tool_function(self, tool_name, body):
        if tool_name == "grounding_google":
            return self.grounding_google(body)
        else:
            return None

    def grounding_google(self, prompt):
        try:
            return self.gemini_client.grounding_google(prompt)
        except Exception as e:
            print(f"Error grounding google: {e}")
            return "Something went wrong!"