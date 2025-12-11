# Data Model: Calculator Application

**Date**: 2024-12-19  
**Feature**: Calculator Application  
**Branch**: `1-calculator-app`

## Overview

The calculator application is stateless and does not require persistent data storage. However, it manages transient state during user interactions. This document describes the conceptual entities and their relationships.

## Entities

### Calculation

**Description**: Represents a single arithmetic operation with two operands and an operator, resulting in a numeric result or error.

**Attributes**:
- `operand1` (float): First number in the calculation
- `operand2` (float): Second number in the calculation
- `operator` (string): Operation to perform ("add", "subtract", "multiply", "divide")
- `result` (float | None): Calculated result, or None if error occurred
- `error` (string | None): Error message if calculation failed, or None if successful

**Validation Rules**:
- `operand1` and `operand2` must be valid numbers (float or int)
- `operator` must be one of: "add", "subtract", "multiply", "divide"
- If `operator` is "divide" and `operand2` is 0, `error` must be set (division by zero)
- `result` and `error` are mutually exclusive (only one can be set)

**State Transitions**:
1. **Initial**: User enters operands and selects operator
2. **Calculating**: Function processes the operation
3. **Success**: Result is calculated and displayed
4. **Error**: Validation fails or invalid operation, error message displayed

---

### User Input

**Description**: Represents numeric values entered by the user, which must be validated before use in calculations.

**Attributes**:
- `value` (string | float): Raw input from user (string from UI, converted to float)
- `is_valid` (boolean): Whether the input is a valid number
- `parsed_value` (float | None): Numeric value after parsing, or None if invalid

**Validation Rules**:
- Input must be parseable as a float or integer
- Empty input is invalid
- Non-numeric characters (except decimal point and minus sign) are invalid
- Very large numbers should be handled gracefully (may lose precision)

**State Transitions**:
1. **Empty**: No input provided
2. **Entering**: User is typing input
3. **Valid**: Input is a valid number, ready for calculation
4. **Invalid**: Input contains invalid characters, error displayed

---

## Relationships

- **Calculation** uses two **User Input** entities (operand1 and operand2)
- **User Input** validation must complete before **Calculation** can proceed
- **Calculation** result or error is displayed to the user

## Session State (Streamlit)

The application uses Streamlit's session state to manage transient data:

- `num1` (float): First number input value
- `num2` (float): Second number input value
- `operation` (string): Selected operation
- `result` (float | None): Current calculation result
- `error` (string | None): Current error message

**State Management**:
- Values persist across widget interactions within the same session
- State is cleared when user refreshes the page
- No persistence between sessions (stateless application)

## Data Flow

1. User enters `num1` and `num2` via st.number_input()
2. User selects `operation` via st.radio() or st.selectbox()
3. Streamlit triggers rerun when values change
4. Application validates inputs (automatic via st.number_input)
5. Calculation function processes operation
6. Result or error is stored in session state
7. UI displays result or error message

## Edge Cases Handled

- **Division by zero**: Caught in divide function, error message displayed
- **Invalid input**: Streamlit's number_input prevents most invalid input
- **Very large numbers**: Python float handles, may lose precision for extremely large values
- **Negative numbers**: Supported, no special handling needed
- **Decimal precision**: Python float handles, display formatting removes trailing zeros
- **Floating-point precision issues**: Accepted limitation (e.g., 0.1 + 0.2 = 0.30000000000000004)

## No Persistent Storage

The application does not require:
- Database
- File storage
- External APIs
- User accounts or sessions
- Calculation history

All state is transient and exists only during the current browser session.

