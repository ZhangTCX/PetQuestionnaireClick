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
QQ = '/html/body/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[2]/fieldset/div[17]/div[2]/ul/li[%s]/a'
note1 = [
'想对一点科普的信息',
'十分期待这个活动',
'什么时候的店庆？',
'皮肤病治疗有优惠吗？',
'小猫咪不愿意洗澡有法子吗？',
'有没有绝育的套餐呀？',
'商品有没有搭配的套餐呢？',
'想要洗浴优惠',
'终于来了，期待活动',
'希望美容折扣颤动起来',
'有线上活动吗？',
'驱虫的活动来一打',
'三折算骨折吗？如果是，请给我一打',
'美容服务能再好一点嘛？',
'牙齿有活动吗？想去洗洗牙',
'在线等活动',
'希望我选的都被选上',
'充值活动',
'有礼品送吗？',
'多点优惠，没有工作又不舍得穷养',
'有免单活动吗？',
'抽奖活动',
'可以多一点宣传科普的？',
'','','','','',
'','','','','',
'','','','','',
'','','','','',
'','','','',''
]

def Click(notenum):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/jq/62351242.aspx')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    #1-你的爱宠是？
    Nornoal(driver,1,2,AA)
    #Justone(driver,1,AA)
    #2-是否绝育？
    Nornoal(driver, 1, 2, BB)
    #Justone(driver,1, BB)
    #3-每月对您家爱宠的开销范围是？
    Nornoal(driver, 1, 4, CC)
    #Justone(driver,2, CC)
    #4.通常花费在哪方面？
    Nornoal(driver, 1, 6, DD)
    #Justone(driver,1, DD)
    #5.您家爱宠会为您家爱宠选用的粮食品牌是？
    Nornoal(driver, 1, 9, EE)
    #Justone(driver,4, EE)
    #6.您多久会为您家爱宠做一次驱虫？
    Nornoal(driver, 1, 5, FF)
    #Justone(driver,1, FF)
    # 7.您通常选用的驱虫药是？
    Nornoal(driver, 1, 6, GG)
    #Justone(driver, 5, GG)
    # 8.您一般选择的购买渠道是什么？
    Nornoal(driver, 1, 5, HH)
    #Justone(driver, 4, HH)
    #9您会定期带宠物去做体检吗？
    Nornoal(driver, 1, 4, II)
    #Justone(driver, 4, II)
    # 10如果做体检最想体检的项目是？
    Nornoal(driver, 1, 5, JJ)
    #Justone(driver, 2, JJ)
    #11如果做体检最想体检的项目是？
    Manychoice(driver, 5, KK)
    #Justone(driver, 5, KK)
    # 12您的爱宠洗护方面偏向于哪种？
    Nornoal(driver, 1, 3, LL)
    #Justone(driver, 3, LL)
    # 13您对宠物SPA有了解吗？
    Nornoal(driver, 1, 3, MM)
    #Justone(driver, 2, MM)
    # 14.希望宠物医院提供哪种服务？
    Nornoal(driver, 1, 5, NN)
    #Justone(driver, 5, NN)
    #15  我院的店庆活动哪方面是您最感兴趣的？
    Manychoice(driver, 4, OO)
    # 16.针对饲养宠物的线上科普您会积极参与吗？
    Nornoal(driver, 1, 2, PP)
    #Justone(driver, 1, PP)
    # 17.希您是否愿意为您家爱宠购买宠物保险？
    Nornoal(driver, 1, 2, QQ)
    #Justone(driver, 1, QQ)
    # 15输入
    # driver.find_element_by_xpath('//*[@id="q18"]').send_keys(note1[notenum])
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
    # AAnum = str(random.randint(1,3))
    # driver.find_element_by_xpath(AA%AAnum).click()
    # driver.implicitly_wait(10)
    # time.sleep(random.uniform(1, 2))

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
    for i in range(26):#输入数字
        try:
            t1 = time.time()
            Click(i)
            t2 = time.time()
            t3 = str(t2 - t1)
            print("想养:第%s次填写,耗时：%s" % (str(i), t3))
        except Exception as e:
            print(e)
            continue
