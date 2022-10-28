import os,time
print("--------AutoPing V1.0--------")#主题介绍，会持续更新
print("Hello,welcome to use the AutoPing V1.0!")
print("You can test the connection of your computer and the target")
print("This file is updating...")
print("enter quit to quit!")
print("-----------------------------")
print("")
localtime=time.asctime(time.localtime(time.time())) #记录当前的时间
while True: #以重复执行
    length=0
    size=os.path.getsize("C:/Users/GJJKJ/Desktop/Project/result.txt")#计算文件大小
    myfile=open("result.txt","a")
    while length==0: #检测用户输入的URL长度，若为0，则要求重新输入
        website=str(input("URL needed:")) #要求用户输入URL
        length=len(website)
    if website=="quit": #检测用户是否需要退出
        break
    a=os.system("ping "+website) #ping
    print(a)
    if a==0 and a!=-1073741510 : #判断网站是否ping通
        print("this website is able to visit")
    else:
        print("this website seems to be banned...,or you have typed in a wrong URLs,Try Again !")
        myfile.write("\n\n"+website+" is unable to visit in \n\n"+localtime)#记录日志
        myfile.close
    if a==-1073741510:
        raise Warning("请不要取消窗口！") #向用户报错
    if size>=7068: #计算文件大小
        myfile.truncate()
"""
I expect to add more functions in this file
for example,you will be able to...
email:scratchwiki@outlook.com

"""
"""
测试数据
报错：youtube.cn
ping通：bilibili.com
ping不通：facebook.com

"""
