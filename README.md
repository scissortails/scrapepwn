# scrapepwn
A Python (3.6.4) script for extracting emails and checking them against [haveibeenpwned](https://haveibeenpwned.com/) for breaches and pastes. If the account has been breached any information will be listed. If pastes are found, so will they.

This is a great tool to finally convince people to [stop sending emails to multiple people via CC](https://www.theregister.co.uk/2018/05/29/bcc_is_hard_okay_organisations_blab_email_addresses_in_gdpr_mailouts/).

## Configuration
There is very little configuration within scrapepwn. The rate limit towards haveibeenpwned's API can be changed but it is not recommended.

## Using scrapepwn
scrapepwn thrives on emails with multiple visible recipients. Simply save the email and point the script towards it. There is only one argument, **path**. Finally, you can run scrapepwn through the following command:
```
python main.py email.txt
```

If scrapepwn finds anything it'll give you an output as follows:
```
 ___ ___ ___ ___ ___ ___ ___ _ _ _ ___
|_ -|  _|  _| .'| . | -_| . | | | |   |
|___|___|_| |__,|  _|___|  _|_____|_|_|
                |_|     |_|


Reading example.txt
Found 1 email addresses

================================test@example.com (1/1)================================

[BREACHES]  One or several breaches have been found (200)
68 breaches found
000webhost - 000webhost.com (2015-03-01)
-Email addresses
-IP addresses
-Names
-Passwords
...

[PASTES] One or several pastes have been found (200)
57 pastes found
BuzzMachines.com 40k+ - http://siph0n.in/exploits.php?id=4560 (AdHocUrl)
balockae.online - http://balockae.online/files/BlackMarketReloaded_users.sql (AdHocUrl)
...
```

## Disclaimer
While it's bad practice (*and probably against GDPR*) to send private email addresses around it is even more nefarious to use this script to gain access to said addresses. This script is meant to deter from poor security practices and demonstrate just how dangerous it can be.