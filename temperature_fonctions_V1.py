def fahrenheit_en_celsius(temp_Fahrenheit):
  "Transform la temperature de Farenheit en Celsius"
  return 5.0 / 9.0 * (temp_Fahrenheit - 32)

def celsius_en_fahrenheit(temp_Celsius):
  "Transform la temperature de Celsius en Farenheit"  
  return 9.0 / 5.0 * temp_Celsius + 32


print(fahrenheit_en_celsius(212))

print(celsius_en_fahrenheit(100))

