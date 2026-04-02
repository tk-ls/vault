## Questions and Follow-Ups!

*If you have any questions at all relating to informatics, or want to follow up something from class, feel free to send me a message through AUCoding Admin.*

## Why C++?

Clearly we want to learn C++. But why not stick with Python?
- Python is **slow** to run.
- C++ has a lot of built-in tools to help us solve informatics problems.

> [!note] Misconception
> "C++ is so much harder than Python. It's impossible to write."

Although C++ has a slightly more complicated **syntax**, remember:
- C++ is a programming language just like Python. A program's underlying logic is always easily transferrable - only the way it's written differs.
- You don't need to know a lot of language specific features (classes, pointers, templating, metaprogramming, etc) to do informatics!

> [!tip]
> We ought to think about programming as a **tool** to get something done, rather than a standalone skill.
> 
> Informatics is a subject where translating your ideas into code isn't the main point. Coming up with efficient solutions to problems is. So you don't need to know *that* much about programming.

## 0. Programming Setup

- Visit [Online GDB](https://www.onlinegdb.com/) - you won't have to worry about the terminal commands to run a script.
- Set the **Language** on upper right to be `C++ 20` (this is just a version of C++).
- To run a program, press `Run` . The output appears on the console at the bottom.

## 1. Your First Program

A program in Python as so:
```python
print("Hello world")
```

Is written formally in C++ as:
```cpp basic.cpp
#include <iostream>

int main() {
	std::cout << "Hello world!" << "\n";
	return 0;
}
```

`#include <iostream>`:
- C++ as a language itself is extremely bare. There isn't a lot of support for things like input, output, etc.
- `#include <...>` goes at the very **start** of your program, and tells C++ what libraries to import.
- It's similar to Python's `import` (e.g. `import math`).
- `iostream` is basically a library which allows for "input output stream" (input and output).

`int main() {...}`":
- In C++, any commands you write must be wrapped inside things called **functions**.
- Anything outside a function is called **global-scope**. (e.g. line 2 is part of global scope).
- `int main() {}` introduces something called a **main function**. When the program is run, it'll start executing the code inside `main()`.
- The `int` keyword means that this function **returns** an integer. C++ is more strict about types than Python, but this will be discussed later.

`std::cout`:
- In C++, we get input (if using `iostream`) through things called **streams**. Think of streams like conveyors or pipes leading in and out of your program.
- `cout` (pronounced "C-out") means "character out"; it's a *stream* designed to pipe things to an output window (by default this is set to the terminal, and called `stdout` - standard out).
- The `std::` prefix is similar to `math.sqrt()` etc. in Python;
	- Since `cout` comes from the `iostream` 'package' (part of a bigger package called the C++ Standard Template Library), we have to specify it with `std` (the 'name'/'namespace' of the package).
	- We can remove the need to type this out every time by writing `using namespace std;` after our imports/includes.

`<<`:
- When dealing with I/O (input/output), C++ recognises `<<` as an **insertion operator**.
- This is basically telling C++, "put whatever is on the right into whatever is on the left".
- We are shoving the string `"Hello world!"` into the pipe which sends things to output.

`"\n"`:
- C++ offers more control than Python over our input format.
- In Python, `print("hi")` always creates a new line after `"hi"` in the console.
- In C++, we can selectively choose whether or not to include this new line. C++ treats `\n` as a single character, called a **newline character**.

Every line in C++ has to end with a **semicolon**. This is because C++ actually doesn't care about lines. You can even put everything on one line (kind of)!
```cpp
#include<iostream>
int main() { cout << "Hello world\n"; return 0; }
```

If we were to make the above Python script more C++-like, we would write it as:
```python
def main():
	print("Hello world!" + "\n", end="")

if __name__ == "__main__":
	main()
```

## Exercises for Section 1

> [!todo] Exercise 1.1
> Try writing a program to print the following to the console:
> ```
> Hello world!
> This is a new
> line!
> ```
> You can do this with a single `cout` line, or you can do this with multiple!

> [!todo] Exercise 1.2
> Replace `iostream` with a special library, `bits/stdc++.h`. Does the program still run?
> 
> `bits/stdc++.h` basically imports *everything* from the C++ Standard Template Library into your code! You won't have to worry about includes ever again (for the most part :D)

## Interlude: Code-Style

C++ allows you to be way more flexible with how you write your code:
- You don't have to write every statement on its own line.
- You don't have to follow indentation rules.
Even so, to maintain readability (for you, mostly), please don't do wacky things ;-;

C++ also supports comments like Python. These are demarcated with `//` rather than `#`:
```cpp
int main() {
	// this function does nothing
	return 0; // return :D
}
```

## 2A. Variables

Python also has variables - to jog your memory:
- A **variable** is a container for some value. These variables can store anything from **numbers**, to **strings**, to **characters**, to **booleans**, etc.
- You can think of variables as a **box** that holds **information**
    - Each **box** has a **label** (variable name)
    - The **inside** of the box contains some **value**
        - This could be something like a **number** (a whole number is called an **integer**)
    - The **type** of the box depends on what it stores; a string? a decimal point number?

C++ is *a lot* stricter about types than Python. For instance, in Python, we can reassign types:
```python
age = None
...
if not age:
	age = 11
```
But in C++,  we have to specify the type of variable we're storing when we create it!
```cpp
#include<bits/stdc++.h>

int main() {
	int age = 11;
	return 0;
}
```

The syntax for this looks like: `<type> <name> = <value>;`
- If you leave the value blank, C++ will often fill the variable with random garbage!

## 2B. Types

C++ has a lot more variable types than Python.
- We never care about how big integers are in Python. A variable can store `x = 1` just as well as it can store `x = 9999999999999`. However, in C++, there are different types for small and big integers!
- Generally, problems will warn you if solving them requires big integers

*From AIO 2024, Problem 5: Tennis Robot II*

Below are the common types you'll see when working in C++:

| Type          | Meaning                                                                                        | Example                                 |
| ------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------- |
| `int`         | Integer: a whole number in the range around $\pm 2 \times 10^9$                                | `int age = 11;`                         |
| `long long`   | Larger integer: a whole number in the range around $\pm 9 \times 10^{18}$                      | `long long big_number = 9999999999999;` |
| `float`       | Decimal number, storing floating points                                                        | `float height = 1.6;`                   |
| `bool`        | Boolean value: true/false, 1/0 (Note: no capitalisation of `true/false`!)                      | `bool is_adult = false;`                |
| `char`        | Character: a single ASCII character (think letter on keyboard) - this includes things like`\n` | `char grade = 'A';`                     |
| `std::string` | String: a list of characters                                                                   | `std::string name = "Alex";`            |
>[!caution]
>In C++, an `std::string` is demarcated with double quotes `"blah"`, while a `char` is denoted with single quotes `'x'` - don't get them mixed up!

We switch between types (known as **typecasting**) with the syntax `(<new_type>)(<variable>)`:
```cpp
int a = 3;
cout << (float)(a) << "\n";
```
Compare this to Python:
```python
a = 3
print(float(a))
```

## 2C. Operations

C++ supports operations almost identical to Python's:
- `a + b`; wow guess what this does
- `a - b`; wow
- `a * b`; wow
- `a / b`; ok this one is different - C++ performs something known as **integer division**.
	- It will look at the integers above and below a floating point value, and return the one **closest to zero**.
	- Think about how this is different from Python's `a / b` or even its `a // b`.
- `a % b`; wow i wonder what this does

Also, like Python, there are shorthands for certain operations:
- `a += 2`; increments `a` by 2.
- `a -= 2`; i don't need to explain this one to you guys
- `a *= 2`; ok buddy
- `a /= 2`; this is equivalent to `a = a / 2`.
- `a %= 2`, etc etc etc

However, **unlike** Python, there are some interesting new shorthands:
- `a++`; increments `a` by 1.
- `a--`; decrements `a` by 1.
This will serve useful in the future.

## Exercises for Section 2

> [!todo] Exercise 2.1
> What will this code output? Hypothesise and then test it out!
> ```cpp
> #include<bits/stdc++.h>
> 
> int main() {
> 	int x = 5;
> 	int y = x + 2;
> 	std::cout << x << " " << y << "\n";
> 	return 0;
> }
> ```

>[!todo] Exercise 2.2
>Write a program. It should assign a variable `name` with a string for your name. It should create a new variable `greeting` which is your name prepended with `"Hello, "`. Print this greeting.

>[!todo] Exercise 2.3
>Previously, I mentioned omitting the initial value will simply fill the variable with some random garbage.
>
>But don't trust me on this - try it out! What happens when you print a variable which you didn't set an explicit value for?

## 3. Input/Output

We already discussed output. In C++, input is streamed from the terminal into your program using the `cin` (C-in) standard input stream.
- Again, think of this as a source or tap of some sort flowing into your program.

To request data, we use the `>>` operator instead (move stuff from `stdin` into our variables):
```cpp
#include<bits/stdc++.h>

int main() {
	int x, y; // this declares two variables of type `int` in one go!
	std::cin >> x >> y; // cin is really smart and knows to separate by space
	std::cout << x << " " << y << "\n";
	return 0;
}
```

`std::cin` generally will separate by whitespaces (the `' '` character), and automatically do things like strip newlines, etc.

There is no automatic prompting system in C++ (compare this with Python's `input("Enter your input: ")` feature). As such, we need to manually write the prompts:

```cpp
#include<bits/stdc++.h>
using namespace std;

int main() {
	string name;
	cout << "Enter your name: ";
	cin >> name;
	cout << "Hello, " << name << "\n";
	return 0;
}
```

## Exercises for Section 3

>[!todo] Exercise 3.1
>What will be in the variable `line` after the input reading?
>```cpp title:main.cpp
>#include<bits/stdc++.h>
>using namespace std;
>
>int main() {
>	string line = "";
>	cin >> line;
>	return 0;
>}
>```
>
>```txt title:cmd.txt
>this is a line of text
>```

>[!todo] Exercise 3.2
>Write a program. This program should prompt for your name, and then your age. It should then print a line of the form: `Meet <name>, a person who is <age> years old.`

## Homework

>[!done] Task
>Solve [**Addition**](https://orac2.info/problem/332/) on ORAC, using C++ 20; your first C++ program to be graded!