import re
import json
import time
import argparse
import requests

# Settings
headers = {'User-Agent': 'scrapepwn'}
rate = 2

def main():
    # https://github.com/scissortails
    #
    # Scrapes a file for email addresses then checks haveibeenpwned for
    # corresponding breaches and pastes.
    #
    # For information on API rate limitation: https://haveibeenpwned.com/API/v2

    # Banner
    print(" ___ ___ ___ ___ ___ ___ ___ _ _ _ ___ ")
    print("|_ -|  _|  _| .'| . | -_| . | | | |   |")
    print("|___|___|_| |__,|  _|___|  _|_____|_|_|")
    print("                |_|     |_|            \n\n")
    
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to email list")
    args = parser.parse_args()
    fileName = args.path
    
    try:
        print("Reading " + fileName)
        text = open(fileName, "r").read()
    except Exception as e:
        print(e)
        return
        
    emails = re.findall(r'[\w.-]+@[\w\.-]+', text)
    emails = list(dict.fromkeys(emails))
    print("Found " + str(len(emails)) + " email addresses\n")

    for edx, email in enumerate(emails):
        print("================================" + email + " (" + str(edx+1) + "/" + str(len(emails)) + ")================================\n")
        if check_breach(email):
            time.sleep(rate)            
            check_paste(email)
        time.sleep(rate)


def check_breach(email):
    req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/" + email + "?includeUnverified=true", headers=headers)
    print("[BREACHES]  " + check_status(req.status_code, "breaches") + " (" + str(req.status_code) + ")")
    
    if req.status_code == 200:
        resp = req.json()
        print(str(len(resp)) + " breaches found")
        for item in resp:
            print(item['Name'] + " - " + item['Domain'] + " (" + item['BreachDate'] + ")")
            # Breach output
            for dataclass in item['DataClasses']:
                print("-" + str(dataclass))
            print("")
        return req.status_code


def check_paste(email):
    req = requests.get("https://haveibeenpwned.com/api/v2/pasteaccount/" + email, headers=headers)
    print("[PASTES] " + check_status(req.status_code, "pastes") + " (" + str(req.status_code) + ")")
    
    if req.status_code == 200:
        resp = req.json()
        print(str(len(resp)) + " pastes found")
        # Paste output
        for item in resp:
            print(str(item['Title']) + " - " + str(item['Id']) + " (" + str(item['Source']) + ")")
            
    
def check_status(status_code, desc):
    if status_code == 200:
        return "One or several " + desc + " have been found"
    elif status_code == 400:
        return "Bad request - Format error"
    elif status_code == 403:
        return "Forbidden - User agent missing"
    elif status_code == 404:
        return "No " + desc + " found"
    elif status_code == 429:
        return "Too many requests, the rate limit has been exceeded"
    else:
        return "Unexpected status code: " + str(status_code)
    
    
if __name__ == "__main__":
    main()