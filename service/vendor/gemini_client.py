from google import genai
import os
from google.genai import types
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch
import json


class GeminiClient:
    def __init__(self):
        # init gemin client and attacht to current_app
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.gemini_client = genai.Client(api_key=self.api_key, http_options={'api_version':'v1alpha'})
        self.model = "gemini-1.5-flash"
        self.thinking_model = "gemini-2.0-flash-thinking-exp"
        print("Gemini client initialized") # Example initialization

    def generate_text(self, prompt):
        try:
            response = self.gemini_client.models.generate_content(model=self.model, prompt=prompt)
            return response.text
        except Exception as e:
            print(f"Error generating text: {e}")
            return None

    def generate_thinking(self, prompt):
        try:
            system_prompt = """
                You will be given a converstion. Go through the converstaion and identify the following
                1. Name and other details of the user like age etc
                2. User' interests and preferences within the interest
                3. User's mood and emotional status
                4. Summary of the conversation


                Additionally,
                Go through the chat history and give a list of imporant keywords from the conversation.
                Consider only the inputs from the user and NOT the assistant
                EXAMPLE
                User: "My favorite team Lakers lost the match today and I feel sad.
                Output: [basketball, sadness, feelings, Lakers]
                Give the output as Json
            """

            print(f"Generating thinking for prompt: {prompt}")
            config = types.GenerateContentConfig(system_instruction = system_prompt)
            response = self.gemini_client.models.generate_content(model=self.thinking_model, config=config, contents=prompt)
            return response.text
        except Exception as e:
            print(f"Error generating thinking: {e}")
            return None
        
    def generate_thinking_with_system_prompt(self, system_prompt, prompt):
        try:
            config = types.GenerateContentConfig(system_instruction = system_prompt)
            response = self.gemini_client.models.generate_content(model=self.thinking_model, config=config, contents=prompt)
            return response.text
        except Exception as e:
            print(f"Error generating thinking with system prompt: {e}")
            return None
        

    async def grounding_google(self, prompt,model='gemini-2.0-flash', system_prompt=""):
        try:
            print(f"prompt: {prompt}")
            google_search_tool = Tool(
                google_search = GoogleSearch()
            )
            config=GenerateContentConfig(
                tools=[google_search_tool],
                system_instruction=system_prompt,
                response_modalities=["TEXT"],
            )

            response = await self.gemini_client.models.generate_content(model=self.model, config=config, contents=prompt)
            text = response.text
            print(f"text: {text}")
            result_json = json.loads(response.json())
            sources = result_json['candidates'][0]['grounding_metadata']['grounding_chunks']

            return("Search response: "+text+"\nSources: "+str(sources))
        except Exception as e:
            print(f"Error grounding google: {e}")
            return None