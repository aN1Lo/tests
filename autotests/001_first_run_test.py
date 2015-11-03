import os
import time
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

# __name__ = [unit[:unit.find('.')] for unit in os.listdir('autotests') if unit.endswith('.py') and "__init__" not in unit]
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
desired_caps['fullReset'] = 'true'
 
wd = webdriver.Remote('http://127.0.0.1:5000/wd/hub', desired_caps)
time.sleep(1)
flag = False

if is_there(wd, 'android:id/button1'):
    wd.find_element_by_id('android:id/button1').click()
    time.sleep(10)
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
