#!/bin/bash
OUTPUT_FILE=`date '+%Y%m%d_%H:%M:%S'`
/usr/bin/nohup /usr/bin/mimms mms://vod2.hcrt.cn/fm918tt?cccode=cc1405 /media/BT/fm${OUTPUT_FILE}.asf -t 90 > /dev/null 2>&1 & 
