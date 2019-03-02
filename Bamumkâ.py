import random

WordCount = 1000

A = [
		["a", "a", "a", "a", "â", "a", "ä", "a", "á"],
		["aa", "aa", "aa", "aa", "âa", "aa", "äa", "aa", "áa"]
	]
I = [
		["i", "i", "i", "i", "î", "i", "ï", "i", "í"],
		["ii", "ii", "ii", "ii", "îi", "ii", "ïi", "ii", "íi"]
	]
U = [
		["u", "u", "u", "u", "û", "u", "ü", "u", "ú"],
		["uu", "uu", "uu", "uu", "ûu", "uu", "üu", "uu", "úu"]
	]

Vowels = [A, I, U]
Onset = ["b", "d", "t", "g", "k", "z", "s", "r", "n", "m",""]
Coda = ["r", "n", "m"]





def BuildSyllable(VowelHarmony, Tonicity):
	# Picking starting consonant, if any
	T_Onset = random.choice(Onset)

	# Is the syllable open or closed
	HasCoda = random.randint(1,3)
	if HasCoda == 1 or HasCoda == 3:
		T_Coda = ""
	else:
		T_Coda = random.choice(Coda)

	# Define length of vowel
	if T_Coda == "":
		VowelLength = 1
	else:
		VowelLength = 0

	# Pick the Nucleus
	VowelSelector = random.randint(1,3)
	if Tonicity == 1:
		if VowelSelector == 1 or VowelSelector == 3:
			if VowelHarmony == 1:
				if VowelLength == 1:
					T_Nucleus = random.choice(I[1])
				else:
					T_Nucleus = random.choice(I[0])
			else:
				if VowelLength == 1:
					T_Nucleus = random.choice(U[1])
				else:
					T_Nucleus = random.choice(U[0])
		else:
			if VowelLength == 1:
				T_Nucleus = random.choice(A[1])
			else:
				T_Nucleus = random.choice(A[0])
	else:
		if VowelSelector == 1 or VowelSelector == 3:
			if VowelHarmony == 1:
				if VowelLength == 1:
					T_Nucleus = random.choice(I[0])
				else:
					T_Nucleus = random.choice(I[1])
			else:
				if VowelLength == 1:
					T_Nucleus = random.choice(U[0])
				else:
					T_Nucleus = random.choice(U[1])
		else:
			if VowelLength == 1:
				T_Nucleus = random.choice(A[0])
			else:
				T_Nucleus = random.choice(A[1])

	# Put it together	
	Syllable = T_Onset + T_Nucleus + T_Coda 
	return Syllable

WordArray = []
counter = 1
while counter < WordCount:
	NumberOfSyllables = random.randint(1,3)
	# VowelHarmony 1 = I, 2 = U
	VowelHarmony = random.randint(1, 2)
	if NumberOfSyllables == 1:
		Word = BuildSyllable(VowelHarmony, 1) + ", "
		#print(Word)
	elif NumberOfSyllables == 2:
		Tonic = BuildSyllable(VowelHarmony,1)
		PreTonic = BuildSyllable(VowelHarmony,0)
		Word = PreTonic + Tonic.upper() + ", "
		#print(Word)
	else:
		Tonic = BuildSyllable(VowelHarmony,1)
		PreTonic = BuildSyllable(VowelHarmony,0)
		PostTonic = BuildSyllable(VowelHarmony,0)
		Word = PreTonic + Tonic.upper() + PostTonic
		#print(Word)
	if Word in WordArray:
		continue
	else:
		WordArray.append(Word)
		counter += 1
print(WordArray)