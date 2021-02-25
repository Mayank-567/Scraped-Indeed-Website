import requests
from bs4 import BeautifulSoup

counter=1

# Link of indeed website

url="https://in.indeed.com/jobs?q=python%20developer&l=Andheri%2C%20Mumbai%2C%20Maharashtra"

html_text=requests.get(url, headers={'User-Agent':'Mozilla/5.0'})

Soup=BeautifulSoup(html_text.content,"html.parser")

divs=Soup.find_all("div", class_="jobsearch-SerpJobCard")
for items in divs:
    if counter>5:
        break
    job_title=items.find("a").text.strip()
    company_name=items.find("span",class_="company").text.strip()

    summary = items.find('div', {'class' : 'summary'}).text.strip().replace('\n', '')
    
    try:
        salary = items.find('span', class_ = 'salaryText').text.strip()
    except:
        salary = 'Not Mentioned'
    print(f'{counter} . Company Name: {company_name}')
    print(f'Job Role: {job_title}')
    print(f'Salary: {salary}')
    print(f'Summary: {summary}')

    print("")
    counter+=1
# print(len(divs))