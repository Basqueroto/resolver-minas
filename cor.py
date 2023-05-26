import pyautogui as p
import time
import cv2 as cv

#info color
#verde: b=60 v=142 verme=56
#vermelho: b=47 v=47 verme=211

y = 0
rose1 = cv.imread("img/image34.png")
# (b, g, r) = rose1[34, 34] #centro1
# (b2, g2, r2) = rose1[50, 40] #centro2
# (b3, g3, r3) = rose1[38, 40] #centro3
# (b, g, r) = rose1[34, 34]
# (b2, g2, r2) = rose1[10, 10]
# print('pixel na ponta azul',b2,'verde', g2,'vermelho', r2)
# print('pixel do meio azul',b,'verde', g,'vermelho', r)

# if r2 > 210:
#     print("fundo vermelho achado")
# elif r > 190:
#     print("bandeira achada")

def color (image):
    medB = 0
    medV = 0
    medVer = 0
    cont = 0
    img = cv.imread(image)
    for i in range(21, 57):
        for j in range(23, 45):
            (b, g, r) = img[i, j]        
            medB += b
            medV += g
            medVer += r
            cont += 1
    medB = medB / cont
    medV = medV / cont
    medVer = medVer / cont
    print(medB, medV, medVer)
    return medB, medV, medVer

# (b,g,r) = color("img/image52.png")

# if g < 205:
#         if b > 140 and g > 170 and r > 210:
#             print ("fundo vermelho")
#         elif  b < 160 and g > 150 and r < 200:
#             print ("verde")
#         elif b >= 160 and g > 150 and r < 200:
#             print("azul")
#         elif b < 160 and g > 60 and r >= 200:
#             print("red")
# else: 
#     print("fundo verde")

(bF, gF, rF) = rose1[10, 10]
print(rF)
(b,g,r) = color('img/image34.png')
if rF > 200:
    print("fundo vermelho achado")
elif b < 160 and g > 60 and r >= 190:
    print("bandeira achada")