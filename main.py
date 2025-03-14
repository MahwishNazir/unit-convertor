import streamlit as st


# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    # Conversion factors to kilograms
    conversion_factors = {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495,
        'stone': 6.35029,
    }
    
    # Convert input value to kilograms
    value_in_kg = value * conversion_factors[from_unit]
    
    # Convert kilograms to the target unit
    conversion_factors_inverse = {v: k for k, v in conversion_factors.items()}
    result = value_in_kg / conversion_factors[to_unit]
    
    return result

# Streamlit app
def main():3
st.title("Weight Converter")
st.write("Convert weight between different units.")
    
    # Input fields
value = st.number_input("Enter weight:", min_value=0.0, step=0.1)
from_unit = st.selectbox("From unit:", ['kg', 'g', 'lb', 'oz', 'stone'])
to_unit = st.selectbox("To unit:", ['kg', 'g', 'lb', 'oz', 'stone'])
    
    # Convert and display result
if value > 0:
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.2f} {to_unit}.")
else:
        st.write("Please enter a positive weight value.")

if __name__ == "__main__":
    main()