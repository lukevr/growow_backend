__author__ = 'luke'

import socket
import subprocess

# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 5777))
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')
try:
    # Run a viewer with an appropriate command line. Uncomment the mplayer
    # version if you would prefer to use mplayer instead of VLC
    #cmdline = ['vlc', '--demux', 'h264', '-']
    #cmd = "ffmpeg -i 'tcp://0.0.0.0:5777' -crf 30 -preset ultrafast -acodec aac -strict experimental -ar 44100 -ac 2 -b:a 96k -vcodec libx264 -r 25 -b:v 500k -f flv 'rtsp://0.0.0.0:1935/live'"

    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
    #player = subprocess.Popen(cmd, stdin=subprocess.PIPE, shell=True)
    while True:
        # Repeatedly read 1k of data from the connection and write it to
        # the media player's stdin
        data = connection.read(1024)
        cmd = 'ffmpeg -re -i input -f rtsp -muxdelay 0.1 rtsp://0.0.0.0/live'
        if not data:
            break
        #player.stdin.write(data)
finally:
    connection.close()
    server_socket.close()
    player.terminate()

#cmd = "ffmpeg -i 'tcp://192.168.11.1:5777' -crf 30 -preset ultrafast -acodec aac -strict experimental -ar 44100 -ac 2 -b:a 96k -vcodec libx264 -r 25 -b:v 500k -f flv 'rtmp://0.0.0.0/live'"
#p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
print("OK!")

#while True:
#    time.sleep(1)