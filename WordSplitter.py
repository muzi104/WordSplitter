from regex import *

file = "words.txt"
lineNo = 1    # line no in file
temp = ""     # store word
Qotation = False
qoutationCount = 0
addCount = 0
equalCount = 0
addFlag = False
equalFlag = False
minusFlag = False
minusCount = 0
multiplyFlag = False
divideFlag = False
moduloFlag = False
notFlag = False
lessthanFlag = False
greaterthanFlag = False
char = ""
AndCount = 0
AndFlag = False
orCount = 0
orFlag = False


def printWord(string):

    global temp
    global char
    global lineNo

    file2 = open("lexical.txt", "a")
    file2.write("{0} {1} {2}\n ".format(str(is_keyword(temp)), temp, lineNo))
    file2.close()
    temp = ""
    
    



def wordCount(file):

    global lineNo
    global temp
    global Qotation
    global qoutationCount
    global addCount
    global equalCount
    global addFlag
    global equalFlag
    global minusCount
    global minusFlag
    global multiplyFlag
    global moduloFlag
    global divideFlag
    global notFlag
    global greaterthanFlag
    global lessthanFlag
    global char
    global AndCount
    global AndFlag
    global orCount
    global orFlag

    punctuator = [',', ';', '(', ')', '{', '}', '[', ']', ':', '?']

    with open(file, 'r') as files:  # open and close files
        for line in files:             # iterate through lines in file
            for char in line:          # iterate through character in a line

                # if new line character founded , print temp increase line no by 1 and reset char and temp
                if char == "\n" and Qotation == False:
                    if temp != "":
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""
                        lineNo += 1
                        print(lineNo)
                    else:
                        temp = ""
                        char = ""
                        lineNo += 1
                        print(lineNo)

                if char == " " and Qotation == True:
                    temp+char
                elif char == " ":
                    addFlag = False
                    addCount = 0
                    minusCount = 0
                    minusFlag = False
                    equalFlag = False
                    multiplyFlag = False
                    equalCount = 0
                    AndCount = 0
                    AndFlag = False
                    orCount = 0
                    orFlag = False
                    if temp != "":
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""
                    char = ""

                if char in punctuator and Qotation == True:
                    temp+char
                elif char in punctuator:
                    if temp != "":
                        print(temp, lineNo)
                        printWord(temp)
                    print(char, lineNo)
                    char = ""

                if char == "\"":
                    Qotation = True
                    qoutationCount += 1

                    if temp != "" and qoutationCount == 1:
                        print(temp, lineNo)
                        printWord(temp)

                    if char == "\"" and qoutationCount == 2:
                        qoutationCount = 0
                        Qotation = False
                        print(temp, lineNo)
                        printWord(temp)

                    char = ""

                elif char == "\n" and qoutationCount == 1:
                    qoutationCount = 0
                    Qotation = False
                    print(temp, lineNo)
                    printWord(temp)
                    char = ""
                    lineNo += 1
                    print(lineNo)

                if char == "+" and Qotation == True:
                    temp+char
                elif char == "+":
                    addCount += 1
                    if temp != "" and addFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    addFlag = True
                    if temp != "" and addCount == 2:
                        addCount = 0
                        addFlag = False
                        temp = temp+char
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "+" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "+" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False
                    char = ""

                if "+" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "+" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    addCount = 0
                    addFlag = False

                # minus
                if char == "-" and Qotation == True:
                    temp+char
                elif char == "-":
                    minusCount += 1
                    if temp != "" and minusFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    minusFlag = True
                    if temp != "" and minusCount == 2:
                        minusCount = 0
                        minusFlag = False
                        temp = temp+char
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "-" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "-" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    minusCount = 0
                    minusFlag = False
                    char = ""

                if "-" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "-" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    minusCount = 0
                    minusFlag = False

                # multiply
                if char == "*" and Qotation == True:
                    temp+char
                elif char == "*":
                    if temp != "" and multiplyFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    multiplyFlag = True

                if "*" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "*" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    multiplyFlag = False
                    char = ""

                if "*" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "*" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    multiplyFlag = False

                # divide
                if char == "/" and Qotation == True:
                    temp+char
                elif char == "/":
                    if temp != "" and divideFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    divideFlag = True

                if "/" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "/" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    divideFlag = False
                    char = ""

                if "/" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "/" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    divideFlag = False

                # modulo
                if char == "%" and Qotation == True:
                    temp+char
                elif char == "%":
                    if temp != "" and moduloFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    moduloFlag = True

                if "%" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "%" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    moduloFlag = False
                    char = ""

                if "%" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "%" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    moduloFlag = False

                # not condition
                if char == "!" and Qotation == True:
                    temp+char
                elif char == "!":
                    if temp != "" and notFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    notFlag = True

                if "!" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "!" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    notFlag = False
                    char = ""

                if "!" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "!" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    notFlag = False

                # greater than condition
                if char == "<" and Qotation == True:
                    temp+char
                elif char == "<":
                    if temp != "" and greaterthanFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    greaterthanFlag = True

                if "<" in temp and char == "=" and Qotation == True:
                    temp+char
                elif "<" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    greaterthanFlag = False
                    char = ""

                if "<" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "<" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    greaterthanFlag = False

                # less than condition
                if char == ">" and Qotation == True:
                    temp+char
                elif char == ">":
                    if temp != "" and lessthanFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    lessthanFlag = True

                if ">" in temp and char == "=" and Qotation == True:
                    temp+char
                elif ">" in temp and char == "=":
                    temp = temp+char
                    print(temp, lineNo)
                    printWord(temp)
                    lessthanFlag = False
                    char = ""

                if ">" in temp and char != "=" and Qotation == True:
                    temp+char
                elif ">" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    lessthanFlag = False

                # && condition
                if char == "&" and Qotation == True:
                    temp+char
                elif char == "&":
                    AndCount += 1
                    if temp != "" and AndFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    AndFlag = True
                    if temp != "" and AndCount == 2:
                        AndCount = 0
                        AndFlag = False
                        temp = temp+char
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""

                # || condition
                if char == "|" and Qotation == True:
                    temp+char
                elif char == "|":
                    orCount += 1
                    if temp != "" and orFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    orFlag = True
                    if temp != "" and orCount == 2:
                        orCount = 0
                        orFlag = False
                        temp = temp+char
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""

                # equals condition
                if char == "=" and Qotation == True:
                    temp+char
                elif char == "=":
                    equalCount += 1
                    if temp != "" and equalFlag == False:
                        print(temp, lineNo)
                        printWord(temp)
                    equalFlag = True
                    if temp != "" and equalCount == 2:
                        equalCount = 0
                        equalFlag = False
                        temp = temp+char
                        print(temp, lineNo)
                        printWord(temp)
                        char = ""

                if "=" in temp and char != "=" and Qotation == True:
                    temp+char
                elif "=" in temp and char != "=":
                    print(temp, lineNo)
                    printWord(temp)
                    equalCount = 0
                    equalFlag = False

                temp = temp+char


wordCount(file)
