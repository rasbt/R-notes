04 – Reading files
================
Sebastian Raschka
6/17/2020

Source file:
<https://github.com/rasbt/R-notes/blob/master/04-reading-data-files.Rmd>

# File Reading Basics

  - If your CSV file is in your working directory (you can display your
    working directory path by executing `getcwd()`), you can load it via
    
    read.csv(‘myfile.csv’)

  - However, if the CSV file you want to read is not in your current
    working directory, this command will fail. If this is personal code
    that you are not intending on sharing with anyone else, it doesn’t
    hurt to provide the full path; for example,
    
    read.csv(‘/Users/sebastian/Data/myfile.csv’)

  - For your convenience, you could also just change your working
    directory path. Both the default R app and R Studio app have options
    for that:

![](images/03/change-working-dir-rstudio.png) \# Tabular Data

## read.table

  - Most of the time, when we use R, we are working with datasets that
    have been preprocessed into a tabular for; often, this tabular data
    is saved as a CSV file (where CSV stands for comma separated
    values).
  - A relatively universal function for loading CSV files into an R
    session is the `read.table()` function.
  - You can get detailed information about the `read.table` function by
    executing `help(read.table)` or visiting the documentation website
    at
    <https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table>
  - Here, we are going to focus on the basics, which are the following
    (including their defaults), but I recommend reading the (short)
    documentation mentioned above so that you know the other important
    options, which you will need rather sooner than later in your
    everyday practice when working with real-world data.

