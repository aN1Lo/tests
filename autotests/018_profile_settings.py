# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\n%s executing...' % __name__[10:])
f.write('\n%s executing...\n' % __name__[10:])
f.flush()


def is_there(driver, id_str):
    try:
        driver.find_element_by_id(id_str)
        print('There is ' + id_str)
        f.write('There is ' + id_str + '\n')
        f.flush()
        return True
    except NoSuchElementException:
        print('Error: There is no ' + id_str)
        f.write('Error: There is no ' + id_str + '\n')
        f.flush()
        return False


def is_there_by_xpath(driver, xpath_str):
    try:
        driver.find_element_by_xpath(xpath_str)
        print('There is ' + xpath_str)
        f.write('There is ' + xpath_str + '\n')
        f.flush()
        return True
    except NoSuchElementException:
        print('Error: There is no ' + xpath_str)
        f.write('Error: There is no ' + xpath_str + '\n')
        f.flush()
        return False


def authorization(driver, login, passwd):
    print('Authorizating...')
    f.write('Authorizating...\n')
    f.flush()
    global flag_auth
    if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
        driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
        if is_there(driver, 'ru.gigme.android.app:id/material_drawer_account_header_current'):
            print('Already authorized.')
            f.write('Already authorized.\n')
            f.flush()
            flag_auth = True
            return True
        else:
            if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Настройки\']'):
                driver.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
                time.sleep(1)
                if is_there(driver, 'ru.gigme.android.app:id/person_name'):
                    driver.find_element_by_id('ru.gigme.android.app:id/person_name').send_keys(login)
                    if is_there(driver, 'ru.gigme.android.app:id/password'):
                        driver.find_element_by_id('ru.gigme.android.app:id/password').send_keys(passwd)
                        if is_there(driver, 'ru.gigme.android.app:id/login_button'):
                            driver.find_element_by_id('ru.gigme.android.app:id/login_button').click()
                            time.sleep(1)
                            if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
                                driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
                                flag_auth = False
                                print('Logged on.')
                                f.write('Logged on.\n')
                                f.flush()
                                return True
    return False

desired_caps = {}
desired_caps['deviceName'] = 'Emulator'
desired_caps['platformVersion'] = '6.0'
desired_caps['platformName'] = 'Android'
desired_caps['exported'] = 'true'
desired_caps['appPackage'] = 'ru.gigme.android.app'
desired_caps['appActivity'] = '.MainActivity'

wd = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)
time.sleep(3)
flag = False

login = 'aN1Lo'
passwd = 'nokiac60'

if authorization(wd, 'an1lo', 'nokiac60') is False:
    flag = False
else:
    time.sleep(1)
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']'):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']') and is_there(wd, 'ru.gigme.android.app:id/favoriteButton') \
                and wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').text == u'Настройки':
            wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').click()
            time.sleep(1)
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']') and is_there(wd, 'ru.gigme.android.app:id/regDateText') \
                    and wd.find_element_by_id('ru.gigme.android.app:id/regDateText').text == u'Дата регистрации 02.09.2015' \
                    and is_there(wd, 'ru.gigme.android.app:id/firstNameText') and wd.find_element_by_id('ru.gigme.android.app:id/firstNameText').text == u'Введите ваше имя' \
                    and is_there(wd, 'ru.gigme.android.app:id/lastNameText') and wd.find_element_by_id('ru.gigme.android.app:id/lastNameText').text == u'Введите вашу фамилию' \
                    and is_there(wd, 'ru.gigme.android.app:id/birthdayText') and wd.find_element_by_id('ru.gigme.android.app:id/birthdayText').text == u'23.11.1993' \
                    and is_there(wd, 'ru.gigme.android.app:id/phoneText') and wd.find_element_by_id('ru.gigme.android.app:id/phoneText').text == '+79610988665' \
                    and is_there(wd, 'ru.gigme.android.app:id/changePassButton'):
                wd.find_element_by_id('ru.gigme.android.app:id/birthdayText').click()
                if is_there(wd, 'ru.gigme.android.app:id/date_picker') and is_there(wd, 'android:id/date_picker_month') \
                        and is_there(wd, 'android:id/date_picker_day') and is_there(wd, 'android:id/date_picker_year') \
                        and wd.find_element_by_id('android:id/date_picker_month').text == 'NOV' \
                        and wd.find_element_by_id('android:id/date_picker_day').text == '23' \
                        and wd.find_element_by_id('android:id/date_picker_year').text == '1993' \
                        and is_there(wd, 'android:id/button1') and wd.find_element_by_id('android:id/button1').text == u'OK':
                    if is_there_by_xpath(wd, '//android.widget.CheckBox[@checked=\'false\']'):
                        # and wd.find_element_by_id('ru.gigme.android.app:id/show_age').checked == 'false':
                        wd.find_element_by_id('ru.gigme.android.app:id/show_age').click()
                    elif is_there_by_xpath(wd, '//android.widget.CheckBox[@checked=\'true\']'):
                        pass
                    wd.find_element_by_id('android:id/button1').click()
                    wd.find_element_by_id('ru.gigme.android.app:id/phoneText').click()
                    if is_there(wd, 'ru.gigme.android.app:id/alertTitle') and wd.find_element_by_id('ru.gigme.android.app:id/alertTitle').text == u'Телефон' \
                            and is_there(wd, 'ru.gigme.android.app:id/message') and wd.find_element_by_id('ru.gigme.android.app:id/message').text == u'(961)098-86-65' \
                            and is_there(wd, 'ru.gigme.android.app:id/annotation') and wd.find_element_by_id('ru.gigme.android.app:id/annotation').text == u'Ваш номер телефона' \
                            and is_there(wd, 'android:id/button1') and wd.find_element_by_id('android:id/button1').text == u'ДАЛЕЕ':
                        wd.find_element_by_id('android:id/button1').click()
                        time.sleep(1)
                        if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                            wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                            time.sleep(1)
                            flag = True
                            wd.quit()
                            print('%s success.' % __name__[10:])
                            f.write('%s success.\n' % __name__[10:])
                            f.flush()

if flag is False:
    wd.quit()
    print('%s failed.' % __name__[10:])
    f.write('%s failed.\n' % __name__[10:])
    f.flush()

f.close()
