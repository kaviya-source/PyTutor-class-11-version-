print('PyTutor (class 11 edition)')
print('Your Digital Companion for Class 11 CS')

import random


def looping_constructs_notes():
      print("""
========================================
ONE-SHOT NOTES : LOOPING CONSTRUCTS
========================================

1. FOR LOOP
----------------
Used to iterate over a sequence such as range, list, string, or tuple.
Best used when the number of iterations is known.

Syntax:
for variable in range(start, stop, step):
    statements

Example:
for i in range(1, 6):
    print(i)

Key Points:
- Iterates over a sequence
- range() is commonly used
- start is inclusive, stop is exclusive

----------------------------------------

2. WHILE LOOP
----------------
Executes a block of code as long as the condition is True.
Best used when the number of iterations is unknown.

Syntax:
i = 1
while i <= 5:
    print(i)
    i += 1

Key Points:
- Condition is checked before each iteration
- If condition never becomes False, it causes an infinite loop

----------------------------------------

3. LOOP CONTROL STATEMENTS
--------------------------

Statement     Use
---------     ---------------------------
break         Exits the loop immediately
continue      Skips the current iteration

----------------------------------------

4. NESTED LOOPS
----------------
A loop inside another loop.

Example:
for i in range(3):
    for j in range(2):
        print(i, j)

----------------------------------------

EXAM TIPS:
✔ Know when to use for vs while
✔ Practice output-based questions
✔ Be careful of infinite loops

========================================
END OF NOTES
========================================
""")
    
