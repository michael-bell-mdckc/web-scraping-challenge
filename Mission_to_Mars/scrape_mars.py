#!/usr/bin/env python
# coding: utf-8

# In[27]:


# dependencies
import pandas as pd
import numpy as np
import requests
import time
from splinter import Browser
from bs4 import BeautifulSoup

time.sleep(5)


# In[28]:


# chromedriver path
def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

# In[29]:


def scrape_info():
    browser = init_browser()
    time.sleep(5)
    ### nasa mars news ###
    nasa_mars_news_url = "https://mars.nasa.gov/news/"
    nasa_mars_news_html = requests.get(nasa_mars_news_url)

    # In[30]:

    nasa_mars_news_soup = BeautifulSoup(
        nasa_mars_news_html.text, "html.parser")

    # In[31]:

    nasa_mars_news_title = nasa_mars_news_soup.find(
        "div", class_="content_title").text.replace("\n", "")

    # In[32]:

    nasa_mars_news_paragraph = nasa_mars_news_soup.find(
        "div", class_="rollover_description_inner").text.replace("\n", "")

    # In[33]:

    ### jpl mars space images ###
    jpl_mars_images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_mars_images_url)
    jpl_mars_images_html = browser.html
    time.sleep(5)

    # In[34]:

    jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")

    # In[35]:

    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(5)

    # In[36]:

    browser.click_link_by_partial_text("more info")
    time.sleep(5)

    # In[37]:

    jpl_mars_images_html = browser.html

    # In[38]:

    jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")

    # In[39]:

    image_url = jpl_mars_images_soup.find("img", class_='main_image')
    image_url = image_url.get("src")

    # In[40]:

    featured_image_url = "https://www.jpl.nasa.gov" + image_url

    # In[41]:

    ### mars weather ###
    twitter_mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    twitter_mars_weather_html = requests.get(twitter_mars_weather_url)

    # In[42]:

    twitter_mars_weather_soup = BeautifulSoup(
        twitter_mars_weather_html.text, "html.parser")
    time.sleep(5)

    # In[44]:

    mars_weather = twitter_mars_weather_soup.find(
        "p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # In[45]:

    ### mars facts ###
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts_tables = pd.read_html(mars_facts_url)

    # In[46]:

    mars_facts_tables = mars_facts_tables[0]

    # In[47]:

    mars_facts_tables.columns = ["Property", "Value"]
    mars_facts_tables.set_index("Property", inplace=True)
    mars_facts = mars_facts_tables.to_html()
    mars_facts = mars_facts.replace("\n", "")

    # In[52]:

    # mars hemispheres ### method 1
    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[53]:

    # usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[56]:

    # mars_hemisphere_name = usgs_soup.find_all("h3")

    # In[57]:

    text_1 = "Cerberus Hemisphere Enhanced"
    browser.click_link_by_partial_text(text_1)
    time.sleep(5)

    # In[58]:

    browser.click_link_by_partial_text("Open")

    # In[59]:

    usgs_html_1 = browser.html

    # In[60]:

    usgs_soup_1 = BeautifulSoup(usgs_html_1, "html.parser")

    # In[61]:

    image_url_1 = usgs_soup_1.find("img", class_='wide-image')
    image_url_1 = image_url_1.get("src")

    # In[62]:

    featured_image_url_1 = "https://astrogeology.usgs.gov" + image_url_1

    # In[63]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[64]:

    # usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[65]:

    text_2 = "Schiaparelli Hemisphere Enhanced"
    browser.click_link_by_partial_text(text_2)
    time.sleep(5)

    # In[66]:

    browser.click_link_by_partial_text("Open")

    # In[67]:

    usgs_html_2 = browser.html

    # In[68]:

    usgs_soup_2 = BeautifulSoup(usgs_html_2, "html.parser")

    # In[69]:

    image_url_2 = usgs_soup_2.find("img", class_='wide-image')
    image_url_2 = image_url_2.get("src")

    # In[70]:

    featured_image_url_2 = "https://astrogeology.usgs.gov" + image_url_2

    # In[71]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[72]:

    # usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[73]:

    text_3 = "Syrtis Major Hemisphere Enhanced"
    browser.click_link_by_partial_text(text_3)
    time.sleep(5)

    # In[74]:

    browser.click_link_by_partial_text("Open")

    # In[75]:

    usgs_html_3 = browser.html

    # In[76]:

    usgs_soup_3 = BeautifulSoup(usgs_html_3, "html.parser")

    # In[77]:

    image_url_3 = usgs_soup_3.find("img", class_='wide-image')
    image_url_3 = image_url_3.get("src")

    # In[78]:

    featured_image_url_3 = "https://astrogeology.usgs.gov" + image_url_3

    # In[79]:

    usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(usgs_url)
    usgs_html = browser.html
    time.sleep(5)

    # In[80]:

    # usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    # In[81]:

    text_4 = "Valles Marineris Hemisphere Enhanced"
    browser.click_link_by_partial_text(text_4)
    time.sleep(5)

    # In[82]:

    browser.click_link_by_partial_text("Open")

    # In[83]:

    usgs_html_4 = browser.html

    # In[84]:

    usgs_soup_4 = BeautifulSoup(usgs_html_4, "html.parser")

    # In[85]:

    image_url_4 = usgs_soup_4.find("img", class_='wide-image')
    image_url_4 = image_url_4.get("src")

    # In[86]:

    featured_image_url_4 = "https://astrogeology.usgs.gov" + image_url_4

    # In[87]:

    # mars hemispheres ### method 2
    # usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # browser.visit(usgs_url)
    # usgs_html = browser.html

    # In[88]:

    # usgs_soup = BeautifulSoup(usgs_html, "html.parser")
    # usgs_soup.body

    # In[89]:

    # mars_hemisphere_name = usgs_soup.find_all("div", class_="description")
    # mars_hemisphere_name

    # In[90]:

    # featured_image_urls = []

    # In[91]:

    # for name in mars_hemisphere_name:
    #     featured_image_url = name.find("a", class_="itemLink product-item")
    #     hemisphere = featured_image_url.get("href")
    #     hemisphere_url = "https://astrogeology.usgs.gov" + hemisphere
    #     print(hemisphere_url)

    #     browser.visit(hemisphere_url)

    #     hemisphere_url_dict = {}

    #     usgs_html = browser.html
    #     usgs_soup = BeautifulSoup(usgs_html, "html.parser")

    #     hemisphere_url = usgs_soup.find("a", text="Original")
    #     hemisphere_url = hemisphere_url.get("href")

    #     hemisphere_name = usgs_soup.find("h2", class_="title").text.replace(" Enhanced", "")

    #     hemisphere_url_dict["title"] = hemisphere_name
    #     hemisphere_url_dict["img_url"] = hemisphere_url

    #     featured_image_urls.append(hemisphere_url_dict)

    # print(featured_image_urls)

    marsData = {"News_Title": nasa_mars_news_title,
                "News_Paragraph": nasa_mars_news_paragraph,
                "JPL_Image_URL": featured_image_url,
                "Twitter_Weather": mars_weather,
                "Facts_Table": mars_facts,
                "Hemisphere_1": text_1,
                "Hemisphere_URL_1": featured_image_url_1,
                "Hemisphere_2": text_2,
                "Hemisphere_URL_2": featured_image_url_2,
                "Hemisphere_3": text_3,
                "Hemisphere_URL_3": featured_image_url_3,
                "Hemisphere_4": text_4,
                "Hemisphere_URL_4": featured_image_url_4
                }

    # In[92]:

    browser.quit()
    time.sleep(5)

    return marsData

    # In[87]:

    # convert jupyter notebook into python script called 'scrape_mars.py'
    # get_ipython().system(
    #     ' jupyter nbconvert --to script --template basic mission_to_mars.ipynb --output scrape_mars')
