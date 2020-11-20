#coding=utf-8

from multiprocessing import Process
import time
import os

def run_proc(*args, **kwargs):
	for i in range(10):
		print('子进程运行中，name= %s,age=%d ,pid=%d...' % (args[0],args[1],os.getpid()))
		print(kwargs)
		time.sleep(0.2)

if __name__=='__main__':
	p = Process(target=run_proc, args=('test',18), kwargs={"m":20,'k':{"a":"b"}})
	p.start()
	time.sleep(1)
	# 无论是否执行完毕，都是立即终止进程
	p.terminate()
