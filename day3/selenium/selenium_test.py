from selenium import webdriver #브라우저를 실행하고 조작하는 객체
from selenium.webdriver.common.by import By # 요소를 찾을 때 사용하는 선택 방식 지정도구(태크나 등등 그런거)

# 1) 브라우저 실행
driver = webdriver.Chrome()

# 2) 웹페이지 접속
driver.get("https://quotes.toscrape.com/")

# 3) 요소 하나 찾기
quote = driver.find_element(By.CLASS_NAME, 'text') #find_element 가 요소 하나 가져오는 메소드 By.CLASS_NAME, 'text'는 클래스 이름인 text를 가져오겠다
print(quote.text)


# 3-1) 요소 여러개 찾기
quotes = driver.find_elements(By.CLASS_NAME, 'text') #find_elements 가 요소 여러개 가져오는 메소드 
for quote in quotes:
    print(quote.text)

driver.quit() #브라우저 종료
