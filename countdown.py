import time
countdown = 1

countdown = int(input("enter a countdown"))

while countdown !=0:
    print(countdown)
    time.sleep(1)
    countdown= countdown-1
print("countdown complete")