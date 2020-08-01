from selenium import webdriver
import random
import time

AA='/html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[%s]/span/a'
BB='/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[%s]/span/a'
CC='/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[%s]/span/a'
DD='/html/body/form/div[5]/div[3]/fieldset/div[4]/div[2]/div[%s]/span/a'
EE='/html/body/form/div[5]/div[3]/fieldset/div[5]/div[2]/div[%s]/span/a'
FF='/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[%s]/span/a'
GG='/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[%s]/span/a'
HH='/html/body/form/div[5]/div[3]/fieldset/div[8]/div[2]/div[%s]/span/a'
II='/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[%s]/span/a'
JJ='/html/body/form/div[5]/div[3]/fieldset/div[10]/div[2]/div[%s]/span/a'
KK='/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[%s]/span/a'
LL='/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[%s]/span/a'
MM='/html/body/form/div[5]/div[3]/fieldset/div[13]/div[2]/div[%s]/span/a'
NN='/html/body/form/div[5]/div[3]/fieldset/div[14]/div[2]/div[%s]/span/a'
OO='/html/body/form/div[5]/div[3]/fieldset/div[15]/div[2]/div[%s]/span/a'
PP='/html/body/form/div[5]/div[3]/fieldset/div[16]/div[2]/div[%s]/span/a'
QQ='/html/body/form/div[5]/div[3]/fieldset/div[17]/div[2]/div[%s]/span/a'
RR='/html/body/form/div[5]/div[3]/fieldset/div[18]/div[2]/div[%s]/span/a'

def Click(notenum):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/m/61723807.aspx?from=timeline')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间




#只适合单选题：当你只想固定选择一个选项的时候
def Justone(driver,num,listnum):
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#只适合单选题：当你想在几个选项里面随机选择
def Nornoal(driver,numone,numtwo,listnum):
    thenum = str(random.randint(numone,numtwo))
    driver.find_element_by_xpath(listnum%thenum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#只适合单选题：选择哪个几个
def Choose(driver,islist,listnum):
    randomnum = int(random.randint(0, len(islist)-1))
    num = islist[randomnum]
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

def Manychoice(driver,i,listnum):
    randomnum = int(random.randint(1, i))
    randomlist = range(1, i+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
        driver.find_element_by_xpath(listnum % num).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))

def Cmanychoice(driver,islist,listnum):
    randomnum = int(random.randint(1, len(islist)))
    randomlist = range(1, len(islist)+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
        driver.find_element_by_xpath(listnum % num).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))