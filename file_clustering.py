import os
import time
import datetime
from datetime import datetime
import shutil, sys

cate_folder = "\\Category";
img_folder = "\\Image"   # please fill images in "Image" folder

if not os.path.exists(os.getcwd()+ cate_folder):
    os.makedirs(os.getcwd()+ cate_folder)

for filename in os.listdir(os.getcwd() + img_folder):
    print (filename)
    info = os.stat(os.getcwd() + img_folder + "\\" + filename)
    year = time.strptime(time.asctime(time.localtime(info.st_mtime))).tm_year
    month = time.strptime(time.asctime(time.localtime(info.st_mtime))).tm_mon
    day = time.strptime(time.asctime(time.localtime(info.st_mtime))).tm_mday  
    if not os.path.exists(os.getcwd()+ cate_folder + "\\" + str(year)):
        os.makedirs(os.getcwd()+ cate_folder + "\\" + str(year))
    if not os.path.exists(os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month)):
        os.makedirs(os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month))        
    if not os.path.exists(os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month) + "\\" + str(day)):
        os.makedirs(os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month) + "\\" + str(day))          
    if os.path.exists(os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month) + "\\" + str(day)):
        s = os.getcwd() + img_folder + "\\" + filename
        print (s)
        s1 = os.getcwd()+ cate_folder + "\\" + str(year) + "\\" + str(month) + "\\" + str(day) + "\\" + filename
        print (s1)
        shutil.copy2(s,s1)
    else:
        print ("Exception: Logic jail & Call me !!")
    

#year = time.strptime(time.asctime(time.localtime(info.st_mtime))).tm_year
#print(time)
    
#localtime = time.asctime( time.localtime(time.time()) )
#print (localtime)
