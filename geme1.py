import random
card_tuple=('李白','张飞','关羽','吕布','刘备')
packet=[]
while True:  
    a=int(input('''
氪金使我更强大！
请选择：            
1.抽卡
2.查看武将馆
3.整理武将馆
4.离开
'''))          
    if a == 1:
        num=int(input('输入抽卡次数'))
        for i in range(0,num):
             n = random.randint(0,4)
             print('恭喜你，抽到{}'.format(card_tuple[n]))
             packet.append(card_tuple[n])
        print('英雄已进入武将馆')  
    elif a == 2:
        print('武将馆中有{}'.format(packet))
    elif a == 3:
        print('正在整理背包，请等待')
        packet.sort()
    elif a == 4:             
        print('正在离开')
        break   