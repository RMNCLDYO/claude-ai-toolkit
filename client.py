import json
import requests
from config import load_config
from loading import Loading

print("------------------------------------------------------------------\n")
print("                         Claude AI Toolkit                        \n")     
print("               API Wrapper & Command-line Interface               \n")   
print("                       [v1.0.2] by @rmncldyo                      \n")  
print("------------------------------------------------------------------\n")

class Client:
    def __init__(self, api_key=None):
        self.config = load_config(api_key=api_key)
        self.api_key = api_key if api_key else self.config.get('api_key')
        self.base_url = self.config.get('base_url')
        self.claude_version = self.config.get('claude_version')
        self.anthropic_version = self.config.get('anthropic_version')
        self.headers = {
            "anthropic-version": self.anthropic_version,
            "content-type": "application/json",
            "x-api-key": self.api_key
        }

    def post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.claude_version}/{endpoint}"
        try:
            loading.start()
            response = requests.post(url, headers=self.headers, json=data)
            response = response.json()
            try:
                response = response["content"][0]["text"]
                return response
            except:
                loading.stop()
                print(f"\nError: {response['error']["message"]}")
                exit(1)
        except Exception as e:
            print(f"HTTP Error: {e}")
            raise
        finally:
            loading.stop()

    def stream_post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.claude_version}/{endpoint}"
        full_response = []
        try:
            loading.start()
            response = requests.post(url, headers=self.headers, json=data, stream=True)
            response.raise_for_status()
            loading.stop()
            response_content = ""
            print("Assistant: ", end="", flush=True)
            for line in response.iter_lines():
                if line and 'text_delta' in line.decode('utf-8'):
                    try:
                        json_line = line.decode('utf-8').split("data: ")[1]
                        event_data = json.loads(json_line)
                        if event_data.get("type") == "content_block_delta":
                            content = event_data.get("delta", {}).get("text", "")
                            print(content, end="", flush=True)
                            response_content += content
                    except Exception as e:
                        print(f"JSON Error: {e}")
                        raise
            full_response.append(response_content)
            print()
            return full_response[0]
        except Exception as e:
            print(f"Stream HTTP Error: {e}")
            raise
        finally:
            loading.stop()
