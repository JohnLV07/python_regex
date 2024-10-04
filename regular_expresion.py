# Python Regular Expression Deep dive
'''
Obejctive:
    The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data. 
    You will tackle a variety of real-world scenarios,
    applying regex to extract, validate, and transform text effectively.


*Task 1*:
    Email Extraction Enhancement

*Problem Statement*
    You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). 
    Modify the script to extract all email addresses except those from the specified domain


*Code Example*:

Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.

Ensure the script still extracts all other valid email addresses. 
'''

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
#this wil replace the email from exclude.com
fixed_text = re.sub(r"\b[A-Za-z0-9._%+-]+@exclude\.com\b", "", text)

new_emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", fixed_text)

print(new_emails)
