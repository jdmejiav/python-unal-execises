n = int(input())
salida =[]
tabla_morse = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--..",
    ".":".-.-.-",
    ",":"-.-.--",
}

for i in range(0,n):
    entrada = input()
    entrada = entrada.lower()
    temp = ""
    for i in entrada:
        try:
            temp+=tabla_morse[i]+" "
        except:
            if i == " ":
                temp+="/ "
    print(temp)
