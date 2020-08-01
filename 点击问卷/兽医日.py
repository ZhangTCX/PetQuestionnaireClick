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

def Click():
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/m/66568013.aspx?from=timeline')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    # 1-你的职业是？
    Choose(driver, [1,2], AA)
    # 2-你是否养宠物？
    Justone(driver, 1, BB)
    # 3-你对宠物知识的了解程度？
    Nornoal(driver, 2, 3, CC)
    # 4、您是否会主动去了解宠物相关的知识？
    Justone(driver, 2, DD)
    # 5、您在关注爱宠健康知识方面，主要来源于那些渠道?
    Cmanychoice(driver, [1,2,4], EE)
    # 6、您在学习宠物健康知识时，一般倾向于那种形式?
    Cmanychoice(driver,[2,3,4], FF)
    # 7、疫情期间，爱宠生病了怎么办?
    Cmanychoice(driver, [2,4], GG)
    # 8、您平时在与宠物相处的过程中，是否注重“人畜共患”问题?
    Choose(driver, [1, 3], HH)
    # 9、如果联合宠物医院开展一系列饲养宠物健康科普，您是否会参与?
    Justone(driver, 1, II)
    # 10、如果开展宠物健康科普，您会关注那些方面?
    Manychoice(driver, 5, JJ)
    # 11、如果宠物医院开展一系列饲养宠物健康科普，你更乐意通过那种渠道参与?
    Manychoice(driver, 3, KK)
    # 提交
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    driver.quit()

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

if __name__ == '__main__':
    for i in range(63):#输入数字
        try:
            t1 = time.time()
            Click()
            t2 = time.time()
            t3 = str(t2 - t1)
            print("想养:第%s次填写,耗时：%s" % (str(i), t3))
        except Exception as e:
            print(e)
            continue


















