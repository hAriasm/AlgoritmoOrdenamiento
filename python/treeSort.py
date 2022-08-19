
# Python3 program to
# implement Tree Sort
 
# Class containing left and
# right child of current
# node and key value 
import numpy as np
from timeit import default_timer
import time

class Node:
 
  def __init__(self,item = 0):
    self.key = item
    self.left,self.right = None,None
 
 
# Root of BST
root = Node()
 
root = None
 
# This method mainly
# calls insertRec()
def insert(key):
  global root
  root = insertRec(root, key)
 
# A recursive function to
# insert a new key in BST
def insertRec(root, key):
 
  # If the tree is empty,
  # return a new node
 
  if (root == None):
    root = Node(key)
    return root
 
  # Otherwise, recur
  # down the tree
  if (key < root.key):
    root.left = insertRec(root.left, key)
  elif (key > root.key):
    root.right = insertRec(root.right, key)
 
  # return the root
  return root
 
# A function to do
# inorder traversal of BST
def inorderRec(root):
  if (root != None):
    inorderRec(root.left)
   # print(root.key ,end = " ")
    inorderRec(root.right)
   
def treeins(arr):
  for i in range(len(arr)):
    insert(arr[i])
 
 
# Driver Code

#a2 = np.loadtxt('../data/data_5000.txt', dtype=int)
#print(a2)
#inicio = default_timer()
#treeins(a2)
#inorderRec(root)
#fin = default_timer()
#print( fin-inicio)
#root= None 
 

array_100 = np.loadtxt('..\data\data_100.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_100= fin-inicio
print(t_100)
root= None 
array_1000 = np.loadtxt('..\data\data_1000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_1000= fin-inicio
print(t_1000)
root= None 
array_2000 = np.loadtxt('..\data\data_2000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_2000= fin-inicio
print(t_2000)
root= None 
array_3000 = np.loadtxt('..\data\data_3000.txt', dtype=int)
inicio = time.time() 
inorderRec(root) 
fin = time.time()
t_3000= fin-inicio
print(t_3000)

root= None 
array_4000 = np.loadtxt('..\data\data_4000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time() 
t_4000= fin-inicio
print(t_4000)

root= None 
array_5000 = np.loadtxt('..\data\data_5000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_5000= fin-inicio
print(t_5000)
root= None 
array_6000 = np.loadtxt('..\data\data_6000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_6000= fin-inicio
print(t_6000)
root= None 
array_7000 = np.loadtxt('..\data\data_7000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_7000= fin-inicio
print(t_7000)
root= None  
array_8000 = np.loadtxt('..\data\data_8000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_8000= fin-inicio
print(t_8000)
root= None  
array_9000 = np.loadtxt('..\data\data_9000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_9000= fin-inicio
print(t_9000)
root= None 
array_10000 = np.loadtxt('..\data\data_10000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_10000= fin-inicio
print(t_10000)
root= None 
array_20000 = np.loadtxt('..\data\data_20000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_20000= fin-inicio
print(t_20000)
root= None 
array_30000 = np.loadtxt('..\data\data_30000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_30000= fin-inicio
print(t_30000)
root= None 
array_40000 = np.loadtxt('..\data\data_40000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_40000= fin-inicio
print(t_40000)
root= None 
array_50000 = np.loadtxt('..\data\data_50000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_50000= fin-inicio
print(t_50000)
root= None 
array_100000 = np.loadtxt('..\data\data_100000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_100000= fin-inicio
print(t_100000)
root= None 
array_200000 = np.loadtxt('..\data\data_200000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_200000= fin-inicio
print(t_200000)
root= None 
array_300000 = np.loadtxt('..\data\data_300000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_300000= fin-inicio
print(t_300000)
root= None 
array_400000 = np.loadtxt('..\data\data_400000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_400000= fin-inicio
print(t_400000)
root= None 
array_500000 = np.loadtxt('..\data\data_500000.txt', dtype=int)
inicio = time.time() 
inorderRec(root)
fin = time.time()
t_500000= fin-inicio
print(t_500000)
root= None 