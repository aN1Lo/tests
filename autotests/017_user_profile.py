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


if is_there_by_xpath(wd, '//android.widget.ImageButton[@text=\'\']'):
    wd.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
    if is_there(wd, 'ru.gigme.android.app:id/material_drawer_account_header_current'):
        wd.find_element_by_id('ru.gigme.android.app:id/material_drawer_account_header_current').click()
        time.sleep(2)
        print('Already authorized.')
        f.write('Already authorized.\n')
        f.flush()
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']') and is_there(wd, 'ru.gigme.android.app:id/profileAvatar') \
                and is_there(wd, 'ru.gigme.android.app:id/lastActivityText') and is_there(wd, 'ru.gigme.android.app:id/profileNameText') \
                and wd.find_element_by_id('ru.gigme.android.app:id/profileNameText').text == login and is_there(wd, 'ru.gigme.android.app:id/userLoginText') \
                and login in wd.find_element_by_id('ru.gigme.android.app:id/userLoginText').text and is_there(wd, 'ru.gigme.android.app:id/favoriteButton') \
                and wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').text == u'Настройки' and is_there(wd, 'ru.gigme.android.app:id/topPosText') \
                and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Место в рейтинге\']') and is_there(wd, 'ru.gigme.android.app:id/subscribersText') \
                and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Подписчиков\']') and is_there(wd, 'ru.gigme.android.app:id/subscribedText') \
                and is_there(wd, 'ru.gigme.android.app:id/favText') and wd.find_element_by_id('ru.gigme.android.app:id/favText').text == u'Подписана' \
                and is_there(wd, 'ru.gigme.android.app:id/action_status') and wd.find_element_by_id('ru.gigme.android.app:id/action_status').text == 'Good enough' \
                and is_there(wd, 'ru.gigme.android.app:id/action_instagram') and wd.find_element_by_id('ru.gigme.android.app:id/action_instagram').text == u'Добавить инстаграм' \
                and is_there(wd, 'ru.gigme.android.app:id/action_album') and wd.find_element_by_id('ru.gigme.android.app:id/action_album').text == u'Фотоальбом':
            wd.find_element_by_id('ru.gigme.android.app:id/subscribersText').click()
            time.sleep(1)
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Подписки\']') \
                    and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ПОДПИСЧИКИ\']') \
                    and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ПОДПИСАНА\']'):
                wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ПОДПИСЧИКИ\']').click()
                if is_there(wd, 'ru.gigme.android.app:id/topUserName'):
                    wd.find_element_by_id('ru.gigme.android.app:id/topUserName').click()
                    time.sleep(1)
                    if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                        wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                        time.sleep(1)
                        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ПОДПИСАНА\']').click()
                        time.sleep(1)
                        if is_there(wd, 'ru.gigme.android.app:id/topUserName'):
                            wd.find_element_by_id('ru.gigme.android.app:id/topUserName').click()
                            time.sleep(1)
                            if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                    wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']'):
                                        print('Profile information is correct.')
                                        f.write('Profile information is correct.\n')
                                        f.flush()
                                        flag = True
                                        wd.quit()
                                        print('%s success.' % __name__[10:])
                                        f.write('%s success.\n' % __name__[10:])
                                        f.flush()
    else:
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Настройки\']'):
            wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Настройки\']').click()
            time.sleep(1)
            if is_there(wd, 'ru.gigme.android.app:id/person_name'):
                wd.find_element_by_id('ru.gigme.android.app:id/person_name').send_keys(login)
                if is_there(wd, 'ru.gigme.android.app:id/password'):
                    wd.find_element_by_id('ru.gigme.android.app:id/password').send_keys(passwd)
                    if is_there(wd, 'ru.gigme.android.app:id/login_button'):
                        wd.find_element_by_id('ru.gigme.android.app:id/login_button').click()
                        time.sleep(3)
                        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']') and is_there(wd, 'ru.gigme.android.app:id/profileAvatar') \
                                and is_there(wd, 'ru.gigme.android.app:id/lastActivityText') and is_there(wd, 'ru.gigme.android.app:id/profileNameText') \
                                and wd.find_element_by_id('ru.gigme.android.app:id/profileNameText').text == login and is_there(wd, 'ru.gigme.android.app:id/userLoginText') \
                                and login in wd.find_element_by_id('ru.gigme.android.app:id/userLoginText').text and is_there(wd, 'ru.gigme.android.app:id/favoriteButton') \
                                and wd.find_element_by_id('ru.gigme.android.app:id/favoriteButton').text == u'Настройки' and is_there(wd, 'ru.gigme.android.app:id/topPosText') \
                                and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Место в рейтинге\']') and is_there(wd, 'ru.gigme.android.app:id/subscribersText') \
                                and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Подписчиков\']') and is_there(wd, 'ru.gigme.android.app:id/subscribedText') \
                                and is_there(wd, 'ru.gigme.android.app:id/favText') and wd.find_element_by_id('ru.gigme.android.app:id/favText').text == u'Подписана' \
                                and is_there(wd, 'ru.gigme.android.app:id/action_status') and wd.find_element_by_id('ru.gigme.android.app:id/action_status').text == 'Good enough' \
                                and is_there(wd, 'ru.gigme.android.app:id/action_instagram') and wd.find_element_by_id('ru.gigme.android.app:id/action_instagram').text == u'Добавить инстаграм' \
                                and is_there(wd, 'ru.gigme.android.app:id/action_album') and wd.find_element_by_id('ru.gigme.android.app:id/action_album').text == u'Фотоальбом':
                            wd.find_element_by_id('ru.gigme.android.app:id/subscribersText').click()
                            time.sleep(1)
                            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Подписки\']') \
                                    and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ПОДПИСЧИКИ\']') \
                                    and is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'ПОДПИСАНА\']'):
                                wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ПОДПИСЧИКИ\']').click()
                                if is_there(wd, 'ru.gigme.android.app:id/topUserName'):
                                    wd.find_element_by_id('ru.gigme.android.app:id/topUserName').click()
                                    time.sleep(1)
                                    if is_there_by_xpath(wd, u'//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                        wd.find_element_by_xpath(u'//android.widget.ImageButton\[@content-desc=\'Navigate up\']').click()
                                        time.sleep(1)
                                        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'ПОДПИСАНА\']').click()
                                        time.sleep(1)
                                        if is_there(wd, 'ru.gigme.android.app:id/topUserName'):
                                            wd.find_element_by_id('ru.gigme.android.app:id/topUserName').click()
                                            time.sleep(1)
                                            if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                                wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                                if is_there_by_xpath(wd, '//android.widget.ImageButton[@content-desc=\'Navigate up\']'):
                                                    wd.find_element_by_xpath('//android.widget.ImageButton[@content-desc=\'Navigate up\']').click()
                                                    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Мой профиль\']'):
                                                        print('Profile information is correct.')
                                                        f.write('Profile information is correct.\n')
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
