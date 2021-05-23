def sequential(block, s_block, length, file_id, directory_entry):
    flag = 0
    l_block = s_block + length
    a = 0

    for j in range(s_block, l_block, 1):
        if block[j] == 0:
            flag = flag+1

    if length == flag:
        for k in range(s_block, l_block, 1):
            if block[k] == 0:
                block[k] = file_id
            a = a+1
        if a != (s_block+length-1):
            print("File", file_id, "is allocated to the disk\n")
            directory_entry.append(str(file_id) + "\t\t\t" + str(s_block) + "\t\t\t" + str(length))
    else:
        print("File", file_id, "is not allocated to the disk\n")


if __name__ == '__main__':
    blockNum = [0]*50
    fileNum = int(input("Enter number of files: "))
    directory = []
    print()

    for i in range(fileNum):
        print("File", i+1)
        start_block = int(input("Enter the starting block: "))
        block_length = int(input("Enter the length of the file: "))
        print("")
        sequential(blockNum, start_block, block_length, i+1, directory)

    print("Sequential File Allocation:")
    for i in range(len(blockNum)):
        print(i, "->", blockNum[i], end="\t\t")
        if (i+1) % 10 == 0:
            print()

    print("\nDirectory: ")
    print("File\t\tStart\t\tlength")
    for i in range(len(directory)):
        print(directory[i])
