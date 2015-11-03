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


def logging_off(driver):
    print('Logging of...')
    f.write('Logging of...\n')
    f.flush()
    if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
        driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
        if is_there(driver, 'ru.gigme.android.app:id/material_drawer_account_header_current'):
            if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Настройки\']'):
                driver.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
                time.sleep(2)
                if is_there_by_xpath(driver, u'//android.widget.TextView[@text=\'Мой профиль\']'):
                    if is_there_by_xpath(driver, '//android.widget.ImageView[@index=\'0\']'):
                        driver.find_element_by_xpath('//android.widget.ImageView[@index=\'0\']').click()
                        if is_there(driver, 'ru.gigme.android.app:id/title'):
                            driver.find_element_by_id('ru.gigme.android.app:id/title').click()
                            time.sleep(1)
                            if is_there_by_xpath(driver, '//android.widget.ImageButton[@text=\'\']'):
                                driver.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
                                print('Logged off.')
                                f.write('Logged off.\n')
                                f.flush()
                                return True
        else:
            print('Already logged off.')
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

if logging_off(wd) is False:
    flag = False
else:
    time.sleep(1)
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']'):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Топ\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']'):
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'СПИСОК\']'):
                # wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'СПИСОК\']').click()
                wd.swipe(100, 700, 700, 700, 600)
                time.sleep(2)
                if is_there(wd, 'ru.gigme.android.app:id/topCircularImage') and is_there(wd, 'ru.gigme.android.app:id/topUserName') \
                        and is_there(wd, 'ru.gigme.android.app:id/topStatus') and is_there(wd, 'ru.gigme.android.app:id/topRank') \
                        and is_there(wd, 'ru.gigme.android.app:id/topLikes'):
                    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ИЗБРАННОЕ\']'):
                        #  wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ИЗБРАННОЕ\']').click()
                        wd.swipe(700, 700, 100, 700, 600)
                        time.sleep(1)
                        if is_there(wd, 'ru.gigme.android.app:id/friend_list') and is_there(wd, 'ru.gigme.android.app:id/empty_view'):
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
