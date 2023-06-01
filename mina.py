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

# fimX = 863 #opera
# fimY = 722

# winX = 495  #opera
# winY = 363
# wCompX = 288
# wCompY = 11

compX = 674 #google
compY = 540



# dimenções do campo
numColumns = 10
numRows = 8

quadX = 67
quadY = 67
quadStartX = 0
quadStartY = 0

prox = True
contador = 0  
# opened = []
# for i in range(numRows):
#     pas = []
#     for j in range(numColumns):
#         pas.append(False)
#     opened.append(True)
# print(opened)    
def color (image, li = 21, lf = 57, ci = 23, cf = 45, can = True): #quadrado padrão
    medB = 0
    medV = 0
    medVer = 0
    cont = 0
    img = cv.imread(image)
    for i in range(li, lf): #lines
        for j in range(ci, cf): #colun
            (b, g, r) = img[i, j]        
            medB += b
            medV += g
            medVer += r
            cont += 1
    if can == True:        
        (bf, gf, rf) = img[40, 40]  
    else:
        gf = 0          
    medB = medB / cont
    medV = medV / cont
    medVer = medVer / cont
    print(medB, medV, medVer)
    return medB, medV, medVer, gf

def foto():
    p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

def compare (img = 'quad.png'):
    (b,g,r,gf) = color(img)
    # print(gf)
    if g < 205 and gf < 205:
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
        elif b > 150 and g > 60 and r <= 200:
            print("roxo")
            return 4
        elif b < 110 and g > 150 and r >= 210:
            print("laranja")
            return 5
        else:
            return 6
    else: 
        print("fundo verde")
        return 6  

# def win ():
#     p.screenshot("win.png", region=(winX, winY, wCompX, wCompY))
#     (b, g, r, gf) = color('win.png', 0, 11, 0, 288, False)
#     if b > 230:
#         print ('vencemos')
#         prox = False
#         return True
#     else: 
#         return False

    


def encontrar (indice,x,y):
    # if win() == True:
    #     return 
    position = [[x - quadX, y], [x - quadX, y - quadY], [x, y - quadY], [x + quadX, y - quadY], [x + quadX, y], [x + quadX, y + quadY], [x, y + quadY], [x - quadX, y + quadY]]
    #verde = 0 bandeira = 1 aberto = 2
    baixo = [0,0,0,0,0,0,0,0]
    vazio = 0
    bombas = indice     
    print(indice, "a função foi iniciada")
    for i in range(0, len(position)):
        b = p.screenshot("redor.png", region=(position[i][0], position[i][1], quadX, quadY))
        b.save(r'C:\Users\Aluno\Desktop\resolver-minas\imgachar\image{}.png'.format(i)) #google
        # b.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\minas\resolver-minas\imgachar\image{}.png'.format(i)) #opera
        b = cv.imread("redor.png")
        (bg, gg, rF) = b[50, 50]
        (b,g,r, gF) = color("redor.png")
        print(i)
        # print(b, g, r, rF)
        if rF > 210: #aqui está p problem
            print("fundo vermelho achado")
            vazio += 1
            baixo[i] = 2
        elif b < 160 and g > 60 and r >= 190:
            print("bandeira achada")
            vazio += 1
            bombas -= 1
            baixo[i] = 1
        print(baixo)
        print(x, y)
    if x >= 1220: #varia
        voltar = [3,4,5]
        for i in voltar:
            if baixo[i] != 2:
                vazio += 1
                baixo[i] = 2
    if x <= startX + 10:
        voltar = [0,1,7]
        for i in voltar:
            if baixo[i] != 2:
                vazio += 1
                baixo[i] = 2
    if y <= startY + 10:
        voltar = [1,2,3]  
        for i in voltar:
            if baixo[i] != 2:
                vazio += 1
                baixo[i] = 2
    if y >= 770: 
        voltar = [5,6,7]  
        for i in voltar:
            if baixo[i] != 2:
                vazio += 1
                baixo[i] = 2                                  


                   
    print('estão vazioes esses espaços ',vazio)
    print('bombas restantes', bombas)
    print(baixo)
    if bombas == 0: 
        print("-------------------achou um lugar para clicar--------------------------")
        for i in range(0, len(baixo)):
            if baixo[i] == 0:
                p.moveTo(position[i][0] + quadX / 2 ,position[i][1] + quadY / 2)
                p.click()
                time.sleep(0.3)
                p.screenshot("quad.png", region=(position[i][0] ,position[i][1], quadX, quadY))
                t = compare()
                if (t != 6):
                    encontrar(t, position[i][0],position[i][1]) 

        
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
            # if win() == True:
            #     return 
            image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
            contador+=1
            # image.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\minas\resolver-minas\img\image{}.png'.format(contador)) #opera
            image.save(r'C:\Users\Aluno\Desktop\resolver-minas\img\image{}.png'.format(contador)) #google
            print(contador)
            t = compare()
            if (t != 6):
                # p.moveTo(quadStartX,quadStartY)
                encontrar(t,quadStartX, quadStartY) 
            quadStartX += quadX
        quadStartX = startX
        quadStartY += quadY


#----------------------ABRIR o jogo--------------------------------      
def abrir ():
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
    p.moveTo(947,568)
    p.click()

    # p.moveTo(437,298) #opera
    # p.click()
    # p.moveTo(432,331)
    # p.click()
    # p.moveTo(434,382)
    # p.click()

    time.sleep(1)
    foto()
    p.PAUSE = 0

    q = 0
    while prox == True:
        q = q + 1
        percorrer()
        if (q > 10):
            break
    p.alert("o loop terminou")     

    # time.sleep(2)
    # percorrer()
    # p.alert("o loop terminou")               

abrir()
# color('img/5.png')
