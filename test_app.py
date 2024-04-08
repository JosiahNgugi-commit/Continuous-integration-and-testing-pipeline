def test_add_pass():
    result = add(5, 3)
    assert result == 8, "Addition test passed"
def test_subtract_pass():
    result = subtract(10, 4)
    assert result == 6, "Subtraction test passed"
def test_multiply_pass():
    result = multiply(6, 7)
    assert result == 42, "Multiplication test passed"
def test_divide_fail():
    result = divide(10, 0)
    assert result == "Error: Division by zero", "Division by zero should raise an error"
def test_invalid_operation_fail():
    result = divide(8, 2)
    assert result == 4, "Invalid operation test failed"
