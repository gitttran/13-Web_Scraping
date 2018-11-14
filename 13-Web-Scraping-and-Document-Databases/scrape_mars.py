from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    # Initialize browser
    browser = init_browser()

    # Visit the Costa Rica climate site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # Scrape articles page into soup
    html = browser.html
    soup = bs(html, "html.parser")

    articles = soup.find_all('li', class_='slide')
    title = articles[0].find('div',class_="content_title").find('a').text
    teaser = articles[0].find('div',class_="article_teaser_body").text

    image_page='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_page)
    # Scrape image page into soup
    html = browser.html
    soup = bs(html, 'html.parser')

    img = soup.find('section',class_='centered_text clearfix main_feature primary_media_feature single').find('article')['style']
    img_url=img.split()[1]
    img_url = img_url[5:57]
    img_url
    featured_image_url = 'https://www.jpl.nasa.gov' + img_url

    # Scrape twitter page into soup
    weather_page='https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_page)
    html = browser.html
    soup = bs(html, 'html.parser')

    timeline=soup.find('div', class_='ProfileTimeline ')
    stream= timeline.find('div',class_='stream')
    olist=stream.find('ol',class_='stream-items js-navigable-stream')
    tweet=olist.find_all('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather= tweet[0].text

    # Scrape facts page into soup
    facts_page='https://space-facts.com/mars/'
    browser.visit(facts_page)
    html = browser.html
    soup = bs(html, 'html.parser')
    table= soup.find('tbody')

    tables = pd.read_html(facts_page)


    # Scrape hemisphere page into soup
    hemi_page='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_page)

    html = browser.html
    soup = bs(html, 'html.parser')

    valles_img_url= 'https://www.jpl.nasa.gov' + img_url
    cerberus_img_url= 'https://www.jpl.nasa.gov' + img_url
    schiaparelli_img_url= 'https://www.jpl.nasa.gov' + img_url
    syrtis_major_img_url= 'https://www.jpl.nasa.gov' + img_url

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]


    # Return results
    return weather
