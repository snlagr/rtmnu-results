from selenium import webdriver
from selenium.webdriver.support.ui import Select
import urllib, os
from PIL import Image

# make folder to save pics
os.makedirs('marksheets', exist_ok=True)

# open browser and load site
browser = webdriver.Firefox()
browser.get("https://rtmnuresults.org/")

# select faculty and exam
faculty = Select(browser.find_element_by_id('ddlselectfaculty'))
faculty.select_by_value("1")
exams = Select(browser.find_element_by_id('ddlselectexam'))
exams.select_by_value("391")

for rollno in range(316950, 317991):
	# enter roll no
	roll_field = browser.find_element_by_id("txtrollno")
	roll_field.clear()
	roll_field.send_keys(str(rollno))

	# submit info / load marksheet page
	sub_button = browser.find_element_by_id("imgbtnviewmarksheet")
	sub_button.click()

	# save screenshot
	browser.save_screenshot("marksheets/" + str(rollno) + ".png")
	browser.back()