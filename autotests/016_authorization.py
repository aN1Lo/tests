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


def logging_off(driver):
    print('\x1b[33mLogging of...\x1b[0m')
    f.write('Logging of...\n')
    f.flush()
    if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']', True):
        driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
        if is_there(driver, 'ru.gigme.android.app:id/material_drawer_account_header_current', True):
            if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Настройки\']', True):
                driver.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
                time.sleep(2)
                if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Мой профиль\']', True):
                    if is_there_by_xpath(driver, '//android.widget.ImageView[@index=\'0\']', True):
                        driver.find_element_by_xpath('//android.widget.ImageView[@index=\'0\']').click()
                        if is_there(driver, 'ru.gigme.android.app:id/title', True):
                            driver.find_element_by_id('ru.gigme.android.app:id/title').click()
                            time.sleep(1)
                            if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']', True):
                                driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
                                print('\x1b[33mLogged off.\x1b[0m')
                                f.write('Logged off.\n')
                                f.flush()
                                return True
        else:
            print('\x1b[33mAlready logged off.\x1b[0m')
            f.write('Already logged off.\n')
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

if logging_off(wd) is False:
    flag = False
else:
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']', False):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
    time.sleep(1)
    login = 'aN1Lo'
    passwd = 'nokiac60'
    if is_there(wd, 'ru.gigme.android.app:id/person_name', False):
        wd.find_element_by_id('ru.gigme.android.app:id/person_name').send_keys(login)
        if is_there(wd, 'ru.gigme.android.app:id/password', False):
            wd.find_element_by_id('ru.gigme.android.app:id/password').send_keys(passwd)
            if is_there(wd, 'ru.gigme.android.app:id/login_button', False):
                wd.find_element_by_id('ru.gigme.android.app:id/login_button').click()
                time.sleep(3)
                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']', False) and is_there(wd, 'ru.gigme.android.app:id/profileAvatar', False) \
                        and is_there(wd, 'ru.gigme.android.app:id/lastActivityText', False) and is_there(wd, 'ru.gigme.android.app:id/profileNameText', False) \
                        and wd.find_element_by_id('ru.gigme.android.app:id/profileNameText').text == login and is_there(wd, 'ru.gigme.android.app:id/userLoginText', False) \
                        and login in wd.find_element_by_id('ru.gigme.android.app:id/userLoginText').text and is_there(wd, 'ru.gigme.android.app:id/favoriteButton', False) \
                        and wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').text == u'Настройки' and is_there(wd, 'ru.gigme.android.app:id/topPosText', False) \
                        and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Место в рейтинге\']', False) and is_there(wd, 'ru.gigme.android.app:id/subscribersText', False) \
                        and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Подписчиков\']', False) and is_there(wd, 'ru.gigme.android.app:id/subscribedText', False) \
                        and is_there(wd, 'ru.gigme.android.app:id/favText', False) and wd.find_element_by_id('ru.gigme.android.app:id/favText').text == u'Подписана' \
                        and is_there(wd, 'ru.gigme.android.app:id/action_status', False) and wd.find_element_by_id('ru.gigme.android.app:id/action_status').text == 'Good enough' \
                        and is_there(wd, 'ru.gigme.android.app:id/action_instagram', False) and wd.find_element_by_id('ru.gigme.android.app:id/action_instagram').text == u'Добавить инстаграм' \
                        and is_there(wd, 'ru.gigme.android.app:id/action_album', False) and wd.find_element_by_id('ru.gigme.android.app:id/action_album').text == u'Фотоальбом':
                    print('\x1b[33mProfile information is correct.\x1b[0m')
                    f.write('Profile information is correct.\n')
                    f.flush()
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
