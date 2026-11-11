from selenium import webdriver #브라우저를 실행하고 조작하는 객체
from selenium.webdriver.common.by import By # 요소를 찾을 때 사용하는 선택 방식 지정도구(태크나 등등 그런거)

# 1) 브라우저 실행
driver = webdriver.Chrome()

# 2) 웹페이지 접속
driver.get("https://quotes.toscrape.com/")

# 2) 다음 페이지 이동 + 반복 수집

MAX_PAGES = 3 

current_page = 1 # 현재 페이지 번호를 추적하기 위한 변수

results = []

while current_page <= MAX_PAGES:
    print(f"===== {current_page}페이지 수집 중 =====")

    quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote') # 새 페이지에서 다시 quote 블록 수집

    for block in quote_blocks:
        quote_text = block.find_element(By.CLASS_NAME, 'text').text
        author = block.find_element(By.CLASS_NAME, 'author').text
        tag_elements = block.find_elements(By.CLASS_NAME, 'tag')
        tags = [t.text for t in tag_elements]
    
        results.append({
            'page' : 1,
            'quote' : quote_text,
            'author' : author,
            'tags' : tags
        })
    # Next 버튼 찾기
    # CSS_SELECTOR : CSS문법을 이용해서 HTML요소를 찾는 방법
    # Selenium에서 가장 많이 쓰이는 방식 중 하나    
    next_buttons = driver.find_elements(By.CSS_SELECTOR, 'li.next a') 

    if not next_buttons: # next 버튼이 없을때 멈추게하는거
        print('다음 페이지가 없어 종료합니다.')
        break

    # 다음 페이지로 이동
    next_buttons[0].click()

    #페이지 번호 1증가
    current_page += 1 

print("최종 수집 개수 :", len(results))

driver.quit()