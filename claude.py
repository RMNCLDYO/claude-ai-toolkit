import os
import time
import base64
import requests
from client import Client

class Chat:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        conversation_history = []

        print("Assistant: Hello! How can I assist you today?")
        while True:
            if prompt:
                user_input = prompt.strip()
                print(f"User: {user_input}")
                prompt = None
            else:
                user_input = input("User: ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Claude AI toolkit. Have a great day!")
                    break

                if not user_input:
                    print("Invalid input detected. Please enter a valid message.")
                    continue
            
            conversation_history.append({"role": "user", "content": user_input})
            
            data = {
                "messages": conversation_history,
                "model": self.model,
                "system_prompt": system_prompt,
                "max_tokens": self.max_tokens,
                "stop_sequences": stop_sequences,
                "stream": stream,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k
            }
            data = {k: v for k, v in data.items() if v is not None}
            
            endpoint = self.client.config.get('messages_endpoint')

            if stream:
                response = self.client.stream_post(endpoint, data)
                assistant_response = response
            else:
                response = self.client.post(endpoint, data)
                assistant_response = response
                print(f"Assistant: {assistant_response}")
            conversation_history.append({"role": "assistant", "content": assistant_response})

class Text:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        if not prompt:
            print("Error: { Invalid input detected }. Please enter a valid message.")
            exit(1)
        
        data = {
            "messages": [{"role": "user", "content": prompt}],
            "model": self.model,
            "system_prompt": system_prompt,
            "max_tokens": self.max_tokens,
            "stop_sequences": stop_sequences,
            "stream": stream,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        endpoint = self.client.config.get('messages_endpoint')

        if stream:
            response = self.client.stream_post(endpoint, data)
            assistant_response = response
        else:
            response = self.client.post(endpoint, data)
            assistant_response = response
            print(f"Assistant: {assistant_response}")

class Vision:
    def __init__(self):
        self.client = None
        self.directory_path = os.path.dirname(__file__)
        self.image_folder_path = os.path.join(self.directory_path, 'images')
        os.makedirs(self.image_folder_path, exist_ok=True)

    def process_image_input(self, image_input):
        if image_input.startswith(('http://', 'https://', 'www')):
            image_path = self.download_image_and_save(image_input)
        elif os.path.exists(image_input):
            image_path = image_input
        else:
            image_path = None
            print(f"\nImage not found at path: {image_input}\n\nPlease check your image path or URL and try again.\n\n( If you are using a URL, please make sure the url starts with `http`, `https`, or `www`.)\n")
            exit()
        return image_path

    def download_image_and_save(self, image_url):
        response = requests.get(image_url)
        extension = self.get_mime_type(image_url).split("/")[1]
        if response.status_code == 200:
            filename = f"{str(time.time())}.{extension}"
            image_path = f"{self.image_folder_path}/{filename}"
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return image_path
        else:
            print(f"Failed to download image at url: {image_url}. Please check the URL and try again.")
            exit()
            
    def image_to_base64(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            print(f"Failed to convert the image to base64. Error: {e}")
            exit()
        
    def get_mime_type(self, image_path):
        if image_path.endswith(".jpg") or image_path.endswith(".jpeg"):
            return "image/jpeg"
        elif image_path.endswith(".png"):
            return "image/png"
        elif image_path.endswith(".webp"):
            return "image/webp"
        elif image_path.endswith(".gif"):
            return "image/gif"
        else:
            print(f"Unsupported image format. Please use a .jpg, .jpeg, .png, .webp, or .gif image file.")
            exit()

    def run(self, api_key=None, model=None, prompt=None, image=None, system_prompt=None, max_tokens=None, stop_sequences=None, stream=None, temperature=None, top_p=None, top_k=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('model')
        self.max_tokens = max_tokens if max_tokens else 1024

        if image:
            image_path = self.process_image_input(image)
            image_base64 = self.image_to_base64(image_path)
            mime_type = self.get_mime_type(image_path)
            
            vision_prompt = [
                {
                    "role": "user", 
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": mime_type,
                                "data": image_base64,
                            }
                        },
                        {
                            "type": "text", 
                            "text": prompt
                        }
                    ]
                }
            ]

        else:
            vision_prompt = None
            
        data = {
            "messages": vision_prompt,
            "model": self.model,
            "system_prompt": system_prompt,
            "max_tokens": self.max_tokens,
            "stop_sequences": stop_sequences,
            "stream": stream,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        endpoint = self.client.config.get('messages_endpoint')

        if stream:
            response = self.client.stream_post(endpoint, data)
            assistant_response = response
        else:
            response = self.client.post(endpoint, data)
            assistant_response = response
            print(f"Assistant: {assistant_response}")