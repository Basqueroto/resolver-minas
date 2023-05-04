import pyautogui as p
import time
import cv2 as cv

# 450x360
# superior = x=435
# y = 392
# inferior
# x = 863
# y = 720
startX = 623
startY = 313
# compX = 448 google
# compY = 361

compX = 674
compY = 540

# dimenções do campo
numColumns = 10
numRows = 8

quadX = 67
quadY = 67
quadStartX = 0
quadStartY = 0

def foto():
    p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

def compare ():
    rose1 = cv.imread("quad.png")
    (bF, gF, rF) = rose1[5, 5]
    (b, g, r) = rose1[34, 34]
    print ("Cor do pixel em (34, 34) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

    if g < 200:
        if r > 210 and b > 130:
            print ("fundo vermelho")
        elif  g > 170 and r < 200:
            print ("verde")
            return 2
        elif g > 110:
            print("azul")
            return 1
        elif g > 60:
            print("red")
            return 3
    else: 
        print("fundo verde")    


def encontrar (indice):
    vazio = 0
    bombas = 0        
    if indice > 0 or indice < "":
        pX = quadStartX
        pY = quadStartY
        b = p.screenshot("quad.png", region=(quadStartX - quadX, quadStartY, quadX, quadY))
        (bF, gF, rF) = b[5, 5]
        if rF > 210 and bF > 130:
            print("fundo achado")
        





def percorrer (): 
    quadStartX = startX
    quadStartY = startY
    contador = 0   
    for i in range (numRows):
        for j in range (numColumns):
            image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
            contador+=1
            image.save(r'C:\Users\Aluno\Desktop\resolver-minas\img\image{}.png'.format(contador))
            print(compare())
            print(contador)
            quadStartX += quadX
        quadStartX = startX
        quadStartY += quadY 
    p.alert("o loop terminou") 

#----------------------ABRIR o jogo-------------------------------- 

p.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
p.PAUSE = 0.5

p.moveTo(1,1)

# abrir google
p.press('winleft')
p.write('google')
p.press('enter')

time.sleep(2)
# abrir campo minado
p.write('campo minado')
p.press('enter')
p.press('f11')
p.moveTo(567,600) #chorme
# p.moveTo(381,358) #opera
time.sleep(2)
p.click()

p.moveTo(595,240) 
p.click()
p.moveTo(595,265)
p.click()
p.moveTo(645,335)
p.click()

# p.moveTo(437,298) opera
# p.click()
# p.moveTo(432,331)
# p.click()
# p.moveTo(434,382)
# p.click()

time.sleep(1)
foto()

time.sleep(2)
percorrer()



