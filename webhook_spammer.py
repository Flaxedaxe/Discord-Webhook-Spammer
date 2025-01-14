import requests

def spam_webhook():
    print("Discord Webhook Spam!")
    print("After you start spamming, press Ctrl+C to stop.")
    print("Made by: flaxedaxe | GitHub: https://github.com/Flaxedaxe")

    webhook_url = input("Enter the Discord Webhook URL: ").strip()
    message = input("Enter the message you want to spam: ").strip()
    
    if not webhook_url.startswith("https://discord.com/api/webhooks/"):
        print("Invalid webhook URL. Please enter a valid Discord webhook URL.")
        return
    
    print("\nSpamming Webhook.\n")
    
    while True:
        try:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                print(f"Message sent: {message}")
            else:
                print(f"Failed to send message. Status code: {response.status_code}")
        except KeyboardInterrupt:
            print("\nSpamming stopped.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    spam_webhook()

