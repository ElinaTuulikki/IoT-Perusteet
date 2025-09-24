import time

time.sleep(0.1) # Wait for USB to become ready

print("Loop starting")
for i in range(10):
    print("Number: ", i)
print("Loop ending")