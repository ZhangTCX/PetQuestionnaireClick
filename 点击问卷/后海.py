from selenium import webdriver
import random
import time

AA="/html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[%s]/span/a"
BB="/html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[%s]/span/a"
CC="/html/body/form/div[5]/div[3]/fieldset/div[3]/div[2]/div[%s]/span/a"

DD="/html/body/form/div[5]/div[3]/fieldset/div[4]/div[2]/div[%s]/span/a"

EE="/html/body/form/div[5]/div[3]/fieldset/div[5]/div[2]/div[%s]/span/a"
FF="/html/body/form/div[5]/div[3]/fieldset/div[6]/div[2]/div[%s]/span/a"
GG="/html/body/form/div[5]/div[3]/fieldset/div[7]/div[2]/div[%s]/span/a"
HH="/html/body/form/div[5]/div[3]/fieldset/div[8]/div[2]/div[%s]/span/a"
II="/html/body/form/div[5]/div[3]/fieldset/div[9]/div[2]/div[%s]/span/a"
JJ="/html/body/form/div[5]/div[3]/fieldset/div[10]/div[2]/div[%s]/span/a"
KK="/html/body/form/div[5]/div[3]/fieldset/div[11]/div[2]/div[%s]/span/a"
LL="/html/body/form/div[5]/div[3]/fieldset/div[12]/div[2]/div[%s]/span/a"
MM="/html/body/form/div[5]/div[3]/fieldset/div[13]/div[2]/div[%s]/span/a"
NN="/html/body/form/div[5]/div[3]/fieldset/div[14]/div[2]/div[%s]/span/a"
OO="/html/body/form/div[5]/div[3]/fieldset/div[15]/div[2]/div[%s]/span/a"
PP="/html/body/form/div[5]/div[3]/fieldset/div[16]/div[2]/table/tbody/tr[2]/td[%s]/a"
QQ="/html/body/form/div[5]/div[3]/fieldset/div[17]/div[2]/div[%s]/span/a"
RR="/html/body/form/div[5]/div[3]/fieldset/div[18]/div[2]/div[%s]/span/a"
note1 =[
'优惠能多一点吗？',
'怎么预约？',
'有没有洗澡卡？',
'充送活动可以有',
'人手不足，每次去都是等好久',
'医生服务很好，我家猫猫很喜欢',
'抽奖活动有吗？',
'可以预约了吗？',
'美团的绝育套餐可以周三约吗？',
'免单活动想要',
'有科普的讲座或者视频就可',
'太贵了，想多一点优惠，给我家仔做个美容',
'体检优惠来一个？',
'美容服务有吗？',
'什么驱虫药比较好？英短',
'建议多一点套餐，这样就不用每次都介绍，最后是半年那种',
'我家辣条是不是可以释放自己就看这次店庆促销力度了',
'不能出门，可以线上预约体检吗？',
'想跟朋友组团购买主粮，有拼团活动可完美',
'啥时候可以去看看饺子就看优惠够不够']

def Click(notenum):
    driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('https://www.wjx.cn/m/61723807.aspx?from=timeline')
    driver.maximize_window()
    driver.implicitly_wait(10)  # 最多等待时间 页面加载时间
    #1、你的职业
    Nornoal(driver,1,3,AA)
    #2、你有宠物吗？
    Justone(driver,1,BB)
    #3、你家宠物是哪一类？
    Nornoal(driver,1,2,CC)
    #5、花费多少？
    Nornoal(driver, 1,3, EE)
    #7、花费最多的？
    Nornoal(driver, 1,3, FF)
    #6、是否驱虫？
    Nornoal(driver, 1,3, GG)
    #8、主粮品牌？
    Justone(driver, 2, HH)
    #9、驱虫药品牌？
    Nornoal(driver,1, 4, II)
    #10、购买渠道？
    Nornoal(driver, 1,6,JJ)
    # 11、网店优势？
    Manychoice(driver, 3, KK)
    # 12、定期体检？
    Nornoal(driver, 1, 3, LL)
    # 13、看重医院什么？
    Manychoice(driver, 4, MM)
    # 14、消费不满意的地方？
    Manychoice(driver, 2, NN)
    # 15、周年庆怎么动心？
    Manychoice(driver, 2, OO)
    # 16、点赞？
    Nornoal(driver,1, 5, PP)
    # 17、会积极参加吗？
    Nornoal(driver,1, 3, QQ)
    # 18、会积极参加吗？
    Manychoice(driver, 5, RR)
    # 19输入
    # driver.find_element_by_xpath('//*[@id="q19"]').send_keys(notenum)
    # driver.implicitly_wait(10)
    # time.sleep(random.uniform(0, 3))
    # 提交
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))
    driver.quit()
#只选一个的方法  单选
def Justone(driver,num,listnum):
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#选择哪个几个的方法 单选
def onetwo(driver,islist,listnum):
    randomnum = int(random.randint(0, len(islist)-1))
    num = islist[randomnum]
    driver.find_element_by_xpath(listnum % num).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#正常排序选择  单选
def Nornoal(driver,numone,numtwo,listnum):
    #numone~numtwo哪个选项到哪个选项
    thenum = str(random.randint(numone,numtwo))
    driver.find_element_by_xpath(listnum%thenum).click()
    driver.implicitly_wait(10)
    time.sleep(random.uniform(1, 2))

#多选
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
    for i in range(45):
        try:
            t1 = time.time()
            Click(i)
            t2 = time.time()
            t3 = str(t2 - t1)
            print("第%s份已填写,耗时：%s" % (str(i), t3))
        except Exception as e:
            print(e)
            continue
