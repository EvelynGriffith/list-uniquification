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

This code is basically a for loop but when exploring it in further detail one realizes that it is a for loop that will go into a csv file and split up the string of data within that file into single lines (using the .splitlines() tool) it will then quote the character '"' and use a delimeter which is a comma. These are going to tell the program when to slpit things and where so that it knows how to display and collect data from the file. Then it will use csv.QUOTE_ALL to quote the things within the file that are needed. This for loop is used to iterate through the file break the things up that are needed based on a couple of different conditions like the comman and apastrophe and then give them back to us.

#### Explain in detail the purpose of the following two Python functions

```def calculate_reduction(list_start, list_final):
    """Calculate the reduction in the size of the list."""
    return len(list_start) - len(list_final)

This piece of code is going to calculat the difference between the start of the list and the end of the list after the program has parsed through and taken out the repeated pieces of data. This will occur by the program taking the len of the starting list, called list_start in this case, and then subtracting it by the len of the final list, list_final. This will be returned to us through the return statement that it already lives in.


def calculate_percent_reduction(list_start, list_final):
    """Calculate the percent reduction in the size of the list."""
    reduction = calculate_reduction(list_start, list_final)
    percent_reduction = (reduction / len(list_start)) * 100
    return percent_reduction
```

This function is going to calculate the percent of reduction, so essentially how much is this program taking away repeated values and where does that leave my list. It will first set a variable called reduction and it will then call on the function called calculate_reduction, which I spoke about above, and it will then use that on this function's list_start, and list_final) in this case it is important to note that list_start is not a global variable so the function does need to repeate it. From there the function will divide reduction by the len of the starting list, list_start, and then multiply it by 100. This will all be done under the variable called percent_reduction and then returned through that variable as well.

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

This function is very important whenever you want to learn how to time something that you are experimenting with in code. Essentially, this function is going to be a function within a function and it is going to create a function called wrap which will take the time of something like a stopwatch would. It does this by allowing someone to, for lack of a better term, decorate a function below it by putting the ornament @timing before the function. This tells the code that you want the function called timing to be used on that other function.

### Experimental Results

## Please use output from running the program to explain which Python function is the fastest. How did you know?

The program that is ultimately the fastest is unique_set. This function when running column 0 of the program had an output average of 0.0101. When running column 1 it had an average output of 0.0045seconds. For this experiment I chose to run each program 4 times and then take the average time for all of them. I figured that this process would give me more accurate results. The unique_set function is compared to unique_setcomprehension with average times of 0.148seconds for column 0, and 0.0058seconds for column 1. Finally I found the averages for unique_dictionary with average times of 0.0101seconds for  column 0 and 0.0058seconds for column 1.

## Please use output from running the program to explain how much list uniquification decreases the size of each column.

List unification really effects the size of the columns but some of the methods are better than others. When running setcomprehension on column 0, the only precent reduction done is 2.31%, however when running the same program on column 1 there is a 99% reduction in information in the list. If this part of the data changes at all it would be by very little percentage wise. This data should be the same for all of the functions because the data that I am feeding into those functions is the same and would therefore (or should therefore) reduce by the same percentage each time. The reason that list unification reduces the size of a column is because it is taking repeated data and merging it into one list. The repeated data is then just being stored as one. This makes sense becuase in column 1, there is a lot more that was repeated and so there is a lot more percentage that is reduced.

## Professional Development

### What was the most confusing concept in this assignment? What did you do to ultimately understand it?

The most confusing concept for me in this project was actually something that I think was meant to be rather simple. I was most confused by the extract function. After figuring out how to write this function, I learned that it was because I didnt fully understand the way that I was meant to break up the string and how the indexing of the string, now turned into a list, would be vital in making sure that the right information is passed through the CLI and presented when called. I guess the reason that this was confusing is because when I was first thinking about the function, I thought that when I broke the string of values from the data.txt file they would be broken first by .splitlines, and then another time by .split(",") and then this would give me the data I needed to get everything to work. However, what I didnt realize was that the data would then only be presented like so: ['[string1]', '[string2]']. This was important because I didnt fully understand that I needed to then index the values out using the [column] variable to attain the data I needed.

### After completing this assignment, what do you think is the purpose of running experiments?

I think the purpose of running experiments is important to understand as a computer scientist because often times when people are learning computer science they are asked to create code in labs and they may not have a full understanding of what it does, and can be pushed to do for them. I think that a lot about computer science is rigid and makes it so that we have very specific ways of doing things, but I think learning about experiments can be really important to give us the "why" behind the coding assingments that we do. Why would I need to know somehting like this and how can it be used to benefit me in some way is always important when looking at any scientific structure.

### Explain how a technical concept in this assignment is connected to a topic in a different assignment

I think the concept of reading and opening files, though rather basic in nature, is something that will always be linked to and used in further things that we do in this class. I think that it can definitely get more complex but I think that knowing how to do it well can also be really monumental in making code both efficient and effective.

### At your own option, do you have any other insights to share about this assignment?
