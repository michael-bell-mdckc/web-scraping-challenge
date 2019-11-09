#!/usr/bin/env python
# coding: utf-8

# In[6]:


# dependencies
import pandas as pd
import numpy as np
import requests
from splinter import Browser
from bs4 import BeautifulSoup


# In[7]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[7]:


### nasa mars news ###
nasa_mars_news_url = "https://mars.nasa.gov/news/"
nasa_mars_news_html = requests.get(nasa_mars_news_url)


# In[4]:


nasa_mars_news_soup = BeautifulSoup(nasa_mars_news_html.text, "html.parser")


# In[7]:


nasa_mars_news_title = nasa_mars_news_soup.find("div", class_="content_title").text
print(f"Latest News Title: {nasa_mars_news_title}")


# In[6]:


nasa_mars_news_paragraph = nasa_mars_news_soup.find("div", class_="rollover_description_inner").text
print(f"Paragraph Text: {nasa_mars_news_paragraph}")


# In[20]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[21]:


### jpl mars space images ###
jpl_mars_images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpl_mars_images_url)
jpl_mars_images_html = browser.html


# In[22]:


jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")


# In[23]:


browser.click_link_by_partial_text('FULL IMAGE')


# In[24]:


browser.click_link_by_partial_text('more info')


# In[25]:


jpl_mars_images_html = browser.html


# In[26]:


jpl_mars_images_soup = BeautifulSoup(jpl_mars_images_html, "html.parser")


# In[32]:


image_url = jpl_mars_images_soup.find("img", class_='main_image')
image_url = image_url.get("src")
print("Image URL:", image_url)


# In[33]:


featured_image_url = "https://www.jpl.nasa.gov" + image_url
print("Featured Image URL:", featured_image_url)


# In[34]:


browser.quit()


# In[46]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[47]:


### mars weather ###
twitter_mars_weather_url = "https://twitter.com/marswxreport?lang=en"
twitter_mars_weather_html = requests.get(twitter_mars_weather_url)


# In[48]:


twitter_mars_weather_soup = BeautifulSoup(twitter_mars_weather_html.text, "html.parser")


# In[53]:


mars_weather = twitter_mars_weather_soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print("Mars Weather:", mars_weather)


# In[ ]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[54]:


### mars facts ###
mars_facts_url = "https://space-facts.com/mars/"
mars_facts_html = requests.get(mars_facts_url)


# In[55]:


mars_facts_soup = BeautifulSoup(mars_facts_html.text, "html.parser")


# In[60]:


mars_facts = mars_facts_soup.find("table", class_="tablepress tablepress-id-p-mars")
print(mars_facts)


# In[31]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


### mars hemispheres ### method 1
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
usgs_html = browser.html


# In[4]:


usgs_soup = BeautifulSoup(usgs_html, "html.parser")


# In[5]:


mars_hemisphere_name = usgs_soup.find_all("h3")
mars_hemisphere_name


# In[5]:


browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')


# In[6]:


browser.click_link_by_partial_text('Open')


# In[13]:


usgs_html_1 = browser.html


# In[14]:


usgs_soup_1 = BeautifulSoup(usgs_html_1, "html.parser")


# In[15]:


image_url_1 = usgs_soup_1.find("img", class_='wide-image')
image_url_1 = image_url_1.get("src")
print("Image URL:", image_url_1)


# In[16]:


featured_image_url_1 = "https://astrogeology.usgs.gov" + image_url_1
print("Featured Image URL:", featured_image_url_1)


# In[17]:


browser.quit()


# In[18]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[19]:


usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
usgs_html = browser.html


# In[20]:


usgs_soup = BeautifulSoup(usgs_html, "html.parser")


# In[21]:


browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')


# In[22]:


browser.click_link_by_partial_text('Open')


# In[23]:


usgs_html_2 = browser.html


# In[24]:


usgs_soup_2 = BeautifulSoup(usgs_html_2, "html.parser")


# In[25]:


image_url_2 = usgs_soup_2.find("img", class_='wide-image')
image_url_2 = image_url_2.get("src")
print("Image URL:", image_url_2)


# In[26]:


featured_image_url_2 = "https://astrogeology.usgs.gov" + image_url_2
print("Featured Image URL:", featured_image_url_2)


# In[27]:


browser.quit()


# In[28]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[29]:


usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
usgs_html = browser.html


# In[30]:


usgs_soup = BeautifulSoup(usgs_html, "html.parser")


# In[31]:


browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')


# In[32]:


browser.click_link_by_partial_text('Open')


# In[33]:


usgs_html_3 = browser.html


# In[34]:


usgs_soup_3 = BeautifulSoup(usgs_html_3, "html.parser")


# In[35]:


image_url_3 = usgs_soup_3.find("img", class_='wide-image')
image_url_3 = image_url_3.get("src")
print("Image URL:", image_url_3)


# In[36]:


featured_image_url_3 = "https://astrogeology.usgs.gov" + image_url_3
print("Featured Image URL:", featured_image_url_3)


# In[37]:


browser.quit()


# In[38]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[39]:


usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
usgs_html = browser.html


# In[40]:


usgs_soup = BeautifulSoup(usgs_html, "html.parser")


# In[41]:


browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')


# In[42]:


browser.click_link_by_partial_text('Open')


# In[43]:


usgs_html_4 = browser.html


# In[44]:


usgs_soup_4 = BeautifulSoup(usgs_html_4, "html.parser")


# In[45]:


image_url_4 = usgs_soup_4.find("img", class_='wide-image')
image_url_4 = image_url_4.get("src")
print("Image URL:", image_url_4)


# In[46]:


featured_image_url_4 = "https://astrogeology.usgs.gov" + image_url_4
print("Featured Image URL:", featured_image_url_4)


# In[47]:


browser.quit()


# In[23]:


# chromedriver path
executable_path = {"executable_path": "chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[24]:


### mars hemispheres ### method 2
usgs_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(usgs_url)
usgs_html = browser.html


# In[25]:


usgs_soup = BeautifulSoup(usgs_html, "html.parser")
usgs_soup.body


# In[26]:


mars_hemisphere_name = usgs_soup.find_all("div", class_="description")
mars_hemisphere_name


# In[27]:


featured_image_urls = []


# In[29]:


for name in mars_hemisphere_name:
    featured_image_url = name.find("a", class_="itemLink product-item")
    hemisphere = featured_image_url.get("href")
    hemisphere_url = "https://astrogeology.usgs.gov" + hemisphere
    print(hemisphere_url)

    browser.visit(hemisphere_url)
    
    hemisphere_url_dict = {}
    
    usgs_html = browser.html
    usgs_soup = BeautifulSoup(usgs_html, "html.parser")
    
    hemisphere_url = usgs_soup.find("a", text="Original")
    hemisphere_url = hemisphere_url.get("href")
    
    hemisphere_name = usgs_soup.find("h2", class_="title").text.replace(" Enhanced", "")
    
    hemisphere_url_dict["title"] = hemisphere_name
    hemisphere_url_dict["img_url"] = hemisphere_url
    
    featured_image_urls.append(hemisphere_url_dict)

print(featured_image_urls)


# In[ ]:


### convert jupyter notebook into python script called 'scrape_mars.py'
get_ipython().system(' jupyter nbconvert --to script --template basic mission_to_mars.ipynb --output scrape_mars')


# In[ ]:




