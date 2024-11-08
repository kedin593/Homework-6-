# Report Module 06


1. Thinking about for-in loops, they all work on sequential data, so based on that, what is each "item" for each of these sequential data types. Separate each item by a comma after the => symbol. 
    * Example: range(1, 3) => 1, 2
    * ('aloha', 'world') => 
    * ['aloha', 'world'] =>
    * 'aloha world' =>

2. For this for-in loop, write an equivalent while loop. 
    ```python
    for i in range(1, 10, 2):
        print(i)
    ```
    ```python
    # your code here

    ```

3. For each of the following types below, write mutable or immutable for them.
   * String -
   * List -
   * Tuple -
   * Set -

4. Given the following code, what is printed?

     ```python
    def mystery_function(x):
        x[1][0] = 100

    x = (3, [1, 2, 3], [4, 5, 6])
    print(x)
    mystery_function(x)
    print(x)
    ```

    ```text
    put the output here

    ```

5. Now with that said, what happens after each of the following statements (you can just say Error if it would error). To help `del` removes or deletes the item. 
    * `del x[1][0]`
    * `del x[1]`
    * `x[1] = []`
    * `x[1] = x[2]`


6. Given the code below:

    ```python
    lst1 = [1, 2, 3]
    lst2 = [4, 5, 6]
    value1 = lst1 + lst2
    value2 = lst1.append(lst2)
    ```

    What is the value of:

    * lst1 
    * lst2
    * value1
    * value2
  
7. Research time. Find an example of the .join method. Write python
   code demonstrating what it does. 

    ```python

    ```

8. Take the following code:

    ```python
    value = [x for x in range(1, 30, 3)]
    ```

    What is the value of value? 

    Rewrite the list comprehension (the term used for the syntax above) as
    both a for loop and while loop.




## Deeper Thinking

For this deeper thinking, we ask you simply to write a reflection of what you have learned up to this point. The reflection should be prose (not bullet points). You should reflect on what you have learned, your study habits, and areas you may need to improve. Be nice to yourself! You have come a long way. Use this reflection as a critical evaluation of areas for growth for this second half of the semester. It should only be about a paragraph or so.

It may sound weird to reflect, but there is a bunch of research on the benefits of reflection both in improving your code quality, but also your hire-ability and later salaries. Treat good reflection as a skill that will improve your career, and this is an opportunity to practice.  