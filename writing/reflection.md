# List Uniquification

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following command?

`poetry run datauniquifier --approach dictionary --column 1 --data-file input/data.txt`

```The chosen approach to uniquify the file is: dictionary

The data file that contains the input is: input\data.txt


 The data file contains 50000 data values in it!

Let's do some uniquification!

🔍 So, was this an efficient approach to uniquifying the data?

The function 'unique_dictionary' took: 0.0050 sec

Estimated overall memory according to the operating system:
   21.82421875 megabytes

🔍 So, did this remove a lot of duplicate data?

   The number of values removed from the data: 49476
   The percent reduction due to uniquification: 98.952
```

### What are the first five lines of the contents of the file that is input into the `datauniquifier`?

```dana74@mahoney-perez.com,"Administrator, charities/voluntary organisations"
nathanjohnson@davila.net,Software engineer
pbush@gmail.com,"Journalist, newspaper"
timothy75@chang.com,Osteopath
gsparks@yahoo.com,"Psychologist, clinical"
```

### What is the output from running the test suite with the command `poetry run task test-silent`?

```collected 11 items

tests\test_analyze.py ......
tests\test_extract.py ..
tests\test_uniquify.py The function 'unique_set' took: 0.0000 sec
.The function 'unique_set' took: 0.0000 sec
.The function 'unique_set' took: 0.0000 sec
.

====================================================== 11 passed in 0.08s ====================================================== 
```

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

```for line in csv.reader(
    data.splitlines(),
    quotechar='"',
    delimiter=",",
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True,
):
```

This code is basically a for loop but when exploring it in further detail one realizes that it is a for loop that will 

#### Explain in detail the purpose of the following two Python functions

TODO: Write at least one paragraph to explain the requested source code

```
def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

## Explain in detail the purpose of the following Python function

```def timing(function):
    """Define a profiling function for execution time."""
    @wraps(function)
    def wrap(*args, **kw):
        ts = time()
        result = function(*args, **kw)
        te = time()
        print("The function %r took: %2.4f sec" % (function.__name__, te - ts))
        return result

    return wrap
```

This function is very important whenever you want to learn how to time something that you are experimenting with in code. Essentially, this function is going to be a function within a function and it is going to create a function called wrap which will

### Experimental Results

## Please use output from running the program to explain which Python function is the fastest. How did you know?

TODO: Your response to this question should use concrete numbers that resulted
from running the `datauniquifier` program.

## Please use output from running the program to explain how much list uniquification decreases the size of each column.

TODO: Your response to this question should use concrete numbers that resulted
from running the `datauniquifier` program.

## Professional Development

### What was the most confusing concept in this assignment? What did you do to ultimately understand it?

The most confusing concept for me in this project was actually something that I think was meant to be rather simple. I was most confused by the extract function. After figuring out how to write this function, I learned that it was because I didnt fully understand the way that I was meant to break up the string and how the indexing of the string, now turned into a list, would be vital in making sure that the right information is passed through the CLI and presented when called. I guess the reason that this was confusing is because when I was first thinking about the function, I thought that when I broke the string of values from the data.txt file they would be broken first by .splitlines, and then another time by .split(",") and then this would give me the data I needed to get everything to work. However, what I didnt realize was that the data would then only be presented like so: ['[string1]', '[string2]']. This was important because I didnt fully understand that I needed to then index the values out using the [column] variable to attain the data I needed.

### After completing this assignment, what do you think is the purpose of running experiments?

I think the purpose of running experiments is important to understand as a computer scientist because often times when people are learning computer science they are asked to create code in labs and they may not have a full understanding of what it does, and can be pushed to do for them. I think that a lot about computer science is rigid and makes it so that we have very specific ways of doing things, but I think learning about experiments can be really important to give us the "why" behind the coding assingments that we do. Why would I need to know somehting like this and how can it be used to benefit me in some way is always important when looking at any scientific structure.

### Explain how a technical concept in this assignment is connected to a topic in a different assignment

I think the concept of reading and opening files, though rather basic in nature, is something that will always be linked to and used in further things that we do in this class. I think that it can definitely get more complex but I think that knowing how to do it well can also be really monumental in making code both efficient and effective.

### At your own option, do you have any other insights to share about this assignment?
