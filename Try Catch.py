#try , catch


try:
    with open('test.txt' , 'r') as reader:
         reader.read()
except Exception as e:
    print(e)

    
try:
    with open('test.txt','r') as reader:

finally:
    print("clean")