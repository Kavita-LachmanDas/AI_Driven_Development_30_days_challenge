# 🧮 Interactive Calculator

A beautiful, animated, and interactive calculator built with Python and Streamlit.

## Features

- ✅ **Multiple Operations**: Add, Subtract, Multiply, Divide, Power, Modulo, and Floor Division
- ✅ **Dual Input Modes**: 
  - Button Mode: Use number inputs and operation buttons
  - Expression Mode: Enter mathematical expressions directly
- ✅ **Input Validation**: Prevents division by zero and invalid expressions
- ✅ **Animated UI**: Smooth transitions and visual feedback
- ✅ **Responsive Design**: Clean, modern, and user-friendly interface
- ✅ **Dynamic Results**: Real-time calculation display with formatted output

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the calculator:
```bash
streamlit run calculator.py
```

The application will open in your default web browser.

## Operations Supported

- ➕ **Add**: Addition of two numbers
- ➖ **Subtract**: Subtraction of two numbers
- ✖️ **Multiply**: Multiplication of two numbers
- ➗ **Divide**: Division of two numbers (with zero-division protection)
- 🔢 **Power**: Exponentiation
- 📊 **Modulo**: Remainder after division
- 🔽 **Floor Divide**: Integer division

## Input Modes

### Button Mode
- Enter two numbers in the input fields
- Click an operation button to calculate

### Expression Mode
- Type a mathematical expression (e.g., `2 + 3 * 4`)
- Click "Calculate" to evaluate

## Error Handling

The calculator validates inputs and prevents:
- Division by zero
- Invalid mathematical expressions
- Invalid characters in expressions

## Technologies

- **Python 3.x**
- **Streamlit**: Web framework for building interactive applications

