import sys
import time

import shapeContainer

ERROR_UNKNOWN_ARGS = 'Invalid arguments. \n Expected:\n command -f infile outfile01 outfile02\nOr:\ncommand -n ' \
                     'number outfile01 outfile02\n '

if __name__ == '__main__':
    startTime = time.time()
    mainContainer = shapeContainer.ShapeContainer()
    args = sys.argv
    print("Program init")
    #input
    if len(args) < 5:
        print(ERROR_UNKNOWN_ARGS)
        exit(0)
    if args[1] == '-f':
        mainContainer.readFile(args[2])
    elif args[1] == '-n':
        if int(args[2]) > 10000 or int(args[2]) < 1:
            print("Invalid input: can't generate less than 1 or more than 10000 shapes!")
            exit(0)

        mainContainer.initRandom(args[2])
    else:
        print(ERROR_UNKNOWN_ARGS)
        exit(0)

    mainContainer.outputContainer(args[3])

    mainContainer.bubbleSort()

    mainContainer.outputContainer(args[4])

    endTime = time.time()
    print(f"execution took {(endTime - startTime):.10f} seconds")
