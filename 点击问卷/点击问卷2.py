from selenium import webdriver
import random
import time
AA = '//*[@id="divquestion1"]/ul/li[%s]/a'# 1-你的职业？
BB = '//*[@id="divquestion2"]/ul/li[%s]/a'# 2-你有宠物吗？
CC = '//*[@id="divquestion3"]/ul/li[%s]/a'# 3-如果没有,你想养吗？
DD ='//*[@id="divquestion4"]/ul/li[%s]/a'# 4-你家宠物是什么种类
EE ='//*[@id="divquestion5"]/ul/li[%s]/a'# 5-宠物年龄段
FF ='//*[@id="divquestion6"]/ul/li[%s]/a'#6-网上晒宠吗
GG ='//*[@id="divquestion7"]/ul/li[%s]/a'#7-每月开销
HH='//*[@id="divquestion8"]/ul/li[%s]/a'#8-定时打虫
II='//*[@id="divquestion9"]/ul/li[%s]/a'#9-花费最多的部分
JJ='//*[@id="divquestion10"]/ul/li[%s]/a'#10-购买渠道
KK='//*[@id="divquestion11"]/ul/li[%s]/a'#11购买注重品牌吗
LL='//*[@id="divquestion12"]/ul/li[%s]/a'#12购买哪个品牌
MM='//*[@id="divquestion13"]/ul/li[%s]/a'#13购买驱虫药品种
OO='//*[@id="divquestion14"]/ul/li[%s]/a'#14觉得消费高吗
PP='//*[@id="divquestion15"]/ul/li[%s]/a'#15有定期检查吗
QQ='//*[@id="divquestion16"]/ul/li[%s]/a'#16比较看重宠物医院那一部分
RR='//*[@id="divquestion17"]/ul/li[%s]/a'#17去医院感觉哪里不方便
SS='//*[@id="divquestion18"]/ul/li[%s]/a'#18多久洗澡
TT='//*[@id="divquestion19"]/ul/li[%s]/a'#19怎么洗护
UU='//*[@id="divquestion20"]/ul/li[%s]/a'#20美容服务态度满意吗
VV='//*[@id="divquestion21"]/ul/li[%s]/a'#21纯中药
WW='//*[@id="divquestion22"]/ul/li[%s]/a'#22回馈顾客
XX='//*[@id="divquestion23"]/ul/li[%s]/a'#23体检想什么优惠
YY='//*[@id="divquestion24"]/ul/li[%s]/a'#24有没买保险
ZZ='//*[@id="divquestion25"]/ul/li[%s]/a'#25会推荐吗
Aa='//*[@id="divquestion26"]/ul/li[%s]/a'#26线上科普参加吗
Bb='//*[@id="divquestion27"]/ul/li[%s]/a'#27希望提供哪种服务
Cc='//*[@id="divquestion28"]/ul/li[%s]/a'#28建议
note= [
'优惠优惠',
'线上有参与渠道吗',
'活动时间多久呀……',
'有啥活动？',
'哈哈哈',
'终于有活动了？',
'上网课，想秒杀',
'买保险的时候来啦'
]
# randomnum = int(random.randint(1, 3))
# randomlist = range(1, 4)
# wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
# for temp in wantnum:
#     JJnum = str(temp)
#     driver.find_element_by_xpath(JJ % JJnum).click()
#     driver.implicitly_wait(10)
#     time.sleep(random.uniform(0, 3))

