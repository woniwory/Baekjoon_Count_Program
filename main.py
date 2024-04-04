from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import sys
import os
from bs4 import BeautifulSoup as bs

os.system('pause')

driver = webdriver.Chrome()

def Input():
    print()
    print("2. 조원들의 백준 ID를 띄어쓰기 구분으로 적어주세요")
    print("Ctrl+C 입력시 종료합니다")
    try:
        cnt_list = sys.stdin.readline().split()
        print()
        print()
        print("현재 입력된 ID: ")
        print()
        for id in cnt_list:
            print(id)
    except KeyboardInterrupt:
        # Ctrl+C 입력시 예외 발생
        sys.exit()  # 종료

    print()
    print("3초 후 탐색을 시작합니다")
    print()
    print()
    time.sleep(3)
    Count(cnt_list)


def Count(cnt_list):
    cnt_list = cnt_list[::-1] 
    while cnt_list:
        target = cnt_list.pop()  # 팀원들의 백준 ID를 pop. popleft는 지원하지 않음
        print()
        print()
        print("=" * 100)
        print()
        print("Baekjoon ID :", target)
        print()
        for i in range(1, 201):  # Brute_Force : 동아리 인원의 최댓값을 200명으로 설정
            try:
                baekjoon_id = driver.find_element(By.XPATH, '//*[@id="contest_scoreboard"]/tbody/tr[' + str(
                    i) + ']/th[2]/a').text  # 백준 ID의 XPath
                if baekjoon_id == str(target):  # 팀원들의 백준 ID와 XPath로 찾은 백준 ID가 일치한다면:

                    print("Baekjoon ID Detected! Index = ", i)

                    cnt = 0  # 맞은 문제 수 cnt를 0으로 초기화
                    for j in range(1, 6):  # default 값으로 5문제로 설정

                        xpath = '//*[@id="contest_scoreboard"]/tbody/tr[' + str(i) + ']/td[' + str(j) + ']'  # 문제의 xpath
                        tmp = driver.find_element(By.XPATH, xpath)
                        print(tmp.text)
                        if '--' not in tmp.text:  # text == '--' : 문제를 풀지 않거나 틀렸다는 의미 -> text != '0 / --' 가 아닐 때만 cnt값이 증가
                            cnt += 1
                    print("맞은 문제 수", cnt)
                    print("=" * 100)
                    break
            except Exception:
                print("=" * 100)
                print()
                print(str(target), ": 해당 ID를 찾을 수 없습니다 !")
                print()
                print("=" * 100)
                Input()

    print()
    print("탐색 종료")
    Input()


def Main():
    print()
    print()
    print("=" * 30 + "백준 Count Program" + "=" * 30)
    print()
    print("Version : 1.1.2")
    print()
    print("1. 페이지가 열리면, 로그인 후 해당 주차의 연습 페이지로 접속해주세요:")
    print("맞은 문제, 안 푼 문제가 표시되는 페이지입니다")
    url = 'https://www.acmicpc.net/group/practice/view/20245'
    driver.get(url)
    page = requests.get("https://www.acmicpc.net/group/practice/view/20245")
    #soup = bs(page.text, "html.parser")
    print()
    print()
    print()
    Input()


Main()



