# DiningHallRecommender

## Introduction:
This is a Udel Dining hall recomendation service that recommends the best dining hall for you to go to based off of your dining preferences. This solves the problem for freshman who have to look at both the CR and Russell menus to determine which one to go to for a meal. Each user must first take a google survey of their allergys, dietary restrictions (vegan, vegitarian, neither), and their preferential food choices. Once the data is collected the best dining hall is chosen and emailed to them 30 minutes prior to the dining hall opening for breakfast, lunch, and dinner. This email is always sent at the same time because the code is running on an AWS EC2 server with chron job instructions. However the regular emails aren't being sent anymore because my free trial for AWS has terminated and most people didn't end up using it that much.

### Files Summary:

### working_web_scraper_3:
This is the main brain. It scrapes the udel dining website for the menus of all 3 dining halls and parses all of the information to make it easy to calculate the best meal. It also formates all the information to make sending the emails much easier. 

#### email_attempt_1:
Simple email sending

### google_sheet_1:
Gets the data from the google sheet and formats it correctly

### Google Survey Link:
https://forms.gle/XzLqrb3DHNRENKPfA


#### What I learned
- Webscraping with Beautiful soup
- Accessing live google sheet data with python
- Sending emails with python
- Setting up an AWS EC2 server
- Setting up chron jobs
- Linux terminal (Ubuntu)

#### Looking back, What I wish I did differnetly
- I would have broken the working_webscraper_3 file into multiple different files. One for webscraping the info and parsing the info, another for caluclating the scores, and another for formating the scores. This would have made the code much more easily understandable. 
- I should implemented more sorting and search algorithms to decrease run time. Once there were lots of emails (20+) it would start to take 2-3 minutes to send all the emails. Durring the time I made this, I didn't know any search or sorting algorithms and looking back on it now I know I could have implemented a whole lot of them.
- While I could fix these things, because this is no longer being used, and no longer needed there isn't much point to.











