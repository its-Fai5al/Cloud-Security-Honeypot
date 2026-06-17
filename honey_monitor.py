import boto3
import requests
import time

# --- ضع بياناتك هنا عند التشغيل فقط، ولا ترفعها للعامة ---
TOKEN = "YOUR_TELEGRAM_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"
BUCKET_NAME = "company-finance-passwords-2026"

def send_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
        requests.get(url)
    except Exception as e:
        print(f"[-] فشل إرسال التنبيه: {e}")

def monitor_s3():
    client = boto3.client('cloudtrail', region_name='eu-north-1')
    last_event_id = None 
    
    print(f"[*] الحارس الأمني يعمل.. يراقب الـ Bucket: {BUCKET_NAME}")
    
    while True:
        try:
            response = client.lookup_events(
                LookupAttributes=[{'AttributeKey': 'ResourceName', 'AttributeValue': BUCKET_NAME}],
                MaxResults=1
            )
            
            if response['Events']:
                event = response['Events'][0]
                current_event_id = event['EventId']
                
                if current_event_id != last_event_id:
                    alert_msg = f"⚠️ تنبيه أمني! نشاط جديد: {event['EventName']} بواسطة {event['Username']}"
                    send_alert(alert_msg)
                    print(f"[!] {alert_msg}")
                    last_event_id = current_event_id 
            
            time.sleep(30) 
            
        except Exception as e:
            print(f"[-] حدث خطأ: {e}")
            time.sleep(60)

if __name__ == "__main__":
    monitor_s3()
