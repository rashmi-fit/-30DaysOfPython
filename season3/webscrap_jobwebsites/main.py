from bs4 import BeautifulSoup
import requests

html_text = requests.get('')
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li',class_ = 'classname')
# print(jobs)
# company_name = jobs.find('h3', class_ = 'classname').text.replace('','')
# skills = jobs.find('span', class_ = 'srp-skills')
# published_date = jobs.find("xpath")
# print(published_date)
# print(f'''
#       company name: {company_name}
#       skills: {skills.text.replace('Skills: ','')}

#       ''')

for job in jobs:
    company_name = job.find('h3', class_='classname').text.replace('', '')
    skills = job.find('span', class_='srp-skills')
    published_date = job.find("xpath")
    print(f'''
          company name: {company_name}
          skills: {skills.text.replace('Skills: ', '')}
          published date: {published_date}
          ''')
