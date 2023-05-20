import pyautogui as p
import time
import cv2 as cv

y = 0
rose1 = cv.imread("img/image13.png")
(b, g, r) = rose1[34, 34]
(b2, g2, r2) = rose1[10, 10]
print('pixel do meio azul',b,'verde', g,'vermelho', r)
print('pixel na ponta azul',b2,'verde', g2,'vermelho', r2)

print()
print('----------------------------------------------')
print()

rose1 = cv.imread("img/image18.png")
(b, g, r) = rose1[34, 34]
(b2, g2, r2) = rose1[10, 10]
print('pixel do meio azul',b,'verde', g,'vermelho', r)
print('pixel na ponta azul',b2,'verde', g2,'vermelho', r2)
 