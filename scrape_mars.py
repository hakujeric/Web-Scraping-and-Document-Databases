#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time
executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


#Nasa Mars News

def marsNews():
    # Visit Nasa news url 
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')


    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Display scrapped data 
    news = [news_title,news_p]
    return news

# ### JPL Mars Space Images - Featured Image

def retrieveImange():
    # Visit Mars Space Images 
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)


    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + featured_image_url

    # Display full link to featured image
    return featured_image_url


# ### Mars Weather

# Visit Mars Weather Twitter through splinter module
weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(weather_url)


# HTML Object 
html_weather = browser.html

# Parse HTML with Beautiful Soup
soup = bs(html_weather, 'html.parser')

# Find all elements that contain tweets
latest_tweets = soup.find_all('div', class_='js-tweet-text-container')
# latest_tweets
# Retrieve all elements that contain news title in the specified range
# Look for entries that display weather related words to exclude non weather related tweets 
for tweet in latest_tweets: 
    weather_tweet = tweet.find('p').text
    if 'Sol' and 'pressure' in weather_tweet:
        mars_weather = weather_tweet
        break
    else: 
        pass
print(mars_weather)


# ### Mars Facts


# Visit Mars facts url 
facts_url = 'http://space-facts.com/mars/'

# Use Panda's `read_html` to parse the url
mars_facts = pd.read_html(facts_url)

# Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
mars_df = mars_facts[0]

# Assign the columns `['Description', 'Value']`
mars_df.columns = ['Description','Value']

# Display mars_df
mars_df


#Convert into HTML Table
mars_html = mars_df.to_html()
mars_html = mars_html.replace("\n", "")
mars_html


# ### Mars Hemispheres

# Visit hemispheres website 
hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemispheres_url)


# In[24]:


# HTML Object
from urllib.parse import urlsplit
hemispheres_html = browser.html

# Parse HTML with Beautiful Soup
soup = bs(hemispheres_html, 'html.parser')

# Retreive all items that contain mars hemispheres information
items = soup.find_all('div', class_='item')

items


# Create empty list for hemisphere urls 
hemisphere_image_urls = []

# Store the main_ul 
hemispheres_main_url = "{0.scheme}://{0.netloc}/".format(urlsplit(hemispheres_url))
hemispheres_main_url



# Loop through the items previously stored
for i in items: 
    # Store title
    title = i.find('h3').text
    
    # Store link that leads to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Visit the link that contains the full image website 
    browser.visit(hemispheres_main_url + partial_img_url)
    
    # HTML Object of individual hemisphere information website 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
    soup = bs( partial_img_html, 'html.parser')
    
    # Retrieve full image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    # Append the retreived information into a list of dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    

# Display hemisphere_image_urls
hemisphere_image_urls

