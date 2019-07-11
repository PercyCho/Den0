import sys
from time import sleep
def fn2():
    print("Wait! Let me boot up my system and log your name into it.")
    sleep(1.5)
    for i in range(2):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.9)
        sys.stdout.flush()
    for i in range(2, 21):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.1)
        sys.stdout.flush()
    for i in range(21, 23):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(1.5)
        sys.stdout.flush()
    for i in range(23, 49):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.2)
        sys.stdout.flush()
    for i in range(49, 52):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.4)
        sys.stdout.flush()
    for i in range(52, 80):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.1)
        sys.stdout.flush()
    for i in range(80, 89):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.2)
        sys.stdout.flush()
    for i in range(89, 94):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.4)
        sys.stdout.flush()
    for i in range(94, 96):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(0.8)
        sys.stdout.flush()
    for i in range(96, 97):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(1.6)
        sys.stdout.flush()
    for i in range(97, 98):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(3.2)
        sys.stdout.flush()
    for i in range(98, 100):
        sys.stdout.write("\r%i %% done uploading files" % i)
        sleep(3.2)
        sys.stdout.flush()
    print("\nGetting started...")
    sleep(3)
    print("Done!")