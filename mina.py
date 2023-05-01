import pyautogui as p
import time

# 450x360
startX = 33
startY = 175

numColumns = 24
numRows = 20

pixel = 25
halfPixel = pixel/2

def foto():
    p.screenshot("board.png", region=(startX, startY, 600, 500))

#----------------------ABRIR o jogo-------------------------------- 

p.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
p.PAUSE = 0.5

p.moveTo(1,1)

# abrir google
p.press('winleft')
p.write('opera')
p.press('enter')

time.sleep(2)
# abrir campo minado
p.write('campo minado')
p.press('enter')
p.press('f11')
# p.moveTo(567,600) #chorme
p.moveTo(592,240) #opera
time.sleep(2)
p.click()

p.moveTo(595,240)
p.click()
p.moveTo(595,265)
p.click()
p.moveTo(645,335)
p.click()

foto()