<!-- end list -->

    read.table(file, header = FALSE, sep = "", ...

The function arguments are as follows: - `file`: the path to the file
you want to read - `header`: a TRUE or FALSE value denoting whether your
file has column names provided in the file - `sep`: defines how the
different data columns are separated

  - Below, we are going to use the `read.table()` function on a simple
    example dataset, the Iris dataset collected by Edgar Anderson and
    first published in

> R. A. Fisher (1936). “The use of multiple measurements in taxonomic
> problems”. Annals of Eugenics. 7 (2): 179–188.
> <doi:10.1111/j.1469-1809.1936.tb02137.x>. hdl:2440/15227.

  - The Iris dataset contains the leaf-size measurements (sepal length
    and width, and petal length and width) of 3 different Iris flower
    species (Iris-Setosa, Iris-Versicolor, and Iris-Virginica).

![](images/03/iris-picture.png)

  - I’ve put an example of this file into the as `iris.csv` into the
    `./data` folder. If you open it in a text file, it looks like this:

<!-- end list -->

``` 150,4,setosa,versicolor,virginica
5.1,3.5,1.4,0.2,0
4.9,3.0,1.4,0.2,0
4.7,3.2,1.3,0.2,0
4.6,3.1,1.5,0.2,0
...
5.9,3.0,5.1,1.8,2
```

  - In this case, the first line is not a column header but a line
    provides some general information about the dataset, saying that it
    has 150 rows (flower entries), 4 features columns (sepal length and
    width in cm, and petal length and width in cm).
  - The last column is an integer column that contains values 0
    (=setosa), 1 (=versicolor), 2 (=virginica).
  - Let’s read in the file into an R dataframe using the `read.table()`
    function. In addition to the previously discussed function
    arguments, we are going to set `skip = 1`, which means that it will
    skip the first line in the dataset (because here, it is just a
    dataset
summary):

<!-- end list -->

``` r
df <- read.table(file = 'data/iris.csv', header = FALSE, sep = ',', skip = 1)
df
```

    ##      V1  V2  V3  V4 V5
    ## 1   5.1 3.5 1.4 0.2  0
    ## 2   4.9 3.0 1.4 0.2  0
    ## 3   4.7 3.2 1.3 0.2  0
    ## 4   4.6 3.1 1.5 0.2  0
    ## 5   5.0 3.6 1.4 0.2  0
    ## 6   5.4 3.9 1.7 0.4  0
    ## 7   4.6 3.4 1.4 0.3  0
    ## 8   5.0 3.4 1.5 0.2  0
    ## 9   4.4 2.9 1.4 0.2  0
    ## 10  4.9 3.1 1.5 0.1  0
    ## 11  5.4 3.7 1.5 0.2  0
    ## 12  4.8 3.4 1.6 0.2  0
    ## 13  4.8 3.0 1.4 0.1  0
    ## 14  4.3 3.0 1.1 0.1  0
    ## 15  5.8 4.0 1.2 0.2  0
    ## 16  5.7 4.4 1.5 0.4  0
    ## 17  5.4 3.9 1.3 0.4  0
    ## 18  5.1 3.5 1.4 0.3  0
    ## 19  5.7 3.8 1.7 0.3  0
    ## 20  5.1 3.8 1.5 0.3  0
    ## 21  5.4 3.4 1.7 0.2  0
    ## 22  5.1 3.7 1.5 0.4  0
    ## 23  4.6 3.6 1.0 0.2  0
    ## 24  5.1 3.3 1.7 0.5  0
    ## 25  4.8 3.4 1.9 0.2  0
    ## 26  5.0 3.0 1.6 0.2  0
    ## 27  5.0 3.4 1.6 0.4  0
    ## 28  5.2 3.5 1.5 0.2  0
    ## 29  5.2 3.4 1.4 0.2  0
    ## 30  4.7 3.2 1.6 0.2  0
    ## 31  4.8 3.1 1.6 0.2  0
    ## 32  5.4 3.4 1.5 0.4  0
    ## 33  5.2 4.1 1.5 0.1  0
    ## 34  5.5 4.2 1.4 0.2  0
    ## 35  4.9 3.1 1.5 0.2  0
    ## 36  5.0 3.2 1.2 0.2  0
    ## 37  5.5 3.5 1.3 0.2  0
    ## 38  4.9 3.6 1.4 0.1  0
    ## 39  4.4 3.0 1.3 0.2  0
    ## 40  5.1 3.4 1.5 0.2  0
    ## 41  5.0 3.5 1.3 0.3  0
    ## 42  4.5 2.3 1.3 0.3  0
    ## 43  4.4 3.2 1.3 0.2  0
    ## 44  5.0 3.5 1.6 0.6  0
    ## 45  5.1 3.8 1.9 0.4  0
    ## 46  4.8 3.0 1.4 0.3  0
    ## 47  5.1 3.8 1.6 0.2  0
    ## 48  4.6 3.2 1.4 0.2  0
    ## 49  5.3 3.7 1.5 0.2  0
    ## 50  5.0 3.3 1.4 0.2  0
    ## 51  7.0 3.2 4.7 1.4  1
    ## 52  6.4 3.2 4.5 1.5  1
    ## 53  6.9 3.1 4.9 1.5  1
    ## 54  5.5 2.3 4.0 1.3  1
    ## 55  6.5 2.8 4.6 1.5  1
    ## 56  5.7 2.8 4.5 1.3  1
    ## 57  6.3 3.3 4.7 1.6  1
    ## 58  4.9 2.4 3.3 1.0  1
    ## 59  6.6 2.9 4.6 1.3  1
    ## 60  5.2 2.7 3.9 1.4  1
    ## 61  5.0 2.0 3.5 1.0  1
    ## 62  5.9 3.0 4.2 1.5  1
    ## 63  6.0 2.2 4.0 1.0  1
    ## 64  6.1 2.9 4.7 1.4  1
    ## 65  5.6 2.9 3.6 1.3  1
    ## 66  6.7 3.1 4.4 1.4  1
    ## 67  5.6 3.0 4.5 1.5  1
    ## 68  5.8 2.7 4.1 1.0  1
    ## 69  6.2 2.2 4.5 1.5  1
    ## 70  5.6 2.5 3.9 1.1  1
    ## 71  5.9 3.2 4.8 1.8  1
    ## 72  6.1 2.8 4.0 1.3  1
    ## 73  6.3 2.5 4.9 1.5  1
    ## 74  6.1 2.8 4.7 1.2  1
    ## 75  6.4 2.9 4.3 1.3  1
    ## 76  6.6 3.0 4.4 1.4  1
    ## 77  6.8 2.8 4.8 1.4  1
    ## 78  6.7 3.0 5.0 1.7  1
    ## 79  6.0 2.9 4.5 1.5  1
    ## 80  5.7 2.6 3.5 1.0  1
    ## 81  5.5 2.4 3.8 1.1  1
    ## 82  5.5 2.4 3.7 1.0  1
    ## 83  5.8 2.7 3.9 1.2  1
    ## 84  6.0 2.7 5.1 1.6  1
    ## 85  5.4 3.0 4.5 1.5  1
    ## 86  6.0 3.4 4.5 1.6  1
    ## 87  6.7 3.1 4.7 1.5  1
    ## 88  6.3 2.3 4.4 1.3  1
    ## 89  5.6 3.0 4.1 1.3  1
    ## 90  5.5 2.5 4.0 1.3  1
    ## 91  5.5 2.6 4.4 1.2  1
    ## 92  6.1 3.0 4.6 1.4  1
    ## 93  5.8 2.6 4.0 1.2  1
    ## 94  5.0 2.3 3.3 1.0  1
    ## 95  5.6 2.7 4.2 1.3  1
    ## 96  5.7 3.0 4.2 1.2  1
    ## 97  5.7 2.9 4.2 1.3  1
    ## 98  6.2 2.9 4.3 1.3  1
    ## 99  5.1 2.5 3.0 1.1  1
    ## 100 5.7 2.8 4.1 1.3  1
    ## 101 6.3 3.3 6.0 2.5  2
    ## 102 5.8 2.7 5.1 1.9  2
    ## 103 7.1 3.0 5.9 2.1  2
    ## 104 6.3 2.9 5.6 1.8  2
    ## 105 6.5 3.0 5.8 2.2  2
    ## 106 7.6 3.0 6.6 2.1  2
    ## 107 4.9 2.5 4.5 1.7  2
    ## 108 7.3 2.9 6.3 1.8  2
    ## 109 6.7 2.5 5.8 1.8  2
    ## 110 7.2 3.6 6.1 2.5  2
    ## 111 6.5 3.2 5.1 2.0  2
    ## 112 6.4 2.7 5.3 1.9  2
    ## 113 6.8 3.0 5.5 2.1  2
    ## 114 5.7 2.5 5.0 2.0  2
    ## 115 5.8 2.8 5.1 2.4  2
    ## 116 6.4 3.2 5.3 2.3  2
    ## 117 6.5 3.0 5.5 1.8  2
    ## 118 7.7 3.8 6.7 2.2  2
    ## 119 7.7 2.6 6.9 2.3  2
    ## 120 6.0 2.2 5.0 1.5  2
    ## 121 6.9 3.2 5.7 2.3  2
    ## 122 5.6 2.8 4.9 2.0  2
    ## 123 7.7 2.8 6.7 2.0  2
    ## 124 6.3 2.7 4.9 1.8  2
    ## 125 6.7 3.3 5.7 2.1  2
    ## 126 7.2 3.2 6.0 1.8  2
    ## 127 6.2 2.8 4.8 1.8  2
    ## 128 6.1 3.0 4.9 1.8  2
    ## 129 6.4 2.8 5.6 2.1  2
    ## 130 7.2 3.0 5.8 1.6  2
    ## 131 7.4 2.8 6.1 1.9  2
    ## 132 7.9 3.8 6.4 2.0  2
    ## 133 6.4 2.8 5.6 2.2  2
    ## 134 6.3 2.8 5.1 1.5  2
    ## 135 6.1 2.6 5.6 1.4  2
    ## 136 7.7 3.0 6.1 2.3  2
    ## 137 6.3 3.4 5.6 2.4  2
    ## 138 6.4 3.1 5.5 1.8  2
    ## 139 6.0 3.0 4.8 1.8  2
    ## 140 6.9 3.1 5.4 2.1  2
    ## 141 6.7 3.1 5.6 2.4  2
    ## 142 6.9 3.1 5.1 2.3  2
    ## 143 5.8 2.7 5.1 1.9  2
    ## 144 6.8 3.2 5.9 2.3  2
    ## 145 6.7 3.3 5.7 2.5  2
    ## 146 6.7 3.0 5.2 2.3  2
    ## 147 6.3 2.5 5.0 1.9  2
    ## 148 6.5 3.0 5.2 2.0  2
    ## 149 6.2 3.4 5.4 2.3  2
    ## 150 5.9 3.0 5.1 1.8  2

  - Optionally, you can also manually assign column names using the
    `col.names`
attribute:

<!-- end list -->

``` r
column_names <- c("sepal length", "sepal width", "petal length", "petal width", "species")
df <- read.table(file = 'data/iris.csv', sep = ',', skip = 1, col.names = column_names)
df
```

    ##     sepal.length sepal.width petal.length petal.width species
    ## 1            5.1         3.5          1.4         0.2       0
    ## 2            4.9         3.0          1.4         0.2       0
    ## 3            4.7         3.2          1.3         0.2       0
    ## 4            4.6         3.1          1.5         0.2       0
    ## 5            5.0         3.6          1.4         0.2       0
    ## 6            5.4         3.9          1.7         0.4       0
    ## 7            4.6         3.4          1.4         0.3       0
    ## 8            5.0         3.4          1.5         0.2       0
    ## 9            4.4         2.9          1.4         0.2       0
    ## 10           4.9         3.1          1.5         0.1       0
    ## 11           5.4         3.7          1.5         0.2       0
    ## 12           4.8         3.4          1.6         0.2       0
    ## 13           4.8         3.0          1.4         0.1       0
    ## 14           4.3         3.0          1.1         0.1       0
    ## 15           5.8         4.0          1.2         0.2       0
    ## 16           5.7         4.4          1.5         0.4       0
    ## 17           5.4         3.9          1.3         0.4       0
    ## 18           5.1         3.5          1.4         0.3       0
    ## 19           5.7         3.8          1.7         0.3       0
    ## 20           5.1         3.8          1.5         0.3       0
    ## 21           5.4         3.4          1.7         0.2       0
    ## 22           5.1         3.7          1.5         0.4       0
    ## 23           4.6         3.6          1.0         0.2       0
    ## 24           5.1         3.3          1.7         0.5       0
    ## 25           4.8         3.4          1.9         0.2       0
    ## 26           5.0         3.0          1.6         0.2       0
    ## 27           5.0         3.4          1.6         0.4       0
    ## 28           5.2         3.5          1.5         0.2       0
    ## 29           5.2         3.4          1.4         0.2       0
    ## 30           4.7         3.2          1.6         0.2       0
    ## 31           4.8         3.1          1.6         0.2       0
    ## 32           5.4         3.4          1.5         0.4       0
    ## 33           5.2         4.1          1.5         0.1       0
    ## 34           5.5         4.2          1.4         0.2       0
    ## 35           4.9         3.1          1.5         0.2       0
    ## 36           5.0         3.2          1.2         0.2       0
    ## 37           5.5         3.5          1.3         0.2       0
    ## 38           4.9         3.6          1.4         0.1       0
    ## 39           4.4         3.0          1.3         0.2       0
    ## 40           5.1         3.4          1.5         0.2       0
    ## 41           5.0         3.5          1.3         0.3       0
    ## 42           4.5         2.3          1.3         0.3       0
    ## 43           4.4         3.2          1.3         0.2       0
    ## 44           5.0         3.5          1.6         0.6       0
    ## 45           5.1         3.8          1.9         0.4       0
    ## 46           4.8         3.0          1.4         0.3       0
    ## 47           5.1         3.8          1.6         0.2       0
    ## 48           4.6         3.2          1.4         0.2       0
    ## 49           5.3         3.7          1.5         0.2       0
    ## 50           5.0         3.3          1.4         0.2       0
    ## 51           7.0         3.2          4.7         1.4       1
    ## 52           6.4         3.2          4.5         1.5       1
    ## 53           6.9         3.1          4.9         1.5       1
    ## 54           5.5         2.3          4.0         1.3       1
    ## 55           6.5         2.8          4.6         1.5       1
    ## 56           5.7         2.8          4.5         1.3       1
    ## 57           6.3         3.3          4.7         1.6       1
    ## 58           4.9         2.4          3.3         1.0       1
    ## 59           6.6         2.9          4.6         1.3       1
    ## 60           5.2         2.7          3.9         1.4       1
    ## 61           5.0         2.0          3.5         1.0       1
    ## 62           5.9         3.0          4.2         1.5       1
    ## 63           6.0         2.2          4.0         1.0       1
    ## 64           6.1         2.9          4.7         1.4       1
    ## 65           5.6         2.9          3.6         1.3       1
    ## 66           6.7         3.1          4.4         1.4       1
    ## 67           5.6         3.0          4.5         1.5       1
    ## 68           5.8         2.7          4.1         1.0       1
    ## 69           6.2         2.2          4.5         1.5       1
    ## 70           5.6         2.5          3.9         1.1       1
    ## 71           5.9         3.2          4.8         1.8       1
    ## 72           6.1         2.8          4.0         1.3       1
    ## 73           6.3         2.5          4.9         1.5       1
    ## 74           6.1         2.8          4.7         1.2       1
    ## 75           6.4         2.9          4.3         1.3       1
    ## 76           6.6         3.0          4.4         1.4       1
    ## 77           6.8         2.8          4.8         1.4       1
    ## 78           6.7         3.0          5.0         1.7       1
    ## 79           6.0         2.9          4.5         1.5       1
    ## 80           5.7         2.6          3.5         1.0       1
    ## 81           5.5         2.4          3.8         1.1       1
    ## 82           5.5         2.4          3.7         1.0       1
    ## 83           5.8         2.7          3.9         1.2       1
    ## 84           6.0         2.7          5.1         1.6       1
    ## 85           5.4         3.0          4.5         1.5       1
    ## 86           6.0         3.4          4.5         1.6       1
    ## 87           6.7         3.1          4.7         1.5       1
    ## 88           6.3         2.3          4.4         1.3       1
    ## 89           5.6         3.0          4.1         1.3       1
    ## 90           5.5         2.5          4.0         1.3       1
    ## 91           5.5         2.6          4.4         1.2       1
    ## 92           6.1         3.0          4.6         1.4       1
    ## 93           5.8         2.6          4.0         1.2       1
    ## 94           5.0         2.3          3.3         1.0       1
    ## 95           5.6         2.7          4.2         1.3       1
    ## 96           5.7         3.0          4.2         1.2       1
    ## 97           5.7         2.9          4.2         1.3       1
    ## 98           6.2         2.9          4.3         1.3       1
    ## 99           5.1         2.5          3.0         1.1       1
    ## 100          5.7         2.8          4.1         1.3       1
    ## 101          6.3         3.3          6.0         2.5       2
    ## 102          5.8         2.7          5.1         1.9       2
    ## 103          7.1         3.0          5.9         2.1       2
    ## 104          6.3         2.9          5.6         1.8       2
    ## 105          6.5         3.0          5.8         2.2       2
    ## 106          7.6         3.0          6.6         2.1       2
    ## 107          4.9         2.5          4.5         1.7       2
    ## 108          7.3         2.9          6.3         1.8       2
    ## 109          6.7         2.5          5.8         1.8       2
    ## 110          7.2         3.6          6.1         2.5       2
    ## 111          6.5         3.2          5.1         2.0       2
    ## 112          6.4         2.7          5.3         1.9       2
    ## 113          6.8         3.0          5.5         2.1       2
    ## 114          5.7         2.5          5.0         2.0       2
    ## 115          5.8         2.8          5.1         2.4       2
    ## 116          6.4         3.2          5.3         2.3       2
    ## 117          6.5         3.0          5.5         1.8       2
    ## 118          7.7         3.8          6.7         2.2       2
    ## 119          7.7         2.6          6.9         2.3       2
    ## 120          6.0         2.2          5.0         1.5       2
    ## 121          6.9         3.2          5.7         2.3       2
    ## 122          5.6         2.8          4.9         2.0       2
    ## 123          7.7         2.8          6.7         2.0       2
    ## 124          6.3         2.7          4.9         1.8       2
    ## 125          6.7         3.3          5.7         2.1       2
    ## 126          7.2         3.2          6.0         1.8       2
    ## 127          6.2         2.8          4.8         1.8       2
    ## 128          6.1         3.0          4.9         1.8       2
    ## 129          6.4         2.8          5.6         2.1       2
    ## 130          7.2         3.0          5.8         1.6       2
    ## 131          7.4         2.8          6.1         1.9       2
    ## 132          7.9         3.8          6.4         2.0       2
    ## 133          6.4         2.8          5.6         2.2       2
    ## 134          6.3         2.8          5.1         1.5       2
    ## 135          6.1         2.6          5.6         1.4       2
    ## 136          7.7         3.0          6.1         2.3       2
    ## 137          6.3         3.4          5.6         2.4       2
    ## 138          6.4         3.1          5.5         1.8       2
    ## 139          6.0         3.0          4.8         1.8       2
    ## 140          6.9         3.1          5.4         2.1       2
    ## 141          6.7         3.1          5.6         2.4       2
    ## 142          6.9         3.1          5.1         2.3       2
    ## 143          5.8         2.7          5.1         1.9       2
    ## 144          6.8         3.2          5.9         2.3       2
    ## 145          6.7         3.3          5.7         2.5       2
    ## 146          6.7         3.0          5.2         2.3       2
    ## 147          6.3         2.5          5.0         1.9       2
    ## 148          6.5         3.0          5.2         2.0       2
    ## 149          6.2         3.4          5.4         2.3       2
    ## 150          5.9         3.0          5.1         1.8       2

  - After looking at the basic example, it would now be a good idea to
    briefly read through the other arguments available for
    `read.table()`, which you may have to use rather sooner than later.
    Here’s a complete list of these arguments:

**file**  
the name of the file which the data are to be read from. Each row of the
table appears as one line of the file. If it does not contain an
absolute path, the file name is relative to the current working
directory, getwd(). Tilde-expansion is performed where supported. This
can be a compressed file (see file).

Alternatively, file can be a readable text-mode connection (which will
be opened for reading if necessary, and if so closed (and hence
destroyed) at the end of the function call). (If stdin() is used, the
prompts for lines may be somewhat confusing. Terminate input with a
blank line or an EOF signal, Ctrl-D on Unix and Ctrl-Z on Windows. Any
pushback on stdin() will be cleared before return.)

file can also be a complete URL. (For the supported URL schemes, see the
‘URLs’ section of the help for url.)

**header**  
a logical value indicating whether the file contains the names of the
variables as its first line. If missing, the value is determined from
the file format: header is set to TRUE if and only if the first row
contains one fewer field than the number of columns.

**sep**  
the field separator character. Values on each line of the file are
separated by this character. If sep = "" (the default for read.table)
the separator is ‘white space’, that is one or more spaces, tabs,
newlines or carriage returns.

**quote**  
the set of quoting characters. To disable quoting altogether, use quote
= "". See scan for the behaviour on quotes embedded in quotes. Quoting
is only considered for columns read as character, which is all of them
unless colClasses is specified.

**dec**  
the character used in the file for decimal points.

**numerals**  
string indicating how to convert numbers whose conversion to double
precision would lose accuracy, see type.convert. Can be abbreviated.
(Applies also to complex-number inputs.)

**row.names**  
a vector of row names. This can be a vector giving the actual row names,
or a single number giving the column of the table which contains the row
names, or character string giving the name of the table column
containing the row names.

If there is a header and the first row contains one fewer field than the
number of columns, the first column in the input is used for the row
names. Otherwise if row.names is missing, the rows are numbered.

Using row.names = NULL forces row numbering. Missing or NULL row.names
generate row names that are considered to be ‘automatic’ (and not
preserved by as.matrix).

**col.names**  
a vector of optional names for the variables. The default is to use “V”
followed by the column number.

**as.is**  
controls conversion of character variables (insofar as they are not
converted to logical, numeric or complex) to factors, if not otherwise
specified by colClasses. Its value is either a vector of logicals
(values are recycled if necessary), or a vector of numeric or character
indices which specify which columns should not be converted to factors.

Note: to suppress all conversions including those of numeric columns,
set colClasses = “character”.

Note that as.is is specified per column (not per variable) and so
includes the column of row names (if any) and any columns to be skipped.

**na.strings**  
a character vector of strings which are to be interpreted as NA values.
Blank fields are also considered to be missing values in logical,
integer, numeric and complex fields. Note that the test happens after
white space is stripped from the input, so na.strings values may need
their own white space stripped in advance.

**colClasses**  
character. A vector of classes to be assumed for the columns. If
unnamed, recycled as necessary. If named, names are matched with
unspecified values being taken to be NA.

Possible values are NA (the default, when type.convert is used), “NULL”
(when the column is skipped), one of the atomic vector classes (logical,
integer, numeric, complex, character, raw), or “factor”, “Date” or
“POSIXct”. Otherwise there needs to be an as method (from package
methods) for conversion from “character” to the specified formal class.

Note that colClasses is specified per column (not per variable) and so
includes the column of row names (if any).

**nrows**  
integer: the maximum number of rows to read in. Negative and other
invalid values are ignored.

**skip**  
integer: the number of lines of the data file to skip before beginning
to read data. \* **check.names**  
logical. If TRUE then the names of the variables in the data frame are
checked to ensure that they are syntactically valid variable names. If
necessary they are adjusted (by make.names) so that they are, and also
to ensure that there are no duplicates.

**fill**  
logical. If TRUE then in case the rows have unequal length, blank fields
are implicitly added. See ‘Details’.

**strip.white**  
logical. Used only when sep has been specified, and allows the stripping
of leading and trailing white space from unquoted character fields
(numeric fields are always stripped). See scan for further details
(including the exact meaning of ‘white space’), remembering that the
columns may include the row names.

**blank.lines.skip**  
logical: if TRUE blank lines in the input are ignored.

**comment.char**  
character: a character vector of length one containing a single
character or an empty string. Use "" to turn off the interpretation of
comments altogether.

**allowEscapes**  
logical. Should C-style escapes such as be processed or read verbatim
(the default)? Note that if not within quotes these could be interpreted
as a delimiter (but not as a comment character). For more details see
scan.

**flush**  
logical: if TRUE, scan will flush to the end of the line after reading
the last of the fields requested. This allows putting comments after the
last field.

**stringsAsFactors**  
logical: should character vectors be converted to factors? Note that
this is overridden by as.is and colClasses, both of which allow finer
control.

**fileEncoding**  
character string: if non-empty declares the encoding used on a file (not
a connection) so the character data can be re-encoded. See the
‘Encoding’ section of the help for file, the ‘R Data Import/Export
Manual’ and ‘Note’.

**encoding**  
encoding to be assumed for input strings. It is used to mark character
strings as known to be in Latin-1 or UTF-8 (see Encoding): it is not
used to re-encode the input, but allows R to handle encoded strings in
their native encoding (if one of those two). See ‘Value’ and ‘Note’.

**text**  
character string: if file is not supplied and this is, then data are
read from the value of text via a text connection. Notice that a literal
string can be used to include (small) data sets within R code.

**skipNul**  
logical: should nuls be skipped?

## `read.csv`

  - Note that there is also a `read.csv()` function; it is the same as
    the `read.table()` function, except that
      - it uses the default value `sep=","` instead of `sep=""` (i.e.,
        the default column separator is a comma instead of a white
        space).
      - it uses the default value `header="TRUE"` instead of
        `header="FALSE"`
  - In practice, it does not make any difference whether you use
    `read.table` or `read.csv` given that you specify the corresponding
    function arguments correctly.
  - Below is an example showing how to use the read the previous
    `iris.csv` file using the `read.csv()`
function:

<!-- end list -->

``` r
df <- read.csv(file = 'data/iris.csv', header = FALSE, skip = 1, col.names = column_names)
df
```

    ##     sepal.length sepal.width petal.length petal.width species
    ## 1            5.1         3.5          1.4         0.2       0
    ## 2            4.9         3.0          1.4         0.2       0
    ## 3            4.7         3.2          1.3         0.2       0
    ## 4            4.6         3.1          1.5         0.2       0
    ## 5            5.0         3.6          1.4         0.2       0
    ## 6            5.4         3.9          1.7         0.4       0
    ## 7            4.6         3.4          1.4         0.3       0
    ## 8            5.0         3.4          1.5         0.2       0
    ## 9            4.4         2.9          1.4         0.2       0
    ## 10           4.9         3.1          1.5         0.1       0
    ## 11           5.4         3.7          1.5         0.2       0
    ## 12           4.8         3.4          1.6         0.2       0
    ## 13           4.8         3.0          1.4         0.1       0
    ## 14           4.3         3.0          1.1         0.1       0
    ## 15           5.8         4.0          1.2         0.2       0
    ## 16           5.7         4.4          1.5         0.4       0
    ## 17           5.4         3.9          1.3         0.4       0
    ## 18           5.1         3.5          1.4         0.3       0
    ## 19           5.7         3.8          1.7         0.3       0
    ## 20           5.1         3.8          1.5         0.3       0
    ## 21           5.4         3.4          1.7         0.2       0
    ## 22           5.1         3.7          1.5         0.4       0
    ## 23           4.6         3.6          1.0         0.2       0
    ## 24           5.1         3.3          1.7         0.5       0
    ## 25           4.8         3.4          1.9         0.2       0
    ## 26           5.0         3.0          1.6         0.2       0
    ## 27           5.0         3.4          1.6         0.4       0
    ## 28           5.2         3.5          1.5         0.2       0
    ## 29           5.2         3.4          1.4         0.2       0
    ## 30           4.7         3.2          1.6         0.2       0
    ## 31           4.8         3.1          1.6         0.2       0
    ## 32           5.4         3.4          1.5         0.4       0
    ## 33           5.2         4.1          1.5         0.1       0
    ## 34           5.5         4.2          1.4         0.2       0
    ## 35           4.9         3.1          1.5         0.2       0
    ## 36           5.0         3.2          1.2         0.2       0
    ## 37           5.5         3.5          1.3         0.2       0
    ## 38           4.9         3.6          1.4         0.1       0
    ## 39           4.4         3.0          1.3         0.2       0
    ## 40           5.1         3.4          1.5         0.2       0
    ## 41           5.0         3.5          1.3         0.3       0
    ## 42           4.5         2.3          1.3         0.3       0
    ## 43           4.4         3.2          1.3         0.2       0
    ## 44           5.0         3.5          1.6         0.6       0
    ## 45           5.1         3.8          1.9         0.4       0
    ## 46           4.8         3.0          1.4         0.3       0
    ## 47           5.1         3.8          1.6         0.2       0
    ## 48           4.6         3.2          1.4         0.2       0
    ## 49           5.3         3.7          1.5         0.2       0
    ## 50           5.0         3.3          1.4         0.2       0
    ## 51           7.0         3.2          4.7         1.4       1
    ## 52           6.4         3.2          4.5         1.5       1
    ## 53           6.9         3.1          4.9         1.5       1
    ## 54           5.5         2.3          4.0         1.3       1
    ## 55           6.5         2.8          4.6         1.5       1
    ## 56           5.7         2.8          4.5         1.3       1
    ## 57           6.3         3.3          4.7         1.6       1
    ## 58           4.9         2.4          3.3         1.0       1
    ## 59           6.6         2.9          4.6         1.3       1
    ## 60           5.2         2.7          3.9         1.4       1
    ## 61           5.0         2.0          3.5         1.0       1
    ## 62           5.9         3.0          4.2         1.5       1
    ## 63           6.0         2.2          4.0         1.0       1
    ## 64           6.1         2.9          4.7         1.4       1
    ## 65           5.6         2.9          3.6         1.3       1
    ## 66           6.7         3.1          4.4         1.4       1
    ## 67           5.6         3.0          4.5         1.5       1
    ## 68           5.8         2.7          4.1         1.0       1
    ## 69           6.2         2.2          4.5         1.5       1
    ## 70           5.6         2.5          3.9         1.1       1
    ## 71           5.9         3.2          4.8         1.8       1
    ## 72           6.1         2.8          4.0         1.3       1
    ## 73           6.3         2.5          4.9         1.5       1
    ## 74           6.1         2.8          4.7         1.2       1
    ## 75           6.4         2.9          4.3         1.3       1
    ## 76           6.6         3.0          4.4         1.4       1
    ## 77           6.8         2.8          4.8         1.4       1
    ## 78           6.7         3.0          5.0         1.7       1
    ## 79           6.0         2.9          4.5         1.5       1
    ## 80           5.7         2.6          3.5         1.0       1
    ## 81           5.5         2.4          3.8         1.1       1
    ## 82           5.5         2.4          3.7         1.0       1
    ## 83           5.8         2.7          3.9         1.2       1
    ## 84           6.0         2.7          5.1         1.6       1
    ## 85           5.4         3.0          4.5         1.5       1
    ## 86           6.0         3.4          4.5         1.6       1
    ## 87           6.7         3.1          4.7         1.5       1
    ## 88           6.3         2.3          4.4         1.3       1
    ## 89           5.6         3.0          4.1         1.3       1
    ## 90           5.5         2.5          4.0         1.3       1
    ## 91           5.5         2.6          4.4         1.2       1
    ## 92           6.1         3.0          4.6         1.4       1
    ## 93           5.8         2.6          4.0         1.2       1
    ## 94           5.0         2.3          3.3         1.0       1
    ## 95           5.6         2.7          4.2         1.3       1
    ## 96           5.7         3.0          4.2         1.2       1
    ## 97           5.7         2.9          4.2         1.3       1
    ## 98           6.2         2.9          4.3         1.3       1
    ## 99           5.1         2.5          3.0         1.1       1
    ## 100          5.7         2.8          4.1         1.3       1
    ## 101          6.3         3.3          6.0         2.5       2
    ## 102          5.8         2.7          5.1         1.9       2
    ## 103          7.1         3.0          5.9         2.1       2
    ## 104          6.3         2.9          5.6         1.8       2
    ## 105          6.5         3.0          5.8         2.2       2
    ## 106          7.6         3.0          6.6         2.1       2
    ## 107          4.9         2.5          4.5         1.7       2
    ## 108          7.3         2.9          6.3         1.8       2
    ## 109          6.7         2.5          5.8         1.8       2
    ## 110          7.2         3.6          6.1         2.5       2
    ## 111          6.5         3.2          5.1         2.0       2
    ## 112          6.4         2.7          5.3         1.9       2
    ## 113          6.8         3.0          5.5         2.1       2
    ## 114          5.7         2.5          5.0         2.0       2
    ## 115          5.8         2.8          5.1         2.4       2
    ## 116          6.4         3.2          5.3         2.3       2
    ## 117          6.5         3.0          5.5         1.8       2
    ## 118          7.7         3.8          6.7         2.2       2
    ## 119          7.7         2.6          6.9         2.3       2
    ## 120          6.0         2.2          5.0         1.5       2
    ## 121          6.9         3.2          5.7         2.3       2
    ## 122          5.6         2.8          4.9         2.0       2
    ## 123          7.7         2.8          6.7         2.0       2
    ## 124          6.3         2.7          4.9         1.8       2
    ## 125          6.7         3.3          5.7         2.1       2
    ## 126          7.2         3.2          6.0         1.8       2
    ## 127          6.2         2.8          4.8         1.8       2
    ## 128          6.1         3.0          4.9         1.8       2
    ## 129          6.4         2.8          5.6         2.1       2
    ## 130          7.2         3.0          5.8         1.6       2
    ## 131          7.4         2.8          6.1         1.9       2
    ## 132          7.9         3.8          6.4         2.0       2
    ## 133          6.4         2.8          5.6         2.2       2
    ## 134          6.3         2.8          5.1         1.5       2
    ## 135          6.1         2.6          5.6         1.4       2
    ## 136          7.7         3.0          6.1         2.3       2
    ## 137          6.3         3.4          5.6         2.4       2
    ## 138          6.4         3.1          5.5         1.8       2
    ## 139          6.0         3.0          4.8         1.8       2
    ## 140          6.9         3.1          5.4         2.1       2
    ## 141          6.7         3.1          5.6         2.4       2
    ## 142          6.9         3.1          5.1         2.3       2
    ## 143          5.8         2.7          5.1         1.9       2
    ## 144          6.8         3.2          5.9         2.3       2
    ## 145          6.7         3.3          5.7         2.5       2
    ## 146          6.7         3.0          5.2         2.3       2
    ## 147          6.3         2.5          5.0         1.9       2
    ## 148          6.5         3.0          5.2         2.0       2
    ## 149          6.2         3.4          5.4         2.3       2
    ## 150          5.9         3.0          5.1         1.8       2

## Writing files

  - `write.table()`, `write.csv()`

# Plain Text Data

  - `readLines()`
  - `writeLines()`

# Writing and Loading Objects

  - Sometimes, it is convenient to save entire R objects. For this, you
    can use the `dump()` function, which takes as input a vector of
    different objects.
  - Suppose we have created two data frame objects, `df_a` and `df_b`
    via some elaborate process, and we want to save it for use later (or
    in another session):

<!-- end list -->

``` r
df_a <- data.frame(MyIntegerVar = 1:2, MyCharVar = c("A", "B"))
df_b <- df_a <- data.frame(MyIntegerVar = 5:6, MyCharVar = c("X", "Y"))
```

  - We can save these data frames using `dump()` as follows:

<!-- end list -->

``` r
dump(c("df_a", "df_b"), file = "my-dataframes.R")
```

  - Then, we can use the `source` function to load the data frame
    objects back into the (/any) R session.

<!-- end list -->

``` r
# delete objects so we can demonstrate that
# they are indeed loaded here as an example:
rm(df_a)
rm(df_b)

# laod objects from the files on disk
source("my-dataframes.R")
df_a
```

    ##   MyIntegerVar MyCharVar
    ## 1            5         X
    ## 2            6         Y

``` r
df_b
```

    ##   MyIntegerVar MyCharVar
    ## 1            5         X
    ## 2            6         Y
