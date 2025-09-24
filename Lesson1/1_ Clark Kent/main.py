import time

time.sleep(0.1)  # Wait for USB to become ready

while True:
    name = input("Enter name: ")

    if name == "Clark Kent":
        print("You are the Superman!")
    else:
        print("You are an ordinary person.")
