05 – Control Structures
================
Sebastian Raschka
07/14/2020

-   [Control Structures in R](#control-structures-in-r)
    -   [If-else Statements](#if-else-statements)
    -   [While Loops](#while-loops)
    -   [For Loops](#for-loops)
    -   [Repeat and Break](#repeat-and-break)
    -   [Next](#next)
    -   [Loop functions / apply
        functions](#loop-functions-apply-functions)

Source file:
<a href="https://github.com/rasbt/R-notes/blob/master/05-control-structures.Rmd" class="uri">https://github.com/rasbt/R-notes/blob/master/05-control-structures.Rmd</a>

Control Structures in R
=======================

-   This document covers essential control structures that you may
    already be familiar with from other programming languages: if-else
    statements, while loops, and for loops.
-   While use of these programming elements is often unnecessary in
    those contexts where we use R, they can come in handy when writing
    your customized R code and functions (functions will be covered in
    the next document).

If-else Statements
------------------

-   If if-else statements are so-called conditional statements; these
    allow us to execute certain code if a condition is true, and execute
    different code, otherwise.
-   There are 3 general types of using if-else.

1.  We can use an `if` statement without the `else`, like so:

<!-- -->

    # ...
    if(some_condition) {
      # code that is executed if some_condition is TRUE
    }
    # ...

1.  The typical if-else approach:

<!-- -->

    # ...
    if(some_condition) {
      # code that is executed if some_condition is TRUE
    } else {
      # code that is executed if some_condition is FALSE
    }
    # ...

1.  Using `elif`:

<!-- -->

    # ...
    if(some_condition1) {
      # code that is executed if some_condition1 is TRUE
    } else if(some_condition_2) {
      # code that is executed if some_condition2 is TRUE
    }
    else {
      # code that is executed if some_condition1 is FALSE
      # and some_condition2 is FALSE
    }
    # ...

-   Note that we can use an arbitrary number of `else if`s. Also, in the
    last example, we can omit the `else` (similar to how we can omit the
    `else` in the first example).

-   To demonstrate the use of if-else concepts, let us take a look at a
    Fizz Buzz example
    (<a href="https://en.wikipedia.org/wiki/Fizz_buzz" class="uri">https://en.wikipedia.org/wiki/Fizz_buzz</a>).
    I.e., a number divisible by 3 results in the word “fizz,” a number
    divisible by 5 results in the word “buzz”, and a number divisible by
    both 3 and 5 results in “fizzbuzz”

<!-- -->

    num <- 15

    if(num%%3 == 0 & num%%5 == 0) {
        print("FizzBuzz")
    } else if(num%%3 == 0) {
        print("Fizz")
    } else if (num%%5 == 0) {
        print("Buzz")
    } else {
        print(num)
    }

    ## [1] "FizzBuzz"

While Loops
-----------

-   While loops allow us to repeatedly execute a portion of code as long
    as a certain condition is true.
-   For example, the following while loop implements a simple counter
    from 1 to 5:

<!-- -->

    counter <- 1
    while(counter <= 5) {
      print(counter)
      counter <- counter + 1
    }

    ## [1] 1
    ## [1] 2
    ## [1] 3
    ## [1] 4
    ## [1] 5

-   Note that it is very important to make sure that the condition can
    be and is falsified at a certain point to avoid infinite while
    loops.

For Loops
---------

-   For loops allow us to execute a portion of code a certain number of
    times.
-   Strictly speaking, for loops are not essential, since the same can
    be accomplished using while loops; however, in practice, it is often
    more convenient to use a for loop rather than a while loop.
-   If you are a Python user, be aware that in R, a sequence i:n
    included the last element (n). The example below shows a for loop
    looping over the values in a sequence (here: 1 to 5):

<!-- -->

    for(i in 1:5) {
      print(i)
    }

    ## [1] 1
    ## [1] 2
    ## [1] 3
    ## [1] 4
    ## [1] 5

    m = 10

    n_minus_1 <- 1
    n_minus_2 <- 0
    cat("# 1 :", n_minus_2, "\n") 

    ## # 1 : 0

    cat("# 2 :", n_minus_1, "\n") 

    ## # 2 : 1

    for(i in 3:m) {
      val = n_minus_1 + n_minus_2
      cat("#", i, ":", val, "\n")
      n_minus_2 <- n_minus_1
      n_minus_1 <- val
    }

    ## # 3 : 1 
    ## # 4 : 2 
    ## # 5 : 3 
    ## # 6 : 5 
    ## # 7 : 8 
    ## # 8 : 13 
    ## # 9 : 21 
    ## # 10 : 34

-   Note that for loop iterations work with any kind of sequence; for
    example, we can also iterate over character vectors:

<!-- -->

    vec <- c("H", "e", "l", "l", "o") 
    for(i in vec) {
      print(i)
    }

    ## [1] "H"
    ## [1] "e"
    ## [1] "l"
    ## [1] "l"
    ## [1] "o"

-   Also, in some contexts, it may be useful to iterate over the indices
    of a vector (as opposed to its elements). We can do this using the
    `seq_along()` function:

<!-- -->

    vec <- c("H", "e", "l", "l", "o") 
    for(i in seq_along(vec)) {
      print(i)
    }

    ## [1] 1
    ## [1] 2
    ## [1] 3
    ## [1] 4
    ## [1] 5

Repeat and Break
----------------

-   While the concepts mentioned above, if-else statements, while loops,
    and for loops are fundamental building blocks of most programming
    languages, a particular control statement in R is `repeat`, which
    allows us to execute an infinite loop.
-   Then, there’s `break` to exit such an infinite loop if a certain
    condition is met.

<!-- -->

    counter <- 1
    repeat {
      counter <- counter + 1
      if(counter >= 5){
        break
      }
    }
    print(counter)

    ## [1] 5

-   Note that we can also use `break` for escaping for loops and while
    loops. For example:

<!-- -->

    vec <- c("H", "e", "l", "l", "o") 
    for(i in vec) {
      if(i == "l"){
        break
      }
      print(i)
    }

    ## [1] "H"
    ## [1] "e"

Next
----

-   `next` is a command that allows us to skip an iteration in a loop,
    it can be used with while loops, for loops, and repeat.
-   To demo how `next` works, the following code will skip every third
    character (note that this is for demonstration purposes, and we
    could also implement a for loop with if-statements that does not
    require the use of `next` to achieve the same results):

<!-- -->

    vec <- c("H", "e", "l", "l", "o", "W", "o", "r", "l", "d") 
    for(i in seq_along(vec)) {
      if(i %% 3 == 0){
        next
      }
      print(vec[i])
    }

    ## [1] "H"
    ## [1] "e"
    ## [1] "l"
    ## [1] "o"
    ## [1] "o"
    ## [1] "r"
    ## [1] "d"

Loop functions / apply functions
--------------------------------

-   The so-called `apply` functions are functions that allow us to apply
    a function to each element in a vector or list. They are technically
    not control structures, but they let us achieve what a for-loop does
    but in a more compact form.

-   Note that there is no performance advantage of using these apply
    functions over regular for-loops, because these apply functions
    themselves are implemented using for-loops; their main advantage is
    that they save us some work and typing.

-   `lapply`: loops over a list and applies a function to each element.

-   The following example demonstrates how we can use the `lapply`
    function to compute the sum of each vector contained in a list:

<!-- -->

    data <- list(c(1., 2., 3.), c(4., 5., 6., 7.))
    lapply(data, sum)

    ## [[1]]
    ## [1] 6
    ## 
    ## [[2]]
    ## [1] 22

-   Note that `lapply` returns a list, but it can be applied to arrays
    or vectors as well – `lapply` converts the input object to a list
    internally.
-   `sapply`, short for “simplified apply” is similar to a `lapply` but
    returns a vector if possible. (The “simplification” here means that
    if each element is a single element of the same type, then the
    resulting list can be simplified into a vector.)

<!-- -->

    data <- list(c(1., 2., 3.), c(4., 5., 6., 7.))
    sapply(data, sum)

    ## [1]  6 22

-   there are more variants, such as `apply` (for matrices), `tapply`
    (applying functions to ragged arrays), and `mapply` (a multivariate
    version of `lapply` for working with multiple lists) that you can
    check out using the help function (e.g., `?apply` to learn more
    about the `apply` function)
