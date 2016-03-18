__author__ = 'luke'

import time
import zmq
import sys

def main():
    port = 5563

    # Prepare our context and publisher
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:" + str(port))


    while True:
        # Write two messages, each with an envelope and content
        key = sys.stdin.read(1)
        if key == "p":
            publisher.send_multipart([b"P", b"Play Video"])
        if key == "s":
            publisher.send_multipart([b"S", b"Stop Video"])
        if key == "q":
            publisher.close()
            context.term()
            break
        time.sleep(0.5)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()