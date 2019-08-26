
### Comedy Show Lab

Imagine that you are the producer for a comedy show at your school.  We need you to use knowledge of linear regression to make predictions as to the success of the show.

### Working through a linear regression 

The comedy show is trying to figure out how much money to spend on advertising in the student newspaper.  The newspaper tells the show that 
 * For every two dollars spent on advertising, three students attend the show.  
 * If no money is spent on advertising, no one will attend the show.  

Write a linear regression function called `attendance` that shows the relationship between advertising and attendance expressed by the newspaper.  


```python
def attendance(advertising):
    pass
```


```python
attendance(100) # 150
```


```python
attendance(50) # 75
```

As the old adage goes, "Don't ask the barber if you need a haircut!" Likewise, despite what the student newspaper says, the comedy show knows from experience that they'll still have a crowd even without an advertising budget.  Some of the comedians in the show have friends (believe it or not), and twenty of those friends will show up.  Write a function called `attendance_with_friends` that models the following: 

 *  When the advertising budget is zero, 20 friends still attend
 * Three additional people attend the show for every two dollars spent on advertising


```python
def attendance_with_friends(advertising):
    pass
```


```python
attendance_with_friends(100) # 170
```


```python
attendance_with_friends(50) # 95
```

#### Plot it

Let's help plot this line so you can get a sense of what your $m$ and $b$ values look like in graph form.

Our x values can be a list of `initial_sample_budgets`,  equal to a list of our budgets.  And we can use the outputs of our `attendance_with_friends` function to determine the list of `attendance_values`, the attendance at each of those x values.


```python
initial_sample_budgets = [0, 50, 100]
attendance_values = [20, 95, 170]
```

First we import the necessary plotly library, and `graph_obs` function, and setup `plotly` to be used without uploading our plots to its website.

Finally, we plot out our regression line using our `attendance_with_friends` function.  Our x values will be the budgets.  For our y values, we need to use our `attendance_with_friends` function to create a list of y-value attendances for every input of x. 


```python
import plotly
from plotly import graph_objs
plotly.offline.init_notebook_mode(connected=True)

trace_of_attendance_with_friends = graph_objs.Scatter(
    x=initial_sample_budgets,
    y=attendance_values,
)

plotly.offline.iplot([trace_of_attendance_with_friends])
```


```python
trace_of_attendance_with_friends
```

Now let's write a couple functions that we can use going forward.  We'll write a function called `m_b_data` that given a slope of a line, $m$, a y-intercept, $b$, will return a dictionary that has a key of `x` pointing to a list of `x_values`, and a key of `y` that points to a list of `y_values`.  Each $y$ value should be the output of a regression line for the provided $m$ and $b$ values, for each of the provided `x_values`.


```python
def m_b_data(m, b, x_values):
    pass
```


```python
m_b_data(1.5, 20, [0, 50, 100]) # {'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
```

Now let's write a function called `m_b_trace` that uses our `m_b_data` function to return a dictionary that includes keys of `name` and `mode` in addition to `x` and `y`.  The values of `mode` and `name` are provided as arguments.  When the `mode` argument is not provided, it has a default value of `lines` and when `name` is not provided, it has a default value of `line function`.


```python
def m_b_trace(m, b, x_values, mode = 'lines', name = 'line function'):
    pass
```


```python
m_b_trace(1.5, 20, [0, 50, 100]) 
# {'mode': 'line', 'name': 'line function', 'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
```

### Calculating lines

The comedy show decides to advertise for two different shows.  The attendance looks like the following.

| Budgets (dollars)        | Attendance           | 
| ------------- |:-------------:| 
| 200       |400 | 
| 400       |700 | 

In code, we represent this as the following:


```python
first_show = {'budget': 200, 'attendance': 400}
second_show = {'budget': 400, 'attendance': 700}
```

Write a function called `marginal_return_on_budget` that returns the expected amount of increase per every dollar spent on budget.  

> The function should use the formula for calculating the slope of a line provided two points.


```python
def marginal_return_on_budget(first_show, second_show):
    pass
```


```python
marginal_return_on_budget(first_show, second_show) # 1.5
```


```python
first_show
```

Just to check, let's use some different data to make sure our `marginal_return_on_budget` function calculates the slope properly.


```python
imaginary_third_show = {'budget': 300, 'attendance': 500}
imaginary_fourth_show = {'budget': 600, 'attendance': 900}
marginal_return_on_budget(imaginary_third_show, imaginary_fourth_show) # 1.3333333333333333
```

