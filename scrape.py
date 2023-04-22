from selenium import webdriver
from selenium.webdriver.common.by import By
import time,webbrowser

def scrapeAndNewtab():
	'''搜尋特定用戶名時間軸最頂三則推文，並各自用瀏覽器新分頁開啟'''
	userName=input("請輸入用戶名\n")
	driver=webdriver.Firefox()
	driver.get(f"https://twitter.com/{userName}")
	
	
	'''處理可能出現的失效頁面：'''
	try:
		driver.find_element(By.XPATH,"//a[@id='button_retry']")
		driver.find_element(By.XPATH,"//a[@id='button_retry']").click()
		time.sleep(3)
	except:pass

	time.sleep(3)
	driver.switch_to.window(driver.window_handles[-1])
	
	'''需要規避額外彈出視窗，可使用下段code'''
	'''main_page = driver.current_window_handle
	if driver.current_window_handle != main_page:
		driver.switch_to.window(main_page)'''

	elementDate=driver.find_elements(By.XPATH,"//time[@datetime]")
	elementUrl=driver.find_elements(By.XPATH,"//a[contains(@href,'status')and @role='link'and contains(@class,'r-qvutc0')]")
	with open('twitter.log','a+')as file:
		for i in range(3):
			content=elementDate[i].get_attribute('datetime').split('T')[0]+'|'+elementUrl[i].get_attribute('href')
			print(content)
			file.write(content)
			webbrowser.open_new_tab(elementUrl[i].get_attribute("href"))

if __name__=='__main__':
	scrapeAndNewtab()
