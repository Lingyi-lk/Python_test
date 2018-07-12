#filename:backup.py
# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

import os
import time
#1.需要备份的文件或者文件夹
source = [r'I:\dys\1.docx']
#2.需要备份的存放目录
target_dir = 'I:\\tar\\'
#3要压缩的文件
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
print target
zip_command = "makecab" +' '+''.join(source)+' '+ target
print zip_command
if os.system(zip_command) == 0:
    print 'Successfull back to',target
else:
    print 'backup failed'
