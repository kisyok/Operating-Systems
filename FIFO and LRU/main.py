def fifo(frame_num, page):
    print("\nPage Replacement Algorithm: FIFO\n")
    print(" Page |  Frame [ ", end="")
    for i in range(frame_num):
        print(i, end=" ")
    print("]  |  Page Fault")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    frame = []
    fault_count = 0
    top = 0
    p_fault = 'X'

    for i in page:
        if i not in frame:  # page not found in frame
            if len(frame) < frame_num:  # there are space in frame(not full yet)
                frame.append(i)
            else:  # frame fully occupied
                frame[top] = i  # fifo
                top = (top + 1) % frame_num  # to make sure top is always in rage of index
            fault_count += 1
            p_fault = '✔'
        else:  # page found in frame
            p_fault = 'X'
        print("   %d\t\t\t " % i, end='')  # to print page
        for j in frame:  # to print frame
            print(j, end=' ')
        for j in range(frame_num - len(frame)):  # to create space
            print(' ', end=' ')
        print("          %s" % p_fault)  # print page fault
    print("\nTotal page fault = ", fault_count)
    print("Failure Rate = %0.2f" % ((fault_count/len(page))*100), "%")
    print("Success Rate = %0.2f" % (100-((fault_count/len(page))*100)), "%")


def lru(frame_num, page):
    print("\nPage Replacement Algorithm: LRU\n")
    print(" Page |  Frame [ ", end="")
    for i in range(frame_num):
        print(i, end=" ")
    print("]  |  Page Fault  |  temp[]")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    frame = []
    fault_count = 0
    p_fault = 'X'
    temp = []  # to store the ref num

    for i in page:
        if i not in frame:  # page not found in frame
            if len(frame) < frame_num:  # there are space in frame(not full yet)
                frame.append(i)
                temp.append(len(frame) - 1)  # store ref num
            else:  # LRU
                lru = temp.pop(0)  # get the ref num that is least recently used
                frame[lru] = i  # replace the page at that frame
                temp.append(lru)  # this page will be most recently used
            p_fault = '✔'
            fault_count += 1
        else:  # page found in frame
            temp.append(temp.pop(temp.index(frame.index(i))))  # to rearrange the ref num
            p_fault = 'X'
        print("   %d\t\t\t " % i, end='')  # to print page
        for j in frame:  # to print frame
            print(j, end=' ')
        for j in range(frame_num - len(frame)):
            print(' ', end=' ')  # to create space
        print("          %s" % p_fault, end="\t\t  ")  # print page fault
        print(temp)
    print("\nTotal page fault = ", fault_count)
    print("Failure Rate = %0.2f" % ((fault_count / len(page)) * 100), "%")
    print("Success Rate = %0.2f" % (100 - ((fault_count / len(page)) * 100)), "%")


if __name__ == '__main__':
    frameNum = int(input("Number of page frames: "))
    pageNum = int(input("Number of page: "))
    page = [0] * pageNum
    for i in range(pageNum):
        print("Page", i, ":", end=" ")
        page[i] = int(input())
    fifo(frameNum, page)
    lru(frameNum, page)

