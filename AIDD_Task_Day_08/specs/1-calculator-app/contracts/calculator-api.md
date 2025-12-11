# Calculator API Contract

**Date**: 2024-12-19  
**Feature**: Calculator Application  
**Branch**: `1-calculator-app`

## Overview

This document describes the functional contracts for the calculator application. Since this is a Streamlit application (not a REST API), these contracts represent the functional interfaces between UI components and calculation functions.

## Function Contracts

### add(operand1: float, operand2: float) -> float

**Purpose**: Performs addition of two numbers.

**Input**:
- `operand1` (float): First number
- `operand2` (float): Second number

**Output**:
- Returns (float): Sum of operand1 and operand2

**Errors**: None (addition is always valid)

**Example**:
```python
result = add(10.0, 5.0)  # Returns 15.0
```

---

### subtract(operand1: float, operand2: float) -> float

**Purpose**: Performs subtraction of two numbers.

**Input**:
- `operand1` (float): First number (minuend)
- `operand2` (float): Second number (subtrahend)

**Output**:
- Returns (float): Difference of operand1 and operand2 (operand1 - operand2)

**Errors**: None (subtraction is always valid)

**Example**:
```python
result = subtract(10.0, 5.0)  # Returns 5.0
```

---

### multiply(operand1: float, operand2: float) -> float

**Purpose**: Performs multiplication of two numbers.

**Input**:
- `operand1` (float): First number
- `operand2` (float): Second number

**Output**:
- Returns (float): Product of operand1 and operand2

**Errors**: None (multiplication is always valid)

**Example**:
```python
result = multiply(10.0, 5.0)  # Returns 50.0
```

---

### divide(operand1: float, operand2: float) -> float

**Purpose**: Performs division of two numbers.

**Input**:
- `operand1` (float): First number (dividend)
- `operand2` (float): Second number (divisor)

**Output**:
- Returns (float): Quotient of operand1 and operand2 (operand1 / operand2)

**Errors**:
- Raises `ValueError` with message "Division by zero is not allowed!" if operand2 is 0

**Example**:
```python
result = divide(10.0, 5.0)  # Returns 2.0
result = divide(10.0, 0.0)  # Raises ValueError
```

---

## UI Component Contracts

### Number Input Component

**Purpose**: Allows user to enter numeric values.

**Contract**:
- Accepts: Numeric input (integers or decimals, positive or negative)
- Validates: Automatically via Streamlit's st.number_input()
- Output: Float value stored in session state
- Error Handling: Invalid input prevented by Streamlit component

---

### Operation Selection Component

**Purpose**: Allows user to select arithmetic operation.

**Contract**:
- Accepts: Selection from available operations ("add", "subtract", "multiply", "divide")
- Validates: Selection must be one of the four valid operations
- Output: String value stored in session state
- Error Handling: Invalid selection prevented by Streamlit component (radio/selectbox)

---

### Result Display Component

**Purpose**: Displays calculation result or error message.

**Contract**:
- Input: Result (float) or Error (string) from calculation
- Format: Result formatted to remove trailing zeros, error displayed with st.error()
- Updates: Automatically when calculation completes or input changes
- Error Handling: Displays error message if calculation failed

---

## Calculation Flow Contract

1. **Input Validation**: 
   - User inputs validated by Streamlit components
   - Values stored in session state

2. **Operation Execution**:
   - Operation function called with validated inputs
   - Function returns result or raises error

3. **Result Handling**:
   - Success: Result formatted and displayed
   - Error: Error message displayed, result cleared

4. **State Update**:
   - Session state updated with result or error
   - UI automatically rerenders

---

## Error Contract

### Division by Zero

**Trigger**: divide() called with operand2 = 0

**Response**:
- Function raises ValueError with message: "Division by zero is not allowed!"
- UI catches exception and displays error using st.error()
- Application continues running (no crash)

---

## Performance Contract

- **Response Time**: Calculation results update within 500ms of input changes (SC-005)
- **Visual Feedback**: Button interactions provide feedback within 100ms (SC-004)
- **Throughput**: Handles rapid input changes (5+ per second) without degradation (SC-008)

---

## Testing Contract

Each function contract must be validated through:
1. Unit testing of individual functions
2. Integration testing of UI components
3. Manual testing of user scenarios from spec.md

