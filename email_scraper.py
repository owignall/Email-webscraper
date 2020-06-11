# This script will first take an input url, then search the website for emails, and then finally return the scraped emails.
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from time import sleep

# Scraping functions
def find_page_emails(url):
    emails = []
    links = []
    # Fetching source text
    source = requests.get(url).text
    # Collecting Emails    
    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+')
    email_matches = email_pattern.finditer(source)
    for match in email_matches:
        emails.append(match.group(0))
    # Collecting Links - from both full urls and partial urls
    link_pattern = re.compile(f'href="({url})' + r'[a-zA-Z0-9/\?(\):;=_.+-]+')
    link_partial_pattern = re.compile(r'href="/[a-zA-Z0-9/\?(\):;=_.+-]+')
    link_matches = link_pattern.finditer(source)
    link_partial_matches = link_partial_pattern.finditer(source)
    for match in link_matches: 
        link = match.group(0)[6:]
        links.append(link)
    for match in link_partial_matches:
        link = url + match.group(0)[6:]
        links.append(link)
    return emails, links 
def find_site_emails(url):
    # Clean user input
    if url[-1] == '/':
        url = url[:-1]
    if url[:4] != 'http':
        url = 'https://' + url
    # Scraping landing page for emails and links
    site_emails = []
    page_emails, links = find_page_emails(url)
    print('\n| Searching |')
    site_emails.extend(page_emails)
    links = list(set(links))
    # Scraping linked pages from landing page
    for link in links:
        try:
            print('Searching: ' + link)
            page_emails, links = find_page_emails(link)
            site_emails.extend(page_emails)
        except: pass
    results = list(set(site_emails))
    return results
# Main function
def main():
    print("| Email Webscraper |")
    print("This script will first take an input url, then search the website for emails, and then finally return the scraped emails.")
    print('(Enter "E" to exit)')
    # Main loop
    while True:
        url = input("\n| Input |\nPlease enter a URL: ")
        if url.upper() == "E":
            break
        try:
            email_list = find_site_emails(url)
            print("\n| Results |")
            for email in email_list:
                print(email)
        except:
            print("\n| Result |\nScaper was unable to find the site you entered.")
        sleep(1)

if __name__ == "__main__":
    main()
