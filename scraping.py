from selenium import webdriver
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("https://kaggle.com/competitions")

competitions = driver.find_elements_by_xpath('/html/body/main/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/div')
print([competition.text.split('\n') for competition in competitions])