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

desired_caps = {}
desired_caps['deviceName'] = 'Emulator'
desired_caps['platformVersion'] = '6.0'
desired_caps['platformName'] = 'Android'
desired_caps['exported'] = 'true'
desired_caps['appPackage'] = 'ru.gigme.android.app'
desired_caps['appActivity'] = '.ui.agreement.FirstRunActivity'
desired_caps['app'] = os.path.abspath('/Users/Adm/Downloads/tests/gigme.apk')
 
wd = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)
time.sleep(1)
flag = False

if is_there(wd, 'android:id/button2'):
    wd.find_element_by_id('android:id/button2').click()
    time.sleep(2)
    if is_there(wd, 'ru.gigme.android.app:id/agreement_text'):
        if is_there(wd, 'ru.gigme.android.app:id/confirm'):
            wd.find_element_by_id('ru.gigme.android.app:id/confirm').click()
            time.sleep(5)
            if is_there(wd, 'ru.gigme.android.app:id/toolbar'):
                if is_there(wd, 'android:id/list'):
                    if is_there(wd, 'ru.gigme.android.app:id/rating_photos_gallery'):
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
