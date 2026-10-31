from selenium.webdriver.common.by import By


class Locator:
    button_for_logging_into_account = (By.XPATH,'.//button[contains(text(),"Войти в аккаунт")]') # кнопка войти в акаунт на главной странице
    click_register_button_in_login_form = (By.XPATH,'.//a[contains(text(),"Зарегистрироваться")]') #кнопка зарегистрироватся в форме входа
    field_for_entering_name_in_registration_form = (By.XPATH,'.//label[text()="Имя"]/following-sibling::input') #поле ввода имя в форме регистраций
    field_for_entering_email_address_in_registration_form = (By.XPATH,'.//label[text()="Email"]/following-sibling::input') #поле ввода Email в форме регистраций 
    field_for_entering_password_in_registration_form = (By.XPATH,'.//label[text()="Пароль"]/following-sibling::input') #поле ввода пароля в форме регистраций
    click_register_button_in_registration_form = (By.XPATH,'.//button[contains(text(),"Зарегистрироваться")]') # кнопка зарегистрироватся в форме регистраций
    email_field_in_login_form =(By.CSS_SELECTOR,"input[type='text']") # поле Email в форме входа
    password_field_in_login_form = (By.CSS_SELECTOR,'input[type="password"]') #поле пароль в форме входа 
    click_login_button_in_login_form = (By.XPATH,'.//button[contains(text(),"Войти")]') #кнопка войти в форме входа
    click_personal_account_button_on_main_page = (By.XPATH,'.//p[contains(text(),"Личный Кабинет")]') # кнопка личный кабинет на главной странице
    login_button_is_located_in_registration_form = (By.XPATH,'.//a[contains(text(),"Войти")]') # кнопка войти войти в форме регистраций
    click_forgot_password_button_in_login_form = (By.XPATH,'.//a[contains(text(),"Восстановить пароль")]') #кнопка востановить пароль в форме входа
    constructor_button_in_personal_account = (By.XPATH,'.//p[contains(text(),"Конструктор")]') # кнопка конструктор в личном кабинете
    logo_in_personal_account = (By.XPATH,'//div[contains(@class,"header__logo")]//a') # логотип в личном кабинете 
    exit_button_in_personal_account = (By.XPATH,'.//button[contains(text(),"Выход")]') # кнопка выход в личном кабинете
    bun_button_in_constructor = (By.XPATH, ".//span[text()='Булки']/parent::div") # кнопка булка в конструкторе
    souces_button_in_constructor = (By.XPATH, ".//span[text()='Соусы']/parent::div") #кнопка соусы в конструкторе
    filling_button_in_constructor = (By.XPATH, ".//span[text()='Начинки']/parent::div") # кнопка начинки в конструкторе
    heading_bun = (By.XPATH,'.//h2[text()="Булки"]') # заголовок булки
    heading_souces = (By.XPATH,'.//h2[text()="Соусы"]') # заголовок соусы
    heading_filling = (By.XPATH,'.//h2[text()="Начинки"]') # заголовок начинки