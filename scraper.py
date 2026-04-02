import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
chromedriver_path = '/Users/user/Documents/Selenium/chromedriver-mac-x64/chromedriver'
countries = ['Spain', 'England']

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.get(website)

wait = WebDriverWait(driver, 10)  

all_matches_btn = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_btn.click()

rows = []

for country in countries:
    dropdown = Select(driver.find_element(By.ID, "country"))
    dropdown.select_by_visible_text(country)

    wait.until(EC.presence_of_element_located((By.XPATH, "//table//tr[td]")))

    wait.until(lambda d: len(d.find_elements(By.XPATH, "//table//tr[td]")) > 0)

    matches = driver.find_elements(By.XPATH, "//table//tr[td]")

    for match in matches:
        cells = match.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 5:
            rows.append([
                cells[0].text,  
                cells[2].text,  
                cells[3].text,  
                cells[4].text  
            ])

df = pd.DataFrame(rows, columns=['date', 'home_team', 'score', 'away_team'])
df.to_csv("football_data.csv", index=False)
print(df)

input("Press Enter to close")
driver.quit()