from eliza import * 

def main():
    running = True
    print("Hello, I'm Eliza. How are you feeling today?")
    while running:
        userInput = input("\n> ")
        if userInput == "quit":
            running = False
            print("Have a great day!")
        print(response(userInput))

if __name__ == "__main__":
    main()