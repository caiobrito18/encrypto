import numpy as np
import re


def transcriptToNums(messsage):

    alphaArray = ["a", "b", "c", "d", "e", "f", "g", "h",
                  "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v",
                  "w", "x", "y", "z", ".", "!", "#", " "]
    transArray = []
    for i in messsage:
        transArray.append(alphaArray.index(i)+1)
    if len(messsage) % 2 != 0:
        transArray.append(30)
    return np.array(transArray, dtype=object)


def transcriptToTxt(message):
    alphaArray = np.array(["a", "b", "c", "d", "e", "f", "g", "h",
                           "i", "j", "k", "l", "m", "n",
                           "o", "p", "q", "r", "s", "t", "u", "v",
                           "w", "x", "y", "z", ".", "!", "#", " "])
    transArray = []
    counter1 = 0
    for i in message:
        transArray.append(
            alphaArray[message[counter1][0].astype(int).__getitem__(0)-1])
        counter1 += 1
    arrayOutput = []
    arrayOutput.append(transArray.__getitem__(0)[0])
    arrayOutput.append(transArray.__getitem__(1)[0])
    textOutput = "" + \
        arrayOutput.__getitem__(0).__str__() + \
        arrayOutput.__getitem__(1).__str__()
    # print(transArray.__getitem__(0)[0].__str__())
    print(textOutput)
    return textOutput


def split(arr):
    arrs = []
    array1 = arr[:int(len(arr)/2)]
    array2 = arr[int(len(arr)/2):]
    for i in range(int(len(arr)/2)):
        arrs.append([int(array1[i]), int(array2[i])])
    return arrs


def encrypt(numsArray, key):
    keys = re.split(",", key)
    # array1 = numsArray[:int(len(numsArray)/2)]
    # array2 = numsArray[int(len(numsArray)/2):]
    array1 = split(numsArray)
    matrix = np.matrix(array1, dtype=object)
    encryptKey = np.matrix([[keys[0], keys[1]],
                            [keys[2], keys[3]]], dtype=float)
    # print(np.matrix(array1))
    # print(np.matrix(encryptKey))
    encrypted = np.matrix_transpose(matrix@encryptKey)
    return np.array(encrypted, dtype=float)


def decrypt(message, key):
    keys = re.split(",", key)
    dcryptKey = np.matrix([[keys[0], keys[2]],
                           [keys[1], keys[3]]], dtype=float)
    dcryptKey = np.linalg.inv(dcryptKey)
    matrixMessage = split(message.split(', '))
    print(np.matrix(matrixMessage))
    return np.matrix_transpose(matrixMessage@dcryptKey)


def main():
    opt = int(input("Gostaria de encriptar(1) ou decriptar(2)?"))
    match opt:
        case 1:
            msg = input("Insira a mensagem; (somente minúsculas)\n")
            key = input("Insira a matriz chave; formato:11,12,21,22\n")
            print(encrypt(transcriptToNums(msg), key))
        case 2:
            msg = input(
                "Insira a mensagem crptografada; 1, 2, 3, 4, 5, n, ...*COM ', '*\n")
            key = input("Insira a matriz chave; formato:11,12,21,22\n")
            decrypted = decrypt(msg, key)
            print(decrypted)
            print(transcriptToTxt(decrypted))

    # text = "quanta verdade seu espirito suporta"
    # text = "your lips my lips apocalypse"
    # transcripted = transcriptToNums(text)
    # secret = encrypt(transcripted)
    # print(transcripted)
    # print('')
    # print(np.matrix(secret))


main()
#
# brokenSecret = decrypt()
# print(brokenSecret)
# prinut(transcriptToTxt(brokenSecret))
