import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="🧮 Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .main {
        font-family: 'Poppins', sans-serif;
    }
    
    .stButton>button {
        width: 100%;
        height: 60px;
        border-radius: 10px;
        border: none;
        font-size: 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .result-box {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .error-box {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        animation: shake 0.5s;
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        25% { transform: translateX(-10px); }
        75% { transform: translateX(10px); }
    }
    
    .success-box {
        background: linear-gradient(135deg, #51cf66 0%, #40c057 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    h1 {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    </style>
""", unsafe_allow_html=True)

# Calculation functions
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

def modulo(a, b):
    """Return remainder of a divided by b"""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed!")
    return a % b

def floor_divide(a, b):
    """Floor division of a by b"""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a // b

# Operation mapping
OPERATIONS = {
    "➕ Add": add,
    "➖ Subtract": subtract,
    "✖️ Multiply": multiply,
    "➗ Divide": divide,
    "🔢 Power": power,
    "📊 Modulo": modulo,
    "🔽 Floor Divide": floor_divide
}

# Parse expression from string input
def parse_expression(expression):
    """Parse a mathematical expression string"""
    try:
        # Remove whitespace
        expression = expression.strip()
        # Replace common operators
        expression = expression.replace('×', '*').replace('÷', '/')
        # Validate expression (only numbers, operators, and spaces)
        if not re.match(r'^[\d+\-*/().\s]+$', expression):
            raise ValueError("Invalid characters in expression")
        # Evaluate safely
        result = eval(expression, {"__builtins__": {}}, {})
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")

def format_result(value):
    """Format result for display, handling decimals and large numbers"""
    try:
        # Format with up to 10 decimal places, remove trailing zeros
        formatted = f"{value:,.10f}".rstrip('0').rstrip('.')
        return formatted
    except Exception:
        return str(value)

def main():
    st.title("🧮 Interactive Calculator")
    st.markdown("---")
    
    # Initialize session state
    if 'result' not in st.session_state:
        st.session_state.result = None
    if 'error' not in st.session_state:
        st.session_state.error = None
    
    # Mode selection
    mode = st.radio(
        "Choose input mode:",
        ["🎯 Button Mode", "⌨️ Expression Mode"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if mode == "🎯 Button Mode":
        # Button mode interface
        col1, col2 = st.columns(2)
        
        with col1:
            num1 = st.number_input("Enter first number:", value=0.0, step=0.1, format="%.10f", key="num1")
        
        with col2:
            num2 = st.number_input("Enter second number:", value=0.0, step=0.1, format="%.10f", key="num2")
        
        st.markdown("### Select Operation:")
        
        # Initialize operation in session state if not exists
        if 'operation' not in st.session_state:
            st.session_state.operation = "➕ Add"
        
        # Create operation selection using radio for dynamic updates
        operation_selected = st.radio(
            "Choose operation:",
            options=list(OPERATIONS.keys()),
            key="operation_radio",
            horizontal=True
        )
        
        # Update session state
        st.session_state.operation = operation_selected
        
        # Dynamic calculation - updates automatically when inputs or operation change
        if num1 is not None and num2 is not None and operation_selected:
            try:
                operation_func = OPERATIONS[operation_selected]
                st.session_state.result = operation_func(num1, num2)
                st.session_state.error = None
            except ValueError as e:
                st.session_state.error = str(e)
                st.session_state.result = None
            except Exception as e:
                st.session_state.error = f"An error occurred: {str(e)}"
                st.session_state.result = None
    
    else:
        # Expression mode interface
        st.markdown("### Enter a mathematical expression:")
        st.markdown("*Example: `2 + 3 * 4` or `10 / 2 - 1`*")
        
        expression = st.text_input(
            "Expression:",
            placeholder="e.g., 2 + 3 * 4",
            key="expression_input"
        )
        
        col1, col2 = st.columns([3, 1])
        with col2:
            calculate_btn = st.button("Calculate", type="primary", use_container_width=True)
        
        if calculate_btn and expression:
            try:
                st.session_state.result = parse_expression(expression)
                st.session_state.error = None
            except ValueError as e:
                st.session_state.error = str(e)
                st.session_state.result = None
            except Exception as e:
                st.session_state.error = f"An error occurred: {str(e)}"
                st.session_state.result = None
    
    # Display results
    st.markdown("---")
    
    if st.session_state.error:
        st.markdown(f'<div class="error-box">⚠️ <strong>Error:</strong> {st.session_state.error}</div>', 
                   unsafe_allow_html=True)
    
    if st.session_state.result is not None:
        result_formatted = format_result(st.session_state.result)
        st.markdown(
            f'<div class="result-box">'
            f'<h2 style="margin: 0; color: #667eea;">Result</h2>'
            f'<h1 style="margin: 10px 0; font-size: 48px; color: #764ba2;">{result_formatted}</h1>'
            f'</div>',
            unsafe_allow_html=True
        )
    
    # Clear button
    if st.session_state.result is not None or st.session_state.error:
        if st.button("🔄 Clear Result", use_container_width=True):
            st.session_state.result = None
            st.session_state.error = None
            st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666; padding: 20px;'>"
        "✨ Built with Python & Streamlit | Interactive & Animated Calculator ✨"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

