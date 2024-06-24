import os

def load_required_env_variables(var_name: str):
    value = os.getenv(var_name)
    if value is None:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            value = os.getenv(var_name)
            if value is None or value.strip() == "":
                print(f"Error: {var_name} environment variable is not defined. Please define it in a .env file or directly in your environment. You can also pass it as an argument to the function.")
                exit(1)
        except ImportError:
            print("Error: dotenv package is not installed. Please install it with 'pip install python-dotenv' or define the environment variables directly.")
            exit(1)
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            exit(1)
    return value

def load_config(api_key=None):
    if not api_key:
        api_key = load_required_env_variables('CLAUDE_API_KEY')
    
    return {
        'api_key': api_key,
        'model': os.getenv('CLAUDE_MODEL', 'claude-3-5-sonnet-20240620'),
        'base_url': os.getenv('CLAUDE_BASE_URL', 'https://api.anthropic.com'),
        'messages_endpoint': os.getenv('CLAUDE_MESSAGES_ENDPOINT', 'messages'),
        'timeout': int(os.getenv('CLAUDE_TIMEOUT', 20)),
        'claude_version': os.getenv('CLAUDE_VERSION', 'v1'),
        'anthropic_version': os.getenv('ANTHROPIC_VERSION', '2023-06-01')
    }