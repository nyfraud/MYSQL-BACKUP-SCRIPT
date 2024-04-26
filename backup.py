import subprocess
import requests
import schedule
import time

# MySQL database details
DB_HOST = 'localhost'
DB_USER = ''   #database username
DB_PASSWORD = ''  #database password
DB_NAME = '' #database tablename

# Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1230715716244869130/TlnTzPcd2fduU9EBkr6eb2o6-TjLVxgqT1J1cWIz7W35E3ND72zh9AS-HWQnTwtGdzCV'  #discord webhook

# Backup file name
BACKUP_FILE = 'backup.sql'

def backup_and_send():
    # MySQL dump command
    dump_command = f"mysqldump -u {DB_USER} -p{DB_PASSWORD} -h {DB_HOST} {DB_NAME} > {BACKUP_FILE}"

    # Execute MySQL dump command
    subprocess.run(dump_command, shell=True)

    # Send backup file to Discord webhook
    with open(BACKUP_FILE, 'rb') as f:
        files = {'file': f}
        requests.post(WEBHOOK_URL, files=files)

    # Clean up backup file
    subprocess.run(f"rm {BACKUP_FILE}", shell=True)

# Schedule backup_and_send function to run every 60 minutes
schedule.every(30).minutes.do(backup_and_send)

# Infinite loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
