""" Python script to convert mass to energy according to Einstein's formula energy = mass * speed_of_light(squared) """


def main():
    input_mass = input("Enter a Mass in kilograms: ").strip()
    print(f"Energy: {convert(int(input_mass))}")
    
    
def convert(input_mass):
    """ Convert Mass to Energy """
    energy = input_mass * (300000000**2)
    return energy

    
main()

