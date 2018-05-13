# Clean Code  
Reading notes of the book [Clean Code: *A Handbook of Agile Software Craftsmanship*](https://www.investigatii.md/uploads/resurse/Clean_Code.pdf) by Robert C. Martin  
## 1. Meaningful names
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
## 2. Functions
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
## 2. Comments
- The proper use of comments is to compensate for our failure to express ourself in code.  
- Comments lie. Not always, and not intentionally, but too often. The older a comment is, and the farther away it is from the code it describes, the more likely it is to be just plain wrong. The reason is simple. Programmers can’t realistically maintain them.  
- Truth can only be found in one place: the code. Only the code can truly tell you what it does. It is the only source of truly accurate information. Therefore, though comments are sometimes necessary, we will expend significant energy to minimize them.
1. <span style="color:red"></span>
