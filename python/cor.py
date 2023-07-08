import pyautogui as p
import time
import cv2 as cv

# def color (image): #google
#     medB = 0
#     medV = 0
#     medVer = 0
#     cont = 0
#     img = cv.imread(image)
#     for i in range(21, 57):
#         for j in range(23, 45):
#             (b, g, r) = img[i, j]        
#             medB += b
#             medV += g
#             medVer += r
#             cont += 1
#     (bf, gf, rf) = img[50, 50]        
#     medB = medB / cont
#     medV = medV / cont
#     medVer = medVer / cont
#     # print(medB, medV, medVer)
#     return medB, medV, medVer, gf

def color (image):
    medB = 0
    medV = 0
    medVer = 0
    cont = 0
    img = cv.imread(image)
    for i in range(7, 34): #lines
        for j in range(15, 30): #colun
            (b, g, r) = img[i, j]        
            medB += b
            medV += g
            medVer += r
            cont += 1
    (bf, gf, rf) = img[40, 40]        
    medB = medB / cont
    medV = medV / cont
    medVer = medVer / cont
    print(medB, medV, medVer)
    return medB, medV, medVer, gf


# def compare ():
#     (b,g,r,gf) = color("img\image47.png")
#     print(gf)
#     if g < 205 and gf < 205:
#         if b > 140 and g > 170 and r > 210:
#             print ("fundo vermelho")
#             return 6
#         elif  b < 160 and g > 150 and r < 200:
#             print ("verde")
#             return 2
#         elif b >= 160 and g > 150 and r < 200:
#             print("azul")
#             return 1
#         elif b < 160 and g > 60 and r >= 200:
#             print("red")
#             return 3
#         else:
#             return 6
#     else: 
#         print("fundo verde")
#         return 6  
# compare()

winX = 495
winY = 363

wCompX = 288
wCompY = 11

time.sleep(2)
p.alert('vamos escanear')
time.sleep(4)
def win ():
    print('ganhamos?')
    p.screenshot("win.png", region=(winX, winY, wCompX, wCompY))
    (b, g, r, gf) = color('win.png')
win()      
p.alert('escaneado')      