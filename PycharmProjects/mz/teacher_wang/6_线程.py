#coding=utf-8

# 时间
import time
# 线程
import threading

def sing():
	for i in range(3):
		print("正在唱歌...%d"%i)
		time.sleep(2)

def dance():
	for i in range(3):
		print("正在跳舞...%d"%i)
		time.sleep(2)

if __name__ == '__main__':
	print('---开始---:%s'%time.ctime())
	t1 = threading.Thread(target=sing)
	t2 = threading.Thread(target=dance)
	t1.start()
	t2.start()
	# join(): 阻塞

	t1.join()
	t2.join()
	print('---结束---:%s'%time.ctime())
