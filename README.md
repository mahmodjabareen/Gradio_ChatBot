Project Name
Gradio_Chatbot

Description
after Deploying your LLM model you can connect this app to interact with your model using UI interface

Installation
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/mahmodjabareen/Gradio_ChatBot.git
cd Gradio_ChatBot
Install the required dependencies:
bash
Copy code
pip install gradio
Configuration
Open the main.py file and set the following variables with your specific values:

python
Copy code
bot_url = "Your_URL"
header_token = "Your_Token"
model_uuid = "YOUR_MODEL_UUID"
Modify the values in the request_payload dictionary in the send_request function according to your requirements.
