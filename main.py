from alignment import needle, water

seq1 = "Hello, my name is omar and this is global alignment".split(" ")
seq2 = "Hello, my name is ASDASD omar and ASDASD this is ASDASD global alignment".split(" ")
seq3 = "Hello, name is and this is alignment".split(" ")

print("###### Using Needleman-Wunsch Algorithm  ######\n\n")

print("> Aligning sequence to a sequence with error added tokens\n")
seq1_aligned, seq2_aligned = needle(seq1, seq2)

print("\n> Aligning sequence to a sequence with some tokens lost\n")
seq1_aligned, seq3_aligned = needle(seq1, seq3)


print("###### Using Smith-Waterman Algorithm   #######\n\n")

print("> Aligning sequence to a sequence with error added tokens\n")
seq1_aligned, seq2_aligned = water(seq1, seq2)

print("\n> Aligning sequence to a sequence with some tokens lost\n")
seq1_aligned, seq3_aligned = water(seq1, seq3)
