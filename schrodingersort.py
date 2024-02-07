# importing useful stuff
import os
import random
import time


# Schrodinger Sort
def SCHROSORT(NUMS):
    TRIES = 0

    # returns the sorted list 
    def IS_Sorted(NUMS):
        if len(NUMS) < 2:
            return True

        for i in range(len(NUMS) - 1):
            if NUMS[i] > NUMS[i + 1]:
                return False

        return True

    # Checks if the list is in order and if it isn't prepares the Cat
    while not IS_Sorted(NUMS):
        random.shuffle(NUMS)
        TRIES = TRIES + 1
        print(TRIES)
        ROLL = random.randint(0, 2)
        if ROLL == 1:
            pass
        else:
            print("cat is dead")
            time.sleep(10)
            os.system("shutdown /s /t 1")

            break

    return NUMS


print("Schrodinger sort")
# Taking an input for the sort
NUM1 = input('Input a list of comma seperated numbers:\n').strip()
NUMS = [int(ITEM_69) for ITEM_69 in NUM1.split(',')]
print(SCHROSORT(NUMS))