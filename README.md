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

## Disclaimer
While it's bad practice (*and probably against GDPR*) to send private email addresses around it is even more nefarious to use this script to gain access to said addresses. This script is meant to deter from poor security practices and demonstrate just how dangerous it can be.