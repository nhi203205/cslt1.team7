frequency=float(input("Enter the frequency: "))
if abs(frequency - 261.63) <= 1:
    print("Name note is C4")
elif abs(frequency - 293.66) <= 1:
    print("Name note is D4")
elif abs(frequency - 329.63) <= 1:
    print("Name note is E4")
elif abs(frequency - 349.23) <= 1:
    print("Name note is F4")
elif abs(frequency - 392.00) <= 1:
    print("Name note is G4")
elif abs(frequency - 440.00) <= 1:
    print("Name note is A4")
elif abs(frequency - 493.88) <= 1:
    print("Name note is B4")
else:
    print("The frequency does not correspond to a known note.")
