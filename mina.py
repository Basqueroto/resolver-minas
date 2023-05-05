import pyautogui as p
import time
import cv2 as cv


# startX = 623 #google 
# startY = 313

startX = 415 #opera
startY = 361

compX = 448 #opera
compY = 361

# compX = 674 #google
# compY = 540

# dimenções do campo
numColumns = 10
numRows = 8

quadX = 44
quadY = 44
quadStartX = 0
quadStartY = 0

def foto():
    p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

def compare ():
    rose1 = cv.imread("quad.png")
    # (bF, gF, rF) = rose1[10, 10]
    (b, g, r) = rose1[21, 21]
    # print ("Cor do pixel em (34, 34) - Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b))

    if g < 200:
        if r > 210 and b > 130:
            print ("fundo vermelho")
            return 6
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
        return 6    


def encontrar (indice,x,y):
    position = [[x - quadX, y], [x - quadX, y - quadY], [x, y - quadY], [x + quadX, y - quadY], [x + quadX, y], [x + quadX, y + quadY], [x, y + quadY], [x - quadX, y + quadY]]
    #verde = 0 bandeira = 1 aberto = 2
    baixo = [0,0,0,0,0,0,0,0]
    vazio = 0
    bombas = indice        
    if indice != 6:  
        print(indice, "a função foi iniciada")
        for i in range(0, len(position)):
            b = p.screenshot("redor.png", region=(position[i][0], position[i][1], quadX, quadY))
            b.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\minas2\resolver-minas\imgachar\image{}.png'.format(i))
            b = cv.imread("redor.png")
            (bF, gF, rF) = b[5, 5]
            (b, g, r) = b[22, 22]
            print ("Vermelho: %d, Verde: %d, Azul: %d" % (rF, gF, bF))
            if rF > 200 and bF > 120:
                print("fundo vermelho achado")
                vazio += 1
                baixo[i] = 2
            elif gF > 199 and g < 90 and r > 190:
                print("bandeira achada")
                vazio += 1
                bombas -= 1
                baixo[i] = 1
        
        print(vazio)
        print(bombas)
        print(baixo)
        if bombas <= 0: 
            for i in range(0, len(baixo)):
                if baixo[i] == 0:
                    p.moveTo(position[i][0] + quadX / 2,position[i][1] + quadY / 2)
                    p.click()
        if 8 - vazio == bombas:
            print("----------------dentro do if das bombas----------------")
            for i in range(0, len(baixo)):
                if baixo[i] == 0:
                    p.moveTo(position[i][0] + quadX / 2,position[i][1] + quadY / 2)
                    p.rightClick()
    return                

def percorrer (): 
    quadStartX = startX
    quadStartY = startY
    contador = 0   
    for i in range (numRows):
        for j in range (numColumns):
            image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
            contador+=1
            image.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\minas2\resolver-minas\img\image{}.png'.format(contador))
            print(compare())
            print(contador)
            encontrar(compare(),quadStartX, quadStartY)  
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

# p.moveTo(595,240) #google
# p.click()
# p.moveTo(595,265)
# p.click()
# p.moveTo(645,335)
# p.click()

p.moveTo(437,298) #opera
p.click()
p.moveTo(432,331)
p.click()
p.moveTo(434,382)
p.click()

time.sleep(1)
foto()

time.sleep(2)
q = 0
while True:
    q = q + 1
    percorrer()
    if (q > 10):
        break