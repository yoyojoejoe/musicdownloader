import sys
import os
import subprocess
from pytube import YouTube
import time

a=sys.argv[0]
b=sys.argv[1]

chinese = "E:\music\chinese"		#資料夾位置
english = "E:\music\english"
piano = "E:\music\piano"

def downloadyoutube(u,x):
	yt = YouTube(u)			#以pytube下載youtube影片
	vids= yt.streams.all()
	vids[0].download(x)
	parent_dir = x
	default_filename = vids[0].default_filename
	new_filename = default_filename[:-1]+"3"
	subprocess.call([			#用ffmpeg將mp4檔案轉為mp3
		'ffmpeg',
		'-i', os.path.join(parent_dir, default_filename),
		os.path.join(parent_dir, new_filename)
	])

	new_filename="del "+x+"\\"+"\""+default_filename+"\""	#刪除mp4檔案
	os.system(new_filename)

if __name__ == '__main__':
	while True:
		a=input("中文資料夾請輸入1;英文請輸入2;純音樂請輸入3 ")
		if a == '1':
			downloadyoutube(b,chinese)
			break
		if a == '2':
			downloadyoutube(b,english)
			break
		if a == '3':
			downloadyoutube(b,piano)
			break
		else:
			print("輸入錯誤請重新輸入")
