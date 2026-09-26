# DNA Sequence Analyzer
# A beginner biotechnology + Python project

def analyze_dna(sequence):
    sequence = sequence.upper().replace(" ", "")

    valid_bases = {"A", "T", "G", "C"}

    if not sequence:
        print("Error: DNA sequence is empty.")
        return

    if not set(sequence).issubset(valid_bases):
        print("Error: Invalid DNA sequence.")
        print("Only A, T, G and C are allowed.")
        return

    length = len(sequence)

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / length) * 100
    at_content = ((a_count + t_count) / length) * 100

    print("\n--- DNA SEQUENCE ANALYSIS ---")
    print("Sequence:", sequence)
    print("Length:", length)

    print("\nBase Count:")
    print("Adenine (A):", a_count)
    print("Thymine (T):", t_count)
    print("Guanine (G):", g_count)
    print("Cytosine (C):", c_count)

    print("\nComposition:")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"AT Content: {at_content:.2f}%")


# Get DNA sequence from the user
dna = input("Enter a DNA sequence: ")

analyze_dna(dna)
