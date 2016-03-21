__author__ = 'luke'

import subprocess

subprocess.call(['./readRPiFifoStream.sh'])

cmd = 'ffmpeg -re -i fifo264 -f rtsp -muxdelay 0.1 rtsp://0.0.0.0/live'
subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)