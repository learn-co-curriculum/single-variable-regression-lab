import unittest
from ipynb.fs.full.index import (attendance, attendance_with_friends, marginal_return_on_budget, y_intercept, shows,
 m_b_data, m_b_trace, y_intercept_provided, build_regression_line, expected_value_for_line)

class TestRegression(unittest.TestCase):
    def test_attendance(self):
        self.assertEqual(attendance(100), 150)
        self.assertEqual(attendance(50), 75)

    def test_attendance_with_friends(self):
        self.assertEqual(attendance_with_friends(100), 170)
        self.assertEqual(attendance_with_friends(50), 95)

    def test_m_b_data(self):
        self.assertEqual(m_b_data(1.5, 20, [0, 50, 100]), {'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]})

    def test_m_b_trace(self):
        trace = {'mode': 'line', 'name': 'line function', 'x': [0, 50, 100], 'y': [20.0, 95.0, 170.0]}
        self.assertEqual(m_b_trace(1.5, 20, [0, 50, 100]), trace)

    def test_marginal_return_on_budget(self):
        first_show = {'budget': 200, 'attendance': 400}
        second_show = {'budget': 400, 'attendance': 700}
        imaginary_third_show = {'budget': 300, 'attendance': 500}
        imaginary_fourth_show = {'budget': 600, 'attendance': 900}

        self.assertEqual(marginal_return_on_budget(first_show, second_show), 1.5)
        self.assertEqual(marginal_return_on_budget(imaginary_third_show, imaginary_fourth_show), 1.3333333333333333)

    def test_y_intercept_provided(self):
        budgets = [0, 200, 400]
        attendance = [100, 400, 700]
        self.assertEqual(y_intercept_provided(budgets, attendance), 100)
        self.assertEqual(y_intercept_provided([200, 400], [400, 700]), False)

    def test_y_intercept(self):
        budgets = [0, 200, 400]
        attendance = [100, 400, 700]
        self.assertEqual(y_intercept(budgets, attendance), 100)
        self.assertEqual(y_intercept([200, 400], [400, 700]), 100)

    def test_build_regression_line(self):
        self.assertEqual(build_regression_line([0, 200, 400], [10, 400, 700]), {'b': 10.0, 'm': 1.725})

    def test_expected_value_for_line(self):
        self.assertEqual(expected_value_for_line(1.5, 100, 100), 250)
