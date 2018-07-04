#!/bin/sh
cd /workspace/mnt/group/face-det/zhubin/Face_attr_recognition5/
echo '===>Start training!' >> GenderAge.log
#python train.py
nohup python train.py > GenderAge.log 2>&1 &
echo '===>Training finished!' >> GenderAge.log
