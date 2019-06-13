import random

word_count = 1000

vowel_a = ["a", "a:"]
vowel_i = ["i", "i:"]
vowel_u = ["u", "u:"]

vowels = [vowel_a, vowel_i, vowel_u]
onset = ["*", "p", "b", "d", "t", "g", "k", "*", "z", "s", "r", "n", "m", "*", "w", "h", "y"]
why = ["w", "h", "y"]
coda = ["r", "n", "m"]

minimum_syllable_count = 1
maximum_syllable_count = 3


def build_syllable(vowel_harmony, tonicity):
    # Picking starting consonant, if any
    syl_onset = random.choice(onset)
    why_selector = random.randint(1, 11)

    if (syl_onset not in why and syl_onset != "*") and why_selector % 3 == 0:
        syl_approx = random.choice(why)
    else:
        syl_approx = ""

    # Is the syllable open or closed
    has_coda = random.randint(1, 3)
    if has_coda == 1 or has_coda == 3:
        syl_coda = ""
    else:
        syl_coda = random.choice(coda)

    # Define length of vowel
    if syl_coda == "":
        vowel_length = 1
    else:
        vowel_length = 0

    # Pick the Nucleus
    vowel_selector = random.randint(1, 2)
    if tonicity == 1:
        if vowel_selector == 1:  
            if vowel_harmony == 1:
                if vowel_length == 1:
                    syl_nucleus = vowel_i[0]
                else:
                    syl_nucleus = vowel_i[1]
            else:
                if vowel_length == 1:
                    syl_nucleus = vowel_u[1]
                else:
                    syl_nucleus = vowel_u[0]
        else:
            if vowel_length == 1:
                syl_nucleus = vowel_a[1]
            else:
                syl_nucleus = vowel_a[0]
    else:
        if vowel_selector == 1 or vowel_selector == 3:
            if vowel_harmony == 1:
                if vowel_length == 1:
                    syl_nucleus = vowel_i[0]
                else:
                    syl_nucleus = vowel_i[1]
            else:
                if vowel_length == 1:
                    syl_nucleus = vowel_u[0]
                else:
                    syl_nucleus = vowel_u[1]
        else:
            if vowel_length == 1:
                syl_nucleus = vowel_a[0]
            else:
                syl_nucleus = vowel_a[1]

    # Put it together
    syllable = syl_onset + syl_approx + syl_nucleus + syl_coda
    return syllable


def in_world_orthography(word):
    new_word = ""
    for i in range(0, len(word)):
        if word[i] == "w" and word[i+1] == "a":
            new_letter = "â"
        elif word[i] == "w" and word[i+1] == "i":
            new_letter = "î"
        elif word[i] == "w" and word[i+1] == "u":
            new_letter = "û"
        elif word[i] == "h" and word[i+1] == "a":
            new_letter = "ä"
        elif word[i] == "h" and word[i+1] == "i":
            new_letter = "ï"
        elif word[i] == "h" and word[i+1] == "u":
            new_letter = "ü"
        elif word[i] == "y" and word[i+1] == "a":
            new_letter = "á"
        elif word[i] == "y" and word[i+1] == "i":
            new_letter = "í"
        elif word[i] == "y" and word[i+1] == "u":
            new_letter = "ú"
        elif word[i] in vowel_a and word[i-1] in why:
            continue
        elif word[i] in vowel_i and word[i-1] in why:
            continue
        elif word[i] in vowel_u and word[i-1] in why:
            continue
        elif word[i] == "*":
            continue
        else:
            new_letter = word[i]
        new_word += new_letter
    return new_word


def build_word(bw_number_of_syllables):
    # vowel_harmony 0 = vowel_a, 1 = vowel_i, 2 = vowel_u
    vowel_harmony = random.randint(1, 2)
    if bw_number_of_syllables == 1:
        word = build_syllable(vowel_harmony, 1)
        tonic = word
        pre_tonic = ""
        post_tonic = ""

    elif bw_number_of_syllables == 2:
        tonic = build_syllable(vowel_harmony, 1)
        pre_tonic = build_syllable(vowel_harmony, 0)
        post_tonic = ""
        word = pre_tonic + tonic.upper()

    else:
        tonic = build_syllable(vowel_harmony, 1)
        pre_tonic = build_syllable(vowel_harmony, 0)
        post_tonic = build_syllable(vowel_harmony, 0)
        word = pre_tonic + tonic.upper() + post_tonic

    orthography = in_world_orthography(word.lower())
    new_word_object = {
        "roman": word,
        "pre_tonic": pre_tonic,
        "tonic": tonic,
        "post_tonic": post_tonic,
        "orthography": orthography
    }
    
    return new_word_object


word_array = []
counter = 1
while counter < word_count:
    number_of_syllables = random.randint(minimum_syllable_count, maximum_syllable_count)
    word_object = build_word(number_of_syllables)
    if word_object in word_array:
        continue
    else:
        word_array.append(word_object)
        counter += 1
print(word_array)

f = open("voc.txt", "a")
for each_word_object in word_array:
    f.write(
        each_word_object["roman"] + ", " + 
        each_word_object["pre_tonic"] + ", " + 
        each_word_object["tonic"] + ", " + 
        each_word_object["post_tonic"] + "\r"
    )
f.close()
