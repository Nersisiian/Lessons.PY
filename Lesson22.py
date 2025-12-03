# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# course = input("Ընտրել կուրսը: ")
# full_name = input("Անուն Ազգանուն: ")
# email = input("Էլ․ փոստ: ")
# phone = input("Հեռախոսահամար: ")
# preferred_time = input("Նախընրած ժամեր: ")

# driver = webdriver.Chrome()
# driver.maximize_window()

# try:
    
#     driver.get("https://smartcode.am/hy/")
#     time.sleep(2)

#     start_button = driver.find_element(By.CSS_SELECTOR, "a.but-main")
#     start_button.click()

#     wait = WebDriverWait(driver, 10)
#     form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.overlay-body form")))
#     time.sleep(1)

#     course_dropdown = driver.find_element(By.CSS_SELECTOR, "select[name='course']")
#     course_dropdown.click()
#     time.sleep(1)
    
#     try:
#         course_dropdown.find_element(By.XPATH, f"//option[contains(text(), '{course}')]").click()
#     except:
        
#         course_dropdown.find_element(By.XPATH, "//option[2]").click()

#     driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(full_name)
#     time.sleep(0.5)

#     driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)
#     time.sleep(0.5)

#     driver.find_element(By.CSS_SELECTOR, "input[type='tel']").send_keys(phone)
#     time.sleep(0.5)

#     time_select = driver.find_element(By.CSS_SELECTOR, "select[name='time']")
#     time_select.click()
#     time.sleep(1)
#     try:
#         time_select.find_element(By.XPATH, f"//option[contains(text(), '{preferred_time}')]").click()
#     except:
    
#         time_select.find_element(By.XPATH, "//option[2]").click()

#     time.sleep(1)

#     submit_button = driver.find_element(By.CSS_SELECTOR, "button.but-main")
#     submit_button.click()

#     print("✅ Ձևը հաջողությամբ ուղարկվեց!")

#     time.sleep(5)

# except Exception as ex:
#     print("❌ Սխալ:", ex)
# finally:
#     driver.quit()

#  pip install selenium webdriver-manager

# --------------------------------------------------------------------------------------------------------------------------------------

# from itertools import permutations as perm

# def permutations(s):
#     return list(set([''.join(p) for p in perm(s)]))



