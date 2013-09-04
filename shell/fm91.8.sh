#!/bin/bash
# 使用mimms自动下载杭州91.8电台，持续时间为90分钟
OUTPUT_FILE=`date '+%Y%m%d_%H:%M:%S'`
/usr/bin/nohup /usr/bin/mimms mms://vod2.hcrt.cn/fm918tt?cccode=cc1405 /media/BT/fm${OUTPUT_FILE}.asf -t 90 > /dev/null 2>&1 & 
