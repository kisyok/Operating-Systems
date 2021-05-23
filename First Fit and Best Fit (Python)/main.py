def firstFit(blockSize, blockNum, programSize, programNum):
    print("\nFirst Fit Memory Allocation")
    # each program is stored in which block
    allocation = [-1] * programNum
    # to check if the block is occupied or not
    occupied = [-1] * blockNum
    # -1 - free, 1 - occupied

    for i in range(programNum):
        for j in range(blockNum):
            if blockSize[j] >= programSize[i] and occupied[j]==-1:
                allocation[i] = j
                occupied[j] = 1
                break

    print("Block size: ", blockSize)
    print("Program size:", programSize)
    print("Process No.     Process Size     Block No.")
    for i in range(programNum):
        print("   ", i+1, "             ", programSize[i], "           ", end=" " )
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not allocated")

def bestFit(blockSize, blockNum, programSize, programNum):
    print("\nBest Fit Memory Allocation")
    allocation = [-1] * programNum
    occupied = [-1] * blockNum

    for i in range(programNum):
        bestBlock = -1
        for j in range(blockNum):
            if blockSize[j] >= programSize[i] and occupied[j]==-1:
                if bestBlock == -1:
                    bestBlock = j
                elif blockSize[bestBlock] > blockSize[j]:
                    bestBlock = j

        if bestBlock != -1:
            allocation[i] = bestBlock
            occupied[bestBlock] = 1

    print("Block size: ", blockSize)
    print("Program size:", programSize)
    print("Process No.     Process Size     Block No.")
    for i in range(programNum):
        print("   ", i + 1, "             ", programSize[i], "           ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not allocated")

if __name__ == '__main__':
    blockNum = int(input("Number of free memory block: "))
    blockSize = [0] * blockNum
    for i in range(0, blockNum, 1):
        blockSize[i] = int(input("Block size: "))

    programNum = int(input("Number of program: "))
    programSize = [0] * programNum
    for i in range(0, programNum, 1):
        programSize[i] = int(input("Program size: "))

    # blockSize = [15, 20, 30, 50]
    # blockNum = 4
    # programSize = [10, 20, 30, 60]
    # programNum = 4

    # blockSize = [100, 500, 200, 300, 600]
    # blockNum = 5
    # programSize = [212, 417, 112, 426]
    # programNum = 4


    firstFit(blockSize, blockNum, programSize, programNum)
    bestFit(blockSize, blockNum, programSize, programNum)



