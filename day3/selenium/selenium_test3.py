from selenium import webdriver #브라우저를 실행하고 조작하는 객체
from selenium.webdriver.common.by import By # 요소를 찾을 때 사용하는 선택 방식 지정도구(태크나 등등 그런거)

# 1) 브라우저 실행
driver = webdriver.Chrome()

# 2) 웹페이지 접속
driver.get("https://quotes.toscrape.com/")

# 1) 한 페이지에서 여러 명언 수집하기
results = [] #수집한 데이터를 저장할 리스트

quote_blocks = driver.find_elements(By.CLASS_NAME, 'quote')

for block in quote_blocks: # 각 블록 안에서 필요한 데이터 찾기
    quote_text = block.find_element(By.CLASS_NAME, 'text').text
    author = block.find_element(By.CLASS_NAME, 'author').text

    tag_elements = block.find_elements(By.CLASS_NAME, 'tag')

    tags = [t.text for t in tag_elements] # 리스트 컴프리헨션을 사용하여 각 tag 요소의 텍스트만 추출
    # - 컴프리헨션 : 박복문을 이용해 새로운 컬렉션을 만드는 축약 문법
    # - [표현식 for 변수 in 반복가능객체]
    # tags= []
    # for t in tag_elements:
    #   tags.append(t.text)

    results.append({
        'page' : 1,
        'quote' : quote_text,
        'author' : author,
        'tags' : tags
        })
    print(f"{author} : {quote_text} / tag: {tags}")

print("현재까지 수집된 개수 :", len(results))

driver.quit()