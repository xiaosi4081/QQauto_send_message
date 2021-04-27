import win32gui
import win32con
import win32clipboard as w

n = 10

def get_msg():
    #发送的消息
    msg = input("发送的消息:")
    return msg

def get_name():
    name = input("发送给:")
    return name

def main():
    xiaoxi = get_msg()
    #窗口名字
    name = get_name()
    #将测试消息复制到剪切板中
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, xiaoxi)
    w.CloseClipboard()
    #获取窗口句柄
    handle = win32gui.FindWindow(None, name)
    #while 1==1:
    for i in range(n):
        #填充消息
        win32gui.SendMessage(handle, 770, 0, 0)
        #回车发送消息
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

if __name__ == "__main__":
    main()
    
版权声明：本文为CSDN博主「时暑」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/wjb123sw99/article/details/83475516

