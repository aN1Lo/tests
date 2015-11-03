# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\x1b[33m\n%s executing...\x1b[0m' % __name__[10:])
f.write('\n%s executing...\n' % __name__[10:])
f.flush()


class User:
    name = ""
    status = ""
    number = ""
    likes = ""
    instagram = False
    # def __init__(self, name1, status1, number1, likes1, instagram1):
    #     self.name = name1
    #     self.status = status1
    #     self.number = number1
    #     self.likes = likes1
    #     self.instagram = instagram1


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
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']', False):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Топ\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']', False):
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'СПИСОК\']', False):
                wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'СПИСОК\']').click()
                time.sleep(1)
                profile = User()
                if is_there(wd, 'ru.gigme.android.app:id/topCircularImage', False) and is_there(wd, 'ru.gigme.android.app:id/topUserName', False) \
                        and is_there(wd, 'ru.gigme.android.app:id/topStatus', False) and is_there(wd, 'ru.gigme.android.app:id/topRank', False) \
                        and is_there(wd, 'ru.gigme.android.app:id/topLikes', False):
                    profile.name = wd.find_element_by_id('ru.gigme.android.app:id/topUserName').text
                    profile.status = wd.find_element_by_id('ru.gigme.android.app:id/topStatus').text
                    profile.number = wd.find_element_by_id('ru.gigme.android.app:id/topRank').text
                    profile.likes = wd.find_element_by_id('ru.gigme.android.app:id/topLikes').text
                    if is_there(wd, 'ru.gigme.android.app:id/instagram', False):
                        profile.instagram = True
                    wd.find_element_by_id('ru.gigme.android.app:id/topCircularImage').click()
                    time.sleep(2)
                    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Профиль\']', False) and is_there(wd, 'ru.gigme.android.app:id/profileAvatar', False) \
                            and is_there(wd, 'ru.gigme.android.app:id/profileNameText', False) and is_there(wd, 'ru.gigme.android.app:id/topPosText', False) \
                            and is_there(wd, 'ru.gigme.android.app:id/favoriteButton', False):
                        current = User()
                        current.name = wd.find_element_by_id('ru.gigme.android.app:id/profileNameText').text
                        current.number = wd.find_element_by_id('ru.gigme.android.app:id/topPosText').text
                        if is_there(wd, 'ru.gigme.android.app:id/statusText', False):
                            current.status = wd.find_element_by_id('ru.gigme.android.app:id/statusText').text
                        if is_there(wd, 'ru.gigme.android.app:id/action_instagram', False):
                            current.instagram = True
                        if profile.name in current.name or current.name in profile.name:
                            if current.number in profile.number:
                                if profile.status == current.status:
                                    if profile.instagram and current.instagram or not (profile.instagram and current.instagram):
                                        print('\x1b[33mUser name is %s\x1b[0m' % profile.name.encode('utf-8', "replace"))
                                        f.write('User name is %s\n' % profile.name.encode('utf-8', "replace"))
                                        f.flush()
                                        print('\x1b[33mUser raiting is %s\x1b[0m' % current.number)
                                        f.write('User raiting is %s\n' % current.number)
                                        f.flush()
                                        print('\x1b[33mUser status is %s\x1b[0m' % profile.status.encode('utf-8', "replace"))
                                        f.write('User status is %s\n' % profile.status.encode('utf-8', "replace"))
                                        f.flush()
                                        if current.instagram:
                                            print('\x1b[33mUser has instagram\x1b[0m')
                                            f.write('User has instagram\n')
                                            f.flush()
                                        else:
                                            print('\x1b[33mUser has no instagram\x1b[0m')
                                            f.write('User has no instagram\n')
                                            f.flush()
                                        flag = True
                                        wd.quit()
                                        print('\x1b[32m%s success.\x1b[0m' % __name__[10:])
                                        f.write('%s success.\n' % __name__[10:])
                                        f.flush()
                                    else:
                                        print('\x1b[31mAmbiguous information about instagram.\x1b[0m')
                                        f.write('Ambiguous information about instagram.\n')
                                        f.flush()
                                else:
                                    print('\x1b[31mCurrent status is %s - status from list %s\x1b[0m'% (current.status.encode('utf-8', "replace"), profile.status.encode('utf-8', "replace")))
                                    f.write('Current status is %s - status from list %s\n' % (current.status.encode('utf-8', "replace"), profile.status.encode('utf-8', "replace")))
                                    f.flush()
                            else:
                                print('\x1b[31mCurrent number is %s - number from list %s\x1b[0m' % (current.number, profile.number))
                                f.write('Current number is %s - number from list %s\n' % (current.number, profile.number))
                                f.flush()
                        else:
                            print('\x1b[31mCurrent name is %s - name from list %s\x1b[0m' % (current.name.encode('utf-8', "replace"), profile.name.encode('utf-8', "replace")))
                            f.write('Current name is %s - name from list %s\n' % (current.name.encode('utf-8', "replace"), profile.name.encode('utf-8', "replace")))
                            f.flush()

if flag is False:
    wd.quit()
    print('\x1b[31m%s failed.\x1b[0m' % __name__[10:])
    f.write('%s failed.\n' % __name__[10:])
    f.flush()

f.close()
