from eliza import Eliza

def main():
    pass

if __name__ == "__main__":
    main()
    eliza1 = Eliza()
    while True:
        statement = input("> ")
        print (eliza1.analyze(statement))
 
        if statement == "quit":
            break
