03 – Selection Syntax
================
Sebastian Raschka

Source file:
<https://github.com/rasbt/R-notes/blob/master/03-selection-syntax.Rmd>

# Selection Syntax

## Selecting Elements from Vectors and Matrices (Single Bracket Indexing)

  - We can use the single brackets `[]` indexing approach to return one
    or more elements from a vector or data frame, not that it returns
    the same object as the original.

<!-- end list -->

``` r
vec_a <- c("x", "y", "z")

vec_a[1] # return a vector containing the first element
```

    ## [1] "x"

``` r
vec_a[1:2] # return a vector containing the first two elements
```

    ## [1] "x" "y"

  - We can also combine the single bracket selection approach with
    logical operators.
  - Suppose we have the following integer vector; we can use the `>=`
    operator to select all numbers that are equal to or larger than a
    certain value (here: greater than or equal to 5):

<!-- end list -->

``` r
vec_b <- c(1:9)
vec_b
```

    ## [1] 1 2 3 4 5 6 7 8 9

``` r
vec_b[vec_b >= 5] 
```

    ## [1] 5 6 7 8 9

  - Also, we can chain multiple logical operators; let’s select all
    elements greater than 5 and smaller than 8:

<!-- end list -->

``` r
vec_b[(vec_b > 5) & (vec_b < 8)]
```

    ## [1] 6 7

### How about Matrices?

  - Analogous to the vector examples above, we can also use the single
    bracket notation to select elements and entire rows and columns from
    matrices. Let’s walk through some examples using a simple 3x2
    matrix:

<!-- end list -->

``` r
my_matrix <- matrix(1:6, 3, 2) # 3x2 matrix
my_matrix
```

    ##      [,1] [,2]
    ## [1,]    1    4
    ## [2,]    2    5
    ## [3,]    3    6

  - Use two values separated by a comma; the first value is the row
    index, the second value is the column index.
  - E.g., to select the 1st element in the 2nd row, we can do

<!-- end list -->

``` r
my_matrix[2, 1]
```

    ## [1] 2

  - To select an entire row, we omit the value after the comma. E.g., to
    select the 2nd row:

<!-- end list -->

``` r
my_matrix[2, ]
```

    ## [1] 2 5

  - Similarly, we can select an entire column by leaving the row value
    empty. E.g., to select the 2nd column:

<!-- end list -->

``` r
my_matrix[, 2]
```

    ## [1] 4 5 6

  - We can also select with logical vectors and matrices. Suppose we
    have the following matrix with missing values:

<!-- end list -->

``` r
my_matrix_with_na = my_matrix # make a copy

my_matrix_with_na[1, 2] <- NA # overwrite element with NA value
my_matrix_with_na
```

    ##      [,1] [,2]
    ## [1,]    1   NA
    ## [2,]    2    5
    ## [3,]    3    6

  - We can create a logical matrix, a mask, denoting wether a value is a
    `NA` or not:

<!-- end list -->

``` r
mask <- is.na(my_matrix_with_na)
mask
```

    ##       [,1]  [,2]
    ## [1,] FALSE  TRUE
    ## [2,] FALSE FALSE
    ## [3,] FALSE FALSE

  - The reason why we call this mask is that it allows us to select us
    specific values from the original matrix, i.e., all the TRUE values:

<!-- end list -->

``` r
my_matrix_with_na[mask]
```

    ## [1] NA

  - Note that we can also invert the selection using the `!` operator
    (which is more useful in this case, assuming we want to filter out
    NA values). E.g., we can select all the non-NA values as follows:

<!-- end list -->

``` r
!mask # inverted mask 
```

    ##      [,1]  [,2]
    ## [1,] TRUE FALSE
    ## [2,] TRUE  TRUE
    ## [3,] TRUE  TRUE

``` r
my_matrix_with_na[!mask]
```

    ## [1] 1 2 3 5 6

## Selecting from Data Frames

  - Suppose we have the following data
frame:

<!-- end list -->

``` r
df <- data.frame(MyIntegerVar = 1:4, MyCharVar = c("A", "B", "A", "B"), MyBoolVar = c(T, F, T, T))
df
```

    ##   MyIntegerVar MyCharVar MyBoolVar
    ## 1            1         A      TRUE
    ## 2            2         B     FALSE
    ## 3            3         A      TRUE
    ## 4            4         B      TRUE

  - To get the 3rd row, we can use the same bracket notation as above
    for matrices:

<!-- end list -->

``` r
df[3, ]
```

    ##   MyIntegerVar MyCharVar MyBoolVar
    ## 3            3         A      TRUE

  - Similarly, we can select the 3rd column as follows:

<!-- end list -->

``` r
df[, 3] # returns a vector
```

    ## [1]  TRUE FALSE  TRUE  TRUE

``` r
# or

df[3] # returns a data frame with 1 column
```

    ##   MyBoolVar
    ## 1      TRUE
    ## 2     FALSE
    ## 3      TRUE
    ## 4      TRUE

### Different Ways for Selecting Columns from a Data Frame

  - However, when working with data frames, we can take advantage of the
    column names when selecting columns. E.g., to select the 3rd column
    similar to `df[3]`, we can do the following:

<!-- end list -->

``` r
df['MyBoolVar']
```

    ##   MyBoolVar
    ## 1      TRUE
    ## 2     FALSE
    ## 3      TRUE
    ## 4      TRUE

  - And to select the third column similar to `df[, 3]` – returning a
    vector instead of a 1-column data frame – we can use the `$` symbol
    as follows:

<!-- end list -->

``` r
df$MyBoolVar
```

    ## [1]  TRUE FALSE  TRUE  TRUE

### Selecting Elements from a Data Frame

  - Note that the selection syntax works similar to a matrix; to select
    the 1st element of the 2nd row, we can do

<!-- end list -->

``` r
df[2, 1]
```

    ## [1] 2

  - however, we can also use the column name approach:

<!-- end list -->

``` r
df[2, 'MyIntegerVar']
```

    ## [1] 2

or

``` r
df$MyIntegerVar[2]
```

    ## [1] 2

### Conditional Selection

  - Also, similar to vectors and matrices, we can use conditional
    statements to select values. For instance, we can use the following
    to select all entries for which `MyIntegerVar` is greater than 1 and
    `MyBoolVar` is true

<!-- end list -->

``` r
df[(df['MyIntegerVar'] > 1) & (df['MyBoolVar'] == TRUE), ] 
```

    ##   MyIntegerVar MyCharVar MyBoolVar
    ## 3            3         A      TRUE
    ## 4            4         B      TRUE
