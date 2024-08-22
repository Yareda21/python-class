ask=input("Enter temp: - ")
def temperature(ask):
    unit = ask[-1]
    number = int( ask[:-1])
    print(unit, number)
    if unit== "c":
        return ((1.8*number)+32)
    if unit== "f":
        return((number-32)*1.8)
result = temperature
print(result)
    