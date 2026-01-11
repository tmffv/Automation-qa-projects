from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

# sys.executable - returns the path to the Python interpreter that is running the script
# os.path.dirname(path) - This function takes a file path (a string)
# as input and returns the directory part of that path, removing the file name
# /Users/tmffv/Desktop/Python/Automation/web_automation/venv/bin - result
application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y") #convert data to string format (MMDDYYYY)

website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/tmffv/Desktop/Python/Automation/web_automation/chromedriver-mac-arm64/chromedriver"

# headless - mode
options = Options()
options.headless = True
options.add_argument("--headless")
options.add_argument("--disable-gpu")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Here we'll get the first element
# driver.find_element(by="xpath", value='//div[@class="story__copy-container"]')

containers = driver.find_elements(by="xpath", value='//div[@class="story__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./a/p').text
    subtitle = container.find_element(by="xpath", value='./a/h3 ').text
    link = container.find_element(by="xpath", value='./a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}
df_headlines = pd.DataFrame(data=my_dict)
# df_headlines.to_csv('headline.csv')
# df_headlines.to_excel('headline.xlsx')
# df_headlines.to_json('headline.json')

file_name = f'headline-{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)


driver.quit()
