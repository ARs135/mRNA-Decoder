# mRNA Decoder

import os

codon_dict = {
    'UUU' : 'Phe : Phenylalanine',
    'UUC' : 'Phe : Phenylalanine',
    'UUA' : 'Leu : Leucine',
    'UUG' : 'Leu : Leucine',
    'UCU' : 'Ser : Serine',
    'UCC' : 'Ser : Serine',
    'UCA' : 'Ser : Serine',
    'UCG' : 'Ser : Serine',
    'UAU' : 'Tyr : Tyrosine',
    'UAC' : 'Tyr : Tyrosine',
    'UAA' : 'Stop',
    'UAG' : 'Stop',
    'UGU' : 'Cys : Cysteine',
    'UGC' : 'Cys : Cysteine',
    'UGA' : 'Stop',
    'UGG' : 'Trp : Tryptophan',
    'CUU' : 'Leu : Leucine',
    'CUC' : 'Leu : Leucine',
    'CUA' : 'Leu : Leucine',
    'CUG' : 'Leu : Leucine',
    'CCU' : 'Pro : Proline',
    'CCC' : 'Pro : Proline',
    'CCA' : 'Pro : Proline',
    'CCG' : 'Pro : Proline',
    'CAU' : 'His : Histidine',
    'CAC' : 'His : Histidine',
    'CAA' : 'Gln : Glutamine',
    'CAG' : 'Gln : Glutamine',
    'CGU' : 'Arg : Arginine',
    'CGC' : 'Arg : Arginine',
    'CGA' : 'Arg : Arginine',
    'CGG' : 'Arg : Arginine',
    'AUU' : 'Ile : IsoLeucine',
    'AUC' : 'Ile : IsoLeucine',
    'AUA' : 'Ile : IsoLeucine',
    'AUG' : 'Met : Methionine',
    'ACU' : 'Thr : Threonine',
    'ACC' : 'Thr : Threonine',
    'ACA' : 'Thr : Threonine',
    'ACG' : 'Thr : Threonine',
    'AAU' : 'Asn : Asparagine',
    'AAC' : 'Asn : Asparagine',
    'AAA' : 'Lys : Lysine',
    'AAG' : 'Lys : Lysine',
    'AGU' : 'Ser : Serine',
    'AGC' : 'Ser : Serine',
    'AGA' : 'Arg : Arginine',
    'AGG' : 'Arg : Arginine',
    'GUU' : 'Val : Valine',
    'GUC' : 'Val : Valine',
    'GUA' : 'Val : Valine',
    'GUG' : 'Val : Valine',
    'GCU' : 'Ala : Alanine',
    'GCC' : 'Ala : Alanine',
    'GCA' : 'Ala : Alanine',
    'GCG' : 'Ala : Alanine',
    'GAU' : 'Asp : Aspartic acid',
    'GAC' : 'Asp : Aspartic acid',
    'GAA' : 'Glu : Glutamic acid',
    'GAG' : 'Glu : Glutamic acid',
    'GGU' : 'Gly : Glycine',
    'GGC' : 'Gly : Glycine',
    'GGA' : 'Gly : Glycine',
    'GGG' : 'Gly : Glycine'
}

def decode_rna(rna_sequence):
    #Split the sequence into codons
    codons = [rna_sequence[i:i+3] for i in range(0, len(rna_sequence), 3)]

    #Frequency Counter
    freq_counter = {}

    #Translate the codons
    amino_acids = []
    for codon in codons:
        amino_acid = codon_dict.get(codon, 'Invalid Codon')
        if amino_acid == 'Stop':
            break
        if amino_acid == 'Invalid Codon':
            print(f"Invalid Codon in Sequence: {codon}. Couldn't process Sequence")
            return amino_acid, None
        amino_acids.append(amino_acid)

        freq_counter[amino_acid] = freq_counter.get(amino_acid, 0) + 1

    amino_acids.append("# of Amino Acids: " + str(len(amino_acids)))

    return amino_acids, freq_counter

#Load and Save Directory Preference
def load_directory():
    if os.path.exists("C:/Users/Administrator/Documents/directory.txt"):
        with open("C:/Users/Administrator/Documents/directory.txt", "r") as dir_file:
            return dir_file.read().strip()
    return None

def save_directory(directory):
    with open("C:/Users/Administrator/Documents/directory.txt", "w") as dir_file:
        dir_file.write(directory)

#File or Manual sequence
while True:
    while True:
        choice = input("Enter 'file' to read from a file (Must be a .txt File). Enter 'manual' to input manually: ")
        if choice in ['file', 'manual']:
            break
        print("Not a Valid Choice. Enter 'file' or 'manual'.")

    #Load Previouse Directory or Ask User
    prev_directory = load_directory()

    if choice == 'manual':
        rna_sequence = input("Enter the mRNA Sequence here: ").replace(" ", "").upper()
        decoded_sequence, freq_counter = decode_rna(rna_sequence)
        print("Decoded Sequence:", decoded_sequence)
        
        #Sort Frequencies from Highest to Lowest
        sorted_freq = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)

        #Calculate Percentages
        total_amino_acids = sum(freq_counter.values())
        if total_amino_acids > 0:
            print("\nAmino Acid Frequencies:")
            for Amino, count in sorted_freq:
                percentage = (count / total_amino_acids) * 100
                print(f"{Amino}: {count} times ({percentage:.2f}%)")

    elif choice == 'file':
        while True:
            if prev_directory:
                filename = input(f"Enter the path of the file (Last Directory You Used: {prev_directory}): ").strip()
                #If entered path is absolute or relative
                if not os.path.isabs(filename):
                    filename = os.path.join(prev_directory, filename)
            else:
                filename = input("Enter the Path of the File: ")

            if not filename.endswith(".txt"):
                print("Must Enter a .txt File")
                continue

            if os.path.exists(filename):
                try:
                    with open(filename, "r") as file:
                        rna_sequence = file.read().strip().replace(" ", "").upper()
                        decoded_sequence, freq_counter = decode_rna(rna_sequence)
                        print("Decoded Sequence From File:", decoded_sequence)
                        save_directory(os.path.dirname(filename))
                        
                        #Sort Frequencies from Highest to Lowest
                        sorted_freq = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)

                        #Calculate Percentages
                        total_amino_acids = sum(freq_counter.values())
                        if total_amino_acids > 0:
                            print("\nAmino Acid Frequencies:")
                            for Amino, count in sorted_freq:
                                percentage = (count / total_amino_acids) * 100
                                print(f"{Amino}: {count} times ({percentage:.2f}%)")
                    break
                except Exception as e:
                    print(f"Error: Can't Read the File: {e}")
                    break
            else:
                print("File not Found. Enter a Valid Path to the File.")
    
    #Ask If They Want to Continue
    continue_choice = input("Do You Want to Decode Another Sequence? (y/n): ").strip().lower()
    if continue_choice != 'y':
        print("Cya Next Time")
        break
    