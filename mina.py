import pyautogui as p
import time
import cv2 as cv


startX = 623 #google 
startY = 313
fimX = 1297
fimY = 853

# startX = 415 #opera
# startY = 361

# compX = 448 #opera
# compY = 361

compX = 674 #google
compY = 540

# dimenções do campo
numColumns = 10
numRows = 8

quadX = 67
quadY = 67
quadStartX = 0
quadStartY = 0

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
    # print(medB, medV, medVer)
    return medB, medV, medVer

def foto():
    p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

def compare ():
    (b,g,r) = color("quad.png")
    if g < 205:
        if b > 140 and g > 170 and r > 210:
            print ("fundo vermelho")
            return 6
        elif  b < 160 and g > 150 and r < 200:
            print ("verde")
            return 2
        elif b >= 160 and g > 150 and r < 200:
            print("azul")
            return 1
        elif b < 160 and g > 60 and r >= 200:
            print("red")
            return 3
        else:
            return 6
    else: 
        print("fundo verde")
        return 6  

def encontrar (indice,x,y):
    position = [[x - quadX, y], [x - quadX, y - quadY], [x, y - quadY], [x + quadX, y - quadY], [x + quadX, y], [x + quadX, y + quadY], [x, y + quadY], [x - quadX, y + quadY]]
    #verde = 0 bandeira = 1 aberto = 2
    baixo = [0,0,0,0,0,0,0,0]
    vazio = 0
    bombas = indice     
    print(indice, "a função foi iniciada")
    for i in range(0, len(position)):
        b = p.screenshot("redor.png", region=(position[i][0], position[i][1], quadX, quadY))
        b.save(r'C:\Users\Aluno\Desktop\resolver-minas\imgachar\image{}.png'.format(i))
        b = cv.imread("redor.png")
        (bF, gF, rF) = b[10, 10]
        (b,g,r) = color("redor.png")
        if rF > 210:
            print("fundo vermelho achado")
            vazio += 1
            baixo[i] = 2
        elif b < 160 and g > 60 and r >= 190:
            print("bandeira achada")
            vazio += 1
            bombas -= 1
            baixo[i] = 1

    if x + quadX > fimX:
        if baixo[3] != 2 or baixo[3] != 2:
            vazio += 1
        if baixo[4] != 2 or baixo[4] != 2:
            vazio += 1
        if baixo[5] != 2 or baixo[5] != 2:
            vazio += 1            
        baixo[3] = 2
        baixo[4] = 2
        baixo[5] = 2
    if x - quadX < fimX:
        if baixo[0] != 2 or baixo[0] != 2:
            vazio += 1
        if baixo[1] != 2 or baixo[1] != 2:
            vazio += 1
        if baixo[7] != 2 or baixo[7] != 2:
            vazio += 1 
        baixo[0] = 2
        baixo[1] = 2
        baixo[7] = 2
    if y + quadY > fimY:
        if baixo[5] != 2 or baixo[5] != 2:
            vazio += 1
        if baixo[6] != 2 or baixo[6] != 2:
            vazio += 1
        if baixo[7] != 2 or baixo[7] != 2:
            vazio += 1 
        baixo[5] = 2
        baixo[6] = 2
        baixo[7] = 2
    if y - quadY < fimY:
        if baixo[1] != 2 or baixo[1] != 2:
            vazio += 1
        if baixo[2] != 2 or baixo[2] != 2:
            vazio += 1
        if baixo[3] != 2 or baixo[3] != 2:
            vazio += 1 
        baixo[1] = 2
        baixo[2] = 2
        baixo[3] = 2
                   
    print('estão vazioes esses espaços ',vazio)
    print('bombas restantes', bombas)
    print(baixo)
    if bombas == 0: 
        print("-------------------achou um lugar para clicar--------------------------")
        for i in range(0, len(baixo)):
            if baixo[i] == 0:
                p.moveTo(position[i][0] + quadX / 2 ,position[i][1] + quadY / 2)
                p.click()
    if 8 - vazio == bombas:
        print("----------------dentro do if das bombas----------------")
        for i in range(0, len(baixo)):
            if baixo[i] == 0:
                p.moveTo(position[i][0] + quadX / 2,position[i][1] + quadY / 2)
                p.rightClick()               

def percorrer (): 
    quadStartX = startX
    quadStartY = startY
    contador = 0   
    for i in range (0, numRows):
        for j in range (0, numColumns):
            image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
            contador+=1
            image.save(r'C:\Users\Aluno\Desktop\resolver-minas\img\image{}.png'.format(contador))
            print(contador)
            t = compare()
            if (t != 6):
                encontrar(t,quadStartX, quadStartY)  
            quadStartX += quadX
        quadStartX = startX
        quadStartY += quadY 

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

p.moveTo(595,240) #google
p.click()
p.moveTo(595,265)
p.click()
p.moveTo(645,335)
p.click()

# p.moveTo(437,298) #opera
# p.click()
# p.moveTo(432,331)
# p.click()
# p.moveTo(434,382)
# p.click()

time.sleep(1)
foto()
p.PAUSE = 0.2

time.sleep(2)
q = 0
while True:
    q = q + 1
    percorrer()
    if (q > 10):
        break
p.alert("o loop terminou")     
time.sleep(2)
# percorrer()