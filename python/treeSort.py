
# Python3 program to
# implement Tree Sort
 
# Class containing left and
# right child of current
# node and key value 
from tokenize import String
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
 
datoss = ["../data/data_100.txt",
"../data/data_1000.txt",		
"../data/data_2000.txt",		
"../data/data_3000.txt",		
"../data/data_4000.txt",		
"../data/data_5000.txt",		
"../data/data_6000.txt",	
"../data/data_7000.txt",		
"../data/data_8000.txt",		
"../data/data_9000.txt",		
"../data/data_10000.txt",
"../data/data_20000.txt",		
"../data/data_30000.txt",		
"../data/data_40000.txt",		
"../data/data_50000.txt",		
"../data/data_100000.txt",		
"../data/data_200000.txt",		
"../data/data_300000.txt",		
"../data/data_400000.txt",
"../data/data_500000.txt"]
for x in range(0,len(datoss)):
  a2 = np.loadtxt(datoss[x], dtype=int)
  inicio = time.time()
  inorderRec(root)
  treeins(a2)
  fin = time.time()
  print(  fin-inicio)
  root = None