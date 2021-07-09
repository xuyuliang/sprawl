import random
# 被调用的随机函数，它将产生30%的英明决策率，70%的傻逼率
def generate_decision():
    d = random.randint(1, 10000)
    # 所以概率上，得到1的概率是30%，我们假定获得1是获得了英明判断
    if d >= 7000:
        return 1
    else:
        return 0



good = 0 #用来放英明判断的计数
# 让业委会的3个成员做1000次决策并投票



for i in range(1000):
    a = generate_decision() #业委会成员A
    b = generate_decision() #业委会成员B
    c = generate_decision() #业委会成员C
    d = generate_decision() #业委会成员d
    e = generate_decision() #业委会成员e
    if a + b + c + d + e >= 3 : #如果投票结果是英明的
        good = good + 1

print('英明率：',good/1000)
good = 0 # 重置；以防万一，让天降伟人在同等环境下做一次对比
for i in range(1000):
    w = generate_decision() #天降伟人独立判断
    if w == 1:
        good = good + 1
print('英明率：',good/1000)
