
x = ['AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS']
print(len(x))
for i in range(1,14):
    enu = i-1
    a = x[enu] + "='/html/body/form/div[5]/div[3]/fieldset/div[" + str(i+2) + "]/div[2]/div[%s"+"]/span/a'"
    print(a)
# /html/body/form/div[5]/div[3]/fieldset/div[1]/div[2]/div[1]/span/a
# /html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[1]/span/a
# /html/body/form/div[5]/div[3]/fieldset/div[2]/div[2]/div[1]/span/a




