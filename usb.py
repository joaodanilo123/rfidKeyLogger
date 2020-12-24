#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener
import requests

#definir a localização do arquivo de log
logFile = "D:/LOG.txt"
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
currentString = "" 
validID = False
host = 'http://localhost/sara/actions/atualizar_reserva.php'

httpResponse = False

def doRequest(id):
    r = requests.post(host, data = {'rfid': id})
    return r

def writeLog(key):

    global validID, currentString, nums, logFile, httpResponse
    keydata = str(key)

    if "'" in keydata:
        keydata = keydata.replace("'", "")
        if keydata in nums and len(currentString) <= 10:
            currentString += keydata
            #abrir o arquivo de log no modo append
            with open(logFile, "a") as f:
                f.write(keydata)

    elif keydata == 'Key.enter' and len(currentString) == 10:
        print(currentString)
        with open(logFile, "a") as f:
            f.write(currentString)
        
        httpResponse = doRequest(currentString)
        print(httpResponse.json())
        currentString = ""
        

    if keydata == "\\x1a":
        exit()


#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog

print('Pronto para ler etiquetas!\n')

with Listener(on_press=writeLog) as l:
    l.join()
