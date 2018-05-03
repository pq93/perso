# Clean Code  
Reading notes of the book [Clean Code: *A Handbook of Agile Software Craftsmanship*](https://www.investigatii.md/uploads/resurse/Clean_Code.pdf) by Robert C. Martin  
## Chapter 1: Clean Code  
### 1. Meaningful names  
1. Use intention-revealing names  
    - Take care with your names and change them when you find better ones  
    - If a name requires a comment, then the name does not reveal its intent  
2. Avoid disinformation  
    - Do not refer to a grouping of accounts as an ***accountList*** unless it's actually a ***List***
    - Beware of using names which vary in small ways
    - Awful example of disinformative names: the use of lower-case ***L*** or uppercase ***O*** as variable names, especially in combination
3. Make meaningful distinctions
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
4. Use pronounceable names
    - If you can't pronounce it, you can't discuss it without sounding like an idiot
5. Use searchable names
    - 