def Click(NUM):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/jq/61195832.aspx')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    # 1-你的职业？
    #AAnum = str(random.randint(1,3))
    AAnumlist = ['2','3','5']
    AAnumONE = random.randint(0,2)
    AAnum = AAnumlist[AAnumONE]
    driver.find_element_by_xpath(AA%AAnum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    # 2-你有宠物吗？
    BBnum = str(random.randint(1, 2))
    BBnum = '1'
    driver.find_element_by_xpath(BB % BBnum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    # 3-如果没有,你想养吗？
    #CCnum = str(random.randint(1, 2))
    CCnum = NUM
    driver.find_element_by_xpath(CC % CCnum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    if CCnum == '2':
        pass#不想养
    else:
        # 4-你家宠物是什么种类
        DDnum = str(random.randint(2, 3))
        driver.find_element_by_xpath(DD % DDnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        # 5-宠物年龄段
        #EEnum = str(random.randint(1, 3))
        EEnum = '2'
        driver.find_element_by_xpath(EE % EEnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #6-网上晒宠吗
        #FFnum = str(random.randint(1, 4))
        FFnum = '1'
        driver.find_element_by_xpath(FF % FFnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #7-每月开销
        GGnum = str(random.randint(2, 3))
        driver.find_element_by_xpath(GG % GGnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #8-定时打虫
        #HHnum = str(random.randint(1, 3))
        HHnum = '1'
        driver.find_element_by_xpath(HH % HHnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #9-花费最多的部分
        IInum = str(random.randint(1, 2))
        driver.find_element_by_xpath(II % IInum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #10-购买渠道(多选）
        #manychoice(driver, 3, JJ)
        JJnum = '3'
        driver.find_element_by_xpath(JJ % JJnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #11购买注重品牌吗
        KKnum = str(random.randint(1, 2))
        driver.find_element_by_xpath(KK % KKnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #12购买哪个品牌
        manychoice(driver, 3, LL)
        #13购买驱虫药品种
        #manychoice(driver, 8, MM)
        MMnumlist = ['1', '3', '7']
        NOP = random.randint(1,3)
        randomlist = range(0, 3)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = MMnumlist[int(x)]
            driver.find_element_by_xpath(MM % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
        #14觉得消费高吗
        OOnum = str(random.randint(2, 3))
        driver.find_element_by_xpath(OO % OOnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #15有定期检查吗
        PPnum = str(random.randint(2, 3))
        driver.find_element_by_xpath(PP % PPnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #16比较看重宠物医院那一部分
        #manychoice(driver, 7, QQ)
        QQnumlist = ['1', '2', '4', '5']
        NOP = random.randint(1, 4)
        randomlist = range(0, 4)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = QQnumlist[int(x)]
            driver.find_element_by_xpath(QQ % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
        #17去医院感觉哪里不方便
        #manychoice(driver, 4, RR)
        RRnumlist = ['3', '5']
        NOP = random.randint(1, 2)
        randomlist = range(0, 2)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = RRnumlist[int(x)]
            driver.find_element_by_xpath(RR % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
        #18多久洗澡
        SSnum = str(random.randint(2, 3))
        driver.find_element_by_xpath(SS % SSnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #19怎么洗护
        #TTnum = str(random.randint(1, 3))
        TTnum = '1'
        driver.find_element_by_xpath(TT % TTnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #20美容服务态度满意吗
        #UUnum = str(random.randint(1, 3))
        UUnum = '2'
        driver.find_element_by_xpath(UU % UUnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #21纯中药
        #VVnum = str(random.randint(1, 4))
        VVnum = '3'
        driver.find_element_by_xpath(VV % VVnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #22回馈顾客
        #manychoice(driver, 5, WW)
        WWnumlist = ['1','4','5']
        NOP = random.randint(1, 3)
        randomlist = range(0, 3)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = WWnumlist[int(x)]
            driver.find_element_by_xpath(WW % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
        #23体检想什么优惠
        #manychoice(driver, 3, XX)
        XXnumlist = ['1', '4']
        NOP = random.randint(1, 2)
        randomlist = range(0, 2)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = XXnumlist[int(x)]
            driver.find_element_by_xpath(XX % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
        #24有没买保险
        #YYnum = str(random.randint(1, 2))
        YYnum = '2'
        driver.find_element_by_xpath(YY % YYnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #25会推荐吗
        #ZZnum = str(random.randint(1, 3))
        ZZnum = '2'
        driver.find_element_by_xpath(ZZ % ZZnum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #26线上科普参加吗
        #Aanum = str(random.randint(1, 2))
        Aanum = '2'
        driver.find_element_by_xpath(Aa % Aanum).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))
        #27希望提供哪种服务
        #manychoice(driver, 5, Bb)
        Bbnumlist = ['4', '5']
        NOP = random.randint(1, 2)
        randomlist = range(0, 2)
        wantnum = random.sample(randomlist, NOP)  # randomnum是你想随机想选出的个数
        for x in wantnum:
            num = Bbnumlist[int(x)]
            driver.find_element_by_xpath(Bb % num).click()
            driver.implicitly_wait(10)
            time.sleep(random.uniform(1, 2))
    #28建议
    # driver.find_element_by_xpath('//*[@id="q28"]').send_keys(note)
    # driver.implicitly_wait(10)
    # time.sleep(random.uniform(1, 2))
    # 提交
    driver.find_element_by_xpath('//*[@id="submit_button"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    driver.quit()

def manychoice(driver,i,a):
    randomnum = int(random.randint(1, i))
    randomlist = range(1, i+1)
    wantnum = random.sample(randomlist, randomnum)  # randomnum是你想随机想选出的个数
    for temp in wantnum:
        num = str(temp)
        driver.find_element_by_xpath(a % num).click()
        driver.implicitly_wait(10)
        time.sleep(random.uniform(1, 2))

if __name__ == '__main__':
    for i in range(30):
        try:
            t1 = time.time()
            Click('1')
            t2 = time.time()
            t3 = str(t2-t1)
            print("想养:第%s次填写,耗时：%s"%(str(i),t3))
        except Exception as e:
            print(e)
            continue
    for t in range(40):
        try:
            t1 = time.time()
            Click('2')
            t2 = time.time()
            t3 = str(t2 - t1)
            print("不想养:第%s次填写,耗时：%s" % (str(t), t3))
        except Exception as e:
            print(e)
            continue
