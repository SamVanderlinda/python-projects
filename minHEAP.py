# A min heap tree that starts with a random set of numbers in every node then sorts them accordingly
import random as rand

#The Heap is represented in this array
array = [None] * 11

#Print tree
def tree():

    print('Min Heap Tree')
    print('      ', array[1],'    ')
    print('     /   \    ')
    print('   ',array[3],'   ',array[4],' ')
    print('   /  \  /  \ ')
    print(' ',array[7],'  ',array[8],array[9],' ',array[10])

#Bubbles lowest number to parent; (node, node, parent index, child dirction)
def bubbling(parent, k):
    
    posL = 2*k +1
    posR = 2*k +2
    
    childL = array[posL]
    childR = array[posR]

    if parent > childL:
        birth(parent, childL, k, posL)
    
    if parent > childR:
        birth(parent, childR, k, posR)

def birth(parent, child, k, pos):
    if parent > child:
        store = parent
        array[k] = child
        array[pos] = store

def main():

    t = 1
    store = 0
    while t < 11:
        array[t] = rand.randint(0,9)
        t = t + 1

    tree()

    #While loop to loop through all nodes to form proper min heap structure
    while(array[1] > array[3] or array[1] > array[4] or array [3] > array[7] or array[3] > array[8] or array[4] > array[9] or array[4] > array[10]):

        bubbling(array[1], 1)

        bubbling(array[3], 3)
    
        bubbling(array[4], 4)
    

    tree()

main()
