'''
可以複製todolist的架構, 但請記得更改class & function的名稱
這個檔案的名字也可以改
'''
import discord
from discord.ext import commands
import json 
from core import Cog_Extension
import urllib
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import discord
from discord.ext import commands
from core import Cog_Extension
from PIL import Image
import requests

class Picture(Cog_Extension):
    @commands.command()
    async def Search(self, ctx, item):
        #找圖片
        PATH="C:\\Users\\minni\\Desktop\\Sprout2023py---2nd-Project-main\\cmds"
        browser = webdriver.Chrome(PATH)
        browser.get("https://pxhere.com/")
        search_box = browser.find_element(By.XPATH, "/html/body/section[1]/div[1]/form/div/input")
        search_box.send_keys(item)
        search_box.send_keys(Keys.RETURN)
        Picture = browser.find_element(By.XPATH, '/html/body/section/div[2]/div[2]/div[2]/div[1]/div/a/img') 
        Picture_link = Picture.get_attribute('src')
        #下載圖片
        f = open('C:\\Users\\minni\\OneDrive\\桌面\\Sprout2023py---2nd-Project-main\\cmds\\pic\\Picture.jpg','wb')
        response = requests.get(Picture_link)
        f.write(response.content)
        f.close()
        #傳圖片
        file = discord.File("C:\\Users\minni\\OneDrive\\桌面\\Sprout2023py---2nd-Project-main\\cmds\\pic\\Picture.jpg")
        await ctx.send(file = file)
        await ctx.send('這是你要的圖片')
        pass 
async def setup(bot):
    await bot.add_cog(Picture(bot))