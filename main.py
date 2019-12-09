import requests
from bs4 import BeautifulSoup

response = requests.get('https://lms.sunmoon.ac.kr/ilos/st/schedule/academic_calendar_list_form.acl?schedule_id=1')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('div', {'class': 'listbox'})  # <div class="listbox">을 찾음
data = []  # 데이터를 저장할 리스트 생성

for tr in table.find_all('tr'):  # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
            day = tr.find('th',{'class':'schedule'}).text  # <th> 태그의 text 값을 가져옴
            schedule = tr.find('td').text  # <td> 태그 리스트의 text를 가져옴
            data.append([schedule, day])  # data 리스트에 날짜, 일정을 추가

data  # data 표시. 주피터 노트북에서는 print를 사용하지 않아도 변수의 값이 표시됨

 # csv로 저장
with open('sunmoon_schedule_2020.csv', 'w') as file:    # sunmoon_schedule_2020.csv 파일을 쓰기 모드로 열기
    file.write('Subject,Start Date,\n') # 컬럼 이름 추가
    for i in data: # data를 반복하면서
        file.write('{0},{1}\n'.format(i[0], i[1]))  # 지점,온도,습도를 줄 단위로 저장
