# Fix the loop! (8 kyu)

- **Language:** Python  
- **Kata Link:** https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python
- **Description:**  
Your collegue wrote an simple loop to list his favourite animals. 
But there seems to be a minor mistake in the grammar, 
which prevents the program to work. Fix it! :)
If you pass the list of your favourite animals to the function, 
you should get the list of the animals with orderings and newlines added.
For example, passing in:
[ "dog", "cat", "elephant" ]
will result in:
"1. dog\n2. cat\n3. elephant\n"

- **Fix Summary:**  
  1. write len()
  2. replace the sentence with "f"{str(i + 1)}. {animals[i]}\n""