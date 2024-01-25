import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.unicesumar.edu.br/")
title = driver.title

driver.implicitly_wait(10)

submit_button = driver.find_element(by=By.LINK_TEXT, value="JÁ SOU ALUNO")
submit_button.click()


#preencher username
campo_username = driver.find_element(By.ID, value="username")
user = "" #inserir login entre os parenteses
for i in user:
    campo_username.send_keys(i)
    time.sleep(0.2)

#preencher passowrd
campo_password = driver.find_element(By.ID, value="password")
password = "" #inserir senha entre os parenteses

for j in password:
    campo_password.send_keys(j)
    time.sleep(0.2)

submit_button_login = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button_login.click()

submit_button_a = driver.find_element(by=By.LINK_TEXT, value="Meu Curso")
submit_button_a.click()

driver.quit()

