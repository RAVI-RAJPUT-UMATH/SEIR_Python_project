# SEIR Python Web Scraper

## Project Overview

This project is a simple command-line based Web Scraper built using Python.

It extracts:

- Page Title
- Page Body Text
- All Hyperlinks from a webpage

The goal of this project was to practically apply the concepts of Web Scraping learned through online courses and self-study.

## Learning Journey

I learned the fundamentals of Web Scraping from:

- A Web Scraping course on Udemy
- Google searches for syntax references and documentation
- Official Python and BeautifulSoup documentation

After understanding concepts like:

- Client-Server Model
- HTTP Requests & Responses
- HTTP Methods (GET, POST)
- Status Codes
- Headers and User-Agent
- HTML Structure
- BeautifulSoup parsing

I implemented those concepts into this project.

This project represents my hands-on practice after completing the learning phase.

##  Technologies Used

- Python
- requests library
- BeautifulSoup (bs4)
- sys module

##  How It Works

1. Takes a URL from command line argument.
2. Sends HTTP GET request using requests.
3. Adds a custom User-Agent header to avoid blocking.
4. Parses HTML using BeautifulSoup.
5. Extracts:
   - <title> tag content
   - <body> text
   - All <a> tag links
