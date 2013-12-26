# -*- coding: utf-8 -*-
# 2013/12/26 15:32
# auth:blueicesir@gmail.com
# auto record autoit3 script only mouse and keyboard
# http://sourceforge.net/projects/pyhook/
# http://sourceforge.net/projects/pywin32/
import pythoncom
import pyHook
import time
from datetime import *

def init():
	global script_file
	global hm

	dt=datetime.now()
	script_name="D:\\autoit_"+ dt.strftime('%Y%m%d%H%M%S')+".au3"
	print "Create Script Name:%s" % script_name
	script_file=open(script_name,'w')
	init_record()
	record()

	script_file.write("Func EnumUser()\n")

	hm = pyHook.HookManager()
 
	# 监听所有键盘事件
	hm.KeyDown = onKeyboardEvent
	hm.HookKeyboard()
 
	# 监听所有鼠标事件
	hm.MouseAll = onMouseEvent
	hm.HookMouse()
 
	# 进入循环，如不手动关闭，程序将一直处于监听状态
	pythoncom.PumpMessages()


def init_record():
	global script_file
	heads={"IE.au3","Inet.au3","Array.au3","WinAPI.au3","File.au3"}
	for fi in heads:
		script_file.write("#include <%s>\n"%fi)
	script_file.write("\n\n\n")

	script_file.write("HotKeySet(\"{Esc}\",\"captureEsc\")\n\n")
	script_file.write("EnumUser()\n\n")


def record():
	global script_file
	script_file.write("Func captureEsc()\n")
	script_file.write("\tMsgBox(0,\"提示!\",\"用户按Esc键，程序终止。\")\n")
	script_file.write("\tExit\n")
	script_file.write("EndFunc\n\n\n")


def onMouseEvent(event):
	global script_file
	global hm
	global inputval
	# print "MessageName:", event.MessageName
	# print "Message:", event.Message
	# print "Time:", event.Time
	# print "Window:", event.Window
	# print "WindowName:", event.WindowName
	# print "Position:", event.Position
	# print "Wheel:", event.Wheel
	# print "Injected:", event.Injected

	# 鼠标中间见按下
	if event.Message==520 or event.Message==519:
		hm.UnhookKeyboard()
		print "UnHookKeyboard."
		hm.UnhookMouse()
		print "UnHookMouse."
		script_file.write("EndFunc\n")
		script_file.close()
		print "Close MacroFile."
		exit()

	# 鼠标左键按下
	if event.Message==513:
		script_file.write("\tMouseMove(%s,%s)\n" %(event.Position[0],event.Position[1],))
		script_file.write("\tMouseClick(\"left\")\n")
		script_file.write("\n")

	# 鼠标右键按下
	if event.Message==516:
		script_file.write("\tMouseMove(%s,%s)\n" %(event.Position[0],event.Position[1],))
		script_file.write("\tSend(\"%s\")\n" % (inputval,))
		script_file.write("\n")
		inputval=''
	return True


def onKeyboardEvent(event):
	global script_file
	global hm
	global inputval
	# print "MessageName:", event.MessageName
	# print "Message:", event.Message
	# print "Time:", event.Time
	# print "Window:", event.Window
	# print "WindowName:", event.WindowName
	# print "Ascii:", event.Ascii, chr(event.Ascii)
	# print "Key:", event.Key
	# print "KeyID:", event.KeyID
	# print "ScanCode:", event.ScanCode
	# print "Extended:", event.Extended
	# print "Injected:", event.Injected
	# print "Alt", event.Alt
	# print "Transition", event.Transition
	inputval=inputval+chr(event.Ascii)
	return True





 
if __name__ == "__main__":
	script_file=''
	hw=''
	inputval=''

	init()

