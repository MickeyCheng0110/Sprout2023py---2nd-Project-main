import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import random 

class Player: #玩家
    '''
    輸入名字
    '''
    def __init__(self, name):
        self.defend = random.randint(5,10)
        self.attact = random.randint(10,15)
        self.health = 100 
        self.lv = 1
        self.flv = 1
        self.equ=[]
        self.name = name
        self.live = 'alive'
    def ability(self):
        return f'名字 : {self.name}   等級 : {self.lv}\n-----------------------------\n你的血量是 : {self.health}\n你的防禦力是 : {self.defend} \n你的攻擊力是 : {self.attact}\n============================\n\n'
    
class Bow: #武器
    '''
    輸入等級
    '''
    def __init__(self, Lv):
        self.AD = '攻擊力: Lv+(1~4)隨機取數 防禦力: 0   先攻'
        self.type = 2
        self.attact = random.randint(1+Lv,4+Lv)
        self.defend = 0
        self.name = '弓'

class sword: #武器
    '''
    輸入等級
    '''
    def __init__(self, Lv):
        self.AD = '攻擊力: Lv+(2~5)隨機取數    防禦力: Lv+(2~4)隨機取數   後攻'
        self.type = 1
        self.defend = random.randint(2+Lv,4+Lv)
        self.attact = random.randint(2+Lv,5+Lv)
        self.name = '劍'

class knife: #武器
    '''
    輸入等級
    '''
    def __init__(self, Lv):
        self.AD = '攻擊力: Lv+(4~8)隨機取數    防禦力: Lv+(1~3)隨機取數   後攻'
        self.type = 1
        self.defend = random.randint(1+Lv,3+Lv)
        self.attact = random.randint(4+Lv,8+Lv)
        self.name = '小刀'
 
class shield: #武器
    '''
    輸入等級
    '''
    def __init__(self, Lv):
        self.AD = '攻擊力: 0~1                 防禦力: Lv+(4~7)隨機取數   後攻'
        self.type = 1
        self.defend = random.randint(4+Lv,7+Lv)
        self.attact = random.randint(0,1)
        self.name = '盾牌'

class Tachi: #武器
    '''
    輸入等級
    '''
    def __init__(self, Lv):
        self.AD = '攻擊力: Lv+(3~6)隨機取數    防禦力: Lv+(3~6)隨機取數   後攻'
        self.type = 1
        self.defend = random.randint(3+Lv,6+Lv)
        self.attact = random.randint(3+Lv,6+Lv)
        self.name = '太刀'

def chose_equ(Lv) : #選武器 
    '''
    輸入等級
    輸出是串列
    '''
    weapons=[Bow(Lv), sword(Lv), knife(Lv), shield(Lv), Tachi(Lv)]
    equ = []
    for i in range(4) :
        equ.append(weapons[i])

    return equ

class 蠃鱼: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(3+lv,8+lv)
        self.attact = random.randint(7+lv,11+lv)
        self.health = random.randint(4+lv,6+lv)
        self.name = '蠃鱼'
        self.life = 'alive' 
        self.intro = '蠃鱼擁有水的祝福，水會不斷地為他加持'
    def dead(self, Player1, round, amonster):
        return '蠃鱼翻肚了'
    def round(self, Player1, round, amonster) :
        if round > 1 :
            self.defend += 1 
            return '蠃鱼使用蓄勢 防禦力+1'
        return '蠃鱼休息了一下'

class 白虎: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(6+lv,11+lv)
        self.attact = random.randint(6+lv,11+lv)
        self.health = random.randint(7+lv,12+lv)
        self.intro = '白虎迅捷如風，在一開始接觸時常被打的措手不及'
        self.name = '白虎'
        self.life = 'alive' 
    def dead(self, Player1, round, amonster):
        return '白虎大吼一聲......虎沒了'
    def round(self, Player1, round, amonster) :
        if round == 1 :
            self.attact += 5
            return  '白虎發動技能 迅風 攻擊力+5'
        elif round == 2 :
            self.attact -= 5
            return  '白虎技能效果消失'
        else :
            return '白虎偷懶了一下     '
