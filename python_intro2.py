#Introdução ao Python 2 -Funções
import time 

def hi(n):

  for i in range(1,n):
      time.sleep(1)
      print(i)
      
hi(int(input("Timer:")))