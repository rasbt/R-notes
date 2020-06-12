02 – Basics
================
Sebastian Raschka

# R Resources and Help

  - Have a look at the official introduction to R, which is freely
    available at
    <https://cran.r-project.org/doc/manuals/r-release/R-intro.html> – it
    is a much more thorough version compared to my series of notes.

# Executing code

  - Personally, I prefer using R Studio when working with R (for
    details, see [01-installing-r.md](01-installing-r.md))
  - In R Studio, you can set up a R Markdown document where you can
    write notes and execute code at the same time – it’s similar to a MS
    Word document that also allows you to run code; in addition, there
    is also a console view to execute code in the conventional way:

![](images/02/run-code-rstudio.png) - One thing to notice about R,
coming from Python or other programming languages, is the somewhat
unusual assignment operator `<-`. We use the assignment operator to
assign an expression (right side of the assignment operator) to a
variable (left side of the assignnment operator). For example

``` r
my_variable <- 3+5
```

  - Note that assignments per se don’t result in any “visible” outputs.
    For example, one way to show the result of executing the expression
    above, `3+5`, you can call the variable that it was assigned to.

<!-- end list -->

``` r
my_variable
```

    ## [1] 8

  - (In computer science contexts, “showing” some result is often called
    “printing” due to the history of computers – back in the day, before
    computer monitors were invented, results had to be printed on
    paper.)

# Reading files

  - If your CSV file is in your working directory (you can display your
    working directory path by executing `getcwd()`), you can load it via
    
    read.csv(‘myfile.csv’)

  - However, if the CSV file you want to read is not in your current
    working directory, this command will fail. If this is personal code
    that you are not intendin on sharing with anyone else, it doesn’t
    hurt to provide the full path; for example,
    
    read.csv(‘/Users/sebastian/Data/myfile.csv’)

  - For your convenience, you could also just change your working
    directory path. Both the default R app and R Studio app have options
    for that:

![](images/02/change-working-dir-rstudio.png)

# Data Types

  - Similar to Python, everything in R is an object.

## Integers

## Floats (real numbers)

  - You may be used to referring to real numbers as floats (or doubles)
    in other programming languages; in R, real numbers are represented
    via the `numeric` data type

numeric in R,

## Boolean

  - 
## Sequences

``` r
1:10
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10

## Strings / Character Vectors

## One-Indexing

# Functions

  - Note that in contrast to Python, R doesn’t require an explicit
    `return` call – if `return` is not used, the R function will return
    the output of its last expression. For instance, the following two
    code snippets

<!-- end list -->

``` r
mean_squared_error <- function(x, y){
  mean_diff <- mean(x - y)
  mean_diff^2
}

mean_squared_error(c(1, 2, 3), c(1, 2, 5))
```

    ## [1] 0.4444444

and

``` r
mean_squared_error <- function(x, y){
  mean_diff <- mean(x - y)
  return(mean_diff^2)
}

mean_squared_error(c(1, 2, 3), c(1, 2, 5))
```

    ## [1] 0.4444444

both return `0.4444444`

  - For your convenience, you can save functions in a separate file and
    load it into your current R session. E.g., you can save the
    `mean_squared_error` we created above as a .R file, for example,
    `mse.R`. Then, you can source the file in your current R session to
    load the function, a shown in the screenshot below:

![](images/02/load-func.png)

# Developing R Packages

  - If you are interested in developing your own R packages (also known
    as “extensions”), have a look at the official guide available at
    <https://cran.r-project.org/doc/manuals/r-release/R-exts.html>.
