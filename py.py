from selenium import webdriver
# 옵션추가
from selenium.webdriver.chrome.options import Options
# 요소 선택
from selenium.webdriver.common.by import By
import time
# 엔터키 작동
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # 대기시간
from selenium.webdriver.support import expected_conditions as EC # 조건이 충족될 때까지 코드 실행을 일시 중지
import pandas as pd
import tk2
def main():
  options = Options()
  # # 로그인 자동
  # options.add_argument('user-data-dir=home\\joon\\user_data\\joon')
  # # 구글 로그인 (자동화 감지 대처)
  # options.add_argument('disable-blink-features=AutomationControlled')

  # 창 최대 크기
  # options.add_argument('--start-maximized')
  # 창 안꺼지게
  options.add_experimental_option('detach',True)
  # 콘솔 로그 없애기
  # options.add_experimental_option('excludeSwitches', ['enable-logging'])

  driver = webdriver.Chrome(options=options)
  driver.maximize_window() # 창크기 최대
  url = 'https://www.upbit.com/exchange?code=CRIX.UPBIT.KRW-BTC'
  driver.get(url)

  pre_rank = pd.DataFrame()
  wait = WebDriverWait(driver, 10)  # 최대 10초 대기
  while 1:
    # 요소가 로드될 때까지 대기
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > table > thead > tr > th:nth-child(3) > a')))
    # print(f'요소 활성화 확인')
    driver.find_element(By.CSS_SELECTOR,'#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > table > thead > tr > th:nth-child(3) > a').click()
    # print(f'등락율 순으로 변경')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > div > div > div:nth-child(1) > table")))
    # print(f'요소 활성화 확인')
    table = driver.find_element(By.CSS_SELECTOR, "#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > div > div > div:nth-child(1) > table")
    tickers = table.find_elements(By.CLASS_NAME,'tit')
    # print(f'요소 찾음:{tickers}')

    rank = []
    for i in tickers:
      rank.append({'종목':i.find_element(By.TAG_NAME,'strong').text})

    rank = pd.DataFrame(rank)
    # print(f'이전데이터:{pre_rank}')
    # print(f'현재 데이터:{rank}')

    if (not pre_rank.empty) and (not pre_rank.equals(rank)):
      # print(f'이전 데이터와 비교')
      diff = rank.where(pre_rank!= rank)
      # 변경된 값 출력
      result = diff.stack()
      # print(f'이전 데이터가 존재하므로 현재와 비교하여 바뀐게 있는지 체크')
      dash = '-'*50
      print(f'바뀐 데이터\n{dash}\n{result}')
      tk2.show_message(result)

    elif pre_rank.empty:
      pre_rank = rank
      # print(f'이전 랭크 데이터가 없으므로 데이터를 넣어줌:{pre_rank}')

    driver.refresh() # 새로고침
    # print('새로고침')
    time.sleep(5)

    pre_rank = pd.DataFrame(rank)


if __name__ =='__main__':
  try:
    main()
  except:
    main()
