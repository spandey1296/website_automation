from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options


def pythonDynamicComponents():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    driver.get("https://github.com/login")

    text_box1 = driver.find_element(by=By.ID, value="login_field")
    text_box2 = driver.find_element(by=By.ID, value="password")
    submit_button = driver.find_element(by=By.NAME, value="commit")

    text_box1.send_keys("GITHUB_USERNAME")
    text_box2.send_keys("GITHUB_PASSWORD")
    submit_button.click()
    WebDriverWait(driver=driver, timeout=50).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )

    error_message = "Incorrect username or password."

    errors = driver.find_elements(By.CLASS_NAME, "flash-error")

    if any(error_message in e.text for e in errors):
        print("[!] Login failed!!!!!")
        driver.quit()

    else:
        print("logged In Successfull!!!!")
        time.sleep(10000)


for i in range(1):
    for attempt in range(1):
        try:
            pythonDynamicComponents()
        except:
            print("Hii Folks! we are trying to connect!!!")
        else:
            break
    else:
        print("# we failed all the attempts - deal with the consequences.")
