from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests as rq
job_name=[]
company_name=[]
location=[]
start_date=[]
Duration=[]
stipends=[]
posted_on=[]
apply_by=[]
r=rq.get("https://internshala.com/internships/python%2Fdjango-internship")
html_doc=r.text
soup = BeautifulSoup(html_doc, 'html.parser')
allposts=soup.findAll(True,{'class':"internship_meta"})

for post in allposts:
    
    job_name.append(post.find('h4',{'title':True}).text.strip())
    
    company_name.append(post.find('a',{'class':'link_display_like_text'}).text.strip())
    location.append(post.find('a',{'class':'location_link'}).text.strip())
    
    table=post.find('table')
    
    print("*"*10)
    tds=table.findAll('td')
    
    start_date.append(tds[0].text.strip())
    Duration.append(tds[1].text.strip())
    stipends.append(tds[2].text.strip())
    posted_on.append(tds[3].text.strip())
    apply_by.append(tds[4].text.strip())
        
 

print(job_name)
print(company_name)
print(location)
print(start_date)
print(Duration)
print(stipends)

print(posted_on)

print(apply_by)


df = pd.DataFrame({'Job name':job_name,'Company name':company_name,'loaction':location,'start date':start_date,'Duration':Duration,'stipends':stipends,'posted on':posted_on,'apply by':apply_by}) 
df.to_excel('pythonintershipjobs.xlsx', index=False, encoding='utf-8')
