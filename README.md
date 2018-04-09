
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

Despite what the student newspaper says, the comedy show knows from experience that they'll still have a crowd even without an advertising budget.  Some of the comedians in the show have friends (believe it or not), and twenty of those friends will show up.  Write a function called `attendance_with_friends` that models the following: 

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

Our x-values can be a list of `initial_sample_budgets`,  equal to a list of our budgets.  And we can use the outputs of our `attendance_with_friends` function to determine the list of `attendance-values`, the attendance at each of those x-values.


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


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>



<div id="eb62a2e6-6b63-4309-bf18-8ab32f241f65" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("eb62a2e6-6b63-4309-bf18-8ab32f241f65", [{"type": "scatter", "x": [0, 50, 100], "y": [20, 95, 170]}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>



```python
trace_of_attendance_with_friends
```




    {'type': 'scatter', 'x': [0, 50, 100], 'y': [20, 95, 170]}



Now let's write a couple functions that we can use going forward.  We'll write a function called `m_b_data` that given a slope of a line, $m$, a y-intercept, $b$, will return a dictionary that has a key of `x` pointing to a list of `x_values`, and a key of `y` that points to a list of `y_values`.  Each $y$ value should be the output of a regression line for the provided $m$ and $b$ values, for each of the provided `x_values`.


```python
def m_b_data(m, b, x_values):
    pass
```


```python
m_b_data(1.5, 20, [0, 50, 100]) # {'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
```

Now let's write a function called `m_b_trace` that uses our `m_b_data` function to return a dictionary that includes keys of `name` and `mode` in addition to `x` and `y`.  The values of `mode` and `name` are provided as arguments.  When the `mode` argument is not provided, it has a default value of `line` and when `name` is not provided, it has a default value of `line function`.


```python
def m_b_trace(m, b, x_values, mode = 'line', name = 'line function'):
    pass
```


```python
m_b_trace(1.5, 20, [0, 50, 100]) 
# {'mode': 'line', 'name': 'line function', 'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
```

### Calculating lines

The comedy show decides to use advertising with three different shows.  The comedy show sets forth it's own predictions, and expexts that the attendance will look like the following for the respective budgets:

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

Let's make sure that our function properly calculates the slope of the line with different data.


```python
imaginary_third_show = {'budget': 300, 'attendance': 500}
imaginary_fourth_show = {'budget': 600, 'attendance': 900}
marginal_return_on_budget(imaginary_third_show, imaginary_fourth_show) # 1.3333333333333333
```

Now we'll begin to write functions that we can use going forward.  The functions will calculate attributes of lines in general, as well be applied to predicting the attendance of the comedy show.

Take the following data.  The comedy show spends zero dollars on advertising for the next show.  Now the attendance chart looks like the following:

| Budgets (dollars)        | Attendance           | 
| ------------- |:-------------:| 
| 0       |100 | 
| 200       |400 | 
| 400       |700 | 


```python
budgets = [0, 200, 400]
attendance_numbers = [100, 400, 700]
```

Write a function called `y_intercept_provided`.  Given a list of `x_values` and a list of `y_values` should find the point with an x_value of zero, and then return the corresponding y-value.  If there is no x-value equal to zero, it returns `False`.

To get you started, we'll provide a function called `sort_points` that returns a list of points sorted by their x_values.  The return value is a list of sorted tuples.


```python
def sorted_points(x_values, y_values):
    values = list(zip(x_values, y_values))
    sorted_values = sorted(values, key=lambda value: value[0])
    return sorted_values
```


```python
sorted_points([4, 1, 6], [4, 6, 7])
```




    [(1, 6), (4, 4), (6, 7)]




```python
def y_intercept_provided(x_values, y_values):
    pass
```


```python
y_intercept_provided([200, 400], [400, 700]) # False
```


```python
budgets = [0, 200, 400]
attendance_numbers = [100, 400, 700]

y_intercept_provided(budgets, attendance_numbers) # 100
```

#### build_regression_line

In this section, we'll write a function called `build_regression_line`.  The function that we end up building will draw a line simply draws a line between our points with the highest and lowest x-values.  We'll see how to draw more accurate regression lines in future lessons.

**First,** write a function called `slope`, that given a list of points, will use the points with the lowest and highest x-values to calculate the slope of a line.  


```python
def slope(x_values, y_values):
    pass
```


```python
slope([200, 400], [400, 700]) # 1.5
```

Now write a function called `y_intercept`.  It calculates the y intercept by the following: 

* If the values provided includes the y_intercept, it returns the provided y_intercept.
* If the values provided do not include the y intercept, it calculates the y intercept by drawing a line from the highest x value provided down to where x = 0.  That drawn line has the slope calculated in the previous function.
> Look to the calculating lines for help in writing this function.


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

Now write a function called `build_regression_line` that given a list of `x_values` and a list of `y_values` returns a dictionary with a key of `m` and a key of `b` to return the `m` and `b` values of the calculated regression line.  Use the  `slope` and `y_intercept` functions to calculate the line.


```python
def build_regression_line(x_values, y_values):
    pass
```


```python
build_regression_line([0, 200, 400], [10, 400, 700]) # {'b': 10.0, 'm': 1.725}
```

**Finally,** let's write a function called `expected_value_for_line` that returns the expected attendance given the $m$, $b$, and $x value$.


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
expected_value_for_line(1.5, 100, 100) # 250.0
```

### Using our functions

Now that we have built these functions, we can use them for our dataset.  Uncomment and run the lines below to see how we can use our functions going forward.


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




    {'mode': 'markers',
     'name': 'comedy show data',
     'x': [200, 400, 300, 600],
     'y': [400, 700, 500, 900]}




```python
# show_regression_line = build_regression_line(show_x_values, show_y_values)
# show_regression_line
```




    {'b': 150.0, 'm': 1.25}




```python
# trace_show_line = m_b_trace(show_regression_line['m'], show_regression_line['b'], show_x_values, name = 'regression line')
```


```python
# trace_show_line
```




    {'mode': 'line',
     'name': 'regression line',
     'x': [200, 400, 300, 600],
     'y': [400.0, 650.0, 525.0, 900.0]}




```python
# plot([comedy_show_trace, trace_show_line])
```


<div id="09f9ce73-0cd6-4c84-9fe1-a22f88f74f45" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("09f9ce73-0cd6-4c84-9fe1-a22f88f74f45", [{"x": [200, 400, 300, 600], "y": [400, 700, 500, 900], "mode": "markers", "name": "comedy show data"}, {"x": [200, 400, 300, 600], "y": [400.0, 650.0, 525.0, 900.0], "mode": "line", "name": "regression line"}], {}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>

