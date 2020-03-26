import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
# headers 에 User-Agent 는 '내'컴퓨터의 정보 보다는, chrome 의 버전 같은 느낌인거 같음.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody >tr')
# print(musics)

i = 1
print('== 지니차트 2020 . 03 . 09 TOP 50 ==\n')
# movies (tr들) 의 반복문을 돌리기
for music in musics:
    title = music.select_one('td.info>a').text
    real_title = title.strip()
    artist = music.select_one('td.info a.artist')
    j = str(i)
    th = j+'위'
    if title is not None:
        print(th, real_title,'\n', '   ',artist.text, '\n') #td_point.text)
    i = i + 1
