# Clean Code  
Reading notes of the book [Clean Code: *A Handbook of Agile Software Craftsmanship*](https://www.amazon.fr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=sr_1_1?ie=UTF8&qid=1526202029&sr=8-1&keywords=clean+code+a+handbook+of+agile+software+craftsmanship) by Robert C. Martin  
[Online PDF](https://www.investigatii.md/uploads/resurse/Clean_Code.pdf)
## Table of contents
1. [Meaningful names](#meaningful-names)
2. [Functions](#functions)
3. [Comments](#comments)
4. [Formatting](#formatting)
5. [Objects and data structures](#objects-and-data-structures)

## Meaningful names
The hardest thing about choosing good names is that it requires good descriptive skills and a shared cultural background.  
1. <span style="color:red">Use intention-revealing names</span>
    - Take care with your names and change them when you find better ones  
    - If a name requires a comment, then the name does not reveal its intent  
2. <span style="color:red">Avoid disinformation</span>
    - Do not refer to a grouping of accounts as an ***accountList*** unless it's actually a ***List***
    - Beware of using names which vary in small ways
    - Awful example of disinformative names: the use of lower-case ***L*** or uppercase ***O*** as variable names, especially in combination
3. <span style="color:red">Make meaningful distinctions</span>
    - If names must be different, then they should also mean something different
    - ***Info*** and ***Data*** are indistinct noise words like ***a***, ***an*** and ***the***
    - The word ***variable*** should never appear in a variable name
    - The word ***table*** should never appear in a table name
    - ***Name*** is better than ***NameString***
    - In the absence of specific conventions,
        - the variable ***moneyAmount*** is indistinguishable from ***money***
        - ***customerInfo*** is indistinguishable from ***customer***
        - ***accountData*** is indistinguishable from ***account***
        - ***theMessage*** is indistinguishable from ***message***
4. <span style="color:red">Use pronounceable names</span>
    - If you can't pronounce it, you can't discuss it without sounding like an idiot
5. <span style="color:red">Use searchable names</span>
    - Longer names trump shorter names
    - Any searchable name trumps a constant in code
6. <span style="color:red">Avoid encodings</span>
    - No need to prefix member variables with ***m_*** anymore
    - Use ***ShapeFactory*** instead of ***IShapeFactory*** to leave interfaces unadorned
7. <span style="color:red">Avoid mental mapping</span>
    - Readers shouldn't have to mentally translate your names into other names they already know
    - A loop counter may be named ***i*** or ***j*** or ***k*** (though never ***l***!) if its scope is very small and no other names can conflict with it
    - In most other contexts a single-letter name is a poor choice
8. <span style="color:red">Class names</span>
    - Classes and objects should have noun or noun phrase names like ***Customer***, ***WikiPage***, ***Account*** and ***AddressParser***
9. <span style="color:red">Method names</span>
    - Methods should have verb or verb phrase names like ***postPayment***, ***deletePage*** or ***save***
10. <span style="color:red">Don't be cute</span>
    - Say what you mean
    - Mean what you say
11. <span style="color:red">Pick one word per concept</span>
    - Pick one work for one abstract concept and stick with it
        - It is confusing to have ***fetch***, ***retrieve*** and ***get*** as equivalent methods of different classes
12. <span style="color:red">Don't pun</span>
    - Avoid using the same word for two purposes
13. <span style="color:red">Use solution domain names</span>
    - Use computer science terms, algorithm names, pattern names, math terms, and so forth
    - It is not wise to draw every name from the problem domain because we don't want our coworkers to have to run back and forth to the customer asking what every name means
14. <span style="color:red">Use problem domain names</span>
    - When there is no "programmer-ease" for what you're doing, use the name from the problem domain
    - At least the programmer who maintains your code can ask a domain expert what it means
15. <span style="color:red">Add meaningful context</span>
    - We may add context by using prefixes: ***addrFirstName***, ***addrLastName***, ***addrState***, and so on
16. <span style="color:red">Don't add gratuitous context</span>
    - The names ***accountAddress*** and ***customerAddress*** are fine names for instances of the class ***Address*** but could be poor names for classes  
## Functions
1. <span style="color:red">Small</span>
    - Functions should be small
    - Blocks and indenting
        - The blocks within ***if*** statements, ***else*** statements, ***while*** statements, and so on should be one line long. Probably that line should be a function call
        - Functions should not be large enough to hold nested structures. The indent level of a function should not be greater than 1 or 2
2. <span style="color:red">Do one thing</span>
    - Functions should do one thing. They should do it well. They should do it only
    - Another way to know that a function is doing more than "one thing" is if you can extract another function from it with a name that is not merely a restatement of tis implementation
3. <span style="color:red">One level of abstraction per function</span>
    - Make sure that the statements within our function are all at the same level of abstraction in order to make sure our function is doing "one thing"
    - Reading code from top to bottom: ***the stepdown rule***
        - We want the code to read like a top-down narrative
        - We want every function to be followed by those at the next level of abstraction so that we can read the program, descending one level of abstraction at a time as we read down the list of functions
4. <span style="color:red">Switch statements</span>
    - By their nature, ***switch*** statements always to do ***N*** things
    - Use polymorphism to make sure that each ***switch*** statement is buried in a low-level class and is never repeated
5. <span style="color:red">Use descriptive names</span>
    - A long descriptive name is better than a short enigmatic name
6. <span style="color:red">Function arguments</span>
    1. General rules
        - The ideal number of arguments for a function is zero (niladic)
        - Next comes one (monadic)
        - Followed closely by two (dyadic)
        - Three arguments (triadic) should be avoided where possible
    2. Choose good names for a function to explain the intent of the function and the order and intent of the arguments
        - In the case of a monad, the function and argument should form a very nice verb/noun pair: ***write(name)***
        - An even better name might be ***writeField(name)***, which tells us that the "name" thing is a "field"
7. <span style="color:red">Have no side effects</span>
    - Sometimes functions will make unexpected changes to the variables of its own class
    - Sometimes functions will make variables to the parameters passed into the function or to system globals
8. <span style="color:red">Prefer exceptions to returning error          codes</span>
    - If you use exceptions instead of returned error codes, then the error processing code can be separated from the happy path code and can be simplified
    - ***Try/catch*** blocks are ugly in their own right. They confuse the structure of the code and mix error processing with normal processing. So it is better to extract the bodies of the ***try*** and ***catch*** blocks out into functions of their own
    - If the keyword ***try*** exists in a function, it should be the very first word in the function and that there should be nothing after the ***catch/finally*** blocks
9. <span style="color:red">Don't repeat yourself</span>
    - Duplication may be the root of all evil in software. Many principles and practices have been created for the purpose of controlling or eliminating it
10. <span style="color:red">Structured programming</span>
    - Every function, and every block within a function, should have one entry and one exit
    - There should only be one ***return*** statement in a function, no ***break*** or ***continue*** statements in a loop, and never, ever, any ***goto*** statements
    - If you keep your functions small, then the occasional multiple ***return***, ***break***, or ***continue*** statement does no harm and can sometimes even be more expressive than the single-entry, single-exit rule
    - ***goto*** only makes sense in large functions, so it should be avoided
11. <span style="color:red">How do you write functions like this?</span>
    - When I write functions, they come out long and complicated. They have lots of indenting and nested loops. They have long argument lists. The names are arbitrary, and there is duplicated code. But I also have a suite of unit tests that cover every one of those clumsy lines of code
    - Then I massage and refine that code, splitting out functions, changing names, eliminating duplication. I shrink the methods and reorder them. Sometimes I break out whole classes, all the while keeping the tests passing
    - In the end, I wind up with functions that follow the rules I've laid down in this chapter
## Comments
- The proper use of comments is to compensate for our failure to express ourself in code.  
- Comments lie. Not always, and not intentionally, but too often. The older a comment is, and the farther away it is from the code it describes, the more likely it is to be just plain wrong. The reason is simple. Programmers can’t realistically maintain them.  
- Truth can only be found in one place: the code. Only the code can truly tell you what it does. It is the only source of truly accurate information. Therefore, though comments are sometimes necessary, we will expend significant energy to minimize them.
1. <span style="color:red">Comments do not make up for bad code</span>
    - Clear and expressive code with few comments is far superior to cluttered and complex code with lots of comments. Rather than spend your time writing the comments that explain the mess you’ve made, spend it cleaning that mess
2. <span style="color:red">Explain yourself in code</span>
    - ***if (employee.isEligibleForFullBenefits())***
3. <span style="color:red">Good comments</span>
    - **Legal comments**: copyright and authorship statements are necessary and reasonable things to put into a comment at the start of each source file
    ```python
    # Copyright (C) 2003,2004,2005 by Object Mentor, Inc. All rights reserved.
    # Released under the terms of the GNU General Public License version 2 or later.
    ```
    - Comments like this should not be contracts or legal tomes. Where possible, refer to a standard license or other external document rather than putting all the terms and conditions into the comment
    - Sometimes it is just helpful to translate the meaning of some obscure argument or return value into something that’s readable. In general it is better to find a way to make that argument or return value clear in its own right; but when its part of the standard library, or in code that you cannot alter, then a helpful clarifying comment can be useful.
    - **Warning of consequences**: sometimes it is useful to warn other programmers about certain consequences
    ```python
    # Don't run unless you have some time to kill.
    ```
    - Nowadays, we’d turn off the test case by using the **@Ignore** attribute with an appropriate explanatory string
    ```java
    @Ignore("Takes too long to run")
    ```
    - **Todo comments**: It is sometimes reasonable to leave “To do” notes in the form of ***//TODO*** comments.
    - **TODO**s are jobs that the programmer thinks should be done, but for some reason can’t do at the moment. It might be a reminder to delete a deprecated feature or a plea for someone else to look at a problem. It might be a request for someone else to think of a better name or a reminder to make a change that is dependent on a planned event. Whatever else a TODO might be, it is ***NOT*** an excuse to leave bad code in the system.
    - Amplification: a comment may be used to amplify the importance of something that may otherwise seem inconsequential
4. <span style="color:red">Bad comments</span>
Usually bad comments are crutches or excuses for poor code or justifications for insufficient decisions, amounting to little more than the programmer talking to himself.
    - **Mumbling**: Plopping in a comment just because you feel you should or because the process requires it, is a hack. Any comment that forces you to look in another module for the meaning of that comment has failed to communicate to you and is not worth the bits it consumes.
    - **Redundant comments**
    - **Misleading comments**
    - **Mandated comments**: It is just plain silly to have a rule that says that every function must have a javadoc, or every variable must have a comment
    - **Journal comments**
    - **Noise comments**
    ```java
    /** The day of the month. */
    private int dayOfMonth;
    ```
    - **Don't use a comment when you can use a function or a variable**
    - **Position markers**: A banner is startling and obvious if you don't see banners very often. So use them very sparingly, and only when the benefit is significant
    - **Closing brace comments**: Although this might make sense for long functions with deeply nested structures, it serves only to clutter the kind of small and encapsulated functions that we prefer. If you find yourself wanting to mark your closing braces, try to shorten your functions instead
    - **Attributions and bylines**: Source code control systems are very good at remembering who added what, when. No need to pollute the code with little bylines
    - **Commented-out code**: Few practices are as odious as commenting-out code
    - **Nonlocal information**: If you must write a comment, then make sure it describes the code it appears near. Don’t offer system-wide information in the context of a local comment.
    - **Too much information**: Don’t put interesting historical discussions or irrelevant descriptions of details into your comments.
    - **Inobvious connection**
## Formatting
You should take care that your code is nicely formatted. You should choose a set of simple rules that govern the format of your code, and then you should consistently apply those rules. If you are working on a team, then the team should agree to a single set of formatting rules and all members should comply. It helps to have an automated tool that can apply those formatting rules for you.  
1. <span style="color:red">The purpose of formatting</span>
The functionality that you create today has a good chance of changing in the next release, but the readability of your code will have a profound effect on all the changes that will ever be made. The coding style and readability set precedents that continue to affect maintainability and extensibility long after the original code has been changed beyond recognition. Your style and discipline survives, even though your code does not.
2. <span style="color:red">Vertical formatting</span>
    - The newspaper metaphor
        - The name should be simple but explanatory. The name, by itself, should be sufficient to tell us whether we are in the right module or not. The topmost parts of the source file should provide the high-level concepts and algorithms. Detail should increase as we move downward, until at the end we find the lowest level functions and details in the source file
    - Vertical distance
        - Concepts that are closely related should be kept vertically close to each other
        - Closely related concepts should not be separated into different files. Indeed, this is one of the reasons that protected variables should be avoided
        - Variables should be declared as close to their usage as possible
    - Vertical ordering
        - A function that is called should be below a function that does the calling
3. <span style="color:red">Horizontal formatting</span>
    - **Line width**: 20~60
    - Never have to scroll to the right
    - Use horizontal white space to associate things that are strongly related and disassociate things that are more weakly related
        - Surround the assignment operators with white space to accentuate them
        - Don't put spaces between the function names and the opening parenthesis
        - Separate arguments within the function call parenthesis to accentuate the comma and show that the arguments are separate
        - Another use for white space is to accentuate the precedence of operators
        ```java
        return (-b + Math.sqrt(determinant)) / (2*a);
        ```
        - The factors have no white space between them because they are high precedence. The terms are separated by white space because addition and subtraction are lower precedence
4. <span style="color:red">Horizontal alignment</span>
    - The alignment seems to emphasize the wrong things and leads my eye away from the true intent
    - Indentation
        - Statements at the level of the file, such as most class declarations, are not indented at all
        - Methods within a class are indented one level to the right of the class
        - Implementations of those methods are implemented one level to the right of the method declaration
        - Block implementations are implemented one level to the right of their containing block
    - Dummy scopes
    ```java
    while (dis.read(buf, 0, readBufferSize) != -1)
        ;
    ```
6. <span style="color:red">Team rules</span>
    - Every programmer has his own favorite formatting rules, but if he works in a team, then the team rules
## Objects and data structures
1. <span style="color:red">Data abstraction</span>
    - Hide implementation
        - A class does not simply push its variables out through getters and setters. Rather it exposes abstract interfaces that allow its users to manipulate the ***essence*** of the data, without having to know its implementation
    ```java
    public interface Point {
        double getX();
        double getY();
        void setCartesian(double x, double y);
        double getR();
        double getTheta();
        void setPolar(double r, double theta);
    }
    ```

    - d
