
# Script to extract names from a Company in Linkedin
# by Roberto Ffrench-Davis

"""
HOW TO USE IT:
1. Log in to Linekdin with your account
2. Go to https://www.linkedin.com/company/COMPANY-NAME-URL-HERE/people/ OR just search for the Company in the search bar and go to People. 
3. Find the "People you may know" section here.
4. Scroll Down to start seeing people that work for that company
5. Keep scrolling down until there are no more people LinkedIn can find
6. Ctrl + S to save the page as HTML. Name it "linkedin.html"
7. Run the script as "python3 linkedin.html > employees.txt" to save the extracted names
8. Now, you can generate a list of emails if you want
"""

import re

with open('linkedin.html', 'r') as file:
    html_content = file.read()

# Pattern that the script will look for to extract the names
pattern = r'lt-line-clamp--single-line org-people-profile-card__profile-title t-black" style="">\s+(.*?)\s+<!---->'


matches = re.findall(pattern, html_content)

for match in matches:
    if match != 'LinkedIn Member':
        print(match.strip())
