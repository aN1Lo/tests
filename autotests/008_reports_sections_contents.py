# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\x1b[33m\n%s executing...\x1b[0m' % __name__[10:])
f.write('\n%s executing...' % __name__[10:])
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

if is_there(wd, 'ru.gigme.android.app:id/toolbar', False):
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ЛЕНТА\']', False):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ЛЕНТА\']').click()
        time.sleep(1)
        if is_there(wd, 'android:id/list', False):
            if is_there(wd, 'ru.gigme.android.app:id/rating_photos_gallery', False):
                if is_there(wd, 'ru.gigme.android.app:id/photo', False):
                    wd.find_element_by_id('ru.gigme.android.app:id/photo').click()
                    time.sleep(2)
                    if is_there(wd, 'ru.gigme.android.app:id/photo', False):
                        if is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']', False):
                            wd.find_element_by_xpath(u'//android.widget.ImageButton\
                            [@content-desc=\'Navigate up\']').click()
                            time.sleep(3)
                            if is_there(wd, 'ru.gigme.android.app:id/popImageView', False) and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Популярное\']', False):
                                wd.find_element_by_id('ru.gigme.android.app:id/popImageView').click()
                                time.sleep(2)
                                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Популярные\']', False) and is_there(wd, 'ru.gigme.android.app:id/popGalleryGrid', False):
                                    if is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']', False):
                                        wd.find_element_by_xpath(u'//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                        time.sleep(3)
                                        if is_there(wd, 'ru.gigme.android.app:id/reports_date', False):
                                            date = ""
                                            date = wd.find_element_by_id('ru.gigme.android.app:id/reports_date').text
                                            if is_there(wd, 'ru.gigme.android.app:id/place', False) and is_there(wd, 'ru.gigme.android.app:id/thumb', False):
                                                place = ""
                                                place = wd.find_element_by_id('ru.gigme.android.app:id/place').text
                                                wd.find_element_by_id('ru.gigme.android.app:id/thumb').click()
                                                time.sleep(3)
                                                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Отчет\']', False) and is_there(wd, 'ru.gigme.android.app:id/smallCirclePhoto', False):
                                                    if is_there(wd, 'ru.gigme.android.app:id/placeTextView', False):
                                                        place_into = ""
                                                        place_into = wd.find_element_by_id('ru.gigme.android.app:id/placeTextView').text
                                                        if place != place_into:
                                                            print('\x1b[31mERROR: Wrong place.\x1b[0m')
                                                            f.write('ERROR: Wrong place.\n')
                                                            f.flush()
                                                        else:
                                                            print('\x1b[33mEvent place is %s\x1b[0m' % place)
                                                            f.write('Event place is %s\n' % place)
                                                            f.flush()
                                                        if is_there(wd, 'ru.gigme.android.app:id/dateTextView', False):
                                                            date_into = ""
                                                            date_into = wd.find_element_by_id('ru.gigme.android.app:id/dateTextView').text
                                                            if date not in date_into:
                                                                print('\x1b[31mERROR: Wrong date.\x1b[0m')
                                                                f.write('ERROR: Wrong date.\n')
                                                                f.flush()
                                                            else:
                                                                print('\x1b[33mEvent date is %s\x1b[0m' % date)
                                                                f.write('Event date is %s\n' % date)
                                                                f.flush()
                                                            if is_there(wd, 'ru.gigme.android.app:id/thumb', False):
                                                                print('\x1b[33mEvent photos exists.\x1b[0m')
                                                                f.write('Event photos exists.\n')
                                                                f.flush()
                                                                if (is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']', False)):
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
