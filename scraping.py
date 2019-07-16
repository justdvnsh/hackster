from selenium import webdriver
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
import json

def scrape_kaggle():
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
        
    with open('competitions_kaggle.json', 'w') as fl:
        json.dump(data, fl)

    return data


def scrape_analytics_vidya():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    driver.get("https://datahack.analyticsvidhya.com/contest/all/")

    active_competitions = driver.find_elements_by_class_name('contest__details__link')
    competitions = [name.text for name in active_competitions]

    actual_competitions = [competitions[i] for i in range(len(competitions) + 1) if i % 2 != 0] 

    driver.close()

    data = []

    for competition in actual_competitions:
        comp = competition.split('\n')
        data.append({
            'competition_name': comp[1],
            'competition_time': comp[2],
            'competition_prizes': comp[3],
            'competition_price': comp[-1]
        })

    with open('competitions_analytics_vidya.json', 'w') as fl:
            json.dump(data, fl)

    return data
