import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
import random
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Wordle(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        PATH="C:\\Users\\minni\\Desktop\\Sprout2023py---2nd-Project-main\\cmds"
        browser = webdriver.Chrome(PATH)
        browser.get("https://gist.githubusercontent.com/cfreshman/d97dbe7004522f7bc52ed2a6e22e2c04/raw/633058e11743065ad2822e1d2e6505682a01a9e6/wordle-nyt-words-14855.txt")
        search = browser.find_element(By.XPATH, "/html/body/pre")
        search=search.text
        self.word_list=list(search.split())
        self.start=0
        pass 
        
        '''
        TODO 
        要在init function 中載入單字庫

        Hint:
        1. 好像有import urllib
        2. data.json中有貼上url了
        '''

    @commands.command()
    async def Play(self, ctx):
        ''' 
        要在爬好的單字庫中, 隨機挑選一個單字做為預設的答案
        '''
        self.word_choice=random.randint(0,len(self.word_list)-1)
        self.word_word=self.word_list[self.word_choice]
        self.word_split=[]
        for i in self.word_word :
            self.word_split.append(i)
        await ctx.send('遊戲說明:')
        await ctx.send('大寫意為字母位置正確')
        await ctx.send('小寫意為字母在該單字裡面但位置不正確')
        await ctx.send('#字號意為不再該單子裡面')
        await ctx.send('還有請輸入小寫的字')
        await ctx.send('在回答之前請輸入$Ask')
        await ctx.send('------------------------------------ ')
        await ctx.send('已成功開始遊戲，請開始作答，你有六次機會')
        self.chance=6
        self.start=1

    
    @commands.command()
    async def Ask(self, ctx, ans):
        correct=0
        half_correct=0
        if self.start!=1 :
            await ctx.send('請先輸入Play')
        else :
            if len(ans) !=5 :
                await ctx.send('請輸入五個字母')
            else :
                if ans not in self.word_list :
                    await ctx.send('這好像不是個單字')
                else: 
                    if ans==self.word_word :
                        await ctx.send('恭喜答對!!!')
                        self.start=0
                    else :
                        word_split=self.word_split.copy()
                        ans_split=[]
                        for i in ans :
                            ans_split.append(i)
                        output=['#', '#', '#', '#', '#']
                        for i in range(5) :
                            if ans_split[i]==word_split[i] :
                                output[i]=ans_split[i].upper()
                                word_split[i]=1
                                ans_split[i]=0
                                correct+=1
    
                        for i in range(5):
                            if ans_split[i] in word_split:
                                output[i]=ans_split[i].lower()
                                word_split[i]=1
                                half_correct+=1
                        response=''.join(output)
                        wrong=5-correct-half_correct
                        await ctx.send(response)
                        await ctx.send(f'在此之中有{correct}個位置正確\n有{half_correct}個位置不正確\n有{wrong}個不正確')
                        await ctx.send('請繼續猜測')

                        self.chance-=1
                    if self.chance == 0 :
                        await ctx.send('你猜測的次數已達到六次，你輸了')
                        await ctx.send(f'正確答案是{self.word_word}')
                        self.start=0
                        
        '''
        ans 是使用者傳入的猜測答案

        TODO
        1. 沒有play直接ask : 請先輸入 Play 指令
        2. 不是5個字的單字 : 請輸入5個字母的單字
        3. 不是單字的英文組合(不在單字庫中) : 這好像不是個單字
        4. 答對 : 恭喜答對!!!
        5. 猜太多次了 : 真可惜, 答案是{answer}
        '''
        pass


async def setup(bot):
    await bot.add_cog(Wordle(bot))