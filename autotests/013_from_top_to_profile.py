# -*- coding: utf-8 -*-

import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

f = open('tests.log', 'a')
print('\n%s executing...' % __name__[10:])
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
if is_there_by_xpath(wd, '//android.widget.ImageButton[@text=\'\']'):
    wd.find_element_by_xpath('//android.widget.ImageButton[@text=\'\']').click()
    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']'):
        wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'Топ\']').click()
        time.sleep(1)
        if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Топ\']'):
            if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'СПИСОК\']'):
                wd.find_element_by_xpath(u'//android.widget.TextView[@text=\'СПИСОК\']').click()
                time.sleep(1)
                profile = User()
                if is_there(wd, 'ru.gigme.android.app:id/topCircularImage') and is_there(wd, 'ru.gigme.android.app:id/topUserName') \
                        and is_there(wd, 'ru.gigme.android.app:id/topStatus') and is_there(wd, 'ru.gigme.android.app:id/topRank') \
                        and is_there(wd, 'ru.gigme.android.app:id/topLikes'):
                    profile.name = wd.find_element_by_id('ru.gigme.android.app:id/topUserName').text
                    profile.status = wd.find_element_by_id('ru.gigme.android.app:id/topStatus').text
                    profile.number = wd.find_element_by_id('ru.gigme.android.app:id/topRank').text
                    profile.likes = wd.find_element_by_id('ru.gigme.android.app:id/topLikes').text
                    if is_there(wd, 'ru.gigme.android.app:id/instagram'):
                        profile.instagram = True
                    wd.find_element_by_id('ru.gigme.android.app:id/topCircularImage').click()
                    time.sleep(2)
                    if is_there_by_xpath(wd, u'//android.widget.TextView[@text=\'Профиль\']') and is_there(wd, 'ru.gigme.android.app:id/profileAvatar') \
                            and is_there(wd, 'ru.gigme.android.app:id/profileNameText') and is_there(wd, 'ru.gigme.android.app:id/topPosText') \
                            and is_there(wd, 'ru.gigme.android.app:id/favoriteButton'):
                        current = User()
                        current.name = wd.find_element_by_id('ru.gigme.android.app:id/profileNameText').text
                        current.number = wd.find_element_by_id('ru.gigme.android.app:id/topPosText').text
                        if is_there(wd, 'ru.gigme.android.app:id/statusText'):
                            current.status = wd.find_element_by_id('ru.gigme.android.app:id/statusText').text
                        if is_there(wd, 'ru.gigme.android.app:id/action_instagram'):
                            current.instagram = True
                        if profile.name in current.name or current.name in profile.name:
                            if current.number in profile.number:
                                if profile.status == current.status:
                                    if profile.instagram and current.instagram or not (profile.instagram and current.instagram):
                                        print('User name is %s' %profile.name.encode('utf-8', "replace"))
                                        f.write('User name is %s\n' %profile.name.encode('utf-8', "replace"))
                                        f.flush()
                                        print('User raiting is ' + current.number)
                                        f.write('User raiting is ' + current.number + '\n')
                                        f.flush()
                                        print('User status is %s' %profile.status.encode('utf-8', "replace"))
                                        f.write('User status is %s\n' %profile.status.encode('utf-8', "replace"))
                                        f.flush()
                                        if current.instagram:
                                            print('User has instagram')
                                            f.write('User has instagram\n')
                                            f.flush()
                                        else:
                                            print('User jas no instagram')
                                            f.write('User jas no instagram\n')
                                            f.flush()
                                        flag = True
                                        wd.quit()
                                        print('%s success.' % __name__[10:])
                                        f.write('%s success.\n' % __name__[10:])
                                        f.flush()
                                    else:
                                        print('Ambiguous information about instagram.')
                                        f.write('Ambiguous information about instagram.\n')
                                        f.flush()
                                else:
                                    print('Current status is %s - status from list %s' % (current.status.encode('utf-8', "replace"), profile.status.encode('utf-8', "replace")))
                                    f.write('Current status is %s - status from list %s\n' % (current.status.encode('utf-8', "replace"), profile.status.encode('utf-8', "replace")))
                                    f.flush()
                            else:
                                print('Current number is %s - number from list %s' % (current.number, profile.number))
                                f.write('Current number is %s - number from list %s\n' % (current.number, profile.number))
                                f.flush()
                        else:
                            print('Current name is %s - name from list %s' % (current.name.encode('utf-8', "replace"), profile.name.encode('utf-8', "replace")))
                            f.write('Current name is %s - name from list %s\n' % (current.name.encode('utf-8', "replace"), profile.name.encode('utf-8', "replace")))
                            f.flush()

if flag is False:
    wd.quit()
    print('%s failed.' % __name__[10:])
    f.write('%s failed.\n' % __name__[10:])
    f.flush()

f.close()
