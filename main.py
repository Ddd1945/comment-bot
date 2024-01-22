from selenium import webdriver
from helpers.actions import click_element, send_text

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://rezka.ag/?filter=watching")

click_element(driver, """//*[@id="main"]/div[4]/div[2]/div/div[1]/div[1]""")
click_element(driver, """//*[@id="comments-0"]""")
click_element(driver, "/html/body/div[4]/div/div/div/div[2]/div/div[2]/button")
send_text(driver, """//*[@id="comments-0"]""", "Самый любимый фильм")
send_text(driver, """//*[@id="comment-name-0"]""", "Ковалёв Денис Иванович")
click_element(driver, "/html/body/div[1]/div/div[4]/div/div[2]/div[1]/form/div/table[2]/tbody/tr[2]/td/div/div/button")
