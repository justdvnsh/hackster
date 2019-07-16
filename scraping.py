from selenium import webdriver
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
import json

def scrape():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    driver.get("https://kaggle.com/competitions")

    active_competition = driver.find_elements_by_class_name('competition-info')
    competitions = [name.text for name in active_competition]

    print(competitions)
    driver.close()

    data = []

    for competition in competitions:
        comp = competition.split('\n')
        if ('Featured' in comp) or ('Research' in comp):
            data.append({
                "competition_name": comp[0],
                "competition_description": comp[1],
                "competition_exclusiveness": comp[2],
                "competition_time": comp[-4],
                "competition_labels": comp[-3],
                "competition_prize": comp[-2],
                "competition_teams": comp[-1]
            })
        
    with open('competitions.json', 'w') as fl:
        json.dump(data, fl)

    return data




