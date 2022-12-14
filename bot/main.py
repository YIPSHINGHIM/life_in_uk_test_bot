
import time

import undetected_chromedriver as Driver
from selenium.webdriver import ActionChains, Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_driver_path = "/usr/local/bin/chromedriver"

opts = ChromeOptions()
opts.add_argument("--window-size=600,300")

driver = Driver.Chrome(executable_path=chrome_driver_path
# options=opts
)

driver.get("https://lifeintheuktestweb.co.uk/test-1-2/")
# driver.set_window_size(1689, 1056)

wait = WebDriverWait(driver, 10)

question_dict = {}

# * print question
def find_question():
    print('this is find question function ')
    question = driver.find_element(By.CLASS_NAME, 'wpProQuiz_question_text')
    print()
    
    return(question.text)

# * find the check button
def click_the_check_button(x):
    print("go into the click_the_check_button function ")
    driver.execute_script("window.scrollTo(1, 250);")

    print("click_the_check_button function")


    wait.until(
        EC.element_to_be_clickable((By.NAME ,'check'))
    )
    

    time.sleep(5)

   
    if x != 0:
        driver.execute_script("window.scrollTo(0, 0);") 
        review_button =driver.find_element(By.NAME ,'review')
        review_button.click()
        time.sleep(2)
        review_button.click()
        driver.execute_script("window.scrollTo(1, 250);")
    

    check_button = driver.find_element(By.NAME ,'check')



    
    time.sleep(2)

    # *click the check button
    print(check_button.click())
    print("clicked check button")



def find_ans(): 

    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"wpProQuiz_answerCorrect"))
    )

    # * print the ans 
    ans_list = driver.find_elements(By.CLASS_NAME, 'wpProQuiz_answerCorrect')

    ans = (ans_list[0].find_element(By.TAG_NAME,"label"))
    print(ans.text)

    # print("after print")
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"wpProQuiz_incorrect"))
    )
    ans_expend_div = driver.find_element(By.CLASS_NAME,"wpProQuiz_incorrect")
    print(ans_expend_div.find_element(By.TAG_NAME,"p").text)

    # time.sleep(3)

def click_next_button():
    wait.until(
        EC.element_to_be_clickable((By.NAME ,'next'))
    )

    next_button = driver.find_element(By.NAME ,'next')

    print("scroll now")
    # time.sleep(2)
    driver.execute_script("window.scrollTo(0,400);")
    # time.sleep(2)

    print(next_button.click())
    print("clicked check button")
    driver.execute_script("window.scrollTo(0, 0);") 


# * for one page it need 
for x in range(3):
    question =find_question() 
    print(question)
    click_the_check_button(x)
    find_ans()
    click_next_button()


# driver.close()
driver.quit()

