# 🛡️ Cloud Security Honeypot Monitor

A proactive cloud security project designed to detect unauthorized access attempts on AWS S3 buckets in real-time.

## 📌 Project Overview
This project acts as a "honeypot" security system. By monitoring a specific S3 bucket for any API activity, the system triggers immediate alerts via Telegram if any interaction is detected. It leverages **AWS CloudTrail** for event auditing and a custom **Python** script for automated threat intelligence.

## 🚀 Key Features
* **Real-time Monitoring:** Continuous auditing of S3 bucket activity using AWS CloudTrail.
* **Intelligent Alerting:** Integrated with the Telegram Bot API to deliver instant notifications.
* **Event Filtering:** Implemented a memory-based filtering logic to prevent spamming and ensure only unique, new events are reported.
* **Security Principle:** Demonstrates the implementation of IAM least-privilege access.

## 🛠 Technologies Used
* **Cloud:** AWS (S3, CloudTrail, IAM)
* **Language:** Python (Boto3 SDK)
* **Communication:** Telegram Bot API

## ⚙️ How it Works
1. **Honeypot:** An S3 bucket serves as the decoy for potential attackers.
2. **Detection:** A Python script periodically polls AWS CloudTrail API to look for activity related to the bucket.
3. **Alerting:** Upon detecting a new event, the script sends a formatted security alert to a designated Telegram chat.

## 📝 How to Run
1. Configure AWS CLI with appropriate read-only permissions.
2. Update the `TOKEN`, `CHAT_ID`, and `BUCKET_NAME` in `honey_monitor.py`.
3. Run the script: `python honey_monitor.py`

---
*Created by its-Fai5al*
