def min_notes(amount):
    valid_notes = [2000,500,100, 50, 20, 10, 5, 1]
    count = 0
    for note in valid_notes:
        count += amount //note
        amount %= note
    print(f"the minimum number of notes to add up to amount is {count}")
    
    
min_notes(4553)