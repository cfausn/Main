"""
    vlc.py
    Colin Fausnaught

    Creates variable length length code from a file input and stores it in a heap, then
    prints the result.
"""


from rit_object import *
import math


class Node(rit_object):
    """
        An object to hold each symbol from the file.

        :param name: the name of the symbol
        :param freq: the number of occurrences of the symbol in the file
        :param codeword: the codeword of the symbol
    """
    __slots__ = ('name','freq','codeword')
    _types = (str,int,str)

class Heap(rit_object):
    """
        A heap which will hold Node objects

        :param array: a list of Node objects
        :param freq: the sum of all Node frequencies in the heap
    """
    __slots__ = ('array','freq')
    _types = (list,int)


def createEmptyHeap():
    """
        creates an empty heap and returns it
    """
    return Heap([],0)

def computeAverage(heap):
    """
        computes the average vlc codeword length based on the algorithm given
        in the lab.

        :param heap: the finished heap to have an average calculated from

        :return: average codeword length
        :rtype: float
    """
    avNum = 0
    avDenom = 0
    for elm in heap.array:
        avNum += len(elm.codeword) * elm.freq
        avDenom += elm.freq

    return avNum / avDenom



def sortHeap(heap,myList):
    """
        sorts the input of the file. Returns a list with only one
        element; a Heap.

        :param heap: initial heap, only used once in the function
        :param myList: a list filled with Heap and Node objects

        :return: myList, a list with only one element, a Heap
        :rtype: List
    """
    if len(myList) <= 1:
        return myList
    else:
        if heap.array == []:
            small = smallest(myList)
            small.codeword = "0" + small.codeword
            heap.array.append(small)
            myList.remove(small)

            secondSmall = smallest(myList)
            secondSmall.codeword = "1" + secondSmall.codeword
            heap.array.append(secondSmall)
            myList.remove(secondSmall)
            heap.freq = small.freq + secondSmall.freq

            myList.append(heap)

            if len(myList) != 1:
                return sortHeap(heap,myList)
            else:
                return myList
        else:
            small = smallest(myList)
            if isinstance(small, Heap):
                newList = myList[:]
                newList.remove(small)
                secondSmall = smallest(newList)

                if isinstance(secondSmall, Heap):
                    appendCodewords("0",small)
                    appendCodewords("1",secondSmall)
                    small.freq = small.freq + secondSmall.freq
                    combineHeaps(small,secondSmall)
                    myList.remove(secondSmall)

                    if len(myList) != 1:
                        return sortHeap(heap,myList)
                    else:
                        return myList
                else:
                    appendCodewords("0",small)
                    myList.remove(secondSmall)
                    secondSmall.codeword = "1" + secondSmall.codeword
                    small.array.append(secondSmall)
                    small.freq = small.freq + secondSmall.freq

                    if len(myList) != 1:
                        return sortHeap(heap,myList)
                    else:
                        return myList

            else:

                myList.remove(small)
                secondSmall = smallest(myList)
                if isinstance(secondSmall, Heap):
                    small.codeword = "0" + small.codeword
                    appendCodewords("1", secondSmall)
                    secondSmall.array.append(small)
                    secondSmall.freq = small.freq + secondSmall.freq

                    if len(myList) != 1:
                        return sortHeap(heap,myList)
                    else:
                        return myList

                else:

                    newHeap = createEmptyHeap()
                    small.codeword = "0" + small.codeword
                    newHeap.array.append(small)

                    myList.remove(secondSmall)
                    secondSmall.codeword = "1" + secondSmall.codeword
                    newHeap.array.append(secondSmall)
                    newHeap.freq = small.freq + secondSmall.freq

                    myList.append(newHeap)
                    if len(myList) != 1:
                        return sortHeap(heap,myList)
                    else:
                        return myList



def appendCodewords(num, heap):
    """
        appends all codewords in a heap based on the number
        passed. (codeword "0" with a passed "1" would change the codeword
        to "10")

        :param num: the number to be appended to the codewords in the heap
        :param heap: a heap to have codewords appended to
    """
    for elm in heap.array:
        elm.codeword = num + elm.codeword


def combineHeaps(heap1, heap2):
    """
        combines two heaps

        :param heap1: the first heap to be combined with another
        :param heap2: the second heap to be combined with
    """
    for elm in heap2.array:
        heap1.array.append(elm)

def smallest(myList):
    """
        Vital for this program. Finds the smallest value in a list
        and returns it.

        :param myList: a list object possibly filled with Nodes and Heaps

        :return small: the smallest value of the list
        :rtype: Node or Heap
    """
    small = myList[0]
    for elm in myList:
        if elm.freq <= small.freq:
            small = elm

    return small


def main():
    """
        gets input from a file, calls the sorting function, and
        then prints out the heap values.
    """
    mySet = set()
    myDict = dict()
    myList = list()

    filename = input("Enter file name: ")

    for line in open(filename):
        for letter in line:
            if letter == '\n':
                break
            elif not letter in mySet:
                mySet.add(letter)
                myDict[letter] = 1
            else:
                myDict[letter] += 1

    heap = createEmptyHeap()

    for key in myDict.keys():
        myList.append(Node(key,myDict[key],''))

    myList = sortHeap(heap,myList)
    print('Variable Length Code Output')
    print('----------------------------------------')

    for elm in myList[0].array:
        print('Symbol: %2s   ' % elm.name, end='')
        print('Codeword: %8s   ' % elm.codeword, end='')
        print('Frequency: %5d' %elm.freq)

    average = computeAverage(myList[0])
    avg_fixed_len = math.log(len(mySet),2)
    print()
    print("Average VLC codeword length: " + str(average) + " bits per symbol")
    print("Average fixed length codeword length: "+ str(avg_fixed_len) + " bits per symbol")


if __name__ == '__main__':
    main()
