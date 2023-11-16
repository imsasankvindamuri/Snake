import time
t1=time.monotonic()
print("Hello, World!")
for i in range(1,11):
    print(i)
t2=time.monotonic()
t=t1-t2
print(f"Time Elapsed: {t} secs")