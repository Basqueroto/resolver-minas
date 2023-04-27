import pyautogui as p
import time

p.alert("O código vai começar. Não utilize nada do computador até o código finalizar!")
p.PAUSE = 0.5

p.moveTo(1,1)

# abrir google
p.press('winleft')
p.write('google chrome')
p.press('enter')

# abrir campo minado
p.write('campo minado')
p.press('enter')
p.press('f11')
p.moveTo(567,600)
time.sleep(2000)
p.click()

p.moveTo(595,240)
p.click()
p.moveTo(595,265)
p.click()
p.moveTo(645,335)
p.click()

# ----------------------------------------lógica-----------------------------

