//Silverback CPU Demo Program
// Name: Emiliano Gutierrez
// Partner's name if any: N/A
// Pledge: I pledge my honor that I have abided by the Stevens Honor System.
//This program loads data from memory, does math, and stores it back


LDR R0, 0      //load value from memory address 0 into R0
LDR R1, 1      //load value from memory address 1 into R1
ADD R2, R0, R1 //add them: R2 = R0 + R1
STR R2, 2      //store result to memory address 2
SUB R3, R2, R0 //subtract: R3 = R2 - R0
STR R3, 3      //store that result to memory address 3