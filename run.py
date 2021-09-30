from GoogleNews import GoogleNews
from requests_html import AsyncHTMLSession
import requests as req
import sqlite3
import asyncio

googlenews = GoogleNews()
show=True
keyword=""

## Take the keyword as  a user input
while(show):
    print("Enter your keyword to search in google news")
    keyword=input("=> ")
    print("Your keyword is --> "+keyword)
    print("Do you want to Continue ?")
    print("Enter y to continue or n to enter the keyword again ?")
    user_key =input("=> ")
    print(user_key)
    if(user_key.lower() == "y"):
        show=False

googlenews.get_news(keyword)
news=googlenews.results()

conn = sqlite3.connect('news.db')
c=conn.cursor()

## If you are running the script for the first time uncomment the section below
## to create a news table in the sqlite database.
## otherwise keeep as it is


# c.execute("""create table news (
#     keyword text,
#     url text,
#     title text,
#     content text
#     )
# """)

## create an Asynchornous HTML Sesssion and use event loop for getting the
## response asynchoronously

session = AsyncHTMLSession()
async def GetHTML(url):
    return await session.get(url)
loop= asyncio.get_event_loop()

## work with each individual information from the news (list of objects with title, link to the page)
for info in news:
    ## get the news details
    url="http://"+info['link']
    url=req.get(url).url
    r=loop.run_until_complete(GetHTML(url))
    paragraphs = r.html.find("p")
    custom_paragraphs=""
    for p in paragraphs:
        ## We will use #### to indicate the seperation of each parargraphs from the content
        custom_paragraphs+=p.text+"####"
    print(info['title'])
    print(info['link'])
    ## insert individual news into sqlite database
    sql="INSERT INTO news (keyword, url, title,content) VALUES(?, ?, ?, ?)"
    c.execute(sql,(keyword,info['link'],info['title'],custom_paragraphs))
    conn.commit()
