from bs4 import BeautifulSoup
import requests

page_number =  [38148, 38284][1]
base_url = "https://sustainabledevelopment.un.org"
url = f"{base_url}/partnership/?p={page_number}"
source = requests.get(url).text

soup = BeautifulSoup(source, 'html.parser')
title = soup.find('div', id='headline').text
raw_description = soup.find('div', id='intro').text.replace('\n\n','\n')
description = raw_description.partition("Partner(s)")[0]
raw_partners = raw_description.partition("Partner(s)")[2]
partners = raw_partners.partition("Progress reports")[0].strip()

mini_source = requests.get(f'{base_url}/getProgressTraffic.php?p={page_number}').text
mini_soup = BeautifulSoup(mini_source, 'html.parser')
registered = mini_soup.find_all('div', class_='timeBox')[1].text.strip()[12:]


sidebar = soup.find('div', class_='homeRight')

basic_info = sidebar.find_all('div', class_='inforow')
time_frame = basic_info[0].text[12:]
website = basic_info[1].a.get('href')

contact_info = sidebar.find_all('div', class_='wrap')
contact_name, position, email = contact_info[5].text.split(',')
contact_name = contact_name.strip()
position = position.strip()
email = email.strip()

raw_targets = soup.find('div', class_='wrap', id='targets')
targets_list = raw_targets.find_all('div', style='float:left;')

targets = ' | '.join(map(lambda x: x.strong.text, targets_list))
# print(targets)

raw_deliverables = soup.find('div', class_='wrap', id='deliverables')
deliverables_list = raw_deliverables.find_all('div', class_='deliv_title')
# for deliv in deliverables_list:
#     print(deliv.text.strip())

deliverables = ' | '.join(map(lambda x: x.text.strip(), deliverables_list))
print(deliverables)