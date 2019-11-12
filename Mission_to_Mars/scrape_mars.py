#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dependencies
import pandas as pd
import numpy as np
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup
time.sleep(5)

# In[2]:


def scrape_info():
    # chromedriver path
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    time.sleep(5)

    # In[3]:

    ### nasa mars news ###
    nasa_mars_news_url = "https://mars.nasa.gov/news/"
    nasa_mars_news_html = requests.get(nasa_mars_news_url)

    # In[4]:

    nasa_mars_news_soup = BeautifulSoup(
        nasa_mars_news_html.text, "html.parser")

    # In[5]:

    nasa_mars_news_title = nasa_mars_news_soup.find(
        "div", class_="content_title").text
    print(f"Latest News Title: {nasa_mars_news_title}")

    # In[6]:

    nasa_mars_news_paragraph = nasa_mars_news_soup.find(
        "div", class_="rollover_description_inner").text
    print(f"Paragraph Text: {nasa_mars_news_paragraph}")

    # In[7]:

    ### jpl mars space images ###
    jpl_mars_images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_mars_images_url)
    jpl_mars_images_html = browser.html
    time.sleep(5)

    # In[8]:

    jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")

    # In[9]:

    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(5)

    # In[10]:

    browser.click_link_by_partial_text("more info")
    time.sleep(5)

    # In[11]:

    jpl_mars_images_html = browser.html

    # In[12]:

    jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")

    # In[13]:

    image_url = jpl_mars_images_soup.find("img", class_='main_image')
    image_url = image_url.get("src")
    print("Image URL:", image_url)

    # In[14]:

    featured_image_url = "https://www.jpl.nasa.gov" + image_url
    print("Featured Image URL:", featured_image_url)

    # In[15]:

    ### mars weather ###
    twitter_mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    twitter_mars_weather_html = requests.get(twitter_mars_weather_url)

    # In[16]:

    twitter_mars_weather_soup = BeautifulSoup(
        twitter_mars_weather_html.text, "html.parser")
    time.sleep(5)

    # In[17]:

    mars_weather = twitter_mars_weather_soup.find(
        "p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print("Mars Weather:", mars_weather)

    # In[18]:

    ### mars facts ###
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts_html = requests.get(mars_facts_url)
    time.sleep(5)

    # In[19]:

    mars_facts_soup = BeautifulSoup(mars_facts_html.text, "html.parser")

    # In[20]:

    mars_facts = mars_facts_soup.find(
        "table", class_="tablepress tablepress-id-p-mars")
    print(mars_facts)

    # In[21]:

    # mars hemispheres ### method 1
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[22]:

    usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[23]:

    mars_hemisphere_name = usgs_soup.find_all("h3")

    # In[24]:

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    time.sleep(5)

    # In[25]:

    browser.click_link_by_partial_text('Open')

    # In[26]:

    usgs_html_1 = browser.html

    # In[27]:

    usgs_soup_1 = BeautifulSoup(usgs_html_1, "html.parser")

    # In[28]:

    image_url_1 = usgs_soup_1.find("img", class_='wide-image')
    image_url_1 = image_url_1.get("src")
    print("Image URL:", image_url_1)

    # In[29]:

    featured_image_url_1 = "https://astrogeology.usgs.gov" + image_url_1
    print("Featured Image URL:", featured_image_url_1)

    # In[30]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[31]:

    usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[32]:

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(5)

    # In[33]:

    browser.click_link_by_partial_text('Open')

    # In[34]:

    usgs_html_2 = browser.html

    # In[35]:

    usgs_soup_2 = BeautifulSoup(usgs_html_2, "html.parser")

    # In[36]:

    image_url_2 = usgs_soup_2.find("img", class_='wide-image')
    image_url_2 = image_url_2.get("src")
    print("Image URL:", image_url_2)

    # In[37]:

    featured_image_url_2 = "https://astrogeology.usgs.gov" + image_url_2
    print("Featured Image URL:", featured_image_url_2)

    # In[38]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[39]:

    usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[40]:

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(5)

    # In[41]:

    browser.click_link_by_partial_text('Open')

    # In[42]:

    usgs_html_3 = browser.html

    # In[43]:

    usgs_soup_3 = BeautifulSoup(usgs_html_3, "html.parser")

    # In[44]:

    image_url_3 = usgs_soup_3.find("img", class_='wide-image')
    image_url_3 = image_url_3.get("src")
    print("Image URL:", image_url_3)

    # In[45]:

    featured_image_url_3 = "https://astrogeology.usgs.gov" + image_url_3
    print("Featured Image URL:", featured_image_url_3)

    # In[46]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[47]:

    usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[48]:

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(5)

    # In[51]:

    browser.click_link_by_partial_text('Open')

    # In[52]:

    usgs_html_4 = browser.html

    # In[53]:

    usgs_soup_4 = BeautifulSoup(usgs_html_4, "html.parser")

    # In[54]:

    image_url_4 = usgs_soup_4.find("img", class_='wide-image')
    image_url_4 = image_url_4.get("src")
    print("Image URL:", image_url_4)
    time.sleep(5)

    # In[55]:

    featured_image_url_4 = "https://astrogeology.usgs.gov" + image_url_4
    print("Featured Image URL:", featured_image_url_4)

    # In[56]:

    # mars hemispheres ### method 2
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html

    # In[57]:

    usgs_soup = BeautifulSoup(usgs_html, "html.parser")
    usgs_soup.body

    # In[58]:

    mars_hemisphere_name = usgs_soup.find_all("div", class_="description")
    mars_hemisphere_name
    time.sleep(5)

    # In[59]:

    featured_image_urls = []

    # In[60]:

    for name in mars_hemisphere_name:
        featured_image_url = name.find("a", class_="itemLink product-item")
        print(featured_image_url)
        hemisphere = featured_image_url.get("href")
        hemisphere_url = "https://astrogeology.usgs.gov" + hemisphere
        print(hemisphere_url)

        browser.visit(hemisphere_url)

        hemisphere_url_dict = {}

        usgs_html = browser.html
        usgs_soup = BeautifulSoup(usgs_html, "html.parser")

        hemisphere_url = usgs_soup.find("a", text="Original")
        hemisphere_url = hemisphere_url.get("href")

        hemisphere_name = usgs_soup.find(
            "h2", class_="title").text.replace(" Enhanced", "")

        hemisphere_url_dict["title"] = hemisphere_name
        hemisphere_url_dict["img_url"] = hemisphere_url

        featured_image_urls.append(hemisphere_url_dict)

    print(featured_image_urls)

    marsData = {"News Title": nasa_mars_news_title,
                "News Paragraph": nasa_mars_news_paragraph,
                "JPL Image URL": featured_image_url,
                "Twitter Weather": mars_weather,
                "Facts Table": mars_facts
                }

    # In[61]:

    browser.quit()
    time.sleep(5)

    # In[62]:

    # convert jupyter notebook into python script called 'scrape_mars.py'
    # get_ipython().system(
    #     ' jupyter nbconvert --to script --template basic mission_to_mars.ipynb --output scrape_mars')

    return marsData
