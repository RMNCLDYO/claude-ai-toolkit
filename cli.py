import argparse
from claude import Chat, Text, Vision

def main():
    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
        pass
    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                            Claude AI Toolkit                          
                   API Wrapper & Command-line Interface               
                          [v1.0.0] by @rmncldyo                      
    ------------------------------------------------------------------

    Claude AI toolit is an API wrapper and command-line interface for Anthropic's latest Claude 3 large-language models.

    | Option(s)             | Description                          | Example Usage                                      |
    |-----------------------|--------------------------------------|----------------------------------------------------|
    | -c, --chat            | Enable chat mode                     | --chat                                             |
    | -t, --text            | Enable text mode                     | --text                                             |
    | -v, --vision          | Enable vision mode                   | --vision                                           |
    | -p,  --prompt         | User prompt                          | --prompt "Hello, how can I assist you today?"      |
    | -i,  --image          | Image file path or url               | --image "path_or_url_goes_here"                    |
    | -a,  --api_key        | Claude API key for authentication    | --api_key "api_key_goes_here"                      |
    | -m,  --model          | The model you would like to use      | --model "model_name_goes_here"                     |
    | -sp, --system_prompt  | System prompt (instructions)         | --system_prompt "You are an advanced AI assistant" |
    | -mt, --max_tokens     | Maximum number of tokens to generate | --max_tokens 1024                                  |
    | -ss, --stop_sequences | Stop sequences for completion        | --stop_sequences ["SAFTEY_WORD", "SAFTERY_WORD_2"] |
    | -st,  --stream        | Enable streaming mode for responses  | --stream                                           |
    | -tm,  --temperature   | Sampling temperature                 | --temperature 0.7                                  |
    | -tp, --top_p          | Nucleus sampling threshold           | --top_p 0.9                                        |
    | -tk, --top_k          | Top-k sampling threshold             | --top_k 40                                         |
    """,
        formatter_class=CustomFormatter,
        epilog="For detailed usage information, visit our ReadMe here: github.com/RMNCLDYO/claude-ai-toolkit"
    )
    parser.add_argument('-c', '--chat', action='store_true', help='Enable chat mode')
    parser.add_argument('-t', '--text', action='store_true', help='Enable text mode')
    parser.add_argument('-v', '--vision', action='store_true', help='Enable vision mode')
    parser.add_argument('-p', '--prompt', type=str, help='Text or Vision prompt', metavar='')
    parser.add_argument('-i', '--image', type=str, help='Image file path or url', metavar='')
    parser.add_argument('-a', '--api_key', type=str, help='Claude API key for authentication', metavar='')
    parser.add_argument('-m', '--model', type=str, default='claude-3-opus-20240229', help='The model you would like to use', metavar='')
    parser.add_argument('-sp', '--system_prompt', type=str, help='Initial system prompt (instructions)', metavar='')
    parser.add_argument('-mt', '--max_tokens', type=int, help='Maximum number of tokens to generate', metavar='')
    parser.add_argument('-ss', '--stop_sequences', type=str, nargs='+', help='Stop sequences for completion', metavar='')
    parser.add_argument('-st', '--stream', action='store_true', help='Enable streaming mode for responses')
    parser.add_argument('-tm', '--temperature', type=float, help='Sampling temperature', metavar='')
    parser.add_argument('-tp', '--top_p', type=float, help='Nucleus sampling threshold', metavar='')
    parser.add_argument('-tk', '--top_k', type=int, help='Top-k sampling threshold', metavar='')

    args = parser.parse_args()
    
    if args.chat:
        Chat().run(args.api_key, args.model,  args.prompt, args.system_prompt, args.max_tokens, args.stop_sequences, args.stream, args.temperature, args.top_p, args.top_k)
    elif args.text:
        Text().run(args.api_key, args.model, args.prompt, args.system_prompt, args.max_tokens, args.stop_sequences, args.stream, args.temperature, args.top_p, args.top_k)
    elif args.vision:
        Vision().run(args.api_key, args.model, args.prompt, args.image, args.system_prompt, args.max_tokens, args.stop_sequences, args.stream, args.temperature, args.top_p, args.top_k)
    else:
        print("Error: Please specify a mode to use. Use --help for more information.")
        exit()

if __name__ == "__main__":
    main()