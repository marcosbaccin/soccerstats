# Importação das bibliotecas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

# Importando e inicializando o driver do Chrome
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Estrutura padrão de link para acessar as estatísticas de gols das ligas no Soccerstats
standard_link = "https://www.soccerstats.com/trends.asp?league="

# Ligas que possuem estatísticas de 1º tempo
leagues = [
    "southafrica",
    "albania",
    "germany",
    "germany2",
    "germany3",
    "germany4",
    "germany6",
    "germany8",
    "germany23",
    "saudiarabia",
    "argentina",
    "argentina2",
    "argentina3",
    "argentina4",  # Page Not Found
    "argentina5",
    "armenia",
    "australia",
    "australia10",
    "australia11",
    "australia4",
    "australia6",
    "australia8",
    "australia3",
    "australia5",
    "austria",
    "austria2",
    "austria7",
    "belarus",
    "belgium",
    "belgium2",
    "bosnia",
    "brazil",
    "brazil2",
    "brazil3",
    "bulgaria",
    "canada",
    "kazakhstan",
    "southkorea",
    "southkorea2",
    "costarica",
    "costarica2",
    "croatia",
    "croatia2",
    "denmark",
    "denmark2",
    "uae",
    "scotland",
    "scotland2",
    "scotland3",
    "scotland4",
    "slovakia",
    "slovenia",
    "spain",
    "spain2",
    "spain3",
    "spain4",
    "usa",
    "usa2",
    "usa3",
    "finland",
    "finland2",
    "france",
    "france2",
    "france3",
    "georgia",
    "greece",
    "hongkong",
    "hungary",
    "faroeislands",
    "england",
    "england2",
    "england3",
    "england4",
    "england5",
    "england15",
    "ireland",
    "ireland2",
    "northernireland",
    "iceland",
    "iceland2",
    "israel",
    "israel2",
    "italy",
    "italy2",
    "italy3",
    "italy4",
    "japan",
    "japan2",
    "japan3",
    "jordan",
    "lithuania",
    "malaysia",
    "malta",
    "mexico",
    "mexico2",
    "norway",
    "norway2",
    "norway3",
    "norway4",
    "netherlands",
    "netherlands2",
    "netherlands3",
    "paraguay",
    "paraguay2",
    "peru",
    "peru2",
    "poland",
    "poland2",
    "portugal",
    "portugal2",
    "czechrepublic",
    "czechrepublic2",
    "russia",
    "russia2",
    "serbia",
    "singapore",
    "sweden",
    "sweden2",
    "sweden3",
    "sweden4",
    "sweden11",
    "switzerland",
    "switzerland2",
    "thailand",
    "turkey",
    "ukraine",
    "vietnam"
]

# Input do usuario para a escolha da liga
print("Leagues:")

for league in leagues:
    print(f"({leagues.index(league)}) {league}")

league = int(input("Choose a league: "))

# Montando o link para acessar a página da liga
link = standard_link + leagues[league]
print(link)

# Acessando a página da liga
driver.get(link)
time.sleep(5)

# Fechando o anúncio caso apareça
try:
    driver.find_element(By.CSS_SELECTOR, "#qc-cmp2-ui > div.qc-cmp2-footer.qc-cmp2-footer-overlay.qc-cmp2-footer-scrolled > div > button.css-47sehv > span").click()
except:
    print("Sem anúncio")

Teams_home_ht = []
One_goal_ht_home = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de gols no 1º tempo)
teams_home_ht = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr")
if len(teams_home_ht) == 0:
    teams_home_ht = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr")

# Pegando as informações
index_gh = 1
for team_h_ht in teams_home_ht:
    t = team_h_ht.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        g = team_h_ht.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[2]/table/tbody/tr[{index_gh}]/td[4]/span").get_attribute("innerHTML")
    except:
        g = team_h_ht.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[2]/table/tbody/tr[{index_gh}]/td[4]/span").get_attribute("innerHTML")

    index_gh += 1
    g = int(g.replace("%", ""))
    Teams_home_ht.append(t)
    One_goal_ht_home.append(g)

# print(Teams_home)
# print(len(Teams_home))
# print(One_goal_ht_home)
# print(len(One_goal_ht_home))

Teams_away_ht = []
One_goal_ht_away = []

teams_away_ht = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr")
if len(teams_away_ht) == 0:
    teams_away_ht = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tbody/tr")

