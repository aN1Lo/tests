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

if is_there_by_xpath(wd, '//android.widget.ImageButton[@text=\'\']', False):
    wd.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Оферта\']', False):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Оферта\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Оферта\']', False) and is_there(wd, 'ru.gigme.android.app:id/agreement_text', False):
            if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']', False):
                wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                time.sleep(1)
                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Отчёты\']', False):
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
