#Cameron Chromiak
#11-5
#Takes sting input then reprents 2 letters at a time. ya know, for fun.

#update 1.1 it still has index errors but they are concealed in a way that makes
#the program look like it works. It needs to be more flexible

def parse(word):
    indexCountEven = 0
    indexCountOdd = 1
    indexLen = len(word)
    if (indexLen % 2 == 0):
        try: 
            for i in range(0, indexLen):
                print(word[indexCountEven],word[indexCountOdd])
                indexCountEven +=2
                indexCountOdd +=2
        except IndexError:
            print("Finished")
    else: #odd number words 
        try:
            for i in range(0, indexLen -1):
                print(word[indexCountEven],word[indexCountOdd])
                indexCountEven +=2
                indexCountOdd +=2
            
                
        except IndexError:
            print(word[-1])
            print("Finished")
            #print("Index Error!") or that 
    main()      
        
def main():
    try:
        takeIn = str(input("Enter Word: "))
        if len(takeIn) > 1:
            parse(takeIn)
        else:
            print("Longer Word!")
            main()
    except(ValueError):
        print("Error")
        main()

main()
