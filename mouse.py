import pyautogui as p
import time


y = 0

while y <= 10:
    print(p.position())
    time.sleep(0.5)

    y+=1
p.alert("pegamos o local")    