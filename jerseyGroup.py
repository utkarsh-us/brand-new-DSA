"""Problem Statement:

Emerson, the sports teacher, wants to pair up students in his sports class to practice a game and assign a unique group ID to each pair. To determine the group ID, Emerson needs to find the largest positive integer that can evenly divide the jersey numbers of both students in a pair without leaving a remainder.

Write an algorithm to help Emerson find the group ID for two given students. Given the jersey numbers of two students, you need to calculate and output the group ID.

Input:
- Two integers, jerseyNum1 and jerseyNum2, representing the jersey numbers of two students. (0 ≤ jerseyNum1, jerseyNum2 < 10^9)

Output:
- An integer representing the group ID of the two students, which is the largest positive integer that divides both jersey numbers without a remainder.

Your task is to write a function or program that can calculate the group ID based on the input jersey numbers and output the result."""



# code-

def groupID(jerseyNum1, jerseyNum2):
    while jerseyNum2:
        jerseyNum1, jerseyNum2 = jerseyNum2, jerseyNum1 % jerseyNum2
    return jerseyNum1

def main():
    jerseyNum1 = int(input("Enter the jersey number of the first student: "))
    jerseyNum2 = int(input("Enter the jersey number of the second student: "))
    result = groupID(jerseyNum1, jerseyNum2)
    print("The group ID is:", result)

if __name__ == "__main__":
    main()



"""I provided you with a Python program that calculates the greatest common divisor (GCD), which is the group ID in this problem. Here's how it works:

1. We define a function named groupID that takes two parameters, jerseyNum1 and jerseyNum2. This function calculates the GCD of these two numbers using the Euclidean algorithm, which repeatedly takes the remainder of the larger number divided by the smaller number until the remainder becomes zero. The GCD is the last non-zero remainder.

2. In the main function:
   - We take user input for jerseyNum1 and jerseyNum2.
   - We call the groupID function to calculate the group ID (GCD) of the two jersey numbers.
   - We print the calculated group ID.

The if __name__ == "__main__": condition ensures that the main function is executed when you run the script as a standalone program.

So, the program takes the jersey numbers of two students as input, calculates their group ID (GCD), and then prints the result as the largest positive integer that divides both jersey numbers without a remainder."""
