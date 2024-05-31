from selenium import webdriver
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs
from bs4 import BeautifulSoup

'''
# 순위
# 가수명
# 앨범명
# 노래 제목

멜론일간차트순위_2024년_5월_31일_11시기준.txt
'''

d = datetime.today()

file_path = f'C:/MyWorkspace/upload/멜론일간차트순위__{d.year}년_{d.month}월_{d.day}일_{d.hour}시기준.txt'


# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해 주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해주는 코드
driver = webdriver.Chrome(options=option, service=service)

driver.get('https://www.melon.com/')

t.sleep(2)

driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]').click()

t.sleep(2)

with codecs.open(file_path, mode='w', encoding='utf-8') as f:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    
    
    for cnt in [50, 100]:
        # 곡 정보가 있는 tr 리스트를 지목해서 얻어오자 (lst50, lst100으로 나누어져 있음)
        song_tr_list = soup.select(f'.lst{cnt}')

        for song_tr in song_tr_list:
            # 순위 찾기
            rank = song_tr.select_one('div.wrap.t_center').text.strip()
            print(rank)

            # 가수 이름 찾기
            artist_name = song_tr.select_one('div.wrap div.ellipsis.rank02 > a').text.strip()
            print(artist_name)

            # 앨범명 찾기
            album_name = song_tr.select_one('div.wrap div.ellipsis.rank03 > a').text.strip()

            # 노래명 찾기
            song_name = artist_name = song_tr.select_one('div.wrap div.ellipsis.rank01 > span > a').text.strip()

            f.write(f'순위: {rank}위\n')
            f.write(f'곡: {song_name}\n')
            f.write(f'가수: {artist_name}\n')
            f.write(f'앨범: {album_name}\n')
            f.write('-' * 40 + '\n')
    
    

    '''
    song_list = soup.select('tr.lst50')

    # first_song_info = song_list[0].find_all('a')
    # song_title = first_song_info[2].text
    # musician = first_song_info[3].text
    # album_title = first_song_info[5].text
    # print(f'곡: {song_title}')
    # print(f'가수: {musician}')
    # print(f'앨범: {album_title}')


    rank = 1

    for song in song_list:
        song_info = song.find_all('a')
        # print(len(song_info), end=' ')
        
        song_title = song_info[2].text

        if len(song_info) == 6: # 가수가 1명인 경우
            musician = song_info[3].text
            album_title = song_info[5].text
        elif len(song_info) == 10: # 가수가 2명인 경우
            musician = song_info[3].text + ', ' + song_info[4].text
            album_title = song_info[7].text
        
        

        f.write(f'순위: {rank}위\n')
        f.write(f'곡: {song_title}\n')
        f.write(f'가수: {musician}\n')
        f.write(f'앨범: {album_title}\n')
        f.write('-' * 40 + '\n')
        rank += 1

    song_list = soup.select('tr.lst100')

    for song in song_list:
        song_info = song.find_all('a')
        # print(len(song_info), end=' ')
        
        song_title = song_info[2].text
        
        if len(song_info) == 6: # 가수가 1명인 경우
            musician = song_info[3].text
            album_title = song_info[5].text
        elif len(song_info) == 10: # 가수가 2명인 경우
            musician = song_info[3].text + ', ' + song_info[4].text
            album_title = song_info[9].text

        f.write(f'순위: {rank}위\n')
        f.write(f'곡: {song_title}\n')
        f.write(f'가수: {musician}\n')
        f.write(f'앨범: {album_title}\n')
        f.write('-' * 40 + '\n')
        rank += 1

        '''

