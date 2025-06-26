import sys

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == 'c':
        if to_unit == 'f':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'k':
            return celsius_to_kelvin(value)

    elif from_unit == 'f':
        if to_unit == 'c':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'k':
            return fahrenheit_to_kelvin(value)

    elif from_unit == 'k':
        if to_unit == 'c':
            return kelvin_to_celsius(value)
        elif to_unit == 'f':
            return kelvin_to_fahrenheit(value)

    raise ValueError("Invalid conversion units.")

def main():
    if len(sys.argv) != 4:
        print("Usage: python temp_converter.py <value> <from_unit> <to_unit>")
        print("Example: python temp_converter.py 100 C F")
        print("Units: C (Celsius), F (Fahrenheit), K (Kelvin)")
        return

    try:
        value = float(sys.argv[1])
        from_unit = sys.argv[2]
        to_unit = sys.argv[3]

        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value}°{from_unit.upper()} = {result:.2f}°{to_unit.upper()}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()


# run this in the terminal to get output
# python temperature_con.py 100 C F