class 小波: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(2+lv,5+lv)
        self.attact = random.randint(3+lv,5+lv)
        self.health = random.randint(5+lv,7+lv)
        self.intro = '這是一隻小波'
        self.name = '小波'
        self.life = 'alive' 
    def dead(self, Player1, round, amonster):
        return '來我們跟小波說再見!  再～見～'
    def round(self, Player1, round, amonster) :
            return '小波做好了戰鬥準備'    
class 苦力怕: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(1+lv,3+lv)
        self.attact = random.randint(1+lv,3+lv)
        self.health = random.randint(10+lv,14+lv)
        self.explore = random.randint(2,4)
        self.bomb = 0
        self.intro = 'creeper? ~oh~man'
        self.name = '苦力怕'
        self.life = 'alive' 
    def dead(self, Player1, round, amonster):
        if self.bomb == 0 :
            return '斯~'
        else :
            return '嘶~~~~~蹦~'
    def round(self, Player1, round, amonster) :
        if round == self.explore :
            return f'嘶~~~~~~\n{Player1.name} :我有一種不祥的預感'
        elif round == self.explore+1 :
            Player1.health -= self.attact*2
            self.bomb = 1
            return f'你受到苦力怕的{self.attact*2}點自爆傷害'
        else :
            return '苦力怕向你走來'

class 鳳凰: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(5+lv,8+lv)
        self.attact = random.randint(3+lv,7+lv)
        self.health = random.randint(10+lv,15+lv)
        self.halfhealth = self.health//2
        self.name = '鳳凰'
        self.live2 = 1
        self.life = 'alive' 
        self.intro = '鳳凰擁有鳳凰火，會浴火重生'
    def dead(self, Player1, round, amonster):
        if self.live2 == 1 :
          self.health = self.halfhealth
          return f'鳳凰使用技能 : 浴火重生\n血量回復{self.halfhealth}'
          self.live2 = 0
    def round(self, Player1, round, amonster) :
        return '鳳凰在天空翱翔'   

class 草精靈: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(3+lv,5+lv)
        self.attact = random.randint(1+lv,2+lv)
        self.health = random.randint(6+lv,8+lv)
        self.name = '草精靈'
        self.life = 'alive' 
        self.intro = '草精靈擅長治癒'
    def dead(self, Player1, round, amonster):
        return f'呀~~~'
    def round(self, Player1, round, amonster) :
        if round > 1 :
            amonster.health += self.attact
            return f'草精靈幫隊友回復了{self.attact}點血量'
        else :
            return '草精靈拿起了鈴鼓'

class 克洛格: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(8+lv,12+lv)
        self.attact = random.randint(4+lv,7+lv)
        self.health = random.randint(6+lv,8+lv)
        self.friend = 'alive'
        self.name = '克洛格'
        self.life = 'alive' 
        self.intro = '克洛格: 克洛格想要找到他的朋友'
    def dead(self, Player1, round, amonster):
        return f'呀哈哈~~~~'
    def round(self, Player1, round, amonster) :
        if amonster.life == 'Dead' and self.friend == 'alive':
            self.friend = 'Dead'
            attack_up = random.randint(8+Player1.lv,12+Player1.lv)
            self.attact += attack_up
            return f'當克洛格發現他的朋友沒了時，他非常的生氣\n攻擊力上升{attack_up}點'
        else :
            if round == 1 :
                return '克洛格: 我的朋友在那邊你可以帶我去找他嗎?'
            else :
                return  '克洛格: 呀哈哈~!' 
class 蒼鷹: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(3+lv,4+lv)
        self.attact = random.randint(5+lv,8+lv)
        self.health = random.randint(6+lv,8+lv)
        self.intro = '翱翔於天空的蒼鷹，不是好欺負的'
        self.name = '蒼鷹'
        self.life = 'alive' 
    def dead(self, Player1, round, amonster):
        return '蒼鷹如流星般的墜落到了地上'
    def round(self, Player1, round, amonster) :
        a = random.randint(1,4)
        if a == 1 :
          return f'蒼鷹招來了旋風，你受到{self.attact}點傷害'
        else :
          return '蒼鷹在天上盤旋'

