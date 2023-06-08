def fahrenheit_en_celsius(temp_Fahrenheit):
  "Transform la temperature de Farenheit en Celsius"
  # temp_celsius est une variable locale, elle existe seulement
  # dans cette fonction 
  temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)
  return temp_Celsius

def celsius_en_fahrenheit(temp_Celsius):
  "Transform la temperature de Celsius en Farenheit"  
  # temp_fahrenheit est une variable locale, elle existe seulement
  # dans cette fonction 
  temp_Fahrenheit = 9.0 / 5.0 * temp_Celsius + 32
  return temp_Fahrenheit


# t_fahrenheit et t_celsius sont de variables globales

t_fahrenheit = 212
print(t_fahrenheit, "Fahrenheit est", fahrenheit_en_celsius(t_fahrenheit), "Celsius.")

t_celsius = 100
print(t_celsius, "Celsius est", celsius_en_fahrenheit(t_celsius), "Fahrenheit.")


t_fahrenheit = 0
print(t_fahrenheit, "Fahrenheit est", fahrenheit_en_celsius(t_fahrenheit), "Celsius.")

t_celsius = 0
print(t_celsius, "Celsius est", celsius_en_fahrenheit(t_celsius), "Fahrenheit.")
