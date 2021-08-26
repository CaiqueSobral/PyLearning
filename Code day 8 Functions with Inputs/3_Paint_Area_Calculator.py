def paintCalc(height, width, cover):
    numberOfCans = round((height * width) / cover)
    print(f"You will need to use {numberOfCans} cans of paint.")

paintCalc(3, 9, 5)