class 頑皮猴: #敵人
    '''
    輸入等級
    '''
    def __init__(self, lv) :
        self.defend = random.randint(2+lv,4+lv)
        self.attact = random.randint(4+lv,6+lv)
        self.health = random.randint(5+lv,7+lv)
        self.intro = '頑皮猴，顧名思義就是頑皮的猴子'
        self.name = '頑皮猴'
        self.life = 'alive' 
    def dead(self, Player1, round, amonster):
        return '頑皮猴從樹上掉了下來'
    def round(self, Player1, round, amonster) :
        a = random.randint(1,2)
        if a == 1 :
          return f'頑皮猴偷襲了你，你受到{self.attact//2}點傷害'
        else :
          return '頑皮猴在樹中穿梭'
          
               

def summon(lv) :
    monster = [蠃鱼, 白虎, 小波, 苦力怕, 鳳凰, 草精靈, 克洛格, 蒼鷹]
    a = random.randint(0,len(monster)-1)
    return monster[a](lv)
    


class Adventure(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.start = 0
        pass
        
    
    @commands.command()
    async def adv_intro(self, ctx):
        await ctx.send('遊戲內有以下指令:')
        await ctx.send('1.$Start : 創造角色 輸入格視為($Start 角色名字)')
        await ctx.send('2.$fight 開始一場戰鬥 只需輸入($Fight)(請不要在戰鬥中再次輸入此指令)')
        await ctx.send('3.$attack 在已開始戰鬥時輸入 輸入格式為: 目標(數字),武器編號(數字)')
        await ctx.send('4.$defend 加防禦(5點)換武器 後面不用輸入任何東西')
        await ctx.send('5.$lvup 在打贏時可以用來提升玩家屬性')
        await ctx.send('6.若沒有武器就無法攻擊只能防禦')
        await ctx.send('7.先攻 : 如果攻擊足夠打死對方則不用受到該目標造成的傷害  後攻則必須承受傷害')
        await ctx.send('\n-----------------------------\n')
        await ctx.send('以下是武器列表 : \n1.弓 攻擊力: Lv+(1~4)隨機取數 防禦力: 0   先攻')
        await ctx.send('2. 劍   攻擊力: Lv+(2~5)隨機取數    防禦力: Lv+(2~4)隨機取數   後攻')
        await ctx.send('3. 小刀 攻擊力: Lv+(4~8)隨機取數    防禦力: Lv+(1~3)隨機取數   後攻')
        await ctx.send('4. 盾牌 攻擊力: 0~1                 防禦力: Lv+(4~7)隨機取數   後攻')
        await ctx.send('5. 太刀 攻擊力: Lv+(3~6)隨機取數    防禦力: Lv+(3~6)隨機取數   後攻')
        await ctx.send('\n-----------------------------\n')


    @commands.command()
    async def start(self, ctx, item): #製造角色
        self.Player1 = Player(item)
        await ctx.send(self.Player1.ability())
        self.Player1.equ = chose_equ(self.Player1.lv)
        await ctx.send('你擁有的武器有')
        for i in range(4) :
            await ctx.send(f'{i+1} : {self.Player1.equ[i].name} {self.Player1.equ[i].AD}')
        self.Start = 1
        self.kill = 0
        self.ad = 0
    
    @commands.command() # 確認裝備
    async def checkequ(self, ctx): 
        await ctx.send('你擁有的武器有')
        for i in range(len(self.Player1.equ)) :
            await ctx.send(f'{i+1} : {self.Player1.equ[i].name} {self.Player1.equ[i].AD}')



        pass 
    @commands.command()
    async def fight(self, ctx): #製造怪物
        if self.Player1.live == 'alive' :
            self.Start = 1
            self.Monster1 = summon(self.Player1.lv)
            self.Monster2 = summon(self.Player1.lv)
            self.round = 1
            await ctx.send(self.Monster1.round(self.Player1, self.round, self.Monster2))
            await ctx.send(self.Monster2.round(self.Player1, self.round, self.Monster1))
            await ctx.send(f'名字 : {self.Monster1.name}   目標1號  狀態:{self.Monster1.life}\n-----------------------------\n血量是 : {self.Monster1.health}\n防禦力是 : {self.Monster1.defend} \n攻擊力是 : {self.Monster1.attact}\n{self.Monster1.intro}\n============================\n')
            await ctx.send(f'名字 : {self.Monster2.name}   目標2號  狀態:{self.Monster2.life}\n-----------------------------\n血量是 : {self.Monster2.health}\n防禦力是 : {self.Monster2.defend} \n攻擊力是 : {self.Monster2.attact}\n{self.Monster2.intro}\n============================\n')
            await ctx.send('你有兩個選擇 : \n1.攻擊 (輸入$attack 目標，武器(請輸入數字(以英文逗號分隔  EX: $attack 1,1\n2.防禦 (輸入$defend)')
            self.ad += 1
        else :
            await ctx.send('未創立角色')

    @commands.command()
    async def attack(self, ctx, item): #計算造成傷害和受到傷害
        if self.Start == 1 and len(self.Player1.equ) > 0:   
            await ctx.send(f'回合:{self.round}')
            a = list(map(str,item.split(',')))
            weapon = int(a[1])-1
            attack = self.Player1.attact + self.Player1.equ[weapon].attact
            if self.Player1.equ[weapon].type == 1 :
                if a[0] == '1' :
                    if self.Monster1.life == 'alive' :
                        if self.Monster1.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster1.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster1.name}造成的{self.Monster1.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster1.name}造成的1點傷害')
                    if self.Monster2.life == 'alive' :
                        if self.Monster2.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster2.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster2.name}造成的{self.Monster2.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster2.name}造成的1點傷害')
                    if attack > self.Monster1.defend :
                        self.Monster1.health-=attack-self.Monster1.defend
                        await ctx.send(f'對{self.Monster1.name}造成{attack-self.Monster1.defend}點傷害')
                    else :
                        self.Monster1.health-=1
                        await ctx.send(f'對{self.Monster1.name}造成1點傷害')
                if a[0] == '2' :
                    if self.Monster1.life == 'alive' :
                        if self.Monster1.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster1.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster1.name}造成的{self.Monster1.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster1.name}造成的1點傷害')
                    if self.Monster2.life == 'alive' :    
                        if self.Monster2.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster2.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster2.name}造成的{self.Monster2.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster2.name}造成的1點傷害')
                    if attack > self.Monster2.defend :
                        self.Monster2.health-=attack-self.Monster2.defend
                        await ctx.send(f'對{self.Monster2.name}造成{attack-self.Monster2.defend}點傷害')
                    else :
                        self.Monster2.health-=1
                        await ctx.send(f'對{self.Monster2.name}造成1點傷害')
            if self.Player1.equ[weapon].type == 2 :
                if a[0] == '1' :
                    if attack > self.Monster1.defend :
                        self.Monster1.health-=attack-self.Monster1.defend
                        await ctx.send(f'對{self.Monster1.name}造成{attack-self.Monster2.defend}點傷害')
                    else :
                        self.Monster1.health-=1
                        await ctx.send(f'對{self.Monster1.name}造成1點傷害')
                    if self.Monster1.health > 0 :
                        if self.Monster1.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster1.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster1.name}造成的{self.Monster1.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Player1.name}造成的1點傷害')
                    if self.Monster2.health > 0 :    
                        if self.Monster2.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster2.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster2.name}造成的{self.Monster2.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Player1.name}造成的1點傷害')
                if a[0] == '2' :
                    if attack > self.Monster2.defend :
                        self.Monster2.health-=attack-self.Monster2.defend
                        await ctx.send(f'對{self.Monster2.name}造成{attack-self.Monster2.defend}點傷害')
                    else :
                        self.Monster2.health-=1
                        await ctx.send(f'對{self.Monster2.name}造成1點傷害')
                    if self.Monster2.health > 0 : 
                        if self.Monster2.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster2.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster2.name}造成的{self.Monster2.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster2.name}造成的1點傷害')
                    if self.Monster1.health > 0 :    
                        if self.Monster1.attact > self.Player1.defend :
                            self.Player1.health-=self.Monster1.attact-self.Player1.defend
                            await ctx.send(f'受到{self.Monster1.name}造成的{self.Monster1.attact-self.Player1.defend}點傷害')
                        else :
                            self.Player1.health-=1
                            await ctx.send(f'受到{self.Monster1.name}造成的1點傷害')
            self.round += 1
            if self.Monster1.health > 0 :
                await ctx.send(self.Monster1.round(self.Player1, self.round, self.Monster2))
            if self.Monster2.health > 0 :
                await ctx.send(self.Monster2.round(self.Player1, self.round, self.Monster1)) 
            if self.Monster1.health < 1 and self.Monster1.life == 'alive':  #怪物是否死亡
                await ctx.send(self.Monster1.dead(self.Player1, self.round, self.Monster2))
                if self.Monster1.health < 1 and self.Monster1.life == 'alive':
                    self.Monster1.life = 'Dead'
                    self.Monster1.health = 0
                    await ctx.send(f'{self.Monster1.name}升天了')
                    self.kill += 1
            if self.Monster2.health <= 0 and self.Monster2.life == 'alive':  #怪物是否死亡
                await ctx.send(self.Monster2.dead(self.Player1, self.round, self.Monster1))
                if self.Monster2.health <= 0 and self.Monster1.life == 'alive':
                    self.Monster2.life = 'Dead'
                    self.Monster2.health = 0
                    await ctx.send(f'{self.Monster2.name}升天了')
                    self.kill += 1
            self.Player1.equ.pop(weapon)
            if self.Player1.health <= 0 :   #玩家是否死亡
                await ctx.send(f'{self.Player1.name}升天了')
                await ctx.send(f'在這次的冒險中你經歷了{self.ad}場戰鬥')
                await ctx.send(f'殺了{self.kill}隻怪物')
                self.Start = 0
            elif self.Monster1.health > 0 or self.Monster2.health > 0 :
                await ctx.send('-----------------------------')
                await ctx.send(self.Player1.ability())
                await ctx.send('你擁有的武器有')
                for i in range(len(self.Player1.equ)) :
                    await ctx.send(f'{i+1} : {self.Player1.equ[i].name} {self.Player1.equ[i].AD}')
                await ctx.send('-----------------------------')
                await ctx.send(f'名字 : {self.Monster1.name}   目標1號  狀態:{self.Monster1.life}\n-----------------------------\n血量是 : {self.Monster1.health}\n防禦力是 : {self.Monster1.defend} \n攻擊力是 : {self.Monster1.attact}\n{self.Monster1.intro}\n============================\n')
                await ctx.send(f'名字 : {self.Monster2.name}   目標2號  狀態:{self.Monster2.life}\n-----------------------------\n血量是 : {self.Monster2.health}\n防禦力是 : {self.Monster2.defend} \n攻擊力是 : {self.Monster2.attact}\n{self.Monster2.intro}\n============================\n')
                await ctx.send('你有兩個選擇 : \n1.攻擊 (輸入$attack 目標，武器(請輸入數字(以英文逗號分隔  EX: $attack 1,1\n2.防禦 (輸入$defend)')
            else :  #戰勝
                await ctx.send(self.Player1.ability())
                await ctx.send('你成功戰勝敵軍\n等級提升: 1')
                await ctx.send('請輸入$lvup (A/D/H 三擇一) 來升級')
                await ctx.send('A : 攻擊(1~2)  D : 防禦(1~2)  H :補血量(10~20)')
                self.Player1.flv+=1
                self.Start = 0        
                

    @commands.command()
    async def lvup(self, ctx, item): #升等加點數
        if self.Player1.flv > self.Player1.lv :
            up = random.randint(1,2)
            hea = random.randint(10,20)
            if item == 'A' :
                self.Player1.attact+=up
                await ctx.send(f'攻擊上升{up}')
            if item == 'D' :
                self.Player1.defend+=up
                await ctx.send(f'防禦上升{up}')
            if item == 'H' :
                self.Player1.health+=hea
                await ctx.send(f'血量回復{hea}')
            self.Player1.lv+=1
            await ctx.send(self.Player1.ability())
            self.Player1.equ = chose_equ(self.Player1.lv)
            for i in range(len(self.Player1.equ)) :
                await ctx.send(f'{i+1} : {self.Player1.equ[i].name} {self.Player1.equ[i].AD}')
            await ctx.send('請輸入$fight來開啟戰鬥')

    @commands.command()
    async def defend(self, ctx): #加防禦換武器
        if self.Start == 1 :
            
            self.Player1.equ = chose_equ(self.Player1.lv)
            if self.Monster1.health > 0 :    
                if self.Monster1.attact > self.Player1.defend+5 :
                    self.Player1.health-=self.Monster1.attact-self.Player1.defend-8
                    await ctx.send(f'受到{self.Monster1.name}造成的{self.Monster1.attact-self.Player1.defend-5}點傷害')
                else :
                    self.Player1.health-=1
                    await ctx.send(f'受到{self.Monster1.name}造成的1點傷害')
            if self.Monster2.health > 0 : 
                if self.Monster2.attact > self.Player1.defend+5 :
                    self.Player1.health-=self.Monster2.attact-self.Player1.defend-5
                    await ctx.send(f'受到{self.Monster2.name}造成的{self.Monster2.attact-self.Player1.defend-5}點傷害')
                else :
                    self.Player1.health-=1
                    await ctx.send(f'受到{self.Monster2.name}造成的1點傷害')
            self.round += 1
            if self.Monster1.health > 0 :
                await ctx.send(self.Monster1.round(self.Player1, self.round, self.Monster2))
            if self.Monster2.health > 0 :
                await ctx.send(self.Monster2.round(self.Player1, self.round, self.Monster1)) 
            if self.Monster1.health < 1 and self.Monster1.life == 'alive':  #怪物是否死亡
                await ctx.send(self.Monster1.dead(self.Player1, self.round, self.Monster2))
                if self.Monster1.health < 1 and self.Monster1.life == 'alive':
                    self.Monster1.life = 'Dead'
                    self.Monster1.health = 0
                    await ctx.send(f'{self.Monster1.name}升天了')
                    self.kill += 1
            if self.Monster2.health <= 0 and self.Monster2.life == 'alive':  #怪物是否死亡
                await ctx.send(self.Monster2.dead(self.Player1, self.round, self.Monster1))
                if self.Monster2.health <= 0 and self.Monster1.life == 'alive':
                    self.Monster2.life = 'Dead'
                    self.Monster2.health = 0
                    await ctx.send(f'{self.Monster2.name}升天了')
                    self.kill += 1
            if self.Player1.health <= 0 :   #玩家是否死亡
                await ctx.send(f'{self.Player1.name}升天了')
                await ctx.send(f'在這次的冒險中你經歷了{self.ad}場戰鬥')
                await ctx.send(f'殺了{self.kill}隻怪物')
                await ctx.send(f'經歷了{self.ad}場戰鬥')
                self.Start = 0
            elif self.Monster1.health > 0 or self.Monster2.health > 0 :
                await ctx.send('-----------------------------')
                await ctx.send(self.Player1.ability())
                await ctx.send('你擁有的武器有')
                for i in range(len(self.Player1.equ)) :
                    await ctx.send(f'{i+1} : {self.Player1.equ[i].name} {self.Player1.equ[i].AD}')
                await ctx.send('-----------------------------')
                await ctx.send(f'名字 : {self.Monster1.name}   目標1號  狀態:{self.Monster1.life}\n-----------------------------\n血量是 : {self.Monster1.health}\n防禦力是 : {self.Monster1.defend} \n攻擊力是 : {self.Monster1.attact}\n{self.Monster1.intro}\n-------------------------------\n')
                await ctx.send(f'名字 : {self.Monster2.name}   目標2號  狀態:{self.Monster2.life}\n-----------------------------\n血量是 : {self.Monster2.health}\n防禦力是 : {self.Monster2.defend} \n攻擊力是 : {self.Monster2.attact}\n{self.Monster2.intro}\n-----------------------------\n')
                await ctx.send('你有兩個選擇 : \n1.攻擊 (輸入$attack 目標，武器(請輸入數字(以英文逗號分隔  EX: $attack 1,1\n2.防禦 (輸入$defend)')
            else :  #戰勝
                await ctx.send('-----------------------------')
                await ctx.send('你成功戰勝敵軍\n等級提升: 1')
                await ctx.send('請輸入$lvup來升級')
                await ctx.send('A : 攻擊(1~2)  D : 防禦(1~2)  H :補血量(10~20)')
                self.Player1.flv+=1
                self.Start = 0  
        pass 
    @commands.command()
    async def quit(self, ctx):
        await ctx.send(f'{self.Player1.name}升天了')
        await ctx.send(f'在這次的冒險中你經歷了{self.ad}場戰鬥')
        await ctx.send(f'殺了{self.kill}隻怪物')
        self.Start = 0
        self.Player1.live ='Dead'


    

async def setup(bot):
    await bot.add_cog(Adventure(bot))