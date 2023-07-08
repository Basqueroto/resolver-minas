import pyautogui as p
import time
import cv2 as cv
import random
import sys
import tkinter
import customtkinter

def prog ():
    # startX = 623 #google 
    # startY = 313

    # fimX = 1297
    # fimY = 853

    # compX = 674 #google
    # compY = 540

    startX = 415 #opera
    startY = 361

    compX = 448 #opera
    compY = 361

    fimX = 863 #opera
    fimY = 722

    winX = 495  #opera
    winY = 363
    wCompX = 240
    wCompY = 11




    # dimenções do campo
    numColumns = 10
    numRows = 8

    quadX = 45
    quadY = 45
    quadStartX = 0
    quadStartY = 0

    prox = True
    contador = 0  
    opened = []
    randL = [] 
    for i in range(numColumns * numRows):
        opened.append(1)
    # print(len(opened))

    def color (image, li = 7, lf = 34, ci = 15, cf = 30, can = True): #quadrado padrão
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
        # print(medB, medV, medVer)
        return medB, medV, medVer, gf

    def foto():
        p.screenshot("boardInit.png", region=(startX, startY, compX, compY))

    def compare (pos = 0):
        (b,g,r,gf) = color('quad.png')
        # print(gf)
        if g < 205 and gf < 205:
            if b > 140 and g > 170 and r > 210:
                print ("fundo vermelho")
                opened[pos] = 2
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
            opened[pos] = 3
            return 6  

    # def win ():
    #     p.screenshot("win.png", region=(winX, winY, wCompX, wCompY))
    #     p.alert('foto dirada')
    #     (b, g, r, gf) = color('win.png', 0, 11, 0, 240, False)
    #     if b > 230:
    #         print ('vencemos')
    #         p.alert('antes do True')
    #         return 1
    #     else:
    #         return 2
        


    def encontrar (indice,x,y, pos = 0):
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
            # b.save(r'C:\Users\Aluno\Desktop\resolver-minas - Copia\imgachar\image{}.png'.format(i)) #google
            # b.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\resolver-minas - Copia\imgachar\image{}.png'.format(i)) #opera
            b = cv.imread("redor.png")
            (bg, gg, rF) = b[40, 40]
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
        if x >= 820: #varia
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
        if y >= 676: 
            voltar = [5,6,7]  
            for i in voltar:
                if baixo[i] != 2:
                    vazio += 1
                    baixo[i] = 2                                  


                    
        print('estão vazioes esses espaços ',vazio)
        print('bombas restantes', bombas)
        print(baixo)
        if bombas == 0: 
            # print("-------------------achou um lugar para clicar--------------------------")
            for i in range(0, len(baixo)):
                if baixo[i] == 0:
                    # p.alert('ele vai clicar')
                    p.moveTo(position[i][0] + quadX / 2 ,position[i][1] + quadY / 2)
                    p.click()
                    print((position[i][0] - startX) / quadX, int((position[i][1] - startY) / quadY * 10), '-----------< to calc')
                    opened[int((position[i][0] - startX) / quadX) + int((position[i][1] - startY) / quadY * 10)] = 1
                    # p.alert('clicou')
                    # print(opened)
                    # p.alert('ante')

                    # time.sleep(0.3)
                    # p.screenshot("quad.png", region=(position[i][0] ,position[i][1], quadX, quadY))
                    # t = compare()
                    # if (t != 6):
                    #     encontrar(t, position[i][0],position[i][1]) 
            opened[pos] = 2
            randL.clear()        
        elif 8 - vazio == bombas:
            # print("----------------dentro do if das bombas----------------")
            for i in range(0, len(baixo)):
                if baixo[i] == 0:
                    p.moveTo(position[i][0] + quadX / 2,position[i][1] + quadY / 2)
                    p.rightClick()
            opened[pos] = 2
            randL.clear()                   
        else:
            opened[pos] = 4

    # def rander(n):
    #     if n < 9:
    #         randlist = [n - 1, n + 1, n + 11, n + 10, n + 9]
    #     elif n >= 79:
    #         randlist = [n - 1, n - 11, n - 10, n - 9]    
    #     else:    
    #         randlist = [n - 1, n - 11, n - 10, n - 9, n + 1, n + 11, n + 10, n + 9]
    #     amostra = random.sample(randlist, 1)
    #     amostra = amostra[0]
    #     print(amostra)
    #     quadStartX = startX
    #     quadStartY = startY
    #     if n > 0:
    #         maisY = int(amostra // 10 * quadY)
    #         maisX = int(amostra % 10 * quadX)
    #         quadStartX += maisX
    #         quadStartY += maisY
    #     p.moveTo(quadStartX, quadStartY)
    #     p.click()    


    def percorrer ():
        win = False
        t = False
        p.screenshot("win.png", region=(winX, winY, wCompX, wCompY))
        (b, g, r, gf) = color('win.png', 0, 11, 0, 240, False)
        if b > 230:
            p.alert('ganhamos? ')
            print(opened)
            return True
        for i in range(len(opened)):
            if opened[i] == 1:
                loca = i
                t = True
                break

        if t == False:
            p.moveTo(startX,startY) 
            for i in range(len(opened)):
                if opened[i] == 3 or opened[i] == 4:
                    win = True
                    opened[i] = 1
            if win == True:        
                return
            else:
                p.alert('ganhamos?')
                return        
        quadStartX = startX
        quadStartY = startY
        print('o local é --------------->', loca)
        print(opened)
        if loca > 0:
            maisY = loca // 10 * quadY
            maisX = loca % 10 * quadX
            quadStartX += maisX
            quadStartY += maisY
            print("as posições em x e y ", loca % 10, loca // 10, '\n \n ')    
        image = p.screenshot("quad.png", region=(quadStartX, quadStartY, quadX, quadY))
        # contador+=1
        # image.save(r'C:\Users\Felipe Basqueroto\OneDrive\Área de Trabalho\resolver-minas - Copia\img\image{}.png'.format(contador)) #opera
        # image.save(r'C:\Users\Aluno\Desktop\resolver-minas - Copia\img\image{}.png'.format(contador)) #google
        # print(contador)
        t = compare(loca)
        if (t != 6):
            # p.moveTo(quadStartX,quadStartY)
            encontrar(t,quadStartX, quadStartY, loca) 
        print(randL)    


    #----------------------ABRIR o jogo--------------------------------      
    def abrir ():
        # p.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
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
        # p.moveTo(947,568)
        # # p.moveTo(startX + 30, startY + 30)
        # p.click()

        p.moveTo(437,298) #opera
        p.click()
        p.moveTo(432,331)
        p.click()
        p.moveTo(560,410)
        p.click()

        time.sleep(1)
        foto()
        p.PAUSE = 0.001
        q = 0
        while prox == True:
            # q = q + 1
            if percorrer() == True:
                break
            # if (q > 500): 
            #     break
        # p.alert("o loop terminou")     

        # time.sleep(2)
        # percorrer()
        # p.alert("o loop terminou") 
        prog()        

    def tela ():
        

        root_tk = tkinter.Tk()  # create the Tk window like you normally do
        root_tk.geometry("400x300")
        root_tk.title("Campo Minado")

        def button_function():
            root_tk.destroy()
            abrir()

        texto = customtkinter.CTkLabel(root_tk, text='aperte o botão para iniciar o bot', width=250, text_font=30)
        texto.pack(padx=10, pady=20)
        texto.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        customtkinter.disable_macos_darkmode()
        # Use CTkButton instead of tkinter Button
        button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function, text="Iniciar", width=200, height=32)
        button.pack(padx=10, pady=10)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        

        root_tk.mainloop()
    tela()

prog()