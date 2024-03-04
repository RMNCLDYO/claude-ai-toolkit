<p align="center">
    <a href=".github/version.json" title="Go to changelog" target="_blank">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Claude+AI+Toolkit&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2Fclaude-ai-toolkit%2Fmain%2F.github%2Fversion.json" alt="Version">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog" target="_blank"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc" target="_blank"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="/">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-dark.png">
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-light.png">
          <img alt="Claude AI" width="500" src="https://raw.githubusercontent.com/RMNCLDYO/claude-ai-toolkit/main/.github/anthropic-logo-light.png">
        </picture>
    </a>
</p>

## Overview

The Claude AI Toolkit is a versatile API wrapper and command-line interface designed to simplify interactions with Anthropic's Claude 3 family of large language models. This toolkit facilitates easy access to the latest Claude models, including Opus, Sonnet, and Haiku, for tasks involving language understanding, conversation, coding, and vision processing. Whether you're a beginner in AI or an experienced developer, the Claude AI Toolkit is built to enhance your productivity and streamline your development process with Claude.

## Features

- **Chat Mode**: Engage in interactive conversations with the Claude model of your choice.
- **Text Mode**: Submit text prompts and receive responses, ideal for scripting and automation.
- **Vision Mode**: Process and analyze images with Claude's advanced vision capabilities.
- **Streaming Support**: Utilize streaming responses for real-time interaction with models.
- **Flexible Configuration**: Customize model parameters, including API keys, model selection, token limits, and more.

## Prerequisites

- Python 3.6+

## Dependencies
The following Python packages are required:
- `requests`: For making HTTP requests to the Claude API.

The following Python packages are optional:
- `python-dotenv`: For managing API keys and other environment variables.

## Installation

1. Clone the repository:
    ```shell
    git clone https://github.com/RMNCLDYO/claude-ai-toolkit.git
    ```

2. Navigate to the folder
    ```shell
    cd claude-ai-toolkit
    ```

3. Install the dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Getting Started

#### Obtaining an API Key

