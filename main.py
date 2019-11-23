import tkinter as tk
import requests
from bs4 import BeautifulSoup
from pytube import YouTube
import tkHyperlinkManager
import win32api
import os
import sys

window=tk.Tk()				#布置tkinter
window.title('musicdownloader')
window.geometry('1200x800')

t =tk.Entry(window, show=None,width=80,font=('Arial', 14) ) 
t.pack()
e = tk.Text(window, height=30,font=('Arial', 20))
e.pack()
hyperlink = tkHyperlinkManager.HyperlinkManager(e)	#超連結布置


def searching():			#以request和beautifulsoup基本函數得到影片之標題、時間、網址以及觀看人數並存在list裡面
	e.delete('1.0','end')
	keyword=t.get()
	t.delete(0,'end')
	url='https://www.youtube.com/results?search_query='+keyword
	res=requests.get(url)
	content=res.content
	soup=BeautifulSoup(content, "html.parser")
	list=[]
	for i in soup.select(".yt-lockup-video"):
		data = i.select("a[rel='spf-prefetch']")
		list.append(data[0].get("href"))


	def click1():									#超連結按鈕，點下後執行下載之外部函數
		a='https://www.youtube.com'+list[0]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click2():
		a='https://www.youtube.com'+list[1]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click3():
		a='https://www.youtube.com'+list[2]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click4():
		a='https://www.youtube.com'+list[3]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click5():
		a='https://www.youtube.com'+list[4]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click6():
		a='https://www.youtube.com'+list[5]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click7():
		a='https://www.youtube.com'+list[6]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click8():
		a='https://www.youtube.com'+list[7]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click9():
		a='https://www.youtube.com'+list[8]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click10():
		a='https://www.youtube.com'+list[9]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click11():
		a='https://www.youtube.com'+list[10]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click12():
		a='https://www.youtube.com'+list[11]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click13():
		a='https://www.youtube.com'+list[12]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click14():
		a='https://www.youtube.com'+list[13]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click15():
		a='https://www.youtube.com'+list[14]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click16():
		a='https://www.youtube.com'+list[15]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click17():
		a='https://www.youtube.com'+list[16]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click18():
		a='https://www.youtube.com'+list[17]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click19():
		a='https://www.youtube.com'+list[18]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click20():
		a='https://www.youtube.com'+list[19]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click21():
		a='https://www.youtube.com'+list[20]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)
	def click22():
		a='https://www.youtube.com'+list[21]
		win32api.ShellExecute(0, 'open', 'pytubefunction.py', a, '', 1)

	a=1
	for i in soup.select(".yt-lockup-video"):			#文字內容
		data = i.select("a[rel='spf-prefetch']")
		data1 = i.select(".yt-lockup-meta-info")
		if a==1:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click1))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==2:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click2))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==3:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click3))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==4:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click4))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==5:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click5))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==6:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click6))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==7:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click7))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==8:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click8))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==9:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click9))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==10:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click10))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==11:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click11))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==12:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click12))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==13:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click13))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==14:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click14))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==15:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click15))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==16:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click16))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==17:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click17))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==18:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click18))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==19:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click19))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==20:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click20))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==21:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click21))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		if a==22:
			try:
				e.insert('end',data[0].get("title"),hyperlink.add(click22))
				e.insert('end','\n')
				e.insert('end',data1[0].get_text(" "))
				e.insert('end','\n')
			except :
				continue
		a=a+1


tk.Button(window,text='搜尋', width=5, height=1,command=searching).place(x=1100,y=0)

window.mainloop()
