# Master Your Logic Building: map to TIP102

Source: the "MASTER YOUR LOGIC BUILDING (Before Starting DSA)" PDF. It has 6 phases and about 120 small problems with practice links on LeetCode, HackerRank, and GeeksforGeeks.

## Do I need to finish this first?

No. TIP102 Week 1 already starts at strings and arrays, and you have worked as a developer, so Phases 1 and 2 (conditions and loops) should be fast. Use this list as a **warm-up and a gap filler**, not a prerequisite:

1. **Quick check (1 to 2 evenings):** do 3 problems from each of Phase 1 and Phase 2. If they feel easy, skip the rest of those phases.
2. **Then start TIP102 Week 1.** Do the matching logic-building phase alongside each week, using the table below.
3. **If a TIP102 problem stalls you on basics** (loop bounds, string indexing, base cases), drop back to the matching phase for a few reps. Claude will suggest this when `/review` or `/hint` spots a fundamentals gap.

## Phase to week map

| Phase | Topic | When | TIP102 weeks it supports |
|---|---|---|---|
| 1 | Conditional Thinking | Do **before Week 1** (only if Week 1 Session 1 feels hard) | Week 1 (conditionals) |
| 2 | Loops & Iteration | Do **before Week 1** (only if Week 1 Session 1 feels hard) | Week 1 (loops) |
| 3 | Recursion | Do **before Week 7** (Recursion) | Week 7 (recursion), Weeks 8-9 (tree recursion) |
| 4 | Basic Arrays | Pair with **Weeks 1-2** (Strings & Arrays, Dictionaries) | Weeks 1-2, 4 |
| 5 | Strings | Pair with **Weeks 1-3** (strings, two pointers, stacks) | Weeks 1, 3 |
| 6 | Mixed Logical Challenges | Pair with **Weeks 2-4** (mixed review) | Weeks 2-4, 12 |

How to practice these in this repo: create `logic-building/phase-N/<name>.py`, use the same UMPIRE template, and run `/review` on it. Tick the box below when done (Claude updates it during `/log-session`).


## Phase 1: Conditional Thinking

### Level 1
- [ ] **Number Identity** : Take a number and determine whether it is
- [ ] **Odd or Even** : Determine whether a given number is odd or even.
- [ ] **Divisibility Check** : Check whether a number is divisible by 3, 5,
- [ ] **Bigger Number** : Take two numbers and determine which one is
- [ ] **Age Category** : Classify a person as a child, teenager, adult, or senior
- [ ] **Character Detector** : Identify whether a character is uppercase,
- [ ] **Grade Calculator** : Convert marks into a grade based on predefined
- [ ] **Time Greeting** : Given an hour, print Morning, Afternoon, Evening,
- [ ] **Mini Calculator** : Take two numbers and an operator and perform the
- [ ] **Number Range** : Determine whether a number is below 50, between

### Level 2
- [ ] **Triangle Classifier** : Given three sides, check whether they form a
- [ ] **Middle Number** : Given three different numbers, find the number
- [ ] **Date Validator** : Given a day and month, determine whether the
- [ ] **Coordinate Checker** : Given (x,y), determine the quadrant, axis,
- [ ] **Ticket Pricing** : Calculate ticket price based on the customer's age.
- [ ] **Electricity Bill** : Calculate the bill according to different
- [ ] **Login Validator** : Check whether a username and password
- [ ] **Right Triangle Check** : Determine whether three numbers can
- [ ] **Number Properties** : Check whether a number is divisible by 2, 3,
- [ ] **Calendar Comparison** : Given two dates in the same year,

### Level 3
- [ ] **ATM Withdrawal** : Approve or reject a withdrawal based on amount,
- [ ] **Clock Angle** : Given hour and minute, calculate the smaller angle
- [ ] **Scholarship Eligibility** : Determine eligibility based on marks,
- [ ] **Smart Discount** : Calculate the final price based on purchase amount,
- [ ] **Number Relationship** : Determine whether three numbers form an
- [ ] **Digit Relationship** : For a three-digit number, check different
- [ ] **Pythagorean Check** : Determine whether three positive integers can
- [ ] **Leap-Year Date** : Validate a complete date while correctly handling leap
- [ ] **Number Classifier** : Given a number, evaluate several properties such as
- [ ] **Mini Decision Engine** : Given age, income, and credit score, determine