1. Sign up and verify your account at [Claude AI](https://console.anthropic.com/).
2. Navigate to API Keys in your account settings.
3. Click Create Key, name it, and save it securely.

### Configuration (*Optional*)

Create a .env file in the root directory and add your API key:
```shell
CLAUDE_API_KEY=your_api_key_here
```

## Usage

### CLI

*Chat with Claude*:
```shell
python cli.py --chat
```

*Ask a question*:
```shell
python cli.py --text --prompt "What is the meaning of life?"
```

*Describe an image*:
```shell
python cli.py --vision --prompt "Describe this image." --image "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
```

*Get usage details and options*:
```shell
python cli.py --help
```

### Wrapper

*Chat with Claude*:
```python
from claude import Chat

Chat().run()
```

> An executable version of this example can be found [here](./examples/example_chat.py). (*You must move this file to the root folder before running the program.*)

*Ask a question*:
```python
from claude import Text

Text().run(prompt="What is the meaning of life?")
```

> An executable version of this example can be found [here](./examples/example_text.py). (*You must move this file to the root folder before running the program.*)

*Describe an image*:
```python
from claude import Vision

Vision().run(prompt="Describe this image.", image="https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg")
```

> An executable version of this example can be found [here](./examples/example_vision.py). (*You must move this file to the root folder before running the program.*)

## Advanced Configuration

### Wrapper Options
| Option(s)        | Description                          | Example Usage                                    |
|------------------|--------------------------------------|--------------------------------------------------|
| `prompt`         | User prompt                          | prompt="Hello, how can I assist you today?"      |
| `image`          | Image file path or url               | image="path_or_url_goes_here"                    |
| `api_key`        | Claude API key for authentication    | api_key="api_key_goes_here"                      |
| `model`          | The model you would like to use      | model="model_name_goes_here"                     |
| `system_prompt`  | System prompt (instructions)         | system_prompt="You are an advanced AI assistant" |
| `max_tokens`     | Maximum number of tokens to generate | max_tokens=1024                                  |
| `stop_sequences` | Stop sequences for completion        | stop_sequences=["SAFTEY_WORD", "SAFTERY_WORD_2"] |
| `stream`         | Enable streaming mode for responses  | stream=True                                      |
| `temperature`    | Sampling temperature                 | temperature=0.7                                  |
| `-top_p`         | Nucleus sampling threshold           | top_p=0.9                                        |
| `top_k`          | Top-k sampling threshold             | top_k=40                                         |

### CLI Options
| Option(s)                  | Description                          | Example Usage                                      |
|----------------------------|--------------------------------------|----------------------------------------------------|
| `-c`,  `--chat`            | Enable chat mode                     | --chat                                             |
| `-t`,  `--text`            | Enable text mode                     | --text                                             |
| `-v`,  `--vision`          | Enable vision mode                   | --vision                                           |
| `-p`,  `--prompt`          | User prompt                          | --prompt "Hello, how can I assist you today?"      |
| `-i`,  `--image`           | Image file path or url               | --image "path_or_url_goes_here"                    |
| `-a`,  `--api_key`         | Claude API key for authentication    | --api_key "api_key_goes_here"                      |
| `-m`,  `--model`           | The model you would like to use      | --model "model_name_goes_here"                     |
| `-sp`, `--system_prompt`   | System prompt (instructions)         | --system_prompt "You are an advanced AI assistant" |
| `-mt`, `--max_tokens`      | Maximum number of tokens to generate | --max_tokens 1024                                  |
| `-ss`, `--stop_sequences`  | Stop sequences for completion        | --stop_sequences ["SAFTEY_WORD", "SAFTERY_WORD_2"] |
| `-st`, `--stream`          | Enable streaming mode for responses  | --stream                                           |
| `-tm`, `--temperature`     | Sampling temperature                 | --temperature 0.7                                  |
| `-tp`, `--top_p`           | Nucleus sampling threshold           | --top_p 0.9                                        |
| `-tk`, `--top_k`           | Top-k sampling threshold             | --top_k 40                                         |

## Advanced Usage

### CLI

*Initiate a chat session passing your API key, with streaming mode set, and a custom system prompt*:
```shell
python cli.py --chat --api_key "your_api_key" --stream --system_prompt "You are a comedian, you respond to all questions as if they are a funny joke."
```

### Wrapper

*Initiate a chat session using the Claude 3 Sonnet model, with top_p and max_tokens set to 100*:
```python
from claude import Chat

Chat().run(model="claude-3-sonnet-20240229", max_tokens=100, top_p=0.9)
```

## Available Models

| **Model**       	| **Latest API model name**  	| **Max Tokens** 	|
|-----------------	|----------------------------	|----------------	|
| Claude 3 Opus   	| `claude-3-opus-20240229`   	| 4096 tokens    	|
| Claude 3 Sonnet 	| `claude-3-sonnet-20240229` 	| 4096 tokens    	|
| Claude 3 Haiku  	| Coming soon                	| 4096 tokens    	|

## API Rate Limits

| **Usage tier** 	| **Requests per minute (RPM)** 	| **Tokens per minute (TPM)** 	| **Tokens per day (TPD)** 	|
|----------------	|-------------------------------	|-----------------------------	|--------------------------	|
| Free           	| 5                             	| 25,000                      	| 300,000                  	|
| Build Tier 1   	| 50                            	| 50,000                      	| 1,000,000                	|
| Build Tier 2   	| 1,000                         	| 100,000                     	| 2,500,000                	|
| Build Tier 3   	| 2,000                         	| 200,000                     	| 5,000,000                	|
| Build Tier 4   	| 4,000                         	| 400,000                     	| 10,000,000               	|
| Scale          	| Custom                        	| Custom                      	| Custom                   	|

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/claude-ai-toolkit/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/claude-ai-toolkit/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
