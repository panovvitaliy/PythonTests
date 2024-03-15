import time

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://www.demoblaze.com/'


def test_simple():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    time.sleep(1)

    contact_link = driver.find_element(by=By.XPATH, value='//a[contains(text(),"Contact")]')
    login_link = driver.find_element(by=By.ID, value='login2')
    signup_link = driver.find_element(by=By.XPATH, value='//a[@data-target="#signInModal"]')
    home_link = driver.find_element(by=By.XPATH, value='(//div/ul/li/a)[1]')
    carousel_next_btn = driver.find_element(by=By.CLASS_NAME, value='carousel-control-next')
    carousel_prev_btn = driver.find_element(by=By.CSS_SELECTOR, value='span[class*="prev"]')
    product_samsung_s6 = driver.find_element(by=By.XPATH, value='//a[contains(text(),"Samsung galaxy s6")]')
    pagination_prev_btn = driver.find_element(by=By.CSS_SELECTOR, value='#prev2.page-link')
    pagination_next_btn = driver.find_element(by=By.CSS_SELECTOR, value='#next2.page-link')
    header_logo = driver.find_element(by=By.XPATH, value='//a/img[@src="bm.png"]')

    # Contact Form
    contact_link.click()
    time.sleep(1)

    contact_email_input = driver.find_element(by=By.XPATH, value='//form/*/input[@id="recipient-email"]')
    contact_name_input = driver.find_element(by=By.XPATH, value='(//form/div)[2]/input')
    message_input = driver.find_element(by=By.CSS_SELECTOR, value='.form-group textarea')
    contact_form_close_btn = driver.find_element(by=By.XPATH,
                                                 value="//div[@aria-labelledby='exampleModalLabel']/*/*/*/button["
                                                       "contains(text(),'Close')]")
    contact_form_close_x_btn = driver.find_element(by=By.XPATH,
                                                   value='//div[@aria-labelledby="exampleModalLabel"]/*/*/*/button['
                                                         '@class="close"]')
    contact_form_send_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[onclick="send()"]')
    contact_form_close_btn.click()

    # Login Form
    login_link.click()
    time.sleep(1)

    login_username_input = driver.find_element(by=By.ID, value='loginusername')
    login_password_input = driver.find_element(by=By.ID, value='loginpassword')
    login_form_close_btn = driver.find_element(by=By.XPATH,
                                               value="//div[@aria-labelledby='logInModalLabel']/*/*/*/button["
                                                     "contains(text(),'Close')]")
    login_form_close_x_btn = driver.find_element(by=By.XPATH,
                                                 value='//div[@aria-labelledby="logInModalLabel"]/*/*/*/button['
                                                       '@class="close"]')
    login_form_login_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[onclick="logIn()"]')
    login_form_close_x_btn.click()

    # Product page
    product_samsung_s6.click()
    time.sleep(1)

    product_page_product_name = driver.find_element(by=By.CSS_SELECTOR, value='#tbodyid > .name')
    product_page_product_img = driver.find_element(by=By.CSS_SELECTOR, value='img[src*="galaxy"]')
    product_page_product_price = driver.find_element(by=By.CSS_SELECTOR, value='h3.price-container')
    product_page_add_to_card_btn = driver.find_element(by=By.CSS_SELECTOR, value='a[onclick*="addToCart"]')
    product_page_add_to_card_btn.click()
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

    # Shopping Cart page
    shopping_cart_link = driver.find_element(by=By.ID, value='cartur')
    shopping_cart_link.click()
    time.sleep(1)

    total_price_info = driver.find_element(by=By.XPATH, value='//*[@id="totalp"]')
    product_name_in_the_cart = driver.find_element(by=By.XPATH, value='(//tr/td)[last()-2]')
    delete_product_in_the_cart_btn = driver.find_element(by=By.XPATH, value='(//tr/td)[last()]/a')
    place_order_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[data-target="#orderModal"]')

    # Place order form
    place_order_btn.click()
    time.sleep(1)

    order_form_name_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                   '"]/*/*/div[2]/*/div[1]/input[@id="name"]')
    order_form_country_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                      '"]/*/*/div[2]/*/div[2]/input[@id="country"]')
    order_form_city_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                   '"]/*/*/div[2]/*/div[3]/input[@id="city"]')
    order_form_credit_card_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                          '"]/*/*/div[2]/*/div[4]/input[@id="card"]')
    order_form_card_month_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                         '"]/*/*/div[2]/*/div[5]/input[@id="month"]')
    order_form_card_year_input = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                        '"]/*/*/div[2]/*/div[6]/input[@id="year"]')
    order_form_purchase_btn = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                     '"]/*/*/div[@class="modal-footer"]/button['
                                                                     '@onclick="purchaseOrder()"]')
    order_form_close_btn = driver.find_element(by=By.XPATH, value="//div[@aria-labelledby='orderModalLabel"
                                                                  "']/*/*/*/button["
                                                                  "contains(text(),'Close')]")
    order_form_close_x_btn = driver.find_element(by=By.XPATH, value='//div[@aria-labelledby="orderModalLabel'
                                                                    '"]/*/*/*/button[@class="close"]')
    order_form_close_x_btn.click()
    time.sleep(1)
    delete_product_in_the_cart_btn.click()
    time.sleep(1)

    # driver.quit()
