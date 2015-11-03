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

if authorization(wd, 'an1lo', 'nokiac60') is False:
    flag = False
else:
    time.sleep(1)
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']'):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
        time.sleep(1)
        print('Logging of...')
        f.write('Logging of...\n')
        f.flush()
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']'):
            if is_there_by_xpath(wd, '//android.widget.ImageView[@index=\'0\']'):
                wd.find_element_by_xpath('//android.widget.ImageView[@index=\'0\']').click()
                if is_there(wd, 'ru.gigme.android.app:id/title'):
                    wd.find_element_by_id('ru.gigme.android.app:id/title').click()
                    time.sleep(1)
                    if is_there(wd, 'ru.gigme.android.app:id/toolbar'):
                        print('Logged off.')
                        f.write('Logged off.\n')
                        f.flush()
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


#def logging_off(driver):
#    print('Logging of...')
#    f.write('Logging of...\n')
#    f.flush()
#    if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
#        driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
#        if is_there(driver, 'ru.gigme.android.app:id/material_drawer_account_header_current'):
#            if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Настройки\']'):
#                driver.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
#                time.sleep(2)
#                if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Мой профиль\']'):
#                    if is_there_by_xpath(driver, '//android.widget.ImageView[@index=\'0\']'):
#                        driver.find_element_by_xpath('//android.widget.ImageView[@index=\'0\']').click()
#                        if is_there(driver, 'ru.gigme.android.app:id/title'):
#                            driver.find_element_by_id('ru.gigme.android.app:id/title').click()
#                            time.sleep(1)
#                            if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
#                                driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
#                                print('Logged off.')
#                                f.write('Logged off.\n')
#                                f.flush()
#                                return True
#        else:
#            print('Already logged off.')
#            f.write('Already logged off.\n')
#            f.flush()
#            return True
#    return False