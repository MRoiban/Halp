import openai
from datetime import datetime
import consolemd


# Set up the API key
openai.api_key = "api key"
date = datetime.now().strftime("Month:%m Day:%d Year:%Y")
message_history = [{"role": "system", "content" : "You are Halp, a large language model trained by OpenAI. Answer as concisely as possible, you shall use metric.\nAs a large language model you know the current date, Today's date: " + date}]
history = []
# Define the function for using the ChatGPT API

def ask_chatbot(prompt)->tuple:
    
    message = {"role": "user", "content": prompt}
    message_history.append(message)
    
    query = []
    query.extend(message_history)
    if len(message_history) > 5:
        # print(len(message_history))
        message_history.pop(0)
        message_history.pop(0)
        
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=query, max_tokens=500
    )
    
    message = response["choices"][0]["message"]
    message_history.append({"role": message["role"], "content": message["content"]})
    timestamp = datetime.now().strftime('%H:%M:%S')
    return message["content"], timestamp

# Define the function for displaying the response on HTML page
def display_results()->str:
    prompt = input("\n\x1b[38;2;255;83;112m>\u001b[0m ")
    if prompt == "exit":
        return prompt
    
    message, timestamp = ask_chatbot(prompt)
    output = f"\n>\033[38;2;137;177;109m [{timestamp}] Halp:\u001b[0m \n{message[0::]}"
    return output

def app()->None:
    out = ""
    mkRenderer = consolemd.Renderer(None, "monokai")
    
    while out != "exit":
        out: str = display_results()
        print()    
        mkRenderer.width = 120
        mkRenderer.render(out)
            
    # file: str = open("/home/jarvis/Documents/Projects/chatGPT-Term/history", "a")
    # file.write(str(message_history))
    # file.close()
    return None


if __name__ == "__main__":
    app()
