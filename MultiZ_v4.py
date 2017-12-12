#! python3

# argument 1 is the input file (needs to exist)
# argument 2 is what you want to name it (something that doesn't already exist or it will be overwritten)
import sys

InFile = open(sys.argv[1], 'r')
OutFile = open(sys.argv[2], "w")
proton = 1.007276
#initialize the counter to keep track of line numbers
LineNumber = 0

#loop through each line in the file
for line in InFile:
    #skipping the first 3 lines
    if LineNumber>2:
        #preparing variables
        ElementList = line.split('\t')
        mass = float(ElementList[8])
        charge = float(ElementList[9])
        if charge == 2:
            OutFile.write(line)
            ElementList[8] = str((mass * (charge+1.0)*proton)/(charge+1.0))
            ElementList[9] = str(charge+1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            PlusOne = "\t".join(ElementList)
            OutFile.write(PlusOne)
            ElementList[8] = str((mass * (charge+2.0)*proton)/(charge+2.0))
            ElementList[9] = str(charge+2.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            PlusTwo = "\t".join(ElementList)
            OutFile.write(PlusTwo)
        if charge == 3:
            OutFile.write(line)
            ElementList[8] = str((mass * (charge-1.0)*proton)/(charge-1.0))
            ElementList[9] = str(charge-1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            MinusOne = "\t".join(ElementList)
            OutFile.write(MinusOne)
            ElementList[8] = str((mass * (charge+1.0)*proton)/(charge+1.0))
            ElementList[9] = str(charge+1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            PlusOne = "\t".join(ElementList)
            OutFile.write(PlusOne)
            ElementList[8] = str((mass * (charge+2.0)*proton)/(charge+2.0))
            ElementList[9] = str(charge+2.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            PlusTwo = "\t".join(ElementList)
            OutFile.write(PlusTwo)
        if charge == 4:
            OutFile.write(line)
            ElementList[8] = str((mass * (charge-2.0)*proton)/(charge-2.0))
            ElementList[9] = str(charge-2.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            MinusTwo = "\t".join(ElementList)
            OutFile.write(MinusTwo)
            ElementList[8] = str((mass * (charge-1.0)*proton)/(charge-1.0))
            ElementList[9] = str(charge-1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            MinusOne = "\t".join(ElementList)
            OutFile.write(MinusOne)
            ElementList[8] = str((mass * (charge+1.0)*proton)/(charge+1.0))
            ElementList[9] = str(charge+1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            PlusOne = "\t".join(ElementList)
            OutFile.write(PlusOne)
        if charge == 5:
            OutFile.write(line)
            ElementList[8] = str((mass * (charge-2.0)*proton)/(charge-2.0))
            ElementList[9] = str(charge-2.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            MinusTwo = "\t".join(ElementList)
            OutFile.write(MinusTwo)
            ElementList[8] = str((mass * (charge-1.0)*proton)/(charge-1.0))
            ElementList[9] = str(charge-1.0)
            ElementList[10] = "n/a"
            ElementList[15] = "n/a"
            ElementList[16] = "n/a"
            MinusOne = "\t".join(ElementList)
            OutFile.write(MinusOne)
    else:
        OutFile.write(line)
    LineNumber = LineNumber + 1
InFile.close()
OutFile.close()

# for copy/pasting if needed later:
# ElementList[8] = str((mass * (charge-2.0)*proton)/(charge-2.0))
# ElementList[9] = str(charge-2.0)
# MinusTwo = "\t".join(ElementList)
# OutFile.write(MinusTwo)
# ElementList[8] = str((mass * (charge-1.0)*proton)/(charge-1.0))
# ElementList[9] = str(charge-1.0)
# MinusOne = "\t".join(ElementList)
# OutFile.write(MinusOne)
# ElementList[8] = str((mass * (charge+1.0)*proton)/(charge+1.0))
# ElementList[9] = str(charge+1.0)
# PlusOne = "\t".join(ElementList)
# OutFile.write(PlusOne)
# ElementList[8] = str((mass * (charge+2.0)*proton)/(charge+2.0))
# ElementList[9] = str(charge+2.0)
# PlusTwo = "\t".join(ElementList)
# OutFile.write(PlusTwo)
# ElementList[10] = "n/a"
# ElementList[15] = "n/a"
# ElementList[16] = "n/a"