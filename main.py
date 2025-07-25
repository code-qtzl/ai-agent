import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt), types.Part(text="I want to call get_files_info..")]),
    ]

    # Loop to call generate_content repeatedly, limited to 20 iterations
    max_iterations = 20
    try:
        for iteration in range(max_iterations):
            if verbose:
                print(f"\n--- Iteration {iteration + 1} ---")
            
            result = generate_content(client, messages, verbose)
            
            # If generate_content returns text (no function calls), we're done
            if result:
                if verbose:
                    print(f"\nFinal response after {iteration + 1} iterations:")
                print(result)
                break
        else:
            if verbose:
                print(f"\nReached maximum iterations ({max_iterations}) without final response")
    except Exception as e:
        print(f"Error occurred during execution: {e}")
        if verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)

def generate_content(client, messages, verbose):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        # Check candidates property and add each candidate's content to messages
        if hasattr(response, 'candidates') and response.candidates:
            for candidate in response.candidates:
                if hasattr(candidate, 'content') and candidate.content:
                    messages.append(candidate.content)
                    if verbose:
                        print(f"Added candidate content to messages: {candidate.content}")

        if not response.function_calls:
            return response.text

        function_responses = []
        for function_call_part in response.function_calls:
            try:
                function_call_result = call_function(function_call_part, verbose)
                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                function_responses.append(function_call_result.parts[0])
            except Exception as e:
                if verbose:
                    print(f"Error calling function {function_call_part.name}: {e}")
                # Continue with other function calls even if one fails
                continue

        if not function_responses:
            raise Exception("no function responses generated, exiting.")
        
        # Convert function responses to a message with role "tool" and add to messages
        tool_message = types.Content(role="tool", parts=function_responses)
        messages.append(tool_message)
        if verbose:
            print(f"Added function responses to messages as tool role")
        
        # Return None to indicate function calls were made (not done yet)
        return None
            
    except Exception as e:
        if verbose:
            print(f"Error in generate_content: {e}")
        raise  # Re-raise the exception to be handled by the main loop


if __name__ == "__main__":
    main()
