# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\n%s executing...' % __name__[10:])
f.write('\n%s executing...' % __name__[10:])
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

if is_there(wd, 'ru.gigme.android.app:id/toolbar'):
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ЛЕНТА\']'):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ЛЕНТА\']').click()
        time.sleep(1)
        if is_there(wd, 'android:id/list'):
            if is_there(wd, 'ru.gigme.android.app:id/rating_photos_gallery'):
                if is_there(wd, 'ru.gigme.android.app:id/photo'):
                    wd.find_element_by_id('ru.gigme.android.app:id/photo').click()
                    time.sleep(2)
                    if is_there(wd, 'ru.gigme.android.app:id/photo'):
                        if is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                            wd.find_element_by_xpath(u'//android.widget.ImageButton\
                            [@content-desc=\'Navigate up\']').click()
                            time.sleep(3)
                            if is_there(wd, 'ru.gigme.android.app:id/popImageView') and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Популярное\']'):
                                wd.find_element_by_id('ru.gigme.android.app:id/popImageView').click()
                                time.sleep(2)
                                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Популярные\']') and is_there(wd, 'ru.gigme.android.app:id/popGalleryGrid'):
                                    if is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                        wd.find_element_by_xpath(u'//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                        time.sleep(3)
                                        if is_there(wd, 'ru.gigme.android.app:id/reports_date'):
                                            date = ""
                                            date = wd.find_element_by_id('ru.gigme.android.app:id/reports_date').text
                                            if is_there(wd, 'ru.gigme.android.app:id/place') and is_there(wd, 'ru.gigme.android.app:id/thumb'):
                                                place = ""
                                                place = wd.find_element_by_id('ru.gigme.android.app:id/place').text
                                                wd.find_element_by_id('ru.gigme.android.app:id/thumb').click()
                                                time.sleep(3)
                                                if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Отчет\']') and is_there(wd, 'ru.gigme.android.app:id/smallCirclePhoto'):
                                                    if is_there(wd, 'ru.gigme.android.app:id/placeTextView'):
                                                        place_into = ""
                                                        place_into = wd.find_element_by_id('ru.gigme.android.app:id/placeTextView').text
                                                        if place != place_into:
                                                            print('ERROR: Wrong place.')
                                                            f.write('ERROR: Wrong place.\n')
                                                            f.flush()
                                                        else:
                                                            print('Event place is ' + place)
                                                            f.write('Event place is ' + place + '\n')
                                                            f.flush()
                                                        if is_there(wd, 'ru.gigme.android.app:id/dateTextView'):
                                                            date_into = ""
                                                            date_into = wd.find_element_by_id('ru.gigme.android.app:id/dateTextView').text
                                                            if date not in date_into:
                                                                print('ERROR: Wrong date.')
                                                                f.write('ERROR: Wrong date.\n')
                                                                f.flush()
                                                            else:
                                                                print('Event date is ' + date)
                                                                f.write('Event date is ' + date + '\n')
                                                                f.flush()
                                                            if is_there(wd, 'ru.gigme.android.app:id/thumb'):
                                                                print('Event photos exists.')
                                                                f.write('Event photos exists.\n')
                                                                f.flush()
                                                                if (is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']')):
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
