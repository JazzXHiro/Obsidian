import requests
import json
import sys
import pyperclip

# Replace this with your Imgur Client ID
CLIENT_ID = "830748a57bd78b8"

def upload_image(image_path):
    url = "https://api.imgur.com/3/upload"
    headers = {"Authorization": f"Client-ID {CLIENT_ID}"}

    with open(image_path, "rb") as image_file:
        payload = {"image": image_file.read(), "type": "file"}

    response = requests.post(url, headers=headers, files=payload)
    data = response.json()

    if response.status_code == 200:
        image_url = data["data"]["link"]
        print(f"Image uploaded successfully: {image_url}")

        # Copy the Markdown image link to clipboard
        markdown_link = f"![]({image_url})"
        pyperclip.copy(markdown_link)
        print("Markdown link copied to clipboard. Paste in Obsidian!")

    else:
        print(f"Error uploading image: {data}")

# Get image path from command-line argument
if len(sys.argv) > 1:
    upload_image(sys.argv[1])
else:
    print("Usage: python upload_to_imgur.py <image_path>")
