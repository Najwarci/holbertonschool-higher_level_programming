#!/usr/bin/python3def safe_print_division(a, b):
  def safe_print_division(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
