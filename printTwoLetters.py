#Cameron Chromiak
#11-5
#Takes sting input then reprents 2 letters at a time. ya know, for fun.


def parse(word):
    indexCountEven = 0
    indexCountOdd = 1
    for i in word:
        print(word[indexCountEven]+word[indexCountOdd])
        indexCountEven +=2
        indexCountOdd +=2
        if i == '':
            break

        
def main():
    try:
            takeIn = str(input("Enter Word: "))
            parse(takeIn)
    except(ValueError):
        print("Error")
        main()

main()
