from puzzle import *

print ("\n***** 15-Puzzle Solver *****\n")

print("What puzzle do you want to use?\n"
      "1. Generate puzzle randomly\n"
      "2. Import from file")
u_input = int(input("> ")); print()

if (u_input == 1):
    puzzleToSolve = puzzle.initializePuzzle()
elif (u_input == 2):
    print("Enter your file or choose an existing one?\n"
          "1. My file\n"
          "2. Existing files")
    u_input = int(input("> ")); print()

    if (u_input == 1):
        filePath = input("Enter file path: "); print()
        puzzleToSolve = puzzle.initializePuzzle(filePath)
    elif (u_input == 2):
        print("Available puzzles:\n"
              "1. Puzzle do\n"
              "2. Puzzle re\n"
              "3. Puzzle mi\n"
              "4. Puzzle fa\n"
              "5. Puzzle sol")
        u_input = int(input("> ")); print()    

        listOfPaths = ["./test-case/tc1.txt",
                       "./test-case/tc2.txt",
                       "./test-case/tc3.txt",
                       "./test-case/tc4.txt",
                       "./test-case/tc5.txt",]    
        puzzleToSolve = puzzle.initializePuzzle(listOfPaths[u_input-1])

print("Your puzzle: ")
puzzleToSolve.printPuzzle()
print("Solving the puzzle...")
puzzleToSolve.solve()

if (puzzleToSolve.isSolved()):
    print("Your puzzle is successfuly solved!\n")

    print("This is how the puzzle being operated...")
    puzzleToSolve.printSolution()

else:
    print("Ah, your puzzle cannot be solved!\n")

print("Total puzzle's configurations checked: {}".format(puzzleToSolve.getTotalGeneratedNodes()))
print("Time taken in solving puzzle: {} seconds\n".format(puzzleToSolve.getTimeTaken()))

print("Fyi, there are some ways to determine whether the puzzle can actually be solved or not.\n")

print("Now, take a look at Kurang function values of your puzzle...")
puzzleToSolve.printKurangValues()

TotalOfKurangPlusX = puzzleToSolve.getTotalOfKurangPlusX()
print("Then, sum all those Kurang values and plus it with X value. We got:\n"
      "KurangTotalPlusX = {}\n".format(TotalOfKurangPlusX))

print("So, basically if that total value results in even number, the puzzle can be solved;\n"
      "{:4}if the result is in odd number, the puzzle cannot be solved.".format(" "))