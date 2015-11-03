# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\x1b[33m\n%s executing...\x1b[0m' % __name__[10:])
f.write('\n%s executing...\n' % __name__[10:])
f.flush()


def is_there(driver, id_str, auth):
    try:
        driver.find_element_by_id(id_str)
        if auth:
            print('\x1b[36mThere is %s\x1b[0m' % id_str)
        else:
            print('There is %s' % id_str)
        f.write('There is %s\n' % id_str)
        f.flush()
        return True
    except NoSuchElementException:
        if auth:
            print('\x1b[36mError: There is no %s\x1b[0m' % id_str)
        else:
            print('\x1b[31mError: There is no %s\x1b[0m' % id_str)
        f.write('Error: There is no %s\n' % id_str)
        f.flush()
        return False


def is_there_by_xpath(driver, xpath_str, auth):
    try:
        driver.find_element_by_xpath(xpath_str)
        if auth:
            print('\x1b[36mThere is %s\x1b[0m' % xpath_str)
        else:
            print('There is %s' % xpath_str)
        f.write('There is %s\n' % xpath_str)
        f.flush()
        return True
    except NoSuchElementException:
        if auth:
            print('\x1b[36mError: There is no %s\x1b[0m' % xpath_str)
        else:
            print('\x1b[31mError: There is no %s\x1b[0m' % xpath_str)
        f.write('Error: There is no %s\n' % xpath_str)
        f.flush()
        return False


def authorization(driver, login, passwd):
    print('\x1b[33mAuthorizating...\x1b[0m')
    f.write('Authorizating...\n')
    global flag_auth
    if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']', True):
        driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
        if is_there(driver, 'ru.gigme.android.app:id/material_drawer_account_header_current', True):
            print('\x1b[33mAlready authorized.\x1b[0m')
            f.write('Already authorized.\n')
            flag_auth = True
            return True
        else:
            if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Настройки\']', True):
                driver.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
                time.sleep(1)
                if is_there(driver, 'ru.gigme.android.app:id/person_name', True):
                    driver.find_element_by_id('ru.gigme.android.app:id/person_name').send_keys(login)
                    if is_there(driver, 'ru.gigme.android.app:id/password', True):
                        driver.find_element_by_id('ru.gigme.android.app:id/password').send_keys(passwd)
                        if is_there(driver, 'ru.gigme.android.app:id/login_button', True):
                            driver.find_element_by_id('ru.gigme.android.app:id/login_button').click()
                            time.sleep(1)
                            if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']', True):
                                driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
                                flag_auth = False
                                print('\x1b[33mLogged on.\x1b[0m')
                                f.write('Logged on.\n')
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
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']', False):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']', False) and is_there(wd, 'ru.gigme.android.app:id/favoriteButton', False) \
                and wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').text == u'Настройки':
            wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').click()
            time.sleep(1)
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']', False) and is_there(wd, 'ru.gigme.android.app:id/regDateText', False) \
                    and wd.find_element_by_id('ru.gigme.android.app:id/regDateText').text == u'Дата регистрации 02.09.2015' \
                    and is_there(wd, 'ru.gigme.android.app:id/firstNameText', False) and wd.find_element_by_id('ru.gigme.android.app:id/firstNameText').text == u'Введите ваше имя' \
                    and is_there(wd, 'ru.gigme.android.app:id/lastNameText', False) and wd.find_element_by_id('ru.gigme.android.app:id/lastNameText').text == u'Введите вашу фамилию' \
                    and is_there(wd, 'ru.gigme.android.app:id/birthdayText', False) and wd.find_element_by_id('ru.gigme.android.app:id/birthdayText').text == u'23.11.1993' \
                    and is_there(wd, 'ru.gigme.android.app:id/phoneText', False) and wd.find_element_by_id('ru.gigme.android.app:id/phoneText').text == '+79610988665' \
                    and is_there(wd, 'ru.gigme.android.app:id/changePassButton', False):
                wd.find_element_by_id('ru.gigme.android.app:id/birthdayText').click()
                if is_there(wd, 'ru.gigme.android.app:id/date_picker', False) and is_there(wd, 'android:id/date_picker_month', False) \
                        and is_there(wd, 'android:id/date_picker_day', False) and is_there(wd, 'android:id/date_picker_year', False) \
                        and wd.find_element_by_id('android:id/date_picker_month').text == 'NOV' \
                        and wd.find_element_by_id('android:id/date_picker_day').text == '23' \
                        and wd.find_element_by_id('android:id/date_picker_year').text == '1993' \
                        and is_there(wd, 'android:id/button1', False) and wd.find_element_by_id('android:id/button1').text == u'OK':
                    if is_there_by_xpath(wd, '//android.widget.CheckBox[@checked=\'false\']', False):
                        # and wd.find_element_by_id('ru.gigme.android.app:id/show_age').checked == 'false':
                        wd.find_element_by_id('ru.gigme.android.app:id/show_age').click()
                    elif is_there_by_xpath(wd, '//android.widget.CheckBox[@checked=\'true\']', False):
                        pass
                    wd.find_element_by_id('android:id/button1').click()
                    wd.find_element_by_id('ru.gigme.android.app:id/phoneText').click()
                    if is_there(wd, 'ru.gigme.android.app:id/alertTitle', False) and wd.find_element_by_id('ru.gigme.android.app:id/alertTitle').text == u'Телефон' \
                            and is_there(wd, 'ru.gigme.android.app:id/message', False) and wd.find_element_by_id('ru.gigme.android.app:id/message').text == u'(961)098-86-65' \
                            and is_there(wd, 'ru.gigme.android.app:id/annotation', False) and wd.find_element_by_id('ru.gigme.android.app:id/annotation').text == u'Ваш номер телефона' \
                            and is_there(wd, 'android:id/button1', False) and wd.find_element_by_id('android:id/button1').text == u'ДАЛЕЕ':
                        wd.find_element_by_id('android:id/button1').click()
                        time.sleep(1)
                        if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']', False):
                            wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                            time.sleep(1)
                            flag = True
                            wd.quit()
                            print('\x1b[32m%s success.\x1b[0m' % __name__[10:])
                            f.write('%s success.\n' % __name__[10:])
                            f.flush()

if flag is False:
    wd.quit()
    print('\x1b[31m%s failed.\x1b[0m' % __name__[10:])
    f.write('%s failed.\n' % __name__[10:])
    f.flush()

f.close()