index_gw = 1
for team_a_ht in teams_away_ht:
    t = team_a_ht.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        g = team_a_ht.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[2]/div[3]/table/tbody/tr[{index_gw}]/td[4]/span").get_attribute("innerHTML")
    except:
        g = team_a_ht.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[2]/div[3]/table/tbody/tr[{index_gw}]/td[4]/span").get_attribute("innerHTML")

    index_gw += 1
    g = int(g.replace("%", ""))
    Teams_away_ht.append(t)
    One_goal_ht_away.append(g)

# print(Teams_away)
# print(len(Teams_away))
# print(One_goal_ht_away)
# print(len(One_goal_ht_away))

Teams_home = []
More_2_goals_home = []
Both_teams_to_score_home = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de jogos com +2.5 gols e BTTS)
teams_home = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr")
if len(teams_home) == 0:
    teams_home = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr")

# Pegando as informações
index_gh = 1
for team_h in teams_home:
    t = team_h.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        m2g = team_h.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[6]/font/span").get_attribute("innerHTML")
    except:
        m2g = team_h.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[6]/font/span").get_attribute("innerHTML")

    try:
        btts = team_h.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[10]/span").get_attribute("innerHTML")
    except:
        btts = team_h.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[3]/table/tbody/tr[{index_gh}]/td[10]/span").get_attribute("innerHTML")

    index_gh += 1
    m2g = int(m2g.replace("%", ""))
    btts = int(btts.replace("%", ""))
    Teams_home.append(t)
    More_2_goals_home.append(m2g)
    Both_teams_to_score_home.append(btts)

Teams_away = []
More_2_goals_away = []
Both_teams_to_score_away = []

# Selecionando a tabela onde estão as informações necessárias (nome dos times e % de jogos com +2.5 gols e BTTS)
teams_away = driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr")
if len(teams_away) == 0:
    teams_away = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr")

# Pegando as informações
index_ga = 1
for team_a in teams_away:
    t = team_a.find_element(By.TAG_NAME, "a").get_attribute("innerHTML")

    try:
        m2g = team_a.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[6]/font/span").get_attribute("innerHTML")
    except:
        m2g = team_a.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[6]/font/span").get_attribute("innerHTML")

    try:
        btts = team_a.find_element(By.XPATH, f"/html/body/div[5]/div[2]/div[2]/div[4]/div[3]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[10]/span").get_attribute("innerHTML")
    except:
        btts = team_a.find_element(By.XPATH, f"/html/body/div[4]/div/div[2]/div[4]/div[2]/div[1]/div[4]/table/tbody/tr[{index_ga}]/td[10]/span").get_attribute("innerHTML")

    index_ga += 1
    m2g = int(m2g.replace("%", ""))
    btts = int(btts.replace("%", ""))
    Teams_away.append(t)
    More_2_goals_away.append(m2g)
    Both_teams_to_score_away.append(btts)

# Salvando as informações em um dataframe
df_h = pd.DataFrame({"Team Home": Teams_home_ht, "One Goal HT home": One_goal_ht_home}, index=None)
df_h.sort_values(by="Team Home", inplace=True, ignore_index=True)
# print(df_h)

# Organizando as informações
df_a = pd.DataFrame({"Team Away": Teams_away_ht, "One Goal HT away": One_goal_ht_away}, index=None)
df_a.sort_values(by="Team Away", inplace=True, ignore_index=True)
# print(df_a)

df_h2 = pd.DataFrame({"Team Home": Teams_home, "More 2 Goals home": More_2_goals_home, "Btts home": Both_teams_to_score_home}, index=None)
df_h2.sort_values(by="Team Home", inplace=True, ignore_index=True)

df_a2 = pd.DataFrame({"Team Away": Teams_away, "More 2 Goals away": More_2_goals_away, "Btts away": Both_teams_to_score_away}, index=None)
df_a2.sort_values(by="Team Away", inplace=True, ignore_index=True)

df_h["One Goal HT away"] = df_a["One Goal HT away"]
df_h["More 2 Goals home"] = df_h2["More 2 Goals home"]
df_h["Btts home"] = df_h2["Btts home"]
df_h["More 2 Goals away"] = df_a2["More 2 Goals away"]
df_h["Btts away"] = df_a2["Btts away"]
print(df_h)

# Salvando os dados coletados em uma planilha
df_h.to_excel(f"Goals_stats_{leagues[league]}.xlsx", index=False)
