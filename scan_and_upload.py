import os
import requests

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', 'https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN')

def upload_file_to_discord(file_path):
    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        response = requests.post(DISCORD_WEBHOOK_URL, files=files)
    if response.status_code == 204 or response.status_code == 200:
        print(f'File {file_path} uploaded successfully!')
    else:
        print(f'Failed to upload file: {response.status_code} - {response.text}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scan_and_upload.py <file_path>")
    else:
        # (Burada dosya tarama işlemi ekleyebilirsin, ör: virustotal API, clamav vb.)
        upload_file_to_discord(sys.argv[1])