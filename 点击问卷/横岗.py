from selenium import webdriver
import random
import time

AA = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[1]/div[2]/ul/li[%s]/a'# 1-你的爱宠是？
BB = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[2]/div[2]/ul/li[%s]/a'# 2-是否绝育？
CC = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[3]/div[2]/ul/li[%s]/a'# 3-花费？
DD = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[4]/div[2]/ul/li[%s]/a'# 4-你家宠物是什么种类
EE = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[5]/div[2]/ul/li[%s]/a'
FF = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[6]/div[2]/ul/li[%s]/a'
GG = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[7]/div[2]/ul/li[%s]/a'
HH = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[8]/div[2]/ul/li[%s]/a'
II = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[9]/div[2]/ul/li[%s]/a'
JJ = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[10]/div[2]/ul/li[%s]/a'
KK = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[11]/div[2]/ul/li[%s]/a'
LL = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[12]/div[2]/ul/li[%s]/a'
MM = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[13]/div[2]/ul/li[%s]/a'
NN = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[14]/div[2]/ul/li[%s]/a'
OO = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[15]/div[2]/ul/li[%s]/a'
PP = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[16]/div[2]/ul/li[%s]/a'
note1=[
'驱虫有连续性的活动吗？',
'会员充值有送吗？',
'礼品能安排上来吗？',
'想要体检活动',
'皇家的主粮多点优惠啦',
'期待更多洗浴活动',
'有治疗皮肤病的药疗保健吗？',
'希望有绝育套餐上线',
'有幼猫的活动的？',
'想要绝育免单啦',
'洗澡洗澡',
'什么时候有讲座呀，相同有关心脏病的',
'狗狗骨折了',
'嘻嘻嘻',
'没有太多的建议，多点活动把',
'线上有商城吗？',
'你们有社群吗？想进去听知识',
'洗浴优惠',
'疫苗有优惠吗？',
'有充送活动吗？',
'大转盘我喜欢玩',
'买狗粮有优惠吗？',
'希望有义诊',
'有小宠物卖吗？',
'有秒杀活动？',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','','','','','','','','','','','',''
]

def Click(notenum):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/jq/62041871.aspx')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    #1-你的爱宠是？
    Nornoal(driver,1,2,AA)
    #Justone(driver,2,AA)
    #2-是否绝育？
    Nornoal(driver, 1, 2, BB)
    #Justone(driver, 1, BB)
    #3-每月对您家爱宠的开销范围是？
    Nornoal(driver, 1, 4, CC)
    #Justone(driver, 2, CC)
    #4.通常花费在哪方面？
    Nornoal(driver, 1, 6, DD)
    #Justone(driver, 1, DD)
    #5.您家爱宠会为您家爱宠选用的粮食品牌是？
    Manychoice(driver, 9, EE)
    #Manychoiceok(driver, 4, 6, 3, EE)
    #6.您多久会为您家爱宠做一次驱虫？
    Nornoal(driver, 1, 5, FF)
    #Justone(driver, 1, FF)
    # 7.您通常选用的驱虫药是？
    Nornoal(driver, 1, 6, GG)
    #Justone(driver, 1, GG)
    # 8.您一般选择的购买渠道是什么？
    Manychoice(driver, 5, HH)
    #Manychoiceok(driver, 3, 4, 2, HH)
    #9您会定期带宠物去做体检吗？
    Nornoal(driver, 1, 4, II)
    #Justone(driver, 3, II)
    # 10如果做体检最想体检的项目是？
    Nornoal(driver, 1, 5, JJ)
    #Justone(driver, 2, JJ)
    #11多久洗一次澡？
    Nornoal(driver, 1, 6, KK)
    #Justone(driver, 5, KK)
    # 12您的爱宠洗护方面偏向于哪种？
    Nornoal(driver, 1, 3, LL)
    #Justone(driver, 3, LL)
    # 13您对宠物SPA有了解吗？
    Nornoal(driver, 1, 3, MM)
    #Justone(driver, 1, MM)
    # 14.我院的店庆活动哪方面是您最感兴趣的？
    Manychoice(driver, 9, NN)
    #Manychoiceok(driver, 6, 8, 3, NN)
    #15  针对饲养宠物的线上科普您会积极参与吗？
    Nornoal(driver, 1, 2, OO)
    #Justone(driver, 1, OO)
    # 16.您是否愿意为您家爱宠购买宠物保险？
    Nornoal(driver, 1, 2, PP)
    #Justone(driver, 1, PP)
    # 15输入
    # driver.find_element_by_xpath('//*[@id="q17"]').send_keys(note1[notenum])
    # driver.implicitly_wait(10)
    # time.sleep(random.uniform(0, 3))
    #提交
    driver.find_element_by_xpath('//*[@id="submit_button"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    driver.quit()

def Justone(driver,num,listnum):
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

def Nornoal(driver,numone,numtwo,listnum):
    #numone~numtwo哪个选项到哪个选项
    thenum = str(random.randint(numone,numtwo))
    driver.find_element_by_xpath(listnum%thenum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

def Manychoiceok(driver,one,two,wantnum,listnum):
    randomnum = int(random.randint(1, wantnum))
    randomlist = range(one, two+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
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

if __name__ == '__main__':
    for i in range(41):#输入数字
        try:
            t1 = time.time()
            Click(i)
            t2 = time.time()
            t3 = str(t2 - t1)
            print("想养:第%s次填写,耗时：%s" % (str(i), t3))
        except Exception as e:
            print(e)
            continue
