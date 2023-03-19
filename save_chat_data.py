import openai
import datetime
import os
import requests
from google.oauth2.credentials import Credentials

# Set up OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Set up the path to the file where you want to store your chats
filename = "chat_data.txt"

# Set up the Google Drive folder ID where you want to save the chat data
folder_id = "YOUR_FOLDER_ID"

# Set up Google Drive API credentials
creds = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/drive'])

# Define a function to save your chat data to Google Drive
def save_chat_data():
    # Get the current date and time
    now = datetime.datetime.now()

    # Get the latest messages from ChatGPT
    response = openai.Completion.create(
        engine="davinci", prompt="...", max_tokens=1024, temperature=0.5
    )
    messages = response.choices[0].text

    # Get the conversation ID from the response
    conversation_id = response.conversation_id

    # Set up the filename to save the chat data
    filename = f"chat_data_{conversation_id}.txt"

    # Write the messages and date/time to the file
    with open(filename, "a") as f:
        f.write("Chat data for " + str(now) + ":\n")
        f.write(messages + "\n\n")

    # Upload the file to Google Drive
    url = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"
    headers = {"Authorization": f"Bearer {creds.token}"}
    params = {"name": filename, "parents": [folder_id]}
    files = {"data": open(filename, "rb")}
    r = requests.post(url, headers=headers, params=params, files=files)

    # Delete the file from local disk
    os.remove(filename)

# Call the function to save the chat data
save_chat_data()