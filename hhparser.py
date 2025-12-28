import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = "https://nn.hh.ru/vacancies/programmist"

driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'div.vacancy-card--n77Dj8TY8VIUF0yM')

parsed_data = []

for vacancy in vacancies:
   try:
     title = vacancy.find_element(By.CSS_SELECTOR, 'span.serp-item__title-text').text
     company = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-serp__vacancy-employer-text').text
     salary = vacancy.find_element(By.CSS_SELECTOR, 'span.magritte-text___pbpft_4-3-0').text
     if salary.text.strip() != '':
         salary_text = salary.text
     else:
         salary_text = 'Зарплата не указана'
     link = vacancy.find_element(By.CSS_SELECTOR, 'a.magritte-link___b4rEM_6-1-2').get_attribute('href')
   except Exception as e:
       print(f"Произошла ошибка при парсинге: {e}")
       continue

   parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)









