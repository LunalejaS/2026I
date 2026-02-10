import math

def info_units_conversion(input_unit, output_unit, value):
    #args
    #input_unit: nombre de la unidad de entrada (i.e., bit, nat, hartley)
    #output_unit: nombre de la unidad de salida (i.e., bit, nat, hartley)
    #return: valor expresado en la unidad de salida
    
    input_unit = input_unit.lower()
    output_unit = output_unit.lower()
    
    if input_unit in ["bit", "bits"]:
        input_unit = "bit"
    elif input_unit in ["nat", "nats"]:
        input_unit = "nat"
    elif input_unit in ["hartley", "hartleys"]:
        input_unit = "hartley"
    
    if output_unit in ["bit", "bits"]:
        output_unit = "bit"
    elif output_unit in ["nat", "nats"]:
        output_unit = "nat"
    elif output_unit in ["hartley", "hartleys"]:
        output_unit = "hartley"
    
    if input_unit == output_unit:
        return value
    
    if input_unit == "bit":
        if output_unit == "nat":
            x = 2 ** value
            return math.log(x)
        elif output_unit == "hartley":
            x = 2 ** value
            return math.log10(x)
    
    elif input_unit == "nat":
        if output_unit == "bit":
            x = math.e ** value
            return math.log2(x)
        elif output_unit == "hartley":
            x = math.e ** value
            return math.log10(x)
    
    elif input_unit == "hartley":
        if output_unit == "bit":
            x = 10 ** value
            return math.log2(x)
        elif output_unit == "nat":
            x = 10 ** value
            return math.log(x)

def main():
    inputUser = input("Ingrese el valor de la unidad de medida y la unidad de medida (ejemplo: 1 bit, 1 nat, 1 hartley): ").strip().split()
    value = float(inputUser[0])
    input_unit = inputUser[1]

    print(value, input_unit)
    output_unit = input("Ingrese la unidad de medida a la que desea convertir (nat, hartley, bit): ").strip()

    resultado = info_units_conversion(input_unit, output_unit, value)
    print(f"{value} {input_unit} es igual a {resultado} {output_unit}.")

if __name__ == "__main__":
    main()