## Phase 2: Loops & Iteration

### Level 1
- [ ] **Counting Up** : Print all integers from 1 to N. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Even Number Hunt** : Given N, print every even number from 1 to N. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Countdown** : Given a number N, print the sequence from N down to 1. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Multiplication Builder** : Take an integer N and generate its multiplication table from 1 through 10. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Running Total** : Calculate the sum of all numbers from 1 through N. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Selective Sum** : Calculate the sum of only the odd numbers between 1 and N. ([practice](https://www.hackerrank.com/challenges/java-loops-i/problem))
- [ ] **Factorial Machine** : Given N, calculate N! using a loop. ([practice](https://leetcode.com/problems/factorial-trailing-zeroes/))
- [ ] **Digit Counter** : Given an integer, count how many digits it contains. ([practice](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/))
- [ ] **Digit Sum** : Take an integer and calculate the sum of all its digits. ([practice](https://leetcode.com/problems/add-digits/))
- [ ] **Digit Product** : Calculate the product of all digits of a positive integer. ([practice](https://leetcode.com/problems/self-dividing-numbers/))

### Level 2
- [ ] **Reverse the Number** : Given an integer, reverse its digits without converting it to a string. ([practice](https://leetcode.com/problems/reverse-integer/))
- [ ] **Palindrome Number** : Determine whether a number reads the same from left to right and right to left. ([practice](https://leetcode.com/problems/palindrome-number/))
- [ ] **Prime Detector** : Determine whether a given number is prime using iteration. ([practice](https://leetcode.com/problems/count-primes/))
- [ ] **Prime Range** : Given two numbers A and B, print every prime number between them. ([practice](https://leetcode.com/problems/count-primes/))
- [ ] **Fibonacci Generator** : Generate the first N numbers of the Fibonacci sequence. ([practice](https://leetcode.com/problems/fibonacci-number/))
- [ ] **Factor Finder** : Print every factor of a given positive integer. ([practice](https://leetcode.com/problems/number-of-common-factors/))
- [ ] **GCD Challenge** : Given two integers, find their greatest common divisor using loops. ([practice](https://leetcode.com/problems/find-greatest-common-divisor-of-array/))
- [ ] **Armstrong Number** : Determine whether a number is an Armstrong number by processing each digit. ([practice](https://www.hackerrank.com/domains/algorithms))
- [ ] **Digit Extremes** : Find the smallest and largest digit present in a given integer. ([practice](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/))
- [ ] **Happy Number** : Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1. ([practice](https://leetcode.com/problems/happy-number/))

## Phase 3: Recursion

### Level 1
- [ ] **Count Forward** : Print numbers from 1 to N using recursion. ([practice](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops/1))
- [ ] **Count Backward** : Print numbers from N down to 1 using recursion. ([practice](https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1))
- [ ] **Even Numbers** : Print all even numbers from 1 to N using recursion. ([practice](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops/1))
- [ ] **Sum of Numbers** : Find the sum of the first N natural numbers using recursion. ([practice](https://www.geeksforgeeks.org/problems/sum-of-first-n-terms/1))
- [ ] **Recursive Factorial** : Calculate the factorial of a given number using recursion. ([practice](https://www.geeksforgeeks.org/problems/factorial5739/1))
- [ ] **Power Calculator** : Calculate xⁿ recursively. ([practice](https://leetcode.com/problems/powx-n/))
- [ ] **Fibonacci** : Find the Nth Fibonacci number using recursion. ([practice](https://leetcode.com/problems/fibonacci-number/))
- [ ] **Fibonacci Sequence** : Print the first N terms of the Fibonacci sequence using recursion. ([practice](https://www.geeksforgeeks.org/problems/nth-fibonacci-number1335/1))
- [ ] **Recursive Digit Sum** : Find the sum of all digits of a number using recursion. ([practice](https://www.geeksforgeeks.org/problems/sum-of-digits1742/1))
- [ ] **Sum of Even Numbers** : Find the sum of the first N even numbers using recursion. ([practice](https://www.geeksforgeeks.org/problems/sum-of-first-n-terms/1))

### Level 2
- [ ] **Count Digits** : Count the number of digits in a given number using recursion. ([practice](https://www.geeksforgeeks.org/problems/count-digits5716/1))
- [ ] **Reverse a String** : Reverse a string using recursion without using a loop. ([practice](https://www.geeksforgeeks.org/problems/reverse-a-string/1))
- [ ] **Palindrome Check** : Check whether a string is a palindrome using recursion. ([practice](https://www.geeksforgeeks.org/problems/palindrome-string0817/1))
- [ ] **Product of Digits** : Find the product of all digits of a number using recursion. ([practice](https://www.geeksforgeeks.org/problems/product-of-digits/1))
- [ ] **Recursive GCD** : Find the GCD of two numbers using Euclid's algorithm recursively. ([practice](https://leetcode.com/problems/find-greatest-common-divisor-of-array/))
- [ ] **Decimal to Binary** : Convert a decimal number into binary using recursion. ([practice](https://www.geeksforgeeks.org/problems/convert-a-number-to-binary-number/1))
- [ ] **Remove a Character** : Remove all occurrences of a given character from a string using recursion. ([practice](https://www.geeksforgeeks.org/problems/remove-character3815/1))
- [ ] **Count Vowels** : Count the number of vowels in a string using recursion. ([practice](https://www.geeksforgeeks.org/problems/count-vowels-in-string/1))
- [ ] **Recursive Pattern** : Print a triangle pattern of stars using recursion. Example: ([practice](https://www.geeksforgeeks.org/problems/print-pattern3549/1))
- [ ] **Increasing + Decreasing** : Using a single recursive function, print numbers in increasing order and then decreasing order. Example for N = 3: 123321 ([practice](https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops/1))

## Phase 4: Basic Arrays

### Level 1
- [ ] **Take n numbers as input and print all the elements of the array** ([practice](https://www.hackerrank.com/challenges/arrays-introduction/problem))
- [ ] **Find the total sum of all elements in an array** ([practice](https://leetcode.com/problems/running-sum-of-1d-array/))
- [ ] **Find the average value of all elements in an array** ([practice](https://www.hackerrank.com/challenges/simple-array-sum/problem))
- [ ] **Find the largest element in an array** ([practice](https://leetcode.com/problems/maximum-subarray/))
- [ ] **Find the smallest element in an array** ([practice](https://leetcode.com/problems/find-smallest-letter-greater-than-target/))
- [ ] **Count how many numbers in the array are positive, negative, and zero** ([practice](https://leetcode.com/problems/sign-of-the-product-of-an-array/))
- [ ] **Count the number of even and odd elements in an array** ([practice](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/))
- [ ] **Find the position (index) of the largest element in an array** ([practice](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/))
- [ ] **Find all elements in the array that are greater than a given number K** ([practice](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/))
- [ ] **Search for a given number X and print whether it exists in the array** ([practice](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/))

### Level 2
- [ ] **Count how many times a given number appears in an array** ([practice](https://leetcode.com/problems/majority-element/))
- [ ] **Find the first and last position of a given element in an array** ([practice](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/))
- [ ] **Check whether all elements in an array are unique** ([practice](https://leetcode.com/problems/contains-duplicate/))
- [ ] **Find the sum of only the even elements in an array** ([practice](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/))
- [ ] **Create a new array containing the square of every element** ([practice](https://leetcode.com/problems/squares-of-a-sorted-array/))
- [ ] **Create a new array containing only the even elements from the original array** ([practice](https://leetcode.com/problems/find-even-difference/))
- [ ] **Replace every negative number in an array with zero** ([practice](https://leetcode.com/problems/move-zeroes/))
- [ ] **Reverse an array without using a built-in reverse function** ([practice](https://leetcode.com/problems/reverse-string/))
- [ ] **Rotate an array one position to the left and print the result** ([practice](https://leetcode.com/problems/rotate-array/))
- [ ] **Find all elements that appear more than once in an array** ([practice](https://leetcode.com/problems/find-all-duplicates-in-an-array/))

## Phase 5: Strings
- [ ] **String Length** : Take a string as input and find the number of characters in it. ([practice](https://leetcode.com/problems/length-of-last-word/))
- [ ] **Character Counter** : Count the number of vowels, consonants, digits, and special characters present in a string. ([practice](https://www.hackerrank.com/challenges/counting-vowels/problem))
- [ ] **Character Frequency** : Take a string and a character as input. Find how many times that character appears in the string. ([practice](https://leetcode.com/problems/first-unique-character-in-a-string/))
- [ ] **Case Converter** : Convert all lowercase characters to uppercase and all uppercase characters to lowercase. ([practice](https://leetcode.com/problems/to-lower-case/))
- [ ] **Reverse the Text** : Reverse a string without using a built-in reverse function. ([practice](https://leetcode.com/problems/reverse-string/))
- [ ] **Palindrome Check** : Check whether a given string reads the same forward and backward. ([practice](https://leetcode.com/problems/valid-palindrome/))
- [ ] **Remove Unwanted Characters** : Create a new string after removing all spaces and digits from the original string. ([practice](https://leetcode.com/problems/valid-palindrome/))
- [ ] **Remove Duplicate Characters** : Given a string, create a new string containing only the first occurrence of each character. ([practice](https://leetcode.com/problems/remove-duplicate-letters/))
- [ ] **Reverse the Words** : Given a sentence, reverse the order of its words while keeping the characters inside each word unchanged. ([practice](https://leetcode.com/problems/reverse-words-in-a-string/))
- [ ] **Find the Longest Word** : Given a sentence, find and print the longest word. ([practice](https://leetcode.com/problems/longest-substring-without-repeating-characters/))
- [ ] **Character Replacement** : Replace every vowel in a string with * and print the resulting string. ([practice](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/))
- [ ] **Anagram Check** : Take two strings and determine whether they contain the same characters with the same frequencies, regardless of order. ([practice](https://leetcode.com/problems/valid-anagram/))

## Phase 6: Mixed Logical Challenges

### Level 1
- [ ] **Find all numbers from 1 to N that are divisible by both 3 and 5** (practice: Fizz Buzz - LeetCode)
- [ ] **Reverse a number and check whether the original and reversed values are the same** (practice: Palindrome Number - LeetCode)
- [ ] **Find the sum of all digits in a given number** (practice: Find the Sum of Digits - HackerRank)
- [ ] **Check whether a number is an Armstrong number** (practice: Armstrong Number - GeeksforGeeks)
- [ ] **Find the largest and smallest values in an integer array** (practice: Min and Max - HackerRank)
- [ ] **Move all zero values to the end while keeping the other elements in their original order** (practice: Move Zeroes - LeetCode)
- [ ] **Find the second-largest distinct number in an array** (practice: Second Largest - HackerRank)
- [ ] **Check whether two strings contain the same characters with the same frequency** (practice: Valid Anagram - LeetCode)
- [ ] **Find the characters that occur more than once in a string** (practice: First Unique Character in a String - LeetCode)

### Level 2
- [ ] **Reverse only the words whose length is even, leaving the other words unchanged** (practice: Reverse Words in a String - LeetCode)
- [ ] **Find the word containing the highest number of vowels in a sentence** (practice: Maximum Number of Vowels in a Substring - LeetCode)
- [ ] **Remove repeated words from a sentence while keeping the first occurrence** (practice: Remove Duplicates from Sorted Array - LeetCode)
- [ ] **Find all pairs in an array whose values add up to a given target** (practice: Two Sum - LeetCode)
- [ ] **Check whether an array is arranged in increasing or decreasing order** (practice: Check if Array Is Sorted and Rotated - LeetCode)
- [ ] **Find the common values shared by two integer arrays** (practice: Intersection of Two Arrays - LeetCode)
- [ ] **Count how many prime numbers are present in an array** (practice: Count Primes - LeetCode)
- [ ] **Print every word in a sentence that reads the same forwards and backwards** (practice: Valid Palindrome - LeetCode)
- [ ] **Rotate an array one position to the right without creating another array** (practice: Rotate Array - LeetCode)
- [ ] **Print Pascal's Triangle for N rows using nested loops** (practice: Pascal's Triangle - LeetCode)

_Parsed automatically from the PDF; a handful of descriptions may be cut short. Check the original PDF if one looks incomplete._
