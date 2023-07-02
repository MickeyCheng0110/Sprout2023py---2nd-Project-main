'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''
import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import random
import numpy as np

class chose(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        pass
        
    #介紹
    @commands.command()
    async def choseintroduce(self, ctx):
        await ctx.send('chose是抽籤:')
        await ctx.send('請輸入範圍和所需要數量\n請以","分隔')
        await ctx.send('Ex: 1,50,10')
        await ctx.send('1 50 是範圍 10 是索取數量')
        await ctx.send('---------------------------')
        await ctx.send('row 是骰骰子 後面不用加東西')
        pass
    
    
    #抽籤 
    @commands.command()   
    async def chose(self, ctx, item):
        await ctx.send(item)
        a,b,c=map(int,item.split(','))
        aa=list(np.arange(a,b))
        response=random.sample(aa, k=c)
        await ctx.send(f'抽到{response}')
        pass

    #骰骰子
    @commands.command()
    async def row(self, ctx):
        response=random.randint(1, 6)
        await ctx.send(f'骰到{response}')
        
        

        pass 

async def setup(bot):
    await bot.add_cog(chose(bot))