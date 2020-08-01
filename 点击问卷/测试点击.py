from selenium import webdriver
from configparser import ConfigParser
from PIL import Image
import random
import time

sex = ["/html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[1]/span",
       "/html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[2]/span"]
age = ['/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[1]/span/a',
       '/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[2]/span/a',
       '/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[3]/span/a',
       '/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[4]/span/a']
money = ['/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[1]/span/a',
         '/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[2]/span/a',
         '/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[3]/span/a',
         '/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[4]/span/a']
pet001 = ['/html/body/form/div[5]/div[3]/fieldset/div[4]/div[2]/div[1]/span',
          '/html/body/form/div[5]/div[3]/fieldset/div[4]/div[2]/div[2]/span']
petdogcat = ['/html/body/form/div[5]/div[3]/fieldset/div[8]/div[2]/div[1]/span/a',
             '/html/body/form/div[5]/div[3]/fieldset/div[8]/div[2]/div[2]/span/a']
Doyoukonw = ['/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[1]/span/a',
             '/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[2]/span/a',
             '/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[3]/span/a']
sick = ['/html/body/form/div[5]/div[3]/fieldset/div[10]/div[2]/div[1]/span/a',
        '/html/body/form/div[5]/div[3]/fieldset/div[10]/div[2]/div[2]/span/a']
sickwhat = ['/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[1]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[2]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[3]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[4]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[5]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[6]/span/a']
doctor = ['/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[1]/span/a',
          '/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[2]/span/a',
          '/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[3]/span/a']
science = ['/html/body/form/div[5]/div[3]/fieldset/div[13]/div[2]/div[1]/span/a',
           '/html/body/form/div[5]/div[3]/fieldset/div[13]/div[2]/div[2]/span/a']
join = ['/html/body/form/div[5]/div[3]/fieldset/div[14]/div[2]/div[1]/span/a',
        '/html/body/form/div[5]/div[3]/fieldset/div[14]/div[2]/div[2]/span/a']

doyouwant = ['/html/body/form/div[5]/div[3]/fieldset/div[5]/div[2]/div[1]/span/a',
             '/html/body/form/div[5]/div[3]/fieldset/div[5]/div[2]/div[2]/span/a']
whatpet = ['/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[1]/span/a',
           '/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[2]/span/a',
           '/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[3]/span/a',
           '/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[4]/span/a']
dontwant = ['/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[1]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[2]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[3]/span/a',
            '/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[4]/span/a']
note = ['问题太多了',
'......',
'，期待优惠',
'有促销吗',
'有打折吗嘻嘻嘻嘻',
'嘻嘻嘻',
'没意见',
'都挺好',
'11111',
'真的有活动？']

def Click(numnote):
    #options = webdriver.ChromeOptions()
    #num = random.randrange(0, len(user_agent))
    #options.add_argument(user_agent[num])
    #,chrome_options=options
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/m/59834653.aspx?from=singlemessage')
    driver.maximize_window()
    driver.implicitly_wait(10)#最多等待时间 页面加载时间
    #性别点击
    #sexnum = random.randrange(0,len(sex))
    sexnum = 1
    driver.find_element_by_xpath(sex[sexnum]).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    #年龄点击
    #agenum = random.randrange(0, len(age))
    agenum = 0
    driver.find_element_by_xpath(age[agenum]).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    #月收入
    #moneynum = random.randrange(0, len(money))
    moneynum = 1
    driver.find_element_by_xpath(money[moneynum]).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    #是否养过宠物  0-养过  1-没有
    #pet001num = random.randrange(0, len(pet001))
    pet001num = 0
    driver.find_element_by_xpath(pet001[pet001num]).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    if pet001num == 0:
        #养猫还是养狗
        #petdogcatnum = random.randrange(0, len(petdogcat))
        petdogcatnum = 0
        driver.find_element_by_xpath(petdogcat[petdogcatnum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #你了不了解宠物皮肤病常识
        #Doyoukonwnum = random.randrange(0, len(Doyoukonw))
        Doyoukonwnum = 2
        driver.find_element_by_xpath(Doyoukonw[Doyoukonwnum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #你的爱宠得过皮肤病吗
        #sicknum = random.randrange(0, len(sick))
        sicknum =0
        driver.find_element_by_xpath(sick[sicknum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #得了什么病
        #sickwhatnum = random.randrange(0, len(sickwhat))
        sickwhatnum = random.randint(0,1)
        if sicknum == 1:
            sickwhatnum = 5
        driver.find_element_by_xpath(sickwhat[sickwhatnum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #诊断是通过什么途径
        #doctornum = random.randrange(0, len(doctor))
        doctornum = 0
        driver.find_element_by_xpath(doctor[doctornum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #是否看过线上科普
        #sciencenum = random.randrange(0, len(science))
        sciencenum = 0
        driver.find_element_by_xpath(science[sciencenum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        #会不会参加
        #joinnum = random.randrange(0, len(join))
        joinnum = 0
        driver.find_element_by_xpath(join[joinnum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
    else:
        #是否有想养宠物的想法  0-想  1-不想
        doyouwantnum = random.randrange(0, len(doyouwant))
        driver.find_element_by_xpath(doyouwant[doyouwantnum]).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(0, 3))
        if doyouwantnum == 0:
            #你想养什么宠物
            whatpetnum = random.randrange(0, len(whatpet))
            driver.find_element_by_xpath(whatpet[whatpetnum]).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(0, 3))
        else:
            #为什么不想养
            dontwantnum = random.randrange(0, len(dontwant))
            driver.find_element_by_xpath(dontwant[dontwantnum]).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(0, 3))
    #15输入
    #driver.find_element_by_xpath('//*[@id="q15"]').send_keys(note[numnote])
    driver.find_element_by_xpath('//*[@id="q15"]').send_keys('无')
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    #提交
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(0, 3))
    driver.quit()

if __name__ == '__main__':
    for i in range(21):
        print("第%s次填写"%str(i))
        Click(i)


