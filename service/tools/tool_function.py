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
        elif tool_name == "location_topics":
            return await self.location_topics(body)
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
    
    async def location_topics(self, body):
        try:
            print(f"body: {body}")
            location = body.get("location")
            system_prompt = "You will be given a location anywhere from the world. Your job is to find conversational topics relevant to the location that a person who has grown up there or stays there will find relevant. This can include things like what the city is famous for, famous spots, weather etc. The topics you find should be relevant for a person who has grown up in the city, a localite."
            return self.gemini_client.grounding_google(prompt=location, model='gemini-2.0-pro',system_prompt=system_prompt)
        except Exception as e:
            print(f"Error grounding google: {e}")
            return "Something went wrong!"