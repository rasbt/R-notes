02 – Data Types
================
Sebastian Raschka

-   [R Resources and Help](#r-resources-and-help)
-   [Executing code](#executing-code)
-   [Data Types](#data-types)
    -   [Floats (real numbers)](#floats-real-numbers)
    -   [Integers](#integers)
    -   [Boolean](#boolean)
-   [Data Structures](#data-structures)
    -   [Vectors and Sequences](#vectors-and-sequences)
    -   [Strings / Character Vectors](#strings-character-vectors)
    -   [Missing Values](#missing-values)
    -   [Lists](#lists)
    -   [One-Indexing](#one-indexing)
    -   [NA values](#na-values)
    -   [Matrices](#matrices)
    -   [Factors](#factors)
    -   [Data Frames](#data-frames)
    -   [Tables](#tables)

Source file:
<a href="https://github.com/rasbt/R-notes/blob/master/02-datatypes.Rmd" class="uri">https://github.com/rasbt/R-notes/blob/master/02-datatypes.Rmd</a>

R Resources and Help
====================

-   Have a look at the official introduction to R, which is freely
    available at
    <https://cran.r-project.org/doc/manuals/r-release/R-intro.html> – it
    is a much more thorough version compared to my series of notes.

Executing code
==============

-   Personally, I prefer using R Studio when working with R (for
    details, see [01-installing-r.md](01-installing-r.md))
-   In R Studio, you can set up a R Markdown document where you can
    write notes and execute code at the same time – it’s similar to a MS
    Word document that also allows you to run code; in addition, there
    is also a console view to execute code in the conventional way:

![](images/02/run-code-rstudio.png) - One thing to notice about R,
coming from Python or other programming languages, is the somewhat
unusual assignment operator `<-`. We use the assignment operator to
assign an expression (right side of the assignment operator) to a
variable (left side of the assignnment operator). For example

    my_variable <- 3+5

-   Note that assignments per se don’t result in any “visible” outputs.
    For example, one way to show the result of executing the expression
    above, `3+5`, you can call the variable that it was assigned to.

<!-- -->

    my_variable

    ## [1] 8

-   (In computer science contexts, “showing” some result is often called
    “printing” due to the history of computers – back in the day, before
    computer monitors were invented, results had to be printed on
    paper.)

Data Types
==========

-   Similar to Python, everything in R is an object. If used Python (or
    Java) before, you may be familiar with that concept. In a broader
    sense, you can think of an object as an instance of a class. In a
    sense, a class is a template that allows you to create different
    objects. You can think of a class as a cookie cutter that can make
    different cookies (objects).

Floats (real numbers)
---------------------

-   You may be used to referring to real numbers as floats (which may
    refer to single-precision or double-precision floats) in other
    programming languages. Often, double-precision floats are also
    abbreviated as “doubles.”
-   In the R community, people also often refer to float (and doubles)
    as `numeric` data type. Here, `numeric` is the class for creating
    such numbers. More precisely, by default, R will typically use
    double-precision real numbers (if you install the 64 bit version of
    R, which I recommend). In R, when you hear `numeric`, you can think
    of it as more of an umbrella term for both single- and
    double-precision floats.
-   You can check the class of an object using the `class()` function;
    and you can check gthe data type via the `typeof()` function. Note
    that by default, numbers are always double-precision floats by
    default:

<!-- -->

    typeof(1)

    ## [1] "double"

    class(1)

    ## [1] "numeric"

    typeof(1.0)

    ## [1] "double"

    class(1.0)

    ## [1] "numeric"

Integers
--------

-   Note that R, by default, creates real numbers (floats or doubles)
    when entering a number as explained in the previous section.
-   If you want to create an integer, you have to explicitly append the
    letter L. E.g.,

<!-- -->

    my_int <- 1L
    my_int

    ## [1] 1

    typeof(my_int)

    ## [1] "integer"

    class(my_int)

    ## [1] "integer"

-   By the way, you can use the `as.double()` and `as.integer()`
    functions to convert between the two respective “numeric” types:

<!-- -->

    my_float <- as.double(my_int)
    typeof(my_float)

    ## [1] "double"

    my_int <- as.integer(my_float)
    typeof(my_int)

    ## [1] "integer"

Boolean
-------

-   True and False values
-   `TRUE` & `FALSE`, or `T` and `F`

Data Structures
===============

Vectors and Sequences
---------------------

-   Vectors can be created using the `vector()` function. The following
    will create a vector consisting of 3 double-precision floats:

<!-- -->

    x <- vector(mode = "double", length = 3)
    x

    ## [1] 0 0 0

-   As you can see in the code snippet above, the vector contains all
    0’s (the default values). We can now fill it with our desired
    values, e.g., 0.1, 0.2, and 0.3, via indexing and assignment as
    follows:

<!-- -->

    x[1] <- 0.1
    x[2] <- 0.2
    x[3] <- 0.3
    x

    ## [1] 0.1 0.2 0.3

-   More conveniently, we can create vectors containing values using the
    `c()` function – think of `c` as short for “concatenate” in this
    context. The type of the vector is the same type as the type of its
    elements. For example, to create a vector of 3 real numbers, we
    could do

<!-- -->

    x <- c(0.1, 0.2, 0.3)
    x

    ## [1] 0.1 0.2 0.3

    typeof(x)

    ## [1] "double"

-   Note that we cannot mix and match objects of different types when
    creating vectors. What will happen is that the vector will assume a
    type when mixing different types, which is float or “double” in the
    case of mixing integers and real numbers:

<!-- -->

    x <- c(1L, 0.2, 0.3, 1L, 10L)
    x

    ## [1]  1.0  0.2  0.3  1.0 10.0

    class(x)

    ## [1] "numeric"

    typeof(x)

    ## [1] "double"

-   Furthermore, if we mix types, R will find a data type, as a common
    denominator, that can represent all values in the vector. For
    instance, if we have a character in the vector, it will convert
    everything to a character vector:

<!-- -->

    x <- c(5, "a")
    x

    ## [1] "5" "a"

    class(x)

    ## [1] "character"

    typeof(x)

    ## [1] "character"

-   For the same reasons mentioned above, a vector that contains
    integers and boolean values, will be cast into an integer vector:

<!-- -->

    x <- c(2, TRUE, FALSE)
    x

    ## [1] 2 1 0

    class(x)

    ## [1] "numeric"

    typeof(x)

    ## [1] "double"

-   I highly recommend avoiding mixing types in vectors; if you would
    like to mix different types, please see the section on “lists”
    below.

### Sequence vectors

-   For creating sequence vectors, similar to Python’s range, we can use
    the colon operator as shown below:

<!-- -->

    1:10

    ##  [1]  1  2  3  4  5  6  7  8  9 10

-   Note that in contrast to Python, sequences include the endpoint,
    though (here: 10; Python would return 1 … 9).

### Dot product

-   Be aware that the `*` symbol will perform an element-wise
    multiplication between two vectors:

<!-- -->

    x <- c(0.1, 0.2, 0.3)
    x * x

    ## [1] 0.01 0.04 0.09

-   To compute the dot product, we need to use the rather awkward
    looking `%*%` operator:

<!-- -->

    x %*% x

    ##      [,1]
    ## [1,] 0.14

Strings / Character Vectors
---------------------------

-   To join two character vectors, we can use the `paste` function:

<!-- -->

    paste("abc", "def", sep="")

    ## [1] "abcdef"

-   We can do C-style formatting using the `sprintf` function. For
    example,

<!-- -->

    sprintf("%d + %d = %d", 1, 2, 3)

    ## [1] "1 + 2 = 3"

-   The notation description is as follows:

<!-- -->

    %s  a string
    %d  an integer
    %0xd    an integer padded with x leading zeros
    %f  decimal notation with six decimals
    %.xf    floating point number with x digits after decimal point
    %e  compact scientific notation, e in the exponent
    %E  compact scientific notation, E in the exponent
    %g  compact decimal or scientific notation (with e)

Missing Values
--------------

-   There are two ways to represent missing values in R, NA and NaN

-   NaN stands for Not a Number, and it is used when the output of a
    mathematical representation cannot be represented by the computer.

-   NA (I assume it stands for Not Available) is used for other cases
    where a value is unknown (and it’s not a NaN); a typical case where
    you would use a NA is when you collected measurements but didn’t
    record a measurement in a particular case – in other words, the
    result is missing.

-   The `is.na()` and `is.nan()` functions allow us to test for missing
    NA and NaN values, respectively:

<!-- -->

    vector_with_na <- c(NA, 0.1, 0.5)
    is.na(vector_with_na)

    ## [1]  TRUE FALSE FALSE

    vector_with_nan <- c(NaN, 0.1, 0.5)
    is.nan(vector_with_nan)

    ## [1]  TRUE FALSE FALSE

-   Note that an NaN value evaluates to “true” via `is.na()`; however, a
    NA value does not evaluate to “true” via `is.nan()`:

<!-- -->

    is.na(vector_with_nan)

    ## [1]  TRUE FALSE FALSE

    is.nan(vector_with_na)

    ## [1] FALSE FALSE FALSE

Lists
-----

-   Similar to Python, lists in R can contain objects from different
    classes. In other words, lists allow us to mix and match data types
    (which is not supported in arrays or vectors).

<!-- -->

    x <- list(1.5, 1L, "A")
    typeof(x)

    ## [1] "list"

    x

    ## [[1]]
    ## [1] 1.5
    ## 
    ## [[2]]
    ## [1] 1
    ## 
    ## [[3]]
    ## [1] "A"

-   Note that the double-bracket refers to the list index of that
    element. For instance, to refer to the 2nd element in the list, we
    can execute

<!-- -->

    x[2]

    ## [[1]]
    ## [1] 1

One-Indexing
------------

-   As seen in the previous section on lists, R’s index, unlike other
    languages such as C or Python, starts as 1 instead of 0.

NA values
---------

Matrices
--------

-   Matrices in R are a special array class that allows us to create
    data structures for representing mathematical matrices.

-   Similar to using the `vector` function, there is a matrix function
    that allows us to create an empty matrix. Via the `nrow` and `ncol`
    parameters, we can specify the dimensions:

<!-- -->

    my_matrix <- matrix(nrow = 4, ncol = 3)
    my_matrix

    ##      [,1] [,2] [,3]
    ## [1,]   NA   NA   NA
    ## [2,]   NA   NA   NA
    ## [3,]   NA   NA   NA
    ## [4,]   NA   NA   NA

    class(my_matrix)

    ## [1] "matrix" "array"

-   Similar to what works with vectors, we can fill the matrix via
    indexing and assignments

<!-- -->

    my_matrix[1,1]<- 1.1
    my_matrix[2,1] <- 2.1
    my_matrix[2,2] <- 2.2
    my_matrix

    ##      [,1] [,2] [,3]
    ## [1,]  1.1   NA   NA
    ## [2,]  2.1  2.2   NA
    ## [3,]   NA   NA   NA
    ## [4,]   NA   NA   NA

-   You can also create a matrix from a sequence directly, i.e.,

<!-- -->

    my_matrix <- matrix(1:12, nrow = 4, ncol = 3)
    my_matrix

    ##      [,1] [,2] [,3]
    ## [1,]    1    5    9
    ## [2,]    2    6   10
    ## [3,]    3    7   11
    ## [4,]    4    8   12

-   Note, if you want to know the number of rows and columns later on,
    there’s a more efficient way than counting them. Calling the `dim`
    function will print the number of rows and columns:

<!-- -->

    dim(my_matrix)

    ## [1] 4 3

-   Interestingly, R matrices are closely tied to R vectors. In fact,
    you can reshape a vector into a matrix by modifying it’s dimension
    attribute:

<!-- -->

    my_vector <- c(1:12)
    my_vector

    ##  [1]  1  2  3  4  5  6  7  8  9 10 11 12

    my_matrix <- my_vector
    dim(my_matrix) <- c(4, 3)
    my_matrix

    ##      [,1] [,2] [,3]
    ## [1,]    1    5    9
    ## [2,]    2    6   10
    ## [3,]    3    7   11
    ## [4,]    4    8   12

-   Another way for creating matrices is by using the `cind()` function
    to combine sequences by stacking them as columns, e.g.,

<!-- -->

    my_matrix <- cbind(1:3, 4:6)
    my_matrix

    ##      [,1] [,2]
    ## [1,]    1    4
    ## [2,]    2    5
    ## [3,]    3    6

-   There is also a `rbind()` function that does the same thing via
    rows:

<!-- -->

    my_matrix <- rbind(1:3, 4:6)
    my_matrix

    ##      [,1] [,2] [,3]
    ## [1,]    1    2    3
    ## [2,]    4    5    6

### Matrix Multiplication

-   Note that matrix multiplication may seem a bit weird in R. For
    instance, using the `*` operator will not perform a matrix
    multiplication but element-wise multiplication:

<!-- -->

    my_matrix <- matrix(1:6, 3, 2)
    my_matrix

    ##      [,1] [,2]
    ## [1,]    1    4
    ## [2,]    2    5
    ## [3,]    3    6

    my_matrix * my_matrix

    ##      [,1] [,2]
    ## [1,]    1   16
    ## [2,]    4   25
    ## [3,]    9   36

-   To perform a matrix multiplication, we need to use the `%*%`
    operator (note the `t` is the transpose function, which we use in
    this simple example to quickly create a matrix with the right shape
    for multiplication):

<!-- -->

    t(my_matrix) %*% my_matrix

    ##      [,1] [,2]
    ## [1,]   14   32
    ## [2,]   32   77

### Other Handy Matrix Functions

-   Particularly useful are the functions `rowSums`, `rowMeans`,
    ’colSums`, and 'colMeans`, which are functions that can carry out
    the respective computations very efficiently. Efficiently here means
    that it both saves us a lot of typing effort and is also implemented
    in a way optimized for speed (compared to using for-loops, which are
    a topic discussed in chapter 05).

<!-- -->

    my_matrix <- matrix(1:6, 3, 2)
    my_matrix

    ##      [,1] [,2]
    ## [1,]    1    4
    ## [2,]    2    5
    ## [3,]    3    6

    rowSums(my_matrix)

    ## [1] 5 7 9

Factors
-------

-   Factors are a useful feature for representing categorical data in
    vector form.

-   Of course, everything can be handled via integer vectors, but it’s a
    nice convenience feature – you can think of factors as integer
    vectors on steroids. That is, integer vectors with the integer
    vectors replaced by labels. (R, in fact, uses an integer vector
    under the hood for factor vectors.)

-   Suppose we have the following factor vector containing a bunch of
    movie ratings:

<!-- -->

    x <- factor(c('great', 'good', 'bad', 'ok', 'good', 'good', 'great'))
    x

    ## [1] great good  bad   ok    good  good  great
    ## Levels: bad good great ok

-   As you can see above, the Levels attribute shows the unique
    categories.
-   Also, there is the handy `table` function for summarizing the counts
    per category:

<!-- -->

    table(x)

    ## x
    ##   bad  good great    ok 
    ##     1     3     2     1

-   As you may recall from my research talks or other lectures, there
    are two types of categorical data, nominal (unordered) and ordinal
    (ordered).
-   Models which assume an ordered variable, e.g., ordinal regression
    models, may require you to specify the order in the factor vector.
    By default, the unique values in the factor variable are ordered
    alphabetically.
-   Using the `levels` parameter as shown below lets us define the
    category order, for example, great &gt; good &gt; ok &gt; bad:

<!-- -->

    x <- factor(c('great', 'good', 'bad', 'ok', 'good', 'good', 'great'),
                levels=c('great', 'good', 'ok', 'bad'))
    x

    ## [1] great good  bad   ok    good  good  great
    ## Levels: great good ok bad

    table(x)

    ## x
    ## great  good    ok   bad 
    ##     2     3     1     1

Data Frames
-----------

-   Data frames are one of the best and distinguishing features of R
    when it comes to data analysis.
-   You can think of a data frame as a table (similar to a table in a
    paper, or a table in an Excel file).
-   Most data comes in tabular form, which is why data frames are a
    convenient data container to work with.
-   Btw. if you have used Python for scientific computing, you have
    likely encountered Pandas `DataFrame` objects. In fact, Pandas’ data
    frames were inspired by R.
-   Data frames look very similar to matrices, however, matrices are
    mathematical objects (rank-2 tensors) used in linear algebra
-   Also, in contrast to matrices, a data frame allows us to have
    columns with different types (and it comes with a descriptive row
    header)
-   Overall, you can think of a data frame as a fancy stack of R lists,
    which comes with a whole set of convenience functions.

<!-- -->

    df <- data.frame(MyIntegerVar = 1:4, MyCharVar = c("A", "B", "A", "B"), MyBoolVar = c(T, F, T, T))
    df

    ##   MyIntegerVar MyCharVar MyBoolVar
    ## 1            1         A      TRUE
    ## 2            2         B     FALSE
    ## 3            3         A      TRUE
    ## 4            4         B      TRUE

-   In case you are working with very long data frames and want to count
    the columns and rows, you can use the `nrow` and `ncol` functions:

<!-- -->

    nrow(df)

    ## [1] 4

    ncol(df)

    ## [1] 3

-   Suppose we want to change the row names later; for this, we can use
    the `names` function and overwrite the data frames `names`
    attribute:

<!-- -->

    names(df)

    ## [1] "MyIntegerVar" "MyCharVar"    "MyBoolVar"

    names(df) <- c("A", "B", "C")
    df

    ##   A B     C
    ## 1 1 A  TRUE
    ## 2 2 B FALSE
    ## 3 3 A  TRUE
    ## 4 4 B  TRUE

-   In practice, we usually construct data frames by loading data from a
    CSV file, for example. More on that in Chapter 03.

-   There are useful functions for data frames that we can use in
    certain contexts. For example, there are the `colSums` and
    `colMeans` function to compute data frame sums and means:

<!-- -->

    df <- data.frame(MyIntegerVar1 = 1:4, MyIntegerVar2 = 5:8)
    df

    ##   MyIntegerVar1 MyIntegerVar2
    ## 1             1             5
    ## 2             2             6
    ## 3             3             7
    ## 4             4             8

    colSums(df)

    ## MyIntegerVar1 MyIntegerVar2 
    ##            10            26

    colMeans(df)

    ## MyIntegerVar1 MyIntegerVar2 
    ##           2.5           6.5

-   Similarly, there exist `rowSums` and `rowMeans` functions:

<!-- -->

    rowSums(df)

    ## [1]  6  8 10 12

    rowMeans(df)

    ## [1] 3 4 5 6

Tables
------

A very useful data structure in R are tables created via the `tables`
function. Tables provide us with counts for each unique element in a
vector. For example

c

    letters <- c("a", "b", "a", "a", "b", "b", "a", "d", "f", "f", "f")
    table(letters)

    ## letters
    ## a b d f 
    ## 4 3 1 3

We can also use tables to extract the count for a specific item using
the square-bracket selection syntax (more on that in chapter 03):

    numbers <- c(1, 2, 1, 1, 2, 2, 1, 4, 6, 6, 6)
    t <- table(numbers)
