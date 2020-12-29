#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener
from httpFunctions import getValidTokens, updateReserve

nums = '1234567890'
validTokens = getValidTokens()

currentString = "" 
httpResponse = False

def validateToken(token, tokensList):
    for t in tokensList:
        if token == t['token']: 
            return True
    
    return False

def handleEnter():

    global currentString, validTokens

    if validateToken(currentString, validTokens):
        print('Token valido')
        #httpResponse = updateReserve(currentString)
        #print(httpResponse.json())
        
    else:
        print('Token não cadastrado')
    
    currentString = ""

def handleKey(keyRaw):

    global validID, currentString, nums, httpResponse
    key = str(keyRaw)

    if "'" in key:
        key = key.replace("'", "")
    
    if key in nums and len(currentString) <= 10:
        currentString += key

    #if key == 'Key.enter':
        #handleEnter()

    if key == "\\x1a":
        exit()

    print(currentString)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog

print('Pronto para ler etiquetas!\n')

with Listener(on_press=handleKey) as l:
    l.join()

