# 📚 CHILD Language Documentation

**Version 1.0.0**

Complete reference guide for the CHILD programming language.

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Basic Concepts](#basic-concepts)
- [Variables](#variables)
- [Data Types](#data-types)
- [Input and Output](#input-and-output)
- [Operators](#operators)
- [Lists](#lists)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Functions](#functions)
- [Comments](#comments)
- [Best Practices](#best-practices)
- [Error Messages](#error-messages)
- [Examples](#examples)

---

## Introduction

CHILD (Computational High-level Instruction Language for Dummies) is a beginner-friendly programming language that uses simple, English-like syntax. It's designed for people who find traditional programming languages intimidating.

### Philosophy

- **Readable**: Code should read like English
- **Simple**: No confusing symbols or syntax
- **Intuitive**: Commands do what they say
- **Accessible**: Anyone can learn to code

### Who Is CHILD For?

- Complete programming beginners
- People intimidated by traditional syntax
- Students learning computational thinking
- Anyone who wants to automate simple tasks

---

## Getting Started

### Installation

1. Download `child.py` from the repository
2. Make sure Python 3.6+ is installed
3. Run your first program:

```bash
python child.py myprogram.child
```

### Your First Program

Create a file called `hello.child`:

```child
say "Hello, World!"
```

Run it:

```bash
python child.py hello.child
```

---

## Basic Concepts

### File Extension

CHILD programs use `.child` or `.chld` extensions.

### Case Sensitivity

CHILD keywords are case-sensitive. Use lowercase for all commands.

✅ Correct: `say "Hello"`  
❌ Wrong: `SAY "Hello"`

### Whitespace

Indentation is recommended for readability but not required.

---

## Variables

Variables store values that you can use later in your program.

### Syntax

```child
remember VALUE as VARIABLENAME
```

### Examples

```child
remember 10 as age
remember "Alice" as name
remember 3.14 as pi
remember 5 + 3 as sum
```

### Variable Names

**Rules:**
- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Cannot be a keyword (`say`, `remember`, `if`, etc.)
- Case-sensitive (`age` and `Age` are different)

**Good names:**
```child
remember 25 as userAge
remember "blue" as favoriteColor
remember 100 as total_score
```

**Avoid:**
```child
remember 25 as x           // Too vague
remember "blue" as a       // Not descriptive
remember 100 as TOTAL      // All caps (conventional for constants)
```

---

## Data Types

CHILD automatically determines data types.

### Numbers

**Integers:**
```child
remember 42 as wholeNumber
remember -17 as negativeNumber
```

**Decimals:**
```child
remember 3.14 as pi
remember -0.5 as half
```

### Strings

Text wrapped in double quotes:

```child
remember "Hello" as greeting
remember "123" as textNumber  // This is text, not a number
```

### Lists

Collections of items:

```child
list [1, 2, 3, 4, 5] as numbers
list ["red", "green", "blue"] as colors
list [] as emptyList
```

---

## Input and Output

### SAY - Output

Print values to the screen:

```child
say "Hello!"
say 42
say myVariable
```

**Multiple lines:**
```child
say "Line 1"
say "Line 2"
say "Line 3"
```

**Combining text:**
```child
remember "World" as place
say "Hello, " + place + "!"
```

### ASK - Input

Get information from the user:

```child
ask "What is your name?" and remember it as name
ask "How old are you?" and remember it as age
```

**Note:** CHILD automatically converts numeric input to numbers.

---

## Operators

### Arithmetic Operators

```child
remember 10 + 5 as sum          // 15
remember 10 - 5 as difference   // 5
remember 10 * 5 as product      // 50
remember 10 / 5 as quotient     // 2
```

**Order of operations** (same as math):
```child
remember 2 + 3 * 4 as result    // 14 (not 20)
remember (2 + 3) * 4 as result  // 20
```

### Comparison Operators

- `is` - equals
- `is not` - not equals
- `is bigger than` - greater than
- `is smaller than` - less than

```child
if age is 18 then
    say "Exactly 18!"
end

if score is not 0 then
    say "You scored!"
end

if temperature is bigger than 30 then
    say "It's hot!"
end

if price is smaller than 10 then
    say "Affordable!"
end
```

---

## Lists

Lists store multiple values in order.

### Creating Lists

```child
list [1, 2, 3, 4, 5] as numbers
list ["apple", "banana", "cherry"] as fruits
list [] as emptyList
```

### Adding Items

```child
list [1, 2, 3] as numbers
add 4 to numbers
// numbers is now [1, 2, 3, 4]
```

### Getting Items

Lists start counting at 0:

```child
list ["red", "green", "blue"] as colors
get item 0 from colors as first    // "red"
get item 1 from colors as second   // "green"
get item 2 from colors as third    // "blue"
```

### List Size

```child
list [10, 20, 30, 40, 50] as numbers
size of numbers as count
say count  // Shows: 5
```

### Looping Through Lists

```child
list ["dog", "cat", "bird"] as animals
for each item in animals as animal
    say animal
end
```

---

## Control Flow

### IF Statements

Execute code only if a condition is true:

```child
if CONDITION then
    // code here
end
```

**Example:**
```child
remember 15 as age
if age is bigger than 12 then
    say "You're a teenager!"
end
```

### IF-OTHERWISE (Else)

Execute different code based on a condition:

```child
if CONDITION then
    // code if true
otherwise
    // code if false
end
```

**Example:**
```child
remember 85 as score
if score is bigger than 60 then
    say "You passed!"
otherwise
    say "Try again!"
end
```

### Nested IF Statements

```child
remember 85 as score

if score is bigger than 89 then
    say "Grade: A"
otherwise
    if score is bigger than 79 then
        say "Grade: B"
    otherwise
        if score is bigger than 69 then
            say "Grade: C"
        otherwise
            say "Grade: F"
        end
    end
end
```

---

## Loops

### REPEAT - Fixed Iterations

Repeat code a specific number of times:

```child
repeat NUMBER times
    // code here
end
```

**Example:**
```child
repeat 5 times
    say "Hello!"
end
```

**With variables:**
```child
remember 3 as count
repeat count times
    say "Counting..."
end
```

### COUNT - Range Loop

Count through a range of numbers:

```child
count from START to END as VARIABLE
    // code here
end
```

**Example:**
```child
count from 1 to 5 as number
    say number
end
// Output: 1, 2, 3, 4, 5
```

**Countdown:**
```child
count from 10 to 1 as number
    say number
end
say "Blastoff!"
```

### FOR EACH - Iterate Through Lists

Loop through each item in a list:

```child
for each item in LISTNAME as VARIABLE
    // code here
end
```

**Example:**
```child
list ["apple", "banana", "cherry"] as fruits
for each item in fruits as fruit
    say fruit
end
```

---

## Functions

Functions let you teach CHILD new commands.

### Defining Functions

**Simple function:**
```child
learn how to FUNCTIONNAME
    // code here
end
```

**Function with parameters:**
```child
learn how to FUNCTIONNAME with PARAM1 and PARAM2
    // code here
end
```

### Calling Functions

```child
do FUNCTIONNAME
do FUNCTIONNAME with VALUE1 and VALUE2
```

### Examples

**No parameters:**
```child
learn how to sayHello
    say "Hello, World!"
    say "Welcome to CHILD!"
end

do sayHello
```

**One parameter:**
```child
learn how to greet with name
    say "Hello, "
    say name
    say "Nice to meet you!"
end

do greet with "Alice"
do greet with "Bob"
```

**Multiple parameters:**
```child
learn how to add with a and b
    remember a + b as sum
    say "The sum is: "
    say sum
end

do add with 5 and 7
do add with 100 and 50
```

**Complex function:**
```child
learn how to printPattern with rows
    count from 1 to rows as i
        repeat i times
            say "* "
        end
        say ""
    end
end

do printPattern with 5
```

---

## Comments

Comments are notes for yourself that CHILD ignores.

### Syntax

```child
// This is a comment
```

### Examples

```child
// Calculate the total price
remember price * quantity as total

say "Total: "  // Display the result
say total
```

**Best practices:**
- Explain WHY, not WHAT
- Keep comments concise
- Update comments when code changes

---

## Best Practices

### 1. Use Descriptive Names

✅ Good:
```child
remember 25 as studentAge
remember "Mathematics" as courseName
```

❌ Avoid:
```child
remember 25 as x
remember "Mathematics" as c
```

### 2. Add Comments

```child
// Calculate discount for premium members
if memberType is "premium" then
    remember price * 0.8 as discountedPrice
end
```

### 3. Break Down Complex Problems

```child
// Instead of one long function...
learn how to processOrder with orderData
    do validateOrder with orderData
    do calculateTotal with orderData
    do sendConfirmation with orderData
end
```

### 4. Keep Functions Small

Each function should do ONE thing well.

### 5. Test Your Code

Test edge cases:
```child
// What if the list is empty?
// What if the number is negative?
// What if the user enters text instead of a number?
```

---

## Error Messages

CHILD provides helpful error messages:

### Common Errors

**Syntax Error:**
```
Oops! Error on line 5: Don't understand this command: sya "Hello"
```
Fix: Check spelling of commands

**Variable Not Found:**
```
Oops! Error on line 3: name 'userAge' is not defined
```
Fix: Make sure you `remember` the variable first

**Missing 'end':**
```
Oops! Error on line 10: Missing 'end' statement
```
Fix: Add `end` to close your `if`, `repeat`, `count`, or `learn` block

**Wrong Number of Parameters:**
```
Oops! Error on line 8: 'greet' needs 1 things, but got 2
```
Fix: Check function definition

---

## Examples

### Example 1: Temperature Converter

```child
say "=== Temperature Converter ==="
ask "Enter temperature in Celsius:" and remember it as celsius

remember celsius * 9 / 5 + 32 as fahrenheit

say "Temperature in Fahrenheit: "
say fahrenheit
```

### Example 2: Grade Calculator

```child
learn how to calculateGrade with score
    if score is bigger than 89 then
        say "Grade: A"
    otherwise
        if score is bigger than 79 then
            say "Grade: B"
        otherwise
            if score is bigger than 69 then
                say "Grade: C"
            otherwise
                say "Grade: F"
            end
        end
    end
end

ask "Enter your score:" and remember it as studentScore
do calculateGrade with studentScore
```

### Example 3: Shopping List Manager

```child
list [] as shoppingList

say "=== Shopping List Manager ==="

repeat 3 times
    ask "Add an item:" and remember it as item
    add item to shoppingList
end

say ""
say "Your shopping list:"
for each item in shoppingList as item
    say "- "
    say item
end

size of shoppingList as totalItems
say ""
say "Total items: "
say totalItems
```

### Example 4: Number Pattern

```child
learn how to printTriangle with height
    count from 1 to height as row
        repeat row times
            say "* "
        end
        say ""
    end
end

ask "Enter triangle height:" and remember it as size
do printTriangle with size
```

---

## Quick Reference

| Command | Usage | Example |
|---------|-------|---------|
| `say` | Print output | `say "Hello"` |
| `remember` | Store value | `remember 5 as x` |
| `ask` | Get input | `ask "Name?" and remember it as name` |
| `list` | Create list | `list [1, 2, 3] as nums` |
| `add` | Add to list | `add 4 to nums` |
| `get item` | Get from list | `get item 0 from nums as first` |
| `size of` | List length | `size of nums as count` |
| `if` | Condition | `if x is 5 then` |
| `otherwise` | Else | `otherwise` |
| `repeat` | Loop N times | `repeat 5 times` |
| `count` | Range loop | `count from 1 to 10 as i` |
| `for each` | List loop | `for each item in nums as n` |
| `learn` | Define function | `learn how to greet with name` |
| `do` | Call function | `do greet with "Alice"` |
| `end` | End block | `end` |
| `//` | Comment | `// This is a note` |

---

## Getting Help

- **Documentation**: You're reading it!
- **Examples**: Check the `examples/` folder
- **Issues**: [Report bugs](https://github.com/RoyalPgYtPc/child-language/issues)
- **Discussions**: [Ask questions](https://github.com/RoyalPgYtPc/child-language/discussions)

---

**Happy Coding! 🎉**

CHILD Language © 2025 RoyalPgYtPc | Licensed under GPL v3