import matplotlib.pyplot as plt

# 사용데이터
""" x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]

plt.style.use("bmh")
plt.subplot(2, 1, 1)    # 1set
plt.plot(x1, y1, "o-")

plt.style.use("ggplot")
plt.subplot(2, 1, 2)
plt.subplot(1, 2, 2)
plt.subplot(3, 1, 2)
plt.plot(x2, y2, ".-")

plt.subplot(2, 1, 1)
plt.subplot(1, 2, 1)
plt.plot(x2, y2, ".-")

plt.subplot(3, 1, 1)
plt.subplot(3, 1, 2)
plt.subplot(3, 1, 3)
plt.plot(x1, y1, ".-")
plt.plot(x2, y2, ".-")

plt.subplot(2, 2, 1)
plt.subplot(2, 2, 4)

plt.title("x4-Graph")
plt.xlabel("x4-data")
plt.ylabel("y4-data")

#이미지 저장
plt.savefig("data/imggg.jpg")
plt.savefig("data/imggg.png")
 """

#다중 막대 그래프
""" x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color="aquamarine", edgecolor="black", hatch="/")
ax2.bar(x_years, y_data, color="salmon", edgecolor="black", hatch="\\")
ax3.bar(x_years, y_data, color="navajowhite", edgecolor="black", hatch="+")
ax4.bar(x_years, y_data, color="lightskyblue", edgecolor="black", hatch="*")

plt.tight_layout()

plt.show()
 """

 #seaborn
import seaborn as sns
import pandas as pd
import FinanceDataReader as fdr
""" 
tips = sns.load_dataset("tips")
print(tips)
sns.regplot(x="total_bill", y="tip", data=tips)
"""

""" tips = sns.load_dataset("tips")
print(tips)
sns.barplot(x="day", y="tip", data=tips)
sns.barplot(x="day", y="total_bill", data=tips)
sns.barplot(x="day", y="total_bill", data=tips)
sns.barplot(x="sex", y="total_bill", data=tips)
sns.barplot(x="sex", y="tip", data=tips)
sns.barplot(x="smorker", y="total_bill", data=tips)
sns.barplot(x="smoker", y="tip", data=tips)
sns.barplot(x="time", y="tatal_bill", data=tips)
plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")
plt.show()  """

#타이타닉 데이터
""" titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)
# 탑승클래스별 인원구성
sns.countplot(x="class", hue="who", data=titanic)

# 클래스별 생존자
sns.countplot(x="class", hue="alive", data=titanic)

# 성별별 생존자
sns.countplot(x="sex", hue="alive", data=titanic)

# 싱글 여행자별 인원구성
sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별
sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
 """

#주식 데이터 분석
"""df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

df0["Close"].plot()
#df0["Open"].plot()
#df0["High"].plot()
#df0["Low"].plot()

plt.grid(True)

#다우지수와 코스피지수 비교
dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# 각 지수별 종가 기준 그래프 출력
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

plt.plot(dow.index, dow.High, "r--", label="Dow")
plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

#해당 날자 기분 증가 상승율, 상대 수익율 계산
d= (dow.Close / dow.Close.loc["2010-06-01"]) * 100
k= (kospi.Close / kospi.Close.loc["2010-06-01"]) * 100
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")
 """
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs
""" headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

url = "https://finance.naver.com/item/sise_day.nhn?code=005930"

res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))

df_list = []

page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
print(df_list)

df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.plot(df["날짜"], df["종가"], "co-") """

pip install yfinance

#MS
ticker = "MSFT"

# Apple
ticker = "APPL"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

plt.plot(data["Close"], label="Close Price")
# 50일 평균
data["MA_50"] = data["Close"].rolling(window=50).mean()

# 200일 평균
data["MA_200"] = data["Close"].rolling(window=200).mean()

#국가별 인구 데이터 분석
url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries= []
populations = []

for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)
top_countries = countries:10]
top_populations =populations[:10]

plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show()
