#filename:backup.py
# -*- coding: gb18030 -*- 
# -*- coding: utf-8 -*-

import os
import time
#1.��Ҫ���ݵ��ļ������ļ���
source = [r'I:\dys\1.docx']
#2.��Ҫ���ݵĴ��Ŀ¼
target_dir = 'I:\\tar\\'
#3Ҫѹ�����ļ�
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'
print target
zip_command = "makecab" +' '+''.join(source)+' '+ target
print zip_command
if os.system(zip_command) == 0:
    print 'Successfull back to',target
else:
    print 'backup failed'
