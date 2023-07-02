import discord
from discord.ext import commands
import json 
from core import Cog_Extension

class TodoList(Cog_Extension):
    # Initialization 
    def __init__(self, bot):
        self.todo = []

        '''
        todo 是一個 list 變數
        你可以在各個function中對self.todo做操作
        來當作模擬todolist

        你可能需要用到的function 
        list : append, remove, sort
        ctx.send(str)

        '''
        
    # Add todolist 
    # item 是要增加的待辨事項
    @commands.command()
    async def AddTodoList(self, ctx, item):
        self.todo.append(item)
        await ctx.send(f'成功將{item}加入表單' )

        pass 

    # Remove todolist
    # item 是要移除的待辨事項
    @commands.command()
    async def RemoveTodoList(self, ctx, item):
        if item in self.todo :
            self.todo.pop(self.todo.index(item))
            await ctx.send(f'成功將{item}刪除')
        else :
            await ctx.send(f'列表中沒有{item}這個事項')

        pass 

    # Sort todolist
    @commands.command()
    async def SortTodoList(self, ctx):
        if self.todo :
            self.todo.sort()
            self_todo_count=1
            for i in self.todo :
                await ctx.send(f'第{self_todo_count}項:   {i}')
                self_todo_count+=1
        else :
            await ctx.send('表單中沒有東西')
        

        pass 


    # Clear todolist
    @commands.command()
    async def ClearTodoList(self, ctx):
       await ctx.send(f'已將表單中的資料清除')
       self.todo.clear()
       
       pass 

async def setup(bot):
    await bot.add_cog(TodoList(bot))