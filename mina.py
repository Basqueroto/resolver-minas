import pyautogui as p
import time

# 450x360
# superior = x=435
# y = 392
# inferior
# x = 863
# y = 720
startX = 415
startY = 361
compX = 448
compY = 361

# dimenções do campo
numColumns = 10
numRows = 8


def foto():
    p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

def percorrer (): 
    quadX = 44.8
    quadY = 44.8
    quadStartX = 415
    quadStartY = 361
    contador = 0   
    for i in range (numRows):
        for j in range (numColumns):
            image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
            contador+=1
            image.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\py\resolver-minas\img\image{}.png'.format(contador))
            quadStartX += quadX

        quadStartX = 415
        quadStartY += quadY 
    p.alert("o loop terminou")       
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
p.moveTo(381,358) #opera
time.sleep(2)
p.click()

# # p.moveTo(595,240) chorme----------------
# p.click()
# p.moveTo(595,265)
# p.click()
# p.moveTo(645,335)
# p.click()

p.moveTo(437,298)
p.click()
p.moveTo(432,331)
p.click()
p.moveTo(434,382)
p.click()

time.sleep(1)
foto()

time.sleep(2)
percorrer()



