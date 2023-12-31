import gradio as gr
import requests
bot_url="YOUR_URL"
header_token="YOUR_TOKEN"
model_uuid="YOUR_MODEL_UUID"
messages = []


#Sending the request
def send_request(message, history):
    # your message
    new_message = {
        "text": message,
        "user_role": True
    }
    messages.append(new_message)
    request_payload = {
        "model_uuid": model_uuid,
        "data": {
            "messages": messages,
            "inference_params": {
                "max_new_tokens": 150,
                "temperature": 0.5,
                "repetition_penalty": 1,
                "top_p": 1,
                "do_sample": True,
                "num_beams": 1,
                "top_k": 50,
                "num_return_sequences": 1,
                "stop_strings": ["", ""]
            },
            "system_prompt": "- You are a helpful assistant chatbot.\n- You answer questions.\n- You are excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.\n- You are more than just an information source, you are also able to write poetry, short stories, and make jokes."
        }
    }
    response = requests.post(bot_url, headers={
        "Content-Type": "application/json",
        "x-api-key": header_token
    }, json=request_payload)
    chunk_response = ""
    reader = response.iter_content(chunk_size=128)
    for chunk in reader:
        chunk_response += chunk.decode('utf-8')
        #appending the respond to the message
    res = {
        "text": chunk_response,
        "user_role": False
    }
    messages.append(res)
    return chunk_response
#Lunching the chat app
chat_interface = gr.ChatInterface(fn=send_request)
chat_interface.launch(share=True)

