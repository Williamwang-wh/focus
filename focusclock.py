import time  
  
while True:  
    current_time = time.strftime("%H:%M:%S")  
    print(current_time, end="", flush=True)  
    print("\r", end="", flush=True)  
    time.sleep(1)
