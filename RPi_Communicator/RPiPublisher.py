__author__ = 'luke'

from Getch import _Getch

import time
import zmq


def main():
    port = 5563

    # Prepare our context and publisher
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:" + str(port))

    key = _Getch()
    while True:
        # Write two messages, each with an envelope and content

        if key == "v":
            publisher.send_multipart([b"A", b"We don't want to see this"])
            publisher.send_multipart([b"B", b"We would like to see this"])
        time.sleep(1)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()