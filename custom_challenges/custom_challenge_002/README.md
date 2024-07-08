# Connected Sinks in a Pipe System

## Problem

We have a pipe system represented by a 2D rectangular grid of cells.
There are three different types of objects located in cells in the grid,
with each cell having either 0 objects or 1 object:

- **Source**: There is 1 source in the system. It is represented by the asterisk character '*'.
- **Sinks**: There are an arbitrary number of sinks in the system.
  They are each represented by a different uppercase letter ('A', 'B', 'C', etc.).
- **Pipes**: There are 10 different shapes of pipes, represented by the following characters: '═', '║', '╔', '╗', '╚', '
  ╝', '╠', '╣', '╦', '╩'.
    - Note that each pipe has openings on 2 or 3 sides of its cell.
    - Two adjacent cells are connected if both have a pipe opening at their shared edge.
    - For example, the two cells '╩ ╦' are connected to each other through their shared edge.
      The two cells '╩ ╔' are not connected to each other through their shared edge,
      but they could possibly still be connected via a path through other cells around them.
    - Treat the source and sinks as having pipe openings at all of their edges.
      For example, the two cells 'A ╦' are connected through their shared edge,
      but the two cells 'B ╔' are not directly connected through their shared edge.
    - A sink may be connected to the source through another sink.
      For example, in the simple pipe system '* ╦ X Y ═ Z', all three sinks are connected to the source.

Your objective is to write a function that determines which sinks are connected to the source in a given pipe system.

As an example, consider the following illustration of a pipe system:

```
* ╣   ╔ ═ A
  ╠ ═ ╝    
  C   ╚ ═ B
```

In this system, the source is connected to sinks A and C, but it is _not_ connected to sink B.

A system is specified by an input text file that contains rows of data representing the grid of objects.
Each row has three pieces of information, separated by a space character:

- The character representing the object (asterisk, uppercase letter, or pipe).
- The x-coordinate of the object in the grid. This has a minimum value of 0.
- The y-coordinate of the object in the grid. This has a minimum value of 0.

Below are the contents of an input file that specifies the example pipe system illustrated above.
The order of the rows within the file is arbitrary, so the rows could be given in any order.
The coordinates (0, 0) will always correspond to the same corner of the grid as in this example,
so make sure to understand in which directions the x- and y-coordinates increase.

```
* 0 2
C 1 0
╠ 1 1
╣ 1 2
═ 2 1
╚ 3 0
╝ 3 1
╔ 3 2
═ 4 0
═ 4 2
B 5 0
A 5 2
```

## Specifications

- Your function must be written in **Python** (preferred) or **JavaScript**.
- The function should take in a single argument, which is a string containing the **file path** for the input text file.
- The function should **return** (_not print_) your answer as a **string of uppercase letters**,
  in **alphabetical order**, with no other characters.
  For example, if the code determines that sinks 'P', 'B', 'J', and 'T' are the only sinks connected to the source,
  your code should return the string 'BJPT'.