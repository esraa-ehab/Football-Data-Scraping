import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = '/Users/user/Documents/Selenium/chromedriver-mac-x64/chromedriver'

service = Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.get(website)

all_matches_btn = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_btn.click()

date = []
home_team = []
score = []
away_team = []

matches = driver.find_elements(By.TAG_NAME, "tr")

for match in matches:
    try:
        date.append(match.find_element(By.XPATH,"./td[1]").text)
        home_team.append(match.find_element(By.XPATH,"./td[3]").text)
        score.append(match.find_element(By.XPATH,"./td[4]").text)
        away_team.append(match.find_element(By.XPATH,"./td[5]").text)
    except:
        continue

data_dict = {
    'date' : date,
    'home_team': home_team,
    'score' : score,
    'away_team' : away_team
}

df = pd.DataFrame(data_dict)
df.to_csv("football_data.csv", index=False)
print(df)

input("Press Enter to close")