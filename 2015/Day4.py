import hashlib
import time

def mine_adventcoin(part_two = False):
    """ Calculate and returns MD5 Hash with leadning 5 or 6 zeroes. """
    # temp = hashlib.md5((code+str(0)).encode()) 
    # result = temp.hexdigest()
    start_time = time.time()
    i = 0
    while True:
        result = hashlib.md5((key+str(i)).encode()).hexdigest()
        if part_two:
            if result[:6] == '000000':
                return i, (time.time() - start_time)
        else:
            if result[:5] == '00000':
                return i, (time.time() - start_time)
        i += 1

key = 'ckczppom'

print("Correct answer for part 1 is: ", mine_adventcoin())


print("Correct answer for part 2 is: ", mine_adventcoin(part_two = True))