Great!  Now we'll begin to write functions that we can use going forward.  The functions will calculate attributes of lines in general and can be used to predict the attendance of the comedy show.

Take the following data.  The comedy show spends zero dollars on advertising for the next show.  The attendance chart now looks like the following:

| Budgets (dollars)        | Attendance           | 
| ------------- |:-------------:| 
| 0       |100 | 
| 200       |400 | 
| 400       |700 | 


```python
budgets = [0, 200, 400]
attendance_numbers = [100, 400, 700]
```

To get you started, we'll provide a function called `sorted_points` that accepts a list of x values and a list of y values and returns a list of point coordinates sorted by their x values.  The return value is a list of sorted tuples.


```python
def sorted_points(x_values, y_values):
    values = list(zip(x_values, y_values))
    sorted_values = sorted(values, key=lambda value: value[0])
    return sorted_values
```


```python
sorted_points([4, 1, 6], [4, 6, 7])
```

#### build_starting_line 

In this section, we'll write a function called `build_starting_line`. The function that we end up building simply draws a line between our points with the highest and lowest x values.  We are selecting these points as an arbitrary "starting" point for our regression line.

>  As John von Neumann said, "truth … is much too complicated to allow anything but approximations."  All models are inherently wrong, but some are useful.  In future lessons, we will learn how to build a regression line that accurately matches our dataset. For now, we will focus on building a useful "starting" line using the first and last points along the x-axis.

**First**, write a function called `slope` that, given a list of x values and a list of y values, will use the points with the lowest and highest x values to calculate the slope of a line.


```python
def slope(x_values, y_values):
    pass
```


```python
slope([200, 400], [400, 700]) # 1.5
```

Now write a function called `y_intercept`.  Use the `slope` function to calculate the slope if it isn't provided as an argument. Then we will use the slope and the values of the point with the highest x value to return the y-intercept.


```python
def y_intercept(x_values, y_values, m = None):
    pass
```


```python
y_intercept([200, 400], [400, 700]) # 100
```


```python
y_intercept([0, 200, 400], [10, 400, 700]) # 10
```

Now write a function called `build_starting_line` that given a list of `x_values` and a list of `y_values` returns a dictionary with a key of `m` and a key of `b` to return the `m` and `b` values of the calculated regression line.  Use the  `slope` and `y_intercept` functions to calculate the line.


```python
def build_starting_line(x_values, y_values):
    pass
```


```python
build_starting_line([0, 200, 400], [10, 400, 700]) # {'b': 10.0, 'm': 1.725}
```

**Finally**, let's write a function called `expected_value_for_line` that returns the expected attendance given the $m$, $b$, and $x$ $value$.


```python
first_show = {'budget': 300, 'attendance': 700}
second_show = {'budget': 400, 'attendance': 900}

shows = [first_show, second_show]
```


```python
def expected_value_for_line(m, b, x_value):
    pass
```


```python
expected_value_for_line(1.5, 100, 100) # 250
```

### Using our functions

Now that we have built these functions, we can use them on our dataset.  Uncomment and run the lines below to see how we can use our functions going forward.


```python
first_show = {'budget': 200, 'attendance': 400}
second_show = {'budget': 400, 'attendance': 700}
third_show = {'budget': 300, 'attendance': 500}
fourth_show = {'budget': 600, 'attendance': 900}

comedy_shows = [first_show, second_show, third_show, fourth_show]

show_x_values = list(map(lambda show: show['budget'], comedy_shows))
show_y_values = list(map(lambda show: show['attendance'], comedy_shows))
```


```python
def trace_values(x_values, y_values, mode = 'markers', name="data"):
    return {'x': x_values, 'y': y_values, 'mode': mode, 'name': name}
```


```python
def plot(traces):
    plotly.offline.iplot(traces)
```


```python
# comedy_show_trace = trace_values(show_x_values, show_y_values, name = 'comedy show data')
# comedy_show_trace
```


```python
# show_starting_line = build_starting_line(show_x_values, show_y_values)
# show_starting_line
```


```python
# trace_show_line = m_b_trace(show_starting_line['m'], show_starting_line['b'], show_x_values, name = 'starting line')
```


```python
# trace_show_line
```


```python
# plot([comedy_show_trace, trace_show_line])
```

As we can see above, we built a "starting" regression line out of the points with the lowest and highest x values. We will learn in future lessons how to improve our line so that it becomes the "best fit" given all of our dataset, not just the first and last points. For now, this approach sufficed since our goal was to practice working with and plotting line functions.
