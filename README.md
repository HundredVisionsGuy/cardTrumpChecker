# cardTrumpChecker()
You are tasked with writing a function that receives two cards each in the form of a tuple, and your job is to determine with of the two cards trumps the other.

**Notes:**
----------
The rules are as follows:
* cards are numbered from 1 - 10
* each card has one of three different colors:
  * green,
  * yellow, and
  * red.
* Higher numbers always trump (beat) lower numbers
  * color doesn't matter if one number is higher than the other
* When the numbers are the same...
  * yellow trumps (beats) green
  * red trumps (beats) yellow
* If both cards have the same number and color, card1 always wins
  * it was played first

**Inputs:**
----------
cardTrumpChecker() receives two inputs (tuples): **card1** and **card2**

* NOTE: each card will be a tuple, like so: **(*card*, *rank*, *color*)**
  * **card** is a string: *"card1"* or *"card2"*
  * **rank** is an integer: between 1 and 10
  * **color** is an string: *"red"* *"yellow"* or *"green"*
  * Examle: ("card1", 9, "red")

**Output:**
------------
cardTrumpChecker() returns 1 output (a string): **card**

**Hints:**
------------
For this challenge, since you are using tuples, you're going to want to review indexing with tuples.

**Examples:**
inputs => output/s
--------------------------------
* ('card1', 5, 'yellow') ('card2', 7, 'green') => card2
* ('card1', 5, 'red') ('card2', 5, 'yellow') => card1
* ('card1', 10, 'green') ('card2', 10, 'yellow') => card2
* ('card1', 2, 'green') ('card2', 1, 'red') => card1
* ('card1', 10, 'red') ('card2', 10, 'red') => card1
