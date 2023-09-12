
# **Project Name**
Gradio_Chatbot
# **Description**
after Deploying your LLM model you can connect this app to interact with your model using UI interface
# **Installation**
Clone this repository to your local machine:
```bash
git clone https://github.com/mahmodjabareen/Gradio_ChatBot.git 
cd Gradio_ChatBot
```
# **Install the required dependencies:**
```bash
pip install gradio
```
# **Configuration**
Open the main.py file and set the following variables with your specific values:

```python
bot_url="YOUR_URL"
header_token="YOUR_TOKEN"
model_uuid="YOUR_MODEL_UUID"
```
Modify the values in the request_payload dictionary in the send_request function according to your requirements.
# **Sharing Your Application**
The sharing feature is enabled by default, making it effortless to share your application. The URL format for your colleagues to access the chatbot will appear as follows:
-   Local URL: http://127.0.0.1:7860
-   Public URL: https://URL.gradio.live
To utilize this feature, you can use the following Python code:
```python
chat_interface.launch(share=True)
```
This code will generate both local and public URLs, simplifying the process of sharing your chatbot application with others in a professional manner.
# **run the app**
```python
python main.py
```