def looping_constructs_MCQs():
    questions = [
        {
            "q": "What will be the output?\nfor i in range(1, 5):\n    print(i, end=\" \")",
            "options": ["A. 1 2 3 4", "B. 1 2 3 4 5", "C. 0 1 2 3 4", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nfor i in range(5):\n    print(i)",
            "options": ["A. 1 to 5", "B. 0 to 4", "C. 0 to 5", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nfor i in range(2, 10, 3):\n    print(i, end=\" \")",
            "options": ["A. 2 5 8", "B. 2 5 8 11", "C. 3 6 9", "D. 2 4 6 8"],
            "ans": "A"
        },

        {
            "q": "How many times will the loop execute?\nfor i in range(10, 1, -2):\n    print(i)",
            "options": ["A. 3", "B. 4", "C. 5", "D. Infinite"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nfor i in range(1, 1):\n    print(i)",
            "options": ["A. 1", "B. 0", "C. Error", "D. No output"],
            "ans": "D"
        },

        
        {
            "q": "What will be the output?\ni = 1\nwhile i <= 3:\n    print(i, end=\" \")\n    i += 1",
            "options": ["A. 1 2 3", "B. 1 2", "C. Infinite loop", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\ni = 5\nwhile i > 0:\n    print(i)",
            "options": ["A. Prints 5 to 1", "B. Infinite loop", "C. Error", "D. No output"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\ni = 0\nwhile i < 5:\n    i += 1\n    print(i, end=\" \")",
            "options": ["A. 0 1 2 3 4", "B. 1 2 3 4 5", "C. 0 1 2 3 4 5", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nfor i in range(5):\n    if i == 3:\n        break\n    print(i, end=\" \")",
            "options": ["A. 0 1 2", "B. 0 1 2 3", "C. 3", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nfor i in range(5):\n    if i == 3:\n        continue\n    print(i, end=\" \")",
            "options": ["A. 0 1 2 4", "B. 0 1 2 3 4", "C. 3", "D. Infinite loop"],
            "ans": "A"
        },

        {
            "q": "Which statement is TRUE?",
            "options": [
                "A. break skips the current iteration",
                "B. continue stops the loop completely",
                "C. continue skips remaining code of loop body",
                "D. break skips only one iteration"
            ],
            "ans": "C"
        },

        
        {
            "q": "What will be the output?\nfor i in range(3):\n    print(i)\nelse:\n    print(\"Done\")",
            "options": ["A. 0 1 2", "B. Done", "C. 0 1 2 Done", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nfor i in range(3):\n    if i == 1:\n        break\n    print(i)\nelse:\n    print(\"Done\")",
            "options": ["A. 0 Done", "B. 0 1 Done", "C. 0", "D. 0 1"],
            "ans": "C"
        },

        
        {
            "q": "How many times will print(\"Hi\") execute?\nfor i in range(3):\n    for j in range(2):\n        print(\"Hi\")",
            "options": ["A. 2", "B. 3", "C. 5", "D. 6"],
            "ans": "D"
        },

        {
            "q": "What will be the output?\nfor i in range(1, 4):\n    for j in range(1, i):\n        print(j, end=\"\")\n    print()",
            "options": [
                "A.\n1\n12\n123",
                "B.\n(blank)\n1\n12",
                "C.\n(blank)\n1\n12",
                "D.\n1\n12"
            ],
            "ans": "C"
        },

        
        {
            "q": "Assertion (A): range(5) generates 5 values.\nReason (R): range(n) generates values from 0 to n−1.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "Assertion (A): A loop can execute zero times.\nReason (R): Loop condition may be false initially.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        }
    ]

    random.shuffle(questions)

    score = 0
    correct = []
    incorrect = []

    print("\n📘 LOOPING MCQ QUIZ STARTED\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['q']}")
        for opt in q["options"]:
            print(opt)

        user_ans = input("Enter your choice (A/B/C/D): ").upper()

        if user_ans == q["ans"]:
            print("✅ Correct!\n")
            score += 1
            correct.append(q["q"])
        else:
            print(f"❌ Wrong! Correct Answer: {q['ans']}\n")
            incorrect.append(q["q"])

    print("\n================================")
    print("📊 QUIZ ANALYSIS")
    print("================================")
    print(f"Total Questions : {len(questions)}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {len(questions) - score}")
    print("Score           :", score, "/", len(questions))

    print("\n✔ Correctly Answered Questions:")
    for q in correct:
        print("-", q)

    print("\n❌ Incorrectly Answered Questions:")
    for q in incorrect:
        print("-", q)

    print("\n🎉 Quiz Completed! Keep practicing loops!")



def looping_constructs_HOTs():
    questions_answers = [
        ('''1. Predict the Output:
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
else:
    print("Done")''',
         '''Output:
0 1 2 3 4 Done
Reason: else executes because loop ends normally.'''),

        ('''2. for loop with break and else:
for i in range(1, 5):
    if i == 3:
        break
else:
    print("Loop finished")''',
         '''Output:
No output
Reason: else does NOT run if loop ends via break.'''),

        ('''3. while loop decreasing by 2:
i = 5
while i > 0:
    print(i, end=" ")
    i -= 2''',
         '''Output:
5 3 1'''),

        ('''4. Assigning i inside for loop:
for i in range(3):
    print(i)
    i = 10''',
         '''Output:
0
1
2
Reason: assigning i inside loop does not affect iteration.'''),

        ('''5. continue inside while loop:
i = 1
while i <= 5:
    i += 1
    if i == 3:
        continue
    print(i, end=" ")''',
         '''Output:
2 4 5 6'''),

        ('''6. Assertion–Reason:
Assertion (A): A loop can have an else block in Python.
Reason (R): The else block executes only when the loop terminates without break.''',
         '''Answer:
A and R are true, R explains A'''),

        ('''7. Assertion–Reason:
Assertion (A): continue stops loop execution completely.
Reason (R): continue transfers control to the next iteration.''',
         '''Answer:
A is false, R is true'''),

        ('''8. Nested for loop:
for i in range(1, 4):
    for j in range(1, i):
        print(j, end="")
    print()''',
         '''Output:

1
12
Reason: First iteration prints blank line.'''),

        ('''9. while loop with break:
i = 1
while i <= 10:
    if i % 3 == 0:
        break
    print(i, end=" ")
    i += 1''',
         '''Output:
1 2
Reason: Loop stops at i = 3.'''),

        ('''10. for loop with pass:
for i in range(5):
    pass
print(i)''',
         '''Output:
4
Reason: Loop variable exists outside loop.'''),

        ('''11. Error Detection:
while i < 5:
    print(i)''',
         '''Error:
i not initialized
Fix: i = 0 before loop'''),

        ('''12. for i in range(1,5,0):
    print(i)''',
         '''Error:
Step value cannot be zero'''),

        ('''13. Infinite loop reason:
i = 1
while i <= 5:
    print(i)''',
         '''Answer:
i is never updated.'''),

        ('''14. continue before print:
i = 0
while i < 3:
    print(i)
    i += 1
    continue
    print("Hello")''',
         '''Output:
0
1
2
Reason: Code after continue is unreachable.'''),

        ('''15. Pattern:
for i in range(1, 5):
    for j in range(i):
        print(i, end="")
    print()''',
         '''Output:
1
22
333
4444'''),

        ('''16. Nested while multiplication:
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i * j, end=" ")
        j += 1
    i += 1''',
         '''Output:
1 2 3 2 4 6 3 6 9''')
    ]

    for q, a in questions_answers:
        print(q)
        input("\nPress Enter to see the answer...")
        print(a)
        print("\n" + "-"*50 + "\n")
        


def string_notes():
    string_notes = """
==============================
ONE-SHOT NOTES : STRINGS
==============================

1. What is a String?
A string is a sequence of characters enclosed in:
- Single quotes (' ')
- Double quotes (" ")
- Triple quotes (''' ''')

Examples:
name = "Python"
msg = 'Hello'
para = '''Welcome to Class 11'''

--------------------------------

2. Characteristics of Strings
✔ Strings are immutable (cannot be changed)
✔ Each character has an index number
✔ Indexing starts from 0
✔ Negative indexing is allowed

s = "HELLO"
Index:  0  1  2  3  4
        H  E  L  L  O

--------------------------------

3. String Indexing
Used to access individual characters.

s = "Python"
print(s[0])    # P
print(s[-1])   # n

--------------------------------

4. String Slicing
Used to extract a part of a string.

Syntax:
string[start : stop : step]

Examples:
s = "Computer"
print(s[0:4])    # Comp
print(s[2:])     # mputer
print(s[::-1])   # retupmoC

--------------------------------

5. String Operations

1) Concatenation (+)
a = "Hello"
b = "World"
print(a + " " + b)

2) Repetition (*)
print("Hi " * 3)

3) Membership (in, not in)
print("a" in "cat")      # True
print("x" not in "cat")  # True

--------------------------------

6. Common String Functions
len()         → Returns length
upper()       → Converts to uppercase
lower()       → Converts to lowercase
capitalize()  → First letter uppercase
title()       → Capitalizes each word
strip()       → Removes spaces
replace()     → Replaces substring
find()        → Finds position
count()       → Counts occurrences

Example:
s = " python "
print(s.strip().upper())

--------------------------------

7. String Traversal

Using for loop:
for ch in "Python":
    print(ch)

Using while loop:
s = "Python"
i = 0
while i < len(s):
    print(s[i])
    i += 1

--------------------------------

8. Immutability of Strings

❌ Wrong:
s[0] = 'H'

✔ Correct:
s = "hello"
s = "H" + s[1:]

--------------------------------

9. String Comparison
Uses ASCII values.

print("apple" > "Apple")   # True

--------------------------------

10. Escape Characters
\\n  → New line
\\t  → Tab
\\'  → Single quote
\\"  → Double quote

--------------------------------

11. Input with Strings
name = input("Enter name: ")
print("Welcome", name)

--------------------------------

12. Exam Tips
✔ Remember strings are immutable
✔ Practice slicing questions
✔ Know common functions
✔ Output-based questions are important

========================================
END OF NOTES
========================================"""
    print(string_notes)





def string_MCQs():
  questions = [
       
        {"q": "Which of the following is a valid string in Python?", 
         "options": ["A. 'Hello", "B. \"Hello\"", "C. Hello", "D. Hello\""], "ans": "B"},
        
        {"q": "What will be the output?\ns = \"Python\"\nprint(s[0])",
         "options": ["A. P", "B. y", "C. n", "D. Error"], "ans": "A"},
        
        {"q": "Which operator is used to concatenate two strings?",
         "options": ["A. *", "B. +", "C. &", "D. %"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"Hi\" * 3)",
         "options": ["A. HiHiHi", "B. Hi 3", "C. Error", "D. Hi*3"], "ans": "A"},
        
        {"q": "Strings in Python are:",
         "options": ["A. Mutable", "B. Immutable", "C. Both", "D. None"], "ans": "B"},
        
        {"q": "What does len(\"Computer\") return?",
         "options": ["A. 7", "B. 8", "C. 9", "D. Error"], "ans": "B"},
        
        {"q": "Which of the following accesses the last character of a string s?",
         "options": ["A. s[len(s)]", "B. s[-1]", "C. s[1]", "D. s[-0]"], "ans": "B"},
        
        {"q": "What will be the output?\ns = \"Hello\"\nprint(s[1:4])",
         "options": ["A. Hel", "B. ell", "C. ello", "D. lo"], "ans": "B"},
        
        {"q": "Which function converts a string to lowercase?",
         "options": ["A. lower()", "B. tolower()", "C. small()", "D. low()"], "ans": "A"},
        
        {"q": "What will be the output?\nprint(\"abc\" == \"ABC\")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},
        
        {"q": "Which of the following is NOT a string method?",
         "options": ["A. split()", "B. find()", "C. append()", "D. replace()"], "ans": "C"},
        
        {"q": "What will be the output?\ns = \"India\"\nprint(s[::-1])",
         "options": ["A. India", "B. aidnI", "C. Error", "D. Iaidn"], "ans": "B"},
        
        {"q": "Which escape character is used for a new line?",
         "options": ["A. /n", "B. \\n", "C. \\t", "D. \\\\"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"Hello\"[::-2])",
         "options": ["A. Hlo", "B. oe", "C. olH", "D. Error"], "ans": "C"},
        
        {"q": "Which statement is TRUE about strings?",
         "options": ["A. Strings can be modified directly", "B. Strings support indexing", "C. Strings store only numbers", "D. Strings cannot be sliced"], "ans": "B"},
        
        {"q": "What will be the output?\ns = \"PYTHON\"\nprint(s[-1:-4:-1])",
         "options": ["A. NOHT", "B. NOH", "C. N", "D. Empty string"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"ab\" + \"cd\" * 2)",
         "options": ["A. abcdcd", "B. abcd2", "C. abccd", "D. Error"], "ans": "A"},
        
        {"q": "What will be the output?\nprint(\"Hello\" > \"hello\")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},
        
        {"q": "What will be the output?\ns = \"Computer\"\nprint(s[1:6:2])",
         "options": ["A. optr", "B. opt", "C. omt", "D. ope"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"Python\" == \"Python \")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},
        
        {"q": "Which statement is FALSE?",
         "options": ["A. Strings support slicing", "B. Strings are immutable", "C. s[0] = 'A' is valid", "D. Strings support indexing"], "ans": "C"},
        
        {"q": "What will be the output?\nprint(\"abc\"[1] * 3)",
         "options": ["A. abcabcabc", "B. bbb", "C. 3b", "D. Error"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(len(\" \"))",
         "options": ["A. 0", "B. 1", "C. Error", "D. None"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"python\".find(\"th\"))",
         "options": ["A. 1", "B. 2", "C. 3", "D. -1"], "ans": "B"},
        
        {"q": "What will be the output?\nprint(\"MISSISSIPPI\".count(\"IS\"))",
         "options": ["A. 1", "B. 2", "C. 3", "D. 4"], "ans": "B"},

       
        {"q": "Assertion (A): Strings in Python are immutable.\nReason (R): Characters of a string can be changed using indexing.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "C"},
        
        {"q": "Assertion (A): \"abc\" > \"ABC\" evaluates to True.\nReason (R): ASCII value of lowercase letters is greater than uppercase letters.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"},
        
        {"q": "Assertion (A): len(\" \") returns 1.\nReason (R): Space is considered a character.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"},
        
        {"q": "Assertion (A): s[::-1] reverses a string.\nReason (R): Negative step in slicing traverses the string backwards.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"},
        
        {"q": "Assertion (A): \"Python\"*0 produces an empty string.\nReason (R): Multiplying a string by zero removes all characters.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"},
        
        {"q": "Assertion (A): \"Hello\".replace('l','L') modifies the original string.\nReason (R): Strings are mutable in Python.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "D"},
        
        {"q": "Assertion (A): \"a\" in \"apple\" returns True.\nReason (R): in operator checks for substring existence.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"},
        
        {"q": "Assertion (A): \"Python\"[10] causes an error.\nReason (R): String index must be within valid range.",
         "options": ["A. Both A and R are true & R explains A", "B. Both A and R are true but R doesn’t explain A", "C. A is true, R is false", "D. A is false, R is true"], "ans": "A"}
    ]
  random.shuffle(questions)
  score = 0
  correct = []
  incorrect = []
  print("\n📘 STRING MCQ QUIZ STARTED\n")
  for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['q']}")
        for opt in q["options"]:
            print(opt)

        user_ans = input("Enter your choice (A/B/C/D): ").upper()

        if user_ans == q["ans"]:
            print("✅ Correct!\n")
            score += 1
            correct.append(q["q"])
        else:
            print(f"❌ Wrong! Correct Answer: {q['ans']}\n")
            incorrect.append(q["q"])

  print("\n================================")
  print("📊 QUIZ ANALYSIS")
  print("================================")
  print(f"Total Questions : {len(questions)}")
  print(f"Correct Answers : {score}")
  print(f"Wrong Answers   : {len(questions) - score}")
  print("Score           :", score, "/", len(questions))
  
  print("\n✔ Correctly Answered Questions:")
  for q in correct:
        print("-", q)

  print("\n❌ Incorrectly Answered Questions:")
  for q in incorrect:
        print("-", q)

  print("\n🎉 Quiz Completed! Keep learning with PyTutor.")



def string_HOTs():
      questions_answers = [
        ('''1. Predict the Output:
s = "abcde"
print(s[::3])''',
         '''Output:
ad
Explanation: start:stop:step → step 3 → indices 0,3 → a,d.'''),

        ('''2. Predict the Output:
s = "python"
print(s[5:0:-1])''',
         '''Output:
nohty
Explanation: slicing backward excludes stop index → 5→1 (0 excluded).'''),

        ('''3. Predict the Output:
s = "python"
print(s[10:])''',
         '''Output:
(empty string)
Explanation: start index > len(s) → returns empty string, no error.'''),

        ('''4. Predict the Output:
s = "python"
print(s[::-2])''',
         '''Output:
nhy
Explanation: reverse (:: -2) → take every second character from end.'''),

        ('''5. Predict the Output:
s = "Python"
s1 = s
s1 += "3"
print(s, s1)''',
         '''Output:
Python Python3
Explanation: Strings are immutable → original s unchanged.'''),

        ('''6. Count vowels (without inbuilt methods):
s = "Programming"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)''',
         '''Output:
3
Explanation: vowels o, a, i counted.'''),

        ('''7. Reverse string using loop:
s = "Python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)''',
         '''Output:
nohtyP
Explanation: add character at front each iteration.'''),

        ('''8. Suffixes of a string:
s = "abc"
for i in range(len(s)):
    print(s[i:])''',
         '''Output:
abc
bc
c'''),

        ('''9. Only consonants using loop:
s = "Hello World"
for ch in s:
    if ch.lower() not in "aeiou ":
        print(ch, end="")''',
         '''Output:
HllWrld
Explanation: ignores vowels & space.'''),

        ('''10. Nested loops + string:
s = "ab"
for i in s:
    for j in s:
        print(i+j, end=" ")''',
         '''Output:
aa ab ba bb
Explanation: Cartesian product of characters.'''),

        ('''11. Remove duplicates:
s = "aabbcc"
s1 = ""
for ch in s:
    if ch not in s1:
        s1 += ch
print(s1)''',
         '''Output:
abc'''),

        ('''12. String multiplication:
s = "Hi"
print(s*3)''',
         '''Output:
HiHiHi'''),

        ('''13. join + split combo:
s = "Python is fun"
print("-".join(s.split()))''',
         '''Output:
Python-is-fun
Explanation: split() → list of words, join("-") → hyphenated.'''),

        ('''14. isalpha and isdigit:
s = "Python3"
print(s.isalpha(), s.isalnum())''',
         '''Output:
False True
Explanation: isalpha → only letters, isalnum → letters/digits allowed.'''),

        ('''15. String formatting trick:
name = "John"
age = 17
print(f"{name} is {age} years old")''',
         '''Output:
John is 17 years old
Explanation: f-strings evaluate expressions inside {}.'''),

        ('''16. Reverse each word in a sentence:
s = "Hello World"
s1 = ""
for word in s.split():
    s1 += word[::-1] + " "
print(s1)''',
         '''Output:
olleH dlroW'''),

        ('''17. Alternate characters in string:
s = "abcdef"
s1 = ""
for i in range(len(s)):
    if i % 2 == 0:
        s1 += s[i]
print(s1)''',
         '''Output:
ace'''),

        ('''18. Check palindrome ignoring case:
s = "Level"
if s.lower() == s[::-1].lower():
    print("Palindrome")''',
         '''Output:
Palindrome'''),

        ('''19. Remove vowels:
s = "Python Programming"
s1 = ""
for ch in s:
    if ch.lower() not in "aeiou":
        s1 += ch
print(s1)''',
         '''Output:
Pythn Prgrmmng'''),

        ('''20. Nested slicing + step:
s = "abcdefgh"
print(s[1:7:2][::-1])''',
         '''Output:
fdb
Explanation: Step 2 → indices 1,3,5 → b,d,f → reversed → fdb.''')
    ]

      for q, a in questions_answers:
        print(q)
        input("\nPress Enter to see the answer...")
        print(a)
        print("\n" + "-"*50 + "\n")





def list_MCQs():
    questions = [

        
        {
            "q": "What will be the output?\nL = [10, 20, 30, 40]\nprint(L[-1])",
            "options": ["A. 10", "B. 20", "C. 30", "D. 40"],
            "ans": "D"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 3]\nprint(L * 2)",
            "options": ["A. [1, 2, 3, 1, 2, 3]", "B. [2, 4, 6]", "C. Error", "D. [1, 2, 3]"],
            "ans": "A"
        },

        {
            "q": "Which statement is TRUE?",
            "options": ["A. Lists are immutable", "B. Lists support indexing", "C. Lists store only integers", "D. Lists cannot be nested"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [1, 2, 3]\nL[1] = 99\nprint(L)",
            "options": ["A. [1, 2, 3]", "B. Error", "C. [1, 99, 3]", "D. [99, 2, 3]"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 3]\nprint(L.append(4))",
            "options": ["A. [1, 2, 3, 4]", "B. 4", "C. None", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 3]\nL = L.append(4)\nprint(L)",
            "options": ["A. [1, 2, 3, 4]", "B. None", "C. Error", "D. [4]"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [1, 2, 3, 4, 5]\nprint(L[1:4:2])",
            "options": ["A. [2, 3]", "B. [2, 4]", "C. [3, 5]", "D. [1, 3]"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 3, 4]\nprint(L[::-1])",
            "options": ["A. [1, 2, 3, 4]", "B. [4, 3, 2, 1]", "C. Error", "D. None"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nA = [1, 2, 3]\nB = A\nB.append(4)\nprint(A)",
            "options": ["A. [1, 2, 3]", "B. [4]", "C. [1, 2, 3, 4]", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nA = [1, 2, 3]\nB = A.copy()\nB.append(4)\nprint(A)",
            "options": ["A. [1, 2, 3, 4]", "B. [1, 2, 3]", "C. [4]", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [[1, 2], [3, 4]]\nprint(L[1][0])",
            "options": ["A. 2", "B. 3", "C. 4", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nL = [[0]] * 3\nL[0][0] = 5\nprint(L)",
            "options": ["A. [[5], [0], [0]]", "B. [[5], [5], [5]]", "C. [[0], [0], [0]]", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [1, 2, 3, 2]\nL.remove(2)\nprint(L)",
            "options": ["A. [1, 3, 2]", "B. [1, 2, 3]", "C. [2, 3, 2]", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nL = [10, 20, 30]\nprint(L.pop())",
            "options": ["A. [10, 20]", "B. 30", "C. None", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [1, 2, 3]\nfor i in L:\n    L.append(i)\n    break\nprint(L)",
            "options": ["A. [1, 2, 3]", "B. [1, 2, 3, 1]", "C. Infinite loop", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "Assertion (A): Lists are mutable.\nReason (R): Elements of a list can be changed after creation.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "Assertion (A): list.copy() creates a shallow copy.\nReason (R): Nested objects still share references.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 3]\nprint(L.extend([4, 5]))",
            "options": ["A. [1, 2, 3, 4, 5]", "B. [4, 5]", "C. None", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nL = [3, 1, 2]\nprint(L.sort())",
            "options": ["A. [1, 2, 3]", "B. [3, 1, 2]", "C. None", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nL = [3, 1, 2]\nL.sort()\nprint(L)",
            "options": ["A. [3, 1, 2]", "B. [1, 2, 3]", "C. None", "D. Error"],
            "ans": "B"
        },

        
        {
            "q": "What will be the output?\nL = [10, 20, 30]\nprint(L.index(20))",
            "options": ["A. 20", "B. 1", "C. 2", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nL = [1, 2, 2, 2]\nprint(L.index(2))",
            "options": ["A. 0", "B. 1", "C. 2", "D. Error"],
            "ans": "B"
        },

      
        {
            "q": "What will be the output?\nprint(bool([]))",
            "options": ["A. True", "B. False", "C. Error", "D. None"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nprint([1, 2] == [1, 2])",
            "options": ["A. True", "B. False", "C. Error", "D. None"],
            "ans": "A"
        },

       
        {
            "q": "Assertion (A): L[:] = [] empties the list.\nReason (R): Slice assignment can modify a list in-place.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "Assertion (A): remove() may cause logical errors inside loops.\nReason (R): It changes list size while iterating.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        }
    ]

    random.shuffle(questions)

    score = 0
    correct = []
    incorrect = []

    print("\n📘 LIST MCQ QUIZ STARTED\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['q']}")
        for opt in q["options"]:
            print(opt)

        user_ans = input("Enter your choice (A/B/C/D): ").upper()

        if user_ans == q["ans"]:
            print("✅ Correct!\n")
            score += 1
            correct.append(q["q"])
        else:
            print(f"❌ Wrong! Correct Answer: {q['ans']}\n")
            incorrect.append(q["q"])

    print("\n================================")
    print("📊 QUIZ ANALYSIS")
    print("================================")
    print(f"Total Questions : {len(questions)}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {len(questions) - score}")
    print("Score           :", score, "/", len(questions))

    print("\n✔ Correctly Answered Questions:")
    for q in correct:
        print("-", q)

    print("\n❌ Incorrectly Answered Questions:")
    for q in incorrect:
        print("-", q)

    print("\n🎉 Quiz Completed! Lists mastered!")




def string_MCQs():
    questions = [

        {"q": "Which of the following is a valid string in Python?",
         "options": ["A. 'Hello", "B. \"Hello\"", "C. Hello", "D. Hello\""], "ans": "B"},

        {"q": "What will be the output?\ns = \"Python\"\nprint(s[0])",
         "options": ["A. P", "B. y", "C. n", "D. Error"], "ans": "A"},

        {"q": "Which operator is used to concatenate two strings?",
         "options": ["A. *", "B. +", "C. &", "D. %"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"Hi\" * 3)",
         "options": ["A. HiHiHi", "B. Hi 3", "C. Error", "D. Hi*3"], "ans": "A"},

        {"q": "Strings in Python are:",
         "options": ["A. Mutable", "B. Immutable", "C. Both", "D. None"], "ans": "B"},

        {"q": "What does len(\"Computer\") return?",
         "options": ["A. 7", "B. 8", "C. 9", "D. Error"], "ans": "B"},

        {"q": "Which of the following accesses the last character of a string s?",
         "options": ["A. s[len(s)]", "B. s[-1]", "C. s[1]", "D. s[-0]"], "ans": "B"},

        {"q": "What will be the output?\ns = \"Hello\"\nprint(s[1:4])",
         "options": ["A. Hel", "B. ell", "C. ello", "D. lo"], "ans": "B"},

        {"q": "Which function converts a string to lowercase?",
         "options": ["A. lower()", "B. tolower()", "C. small()", "D. low()"], "ans": "A"},

        {"q": "What will be the output?\nprint(\"abc\" == \"ABC\")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},

        {"q": "Which of the following is NOT a string method?",
         "options": ["A. split()", "B. find()", "C. append()", "D. replace()"], "ans": "C"},

        {"q": "What will be the output?\ns = \"India\"\nprint(s[::-1])",
         "options": ["A. India", "B. aidnI", "C. Error", "D. Iaidn"], "ans": "B"},

        {"q": "Which escape character is used for a new line?",
         "options": ["A. /n", "B. \\n", "C. \\t", "D. \\\\"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"Hello\"[::-2])",
         "options": ["A. Hlo", "B. oe", "C. olH", "D. Error"], "ans": "C"},

        {"q": "Which statement is TRUE about strings?",
         "options": ["A. Strings can be modified directly",
                     "B. Strings support indexing",
                     "C. Strings store only numbers",
                     "D. Strings cannot be sliced"], "ans": "B"},

        {"q": "What will be the output?\ns = \"PYTHON\"\nprint(s[-1:-4:-1])",
         "options": ["A. NOHT", "B. NOH", "C. N", "D. Empty string"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"ab\" + \"cd\" * 2)",
         "options": ["A. abcdcd", "B. abcd2", "C. abccd", "D. Error"], "ans": "A"},

        {"q": "What will be the output?\nprint(\"Hello\" > \"hello\")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},

        {"q": "What will be the output?\ns = \"Computer\"\nprint(s[1:6:2])",
         "options": ["A. optr", "B. opt", "C. omt", "D. ope"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"Python\" == \"Python \")",
         "options": ["A. True", "B. False", "C. Error", "D. None"], "ans": "B"},

        {"q": "Which statement is FALSE?",
         "options": ["A. Strings support slicing",
                     "B. Strings are immutable",
                     "C. s[0] = 'A' is valid",
                     "D. Strings support indexing"], "ans": "C"},

        {"q": "What will be the output?\nprint(\"abc\"[1] * 3)",
         "options": ["A. abcabcabc", "B. bbb", "C. 3b", "D. Error"], "ans": "B"},

        {"q": "What will be the output?\nprint(len(\" \"))",
         "options": ["A. 0", "B. 1", "C. Error", "D. None"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"python\".find(\"th\"))",
         "options": ["A. 1", "B. 2", "C. 3", "D. -1"], "ans": "B"},

        {"q": "What will be the output?\nprint(\"MISSISSIPPI\".count(\"IS\"))",
         "options": ["A. 1", "B. 2", "C. 3", "D. 4"], "ans": "B"},

        {"q": "Assertion (A): Strings in Python are immutable.\nReason (R): Characters of a string can be changed using indexing.",
         "options": ["A. Both A and R are true & R explains A",
                     "B. Both A and R are true but R doesn’t explain A",
                     "C. A is true, R is false",
                     "D. A is false, R is true"], "ans": "C"}
    ]

    random.shuffle(questions)

    score = 0
    correct = []
    incorrect = []

    print("\n📘 STRING MCQ QUIZ STARTED\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['q']}")
        for opt in q["options"]:
            print(opt)

        user_ans = input("Enter your choice (A/B/C/D): ").upper()

        if user_ans == q["ans"]:
            print("✅ Correct!\n")
            score += 1
            correct.append(q["q"])
        else:
            print(f"❌ Wrong! Correct Answer: {q['ans']}\n")
            incorrect.append(q["q"])

    print("\n================================")
    print("📊 QUIZ ANALYSIS")
    print("================================")
    print(f"Total Questions : {len(questions)}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {len(questions) - score}")
    print("Score           :", score, "/", len(questions))

    print("\n✔ Correctly Answered Questions:")
    for q in correct:
        print("-", q)

    print("\n❌ Incorrectly Answered Questions:")
    for q in incorrect:
        print("-", q)

    print("\n🎉 Quiz Completed! Keep learning with PyTutor.")




def list_HOTs():
      
    qa = [

        ('''1. Predict the Output:
L = [1, 2, 3]
print(L * 2)''',
         '''Output:
[1, 2, 3, 1, 2, 3]
Explanation: List multiplication repeats elements.'''),

        ('''2. Predict the Output:
L = [1, 2, 3]
L.append([4, 5])
print(L)''',
         '''Output:
[1, 2, 3, [4, 5]]
Explanation: append() adds as a single element.'''),

        ('''3. Predict the Output:
L = [1, 2, 3]
L.extend([4, 5])
print(L)''',
         '''Output:
[1, 2, 3, 4, 5]
Explanation: extend() adds elements individually.'''),

        ('''4. Predict the Output:
L = [10, 20, 30]
print(L.pop())
print(L)''',
         '''Output:
30
[10, 20]
Explanation: pop() removes and returns last element.'''),

        ('''5. Predict the Output:
L = [1, 2, 3]
L = L.append(4)
print(L)''',
         '''Output:
None
Explanation: append() returns None.'''),

        ('''6. Slicing:
L = [1, 2, 3, 4, 5]
print(L[1:4:2])''',
         '''Output:
[2, 4]'''),

        ('''7. Reverse list using slicing:
L = [1, 2, 3, 4]
print(L[::-1])''',
         '''Output:
[4, 3, 2, 1]'''),

        ('''8. Slice replacement:
L = [1, 2, 3, 4]
L[1:3] = [10]
print(L)''',
         '''Output:
[1, 10, 4]
Explanation: Slice replacement can change list size.'''),

        ('''9. Insert using slicing:
L = [1, 2, 3, 4]
L[1:1] = [9, 8]
print(L)''',
         '''Output:
[1, 9, 8, 2, 3, 4]
Explanation: Inserts without deleting elements.'''),

        ('''10. Loop + list:
L = [10, 20, 30]
for x in L:
    x += 5
print(L)''',
         '''Output:
[10, 20, 30]
Explanation: Modifying x does not modify list.'''),

        ('''11. Loop using index:
L = [1, 2, 3, 4]
for i in range(len(L)):
    L[i] += 1
print(L)''',
         '''Output:
[2, 3, 4, 5]
Explanation: Index-based modification affects list.'''),

        ('''12. Appending during loop:
L = [1, 2, 3]
for i in range(len(L)):
    L.append(i)
print(L)''',
         '''Output:
[1, 2, 3, 0, 1, 2]
Explanation: range(len(L)) is fixed initially.'''),

        ('''13. Removing elements in loop:
L = [1, 2, 3, 4]
for i in L:
    if i % 2 == 0:
        L.remove(i)
print(L)''',
         '''Output:
[1, 3]
Explanation: Removing shifts indices.'''),

        ('''14. Reference vs copy:
A = [1, 2, 3]
B = A
B.append(4)
print(A)''',
         '''Output:
[1, 2, 3, 4]
Explanation: Both reference same list.'''),

        ('''15. Slice copy:
A = [1, 2, 3]
B = A[:]
B.append(4)
print(A, B)''',
         '''Output:
[1, 2, 3] [1, 2, 3, 4]
Explanation: Slicing creates a copy.'''),

        ('''16. Nested list indexing:
L = [[1, 2], [3, 4]]
print(L[0][1])''',
         '''Output:
2'''),

        ('''17. MOST DANGEROUS:
L = [[0]*3]*3
L[0][1] = 5
print(L)''',
         '''Output:
[[0, 5, 0], [0, 5, 0], [0, 5, 0]]
Explanation: All rows refer to same list.'''),

        ('''18. List comprehension:
L = [[i]*3 for i in range(3)]
print(L)''',
         '''Output:
[[0, 0, 0], [1, 1, 1], [2, 2, 2]]
Explanation: Separate lists created.'''),

        ('''19. sorted() vs original list:
L = [3, 1, 2]
print(sorted(L))
print(L)''',
         '''Output:
[1, 2, 3]
[3, 1, 2]
Explanation: sorted() does not modify list.'''),

        ('''20. reverse():
L = [1, 2, 3]
L.reverse()
print(L)''',
         '''Output:
[3, 2, 1]
Explanation: reverse() modifies list in-place.''')
    ]

    for q, a in qa:
        print(q)
        input("\nPress Enter to see the answer...")
        print(a)
        print("\n" + "-" * 55 + "\n")




        
def list_notes():
    print("""
========================================
ONE-SHOT NOTES : LIST
========================================

1. WHAT IS A LIST?
------------------
A list is an ordered collection of elements enclosed in square brackets [ ].
A list can store multiple values of different data types.

Example:
marks = [90, 85, 78]
data = [10, "Python", 3.5]

----------------------------------------

2. CHARACTERISTICS OF LIST
--------------------------
✔ Ordered
✔ Mutable (can be changed)
✔ Allows duplicate values
✔ Can store different data types

----------------------------------------

3. ACCESSING LIST ELEMENTS (INDEXING)
-------------------------------------
Indexing starts from 0.
Negative indexing is also allowed.

Example:
lst = [10, 20, 30, 40]
print(lst[0])    # 10
print(lst[-1])   # 40

----------------------------------------

4. LIST SLICING
----------------
Used to access a part of the list.

Syntax:
list[start : stop : step]

Example:
lst = [1, 2, 3, 4, 5]
print(lst[1:4])    # [2, 3, 4]
print(lst[::-1])   # [5, 4, 3, 2, 1]

----------------------------------------

5. LIST OPERATIONS
------------------
1. Concatenation (+)
a = [1, 2]
b = [3, 4]
print(a + b)

2. Repetition (*)
print([1, 2] * 3)

3. Membership (in, not in)
print(3 in [1, 2, 3])     # True

----------------------------------------

6. COMMON LIST FUNCTIONS
------------------------
Function        Description
append()        Adds element at end
insert()        Adds element at position
remove()        Removes element
pop()           Removes last element
sort()          Sorts the list
reverse()       Reverses the list
len()           Returns length

Example:
lst = [3, 1, 2]
lst.sort()
print(lst)

----------------------------------------

7. LIST TRAVERSAL
------------------
Accessing elements one by one.

Using for loop:
for i in [10, 20, 30]:
    print(i)

Using while loop:
lst = [10, 20, 30]
i = 0
while i < len(lst):
    print(lst[i])
    i += 1

----------------------------------------

8. MODIFYING A LIST (MUTABILITY)
--------------------------------
Lists are mutable.

Example:
lst = [1, 2, 3]
lst[0] = 10
print(lst)

----------------------------------------

9. NESTED LIST
---------------
A list inside another list.

Example:
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])   # 2

----------------------------------------

EXAM TIPS:
✔ Lists are mutable (important difference from strings)
✔ Practice indexing and slicing
✔ Output-based questions are common
✔ Know difference between append() and insert()

========================================
END OF NOTES
========================================
""")

    




def tuple_dictionary_MCQs():

    questions = [

        {
            "q": "Which of the following creates a tuple?",
            "options": ["A. (10)", "B. (10,)", "C. [10]", "D. {10}"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\nt[1] = 9\nprint(t)",
            "options": ["A. (1, 9, 3)", "B. Error", "C. (1, 2, 3)", "D. None"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\nprint(t * 2)",
            "options": ["A. (1, 2, 3, 1, 2, 3)", "B. (2, 4, 6)", "C. Error", "D. None"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nt = (10, 20, 30, 40)\nprint(t[1:3])",
            "options": ["A. (20, 30)", "B. (20, 30, 40)", "C. (10, 20)", "D. Error"],
            "ans": "A"
        },

        {
            "q": "Which statement is TRUE?",
            "options": ["A. Tuples are mutable", "B. Tuples support slicing", "C. Tuples have append()", "D. Tuples can change size"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, [2, 3])\nt[1][0] = 99\nprint(t)",
            "options": ["A. Error", "B. (1, [99, 3])", "C. (99, [2, 3])", "D. (1, [2, 3])"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, (3, 4))\nt[2] = (5, 6)",
            "options": ["A. (1, 2, (5, 6))", "B. Error", "C. (1, 2, (3, 4))", "D. None"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\na, b = t",
            "options": ["A. a=1, b=2", "B. Error", "C. a=1, b=2, c=3", "D. a=1, b=3"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\na, *b = t\nprint(b)",
            "options": ["A. [2, 3]", "B. (2, 3)", "C. 2", "D. Error"],
            "ans": "A"
        },

        {
            "q": "Which can be a dictionary key?",
            "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {1: 'A', 1: 'B'}\nprint(d)",
            "options": ["A. {1: 'A'}", "B. {1: 'B'}", "C. Error", "D. {1: 'A', 1: 'B'}"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {'a': 1, 'b': 2}\nprint(d['c'])",
            "options": ["A. None", "B. Error", "C. 0", "D. 'c'"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {'x': 1}\nprint(d.get('y', 5))",
            "options": ["A. None", "B. Error", "C. 5", "D. 'y'"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nd = {'a': 1}\nprint(d.pop('a'))",
            "options": ["A. {'a': 1}", "B. 1", "C. None", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {'a': 1}\nprint(d.pop('b', 99))",
            "options": ["A. Error", "B. None", "C. 99", "D. 'b'"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nd = {'a': 1, 'b': 2}\nfor x in d:\n    print(x, end=' ')",
            "options": ["A. a b", "B. 1 2", "C. (a,1) (b,2)", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nd = {'a': 1, 'b': 2}\nfor x in d.values():\n    print(x, end=' ')",
            "options": ["A. a b", "B. 1 2", "C. Error", "D. (a,1)"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {'a': [1, 2]}\ne = d.copy()\ne['a'].append(3)\nprint(d)",
            "options": ["A. {'a': [1, 2]}", "B. {'a': [1, 2, 3]}", "C. Error", "D. {'a': 3}"],
            "ans": "B"
        },

        {
            "q": "Assertion (A): Tuples are immutable.\nReason (R): Elements of a tuple cannot be changed.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "Assertion (A): Dictionary keys must be immutable.\nReason (R): Mutable objects can change hash value.",
            "options": [
                "A. Both A and R are true & R explains A",
                "B. Both A and R are true but R doesn’t explain A",
                "C. A is true, R is false",
                "D. A is false, R is true"
            ],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nt = ()\nprint(type(t))",
            "options": ["A. <class 'tuple'>", "B. <class 'list'>", "C. <class 'set'>", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nt = 1, 2, 3\nprint(t)",
            "options": ["A. (1, 2, 3)", "B. [1, 2, 3]", "C. Error", "D. {1, 2, 3}"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\nprint(len(t))",
            "options": ["A. 2", "B. 3", "C. Error", "D. 4"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\nprint(t + (4))",
            "options": ["A. (1, 2, 3, 4)", "B. Error", "C. (1, 2, 3)", "D. None"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {}\nprint(type(d))",
            "options": ["A. <class 'dict'>", "B. <class 'set'>", "C. <class 'tuple'>", "D. Error"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nd = dict()\nd[1] = 'One'\nd[1.0] = 'Float'\nprint(d)",
            "options": ["A. {1: 'One', 1.0: 'Float'}", "B. {1: 'Float'}", "C. {1.0: 'One'}", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {True: 'Yes', 1: 'No'}\nprint(d)",
            "options": ["A. {True: 'Yes', 1: 'No'}", "B. {1: 'Yes'}", "C. {True: 'No'}", "D. Error"],
            "ans": "C"
        },

        {
            "q": "What will be the output?\nd = {'a': 1, 'b': 2}\nprint(list(d))",
            "options": ["A. [1, 2]", "B. ['a', 'b']", "C. [('a',1), ('b',2)]", "D. Error"],
            "ans": "B"
        },

        {
            "q": "What will be the output?\nd = {'x': 1}\nprint('x' in d)",
            "options": ["A. True", "B. False", "C. Error", "D. None"],
            "ans": "A"
        },

        {
            "q": "What will be the output?\nt = (1, 2, 3)\nprint(max(t) - min(t))",
            "options": ["A. 1", "B. 2", "C. 3", "D. Error"],
            "ans": "B"
        }
    ]

    random.shuffle(questions)

    score = 0
    correct = []
    incorrect = []

    print("\n📘 TUPLE & DICTIONARY MCQ QUIZ STARTED\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['q']}")
        for opt in q["options"]:
            print(opt)

        user_ans = input("Enter your choice (A/B/C/D): ").upper()

        if user_ans == q["ans"]:
            print("✅ Correct!\n")
            score += 1
            correct.append(q["q"])
        else:
            print(f"❌ Wrong! Correct Answer: {q['ans']}\n")
            incorrect.append(q["q"])

    print("\n================================")
    print(" QUIZ ANALYSIS")
    print("================================")
    print(f"Total Questions : {len(questions)}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {len(questions) - score}")
    print("Score           :", score, "/", len(questions))

    print("\n✔ Correctly Answered Questions:")
    for q in correct:
        print("-", q)

    print("\n❌ Incorrectly Answered Questions:")
    for q in incorrect:
        print("-", q)

    print("\n Quiz Completed! Tuples & Dictionaries mastered!")

def tuple_dict_hots():
    qa = [

        ('''1. Predict the Output:
t = (10)
print(type(t))''',
         '''Output:
<class 'int'>
Explanation: Without comma, it is NOT a tuple.'''),

        ('''2. Predict the Output:
t = (10,)
print(type(t))''',
         '''Output:
<class 'tuple'>
Explanation: Single-element tuple requires a comma.'''),

        ('''3. Predict the Output:
t = (1, 2, 3)
t[0] = 9
print(t)''',
         '''Error:
TypeError: tuple object does not support item assignment
Explanation: Tuples are immutable.'''),

        ('''4. MOST TRICKY:
t = (1, 2, [3, 4])
t[2][0] = 9
print(t)''',
         '''Output:
(1, 2, [9, 4])
Explanation: Mutable object inside tuple can change.'''),

        ('''5. Predict the Output:
t = (1, 2, 3)
print(t * 2)''',
         '''Output:
(1, 2, 3, 1, 2, 3)
Explanation: Tuple multiplication repeats elements.'''),

        ('''6. Loop + Tuple:
t = (10, 20, 30)
for x in t:
    x += 5
print(t)''',
         '''Output:
(10, 20, 30)
Explanation: Tuples cannot be modified.'''),

        ('''7. Tuple concatenation:
t = (1, 2, 3)
t = t + (4, 5)
print(t)''',
         '''Output:
(1, 2, 3, 4, 5)
Explanation: New tuple created.'''),

        ('''8. Tuple slicing:
t = (1, 2, 3, 4)
print(t[1:3])''',
         '''Output:
(2, 3)'''),

        ('''9. Tuple unpacking:
a, b, c = (10, 20, 30)
print(a, b, c)''',
         '''Output:
10 20 30'''),

        ('''10. Tuple unpacking error:
a, b = (1, 2, 3)''',
         '''Error:
ValueError: too many values to unpack'''),

        ('''11. Extended unpacking:
a, *b = (1, 2, 3, 4)
print(a, b)''',
         '''Output:
1 [2, 3, 4]
Explanation: *b collects remaining elements.'''),

        ('''12. Dictionary access:
d = {1: 'A', 2: 'B'}
print(d[3])''',
         '''Error:
KeyError: 3
Explanation: Key does not exist.'''),

        ('''13. Dictionary get():
d = {1: 'A', 2: 'B'}
print(d.get(3, "Not Found"))''',
         '''Output:
Not Found
Explanation: get() avoids KeyError.'''),

        ('''14. Dictionary overwrite:
d = {1: 'A', 2: 'B'}
d[2] = 'C'
print(d)''',
         '''Output:
{1: 'A', 2: 'C'}
Explanation: Keys are unique.'''),

        ('''15. Duplicate keys:
d = {1: 'A', 1: 'B', 1: 'C'}
print(d)''',
         '''Output:
{1: 'C'}
Explanation: Last value wins.'''),

        ('''16. Loop through dictionary:
d = {1: 10, 2: 20}
for k in d:
    print(k, d[k])''',
         '''Output:
1 10
2 20'''),

        ('''17. Modifying values variable:
d = {1: 2, 3: 4}
for v in d.values():
    v += 1
print(d)''',
         '''Output:
{1: 2, 3: 4}
Explanation: v is a copy, not reference.'''),

        ('''18. VERY TRICKY:
d = {'a': 1, 'b': 2}
for k, v in d.items():
    d[k] = v * 2
print(d)''',
         '''Output:
{'a': 2, 'b': 4}
Explanation: Modifying values during iteration is allowed.'''),

        ('''19. pop():
d = {1: 'A', 2: 'B'}
print(d.pop(1))
print(d)''',
         '''Output:
A
{2: 'B'}'''),

        ('''20. pop() with default:
d = {1: 'A', 2: 'B'}
print(d.pop(3, "NA"))''',
         '''Output:
NA'''),

        ('''21. setdefault():
d = {'x': 1}
d.setdefault('x', 5)
d.setdefault('y', 10)
print(d)''',
         '''Output:
{'x': 1, 'y': 10}
Explanation: setdefault adds key only if absent.'''),

        ('''22. Nested dictionary:
d = {'A': {'B': 10}}
print(d['A']['B'])''',
         '''Output:
10'''),

        ('''23. Mutable value inside dict:
d = {1: [10, 20]}
d[1].append(30)
print(d)''',
         '''Output:
{1: [10, 20, 30]}
Explanation: Values can be mutable.''')
    ]

    for q, a in qa:
        print(q)
        input("\nPress Enter to see the answer...")
        print(a)
        print("\n" + "-"*60 + "\n")

def tuple_dictionary_notes():
    print("""
========================================
ONE-SHOT NOTES : TUPLE & DICTIONARY
========================================

PART A : TUPLE
==============

1. WHAT IS A TUPLE?
------------------
A tuple is an ordered collection of elements enclosed in parentheses ( ).
Tuples can store multiple values of different data types.

Example:
t = (10, 20, 30)
data = (1, "Python", 3.5)

----------------------------------------

2. CHARACTERISTICS OF TUPLE
---------------------------
✔ Ordered
✔ Immutable (cannot be changed)
✔ Allows duplicate values
✔ Faster than lists

----------------------------------------

3. ACCESSING TUPLE ELEMENTS
---------------------------
Indexing starts from 0.
Negative indexing is allowed.

Example:
t = (5, 10, 15)
print(t[0])    # 5
print(t[-1])   # 15

----------------------------------------

4. TUPLE SLICING
----------------
Used to access a part of a tuple.

Syntax:
tuple[start : stop : step]

Example:
t = (1, 2, 3, 4, 5)
print(t[1:4])    # (2, 3, 4)

----------------------------------------

5. TUPLE OPERATIONS
-------------------
1. Concatenation (+)
print((1, 2) + (3, 4))

2. Repetition (*)
print((1, 2) * 3)

3. Membership (in, not in)
print(2 in (1, 2, 3))   # True

----------------------------------------

6. TUPLE FUNCTIONS
------------------
Function        Description
len()           Returns length
max()           Largest value
min()           Smallest value
count()         Counts occurrences
index()         Returns index

----------------------------------------

7. IMMUTABILITY OF TUPLE
------------------------
Tuple elements cannot be changed.

❌ Wrong:
t[0] = 100

✔ Correct:
t = (100,) + t[1:]

----------------------------------------

PART B : DICTIONARY
===================

8. WHAT IS A DICTIONARY?
-----------------------
A dictionary is an unordered collection of key-value pairs enclosed in braces { }.

Example:
student = {"name": "Asha", "age": 16, "marks": 90}

----------------------------------------

9. CHARACTERISTICS OF DICTIONARY
--------------------------------
✔ Stores data as key : value
✔ Keys are unique and immutable
✔ Values can be changed
✔ Unordered (no index)

----------------------------------------

10. ACCESSING DICTIONARY ELEMENTS
---------------------------------
Values are accessed using keys.

Example:
print(student["name"])

----------------------------------------

11. MODIFYING A DICTIONARY
--------------------------
Values can be updated or added.

Example:
student["age"] = 17
student["grade"] = "A"

----------------------------------------

12. COMMON DICTIONARY FUNCTIONS
-------------------------------
Function        Description
keys()          Returns all keys
values()        Returns all values
items()         Returns key-value pairs
get()           Returns value safely
pop()           Removes item
len()           Number of pairs

Example:
print(student.keys())

----------------------------------------

13. DICTIONARY TRAVERSAL
------------------------
Using for loop:

for key in student:
    print(key, student[key])

----------------------------------------

EXAM TIPS:
✔ Tuples are immutable, lists are mutable
✔ Dictionary keys must be unique
✔ Practice output-based questions
✔ Know common methods

========================================
END OF NOTES
========================================
""")

    

    

while True:
    print('\nWHAT YOU NEED:\n 1.one-shot notes \n 2.MCQs \n 3.HOTs \n 4.EXIT\n')#CHOICE
    ch=input('enter your choice:')
    if not ch.isdigit():
        print('enter the right choice!!')
    else:
        choice=int(ch)
        if choice>0 and choice<5:
            print('\n\nTHE TOPICS: \n 1.looping constructs \n 2.string \n 3.list \n 4.tuple & dictionary \n 5.Go Back\n')#TOPIC
            topic=input('ENTER YOUR TOPIC CHOICE: ')
            if not topic.isdigit():
                print('enter the right choice!!')
            else:
                to=int(topic)
                if to>0 and to<6:
                    if choice==1:
                        if to==1:
                              print('Click below to access the notes.')
                              looping_constructs_notes()
                        elif to==2:
                              print('Click below to access the notes.')
                              string_notes()
                        elif to==3:
                              print('Click below to access the notes.')
                              list_notes()
                        elif to==4:
                              print('Click below to access the notes.')
                              tuple_dictionary_notes()
                        elif to==5:
                              continue
                        else:
                              print()
                    elif choice==2:
                        if to==1:
                              looping_constructs_MCQs()
                        elif to==2:
                              string_MCQs()
                        elif to==3:
                              list_MCQs()
                        elif to==4:
                              tuple_dictionary_MCQs()
                        elif to==5:
                              continue
                        else:
                              print()
                    elif choice==3:
                          if to==1:
                                looping_constructs_HOTs()
                          elif to==2:
                                string_HOTs()
                          elif to==3:
                                list_HOTs()
                          elif to==4:
                                tuple_dict_hots()
                          elif to==5:
                                continue
                          else:
                                print()
                    elif choice==4:
                          break
                    else:
                          print()
                  
                else:
                      print('Enter the right choice!!')
        else:
              print('Enter the right choice!!')
              
                        
                                
                                
                                
                          
                              
                              
                            
                            
                        
                        
                        

    
    

