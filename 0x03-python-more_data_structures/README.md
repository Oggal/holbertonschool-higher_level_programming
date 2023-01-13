Project 0x03 1149 Python - More Data Stauctures: Set & Dictionary


So I could use emacs's scratch buffer to whiteboard, or I can publicly ramble here some.

So Task 12, write a function that converts a roman numeral into an int.
First question is 4 IV or IIII? Because if we're following the 'Rule' that no 3 letters should repeat, and a smaller 'leter' after a larger one means to subtract the value of the smaller after adding the larger (or add the value of the larger minus the smaller, it's all addion really, just of a negative) then I think I could walk from the end of the string to the front and build a running total.

If I can't google why did they link to wikipedia? that's the first place I look for a question like this... And I'm assuming what books I have with roman numerals are off limits too...
So lets make a quick list...
int 	|  string
1	|I
2	|II
3	|III
4	|Iv
5	|V
6     	|vI
7     	|vII
8	|VIII
9	|IX
10    	|X		Why does V only get used twice, where I and X get used 3 times?
87	|LXXXVII
707	|DCCVII
Just gonna assume I can pull the table from wikipedia, really just need the values of single letters
1:I  5:V
10:X 50:L
100:C	500:D
1000:M

Are roman numerals caps sensetive?
Can they be negative? not for this, can assume between 1 and 3999(MMMIC?, I know it's technically wrong but still)
Going to start with the walking sum plan.
Will need to track the current char and previous.
Create a dictionary Keyed with the chars, storing the values.
then starting at the tail of the string...
If the last letter doesn't exist, or is not larger than the current(again, starting from the right, going left):
       add the current to the sum
else:
	subtract the current from the sum(the previous was already added.)
till we hit the head of the string.
