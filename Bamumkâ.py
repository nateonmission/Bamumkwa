import random

WordCount = 1000

A = ["a", "a:"]
I = ["i", "i:"]
U = ["u", "u:"]

Vowels = [A, I, U]
Onset = ["*", "b", "d", "t", "g", "k", "*", "z", "s", "r", "n", "m", "*", "w", "h", "y"]
Why = ["w", "h", "y"]
Coda = ["r", "n", "m"]

MinSyl = 1
MaxSyl = 3

def BuildSyllable(VowelHarmony, Tonicity):
	# Picking starting consonant, if any
	T_Onset = random.choice(Onset)
	Why_selector = random.randint(1, 11)

	if (T_Onset not in Why and T_Onset != "*") and Why_selector % 3 == 0:
		T_approx = random.choice(Why)
	else:
		T_approx = ""


	# Is the syllable open or closed
	HasCoda = random.randint(1, 3)
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
	VowelSelector = random.randint(1, 3)
	if Tonicity == 1:
		if VowelSelector == 1 or VowelSelector == 3:
			if VowelHarmony == 1:
				if VowelLength == 1:
					T_Nucleus = I[0]
				else:
					T_Nucleus = I[1]
			else:
				if VowelLength == 1:
					T_Nucleus = U[1]
				else:
					T_Nucleus = U[0]
		else:
			if VowelLength == 1:
				T_Nucleus = A[1]
			else:
				T_Nucleus = A[0]
	else:
		if VowelSelector == 1 or VowelSelector == 3:
			if VowelHarmony == 1:
				if VowelLength == 1:
					T_Nucleus = I[0]
				else:
					T_Nucleus = I[1]
			else:
				if VowelLength == 1:
					T_Nucleus = U[0]
				else:
					T_Nucleus = U[1]
		else:
			if VowelLength == 1:
				T_Nucleus = A[0]
			else:
				T_Nucleus = A[1]

	# Put it together
	Syllable = T_Onset + T_approx + T_Nucleus + T_Coda
	return Syllable

def Ortho(Word):
	NewWord = ""
	for i in range(0, len(Word)):
		if Word[i] == "w" and Word[i+1] == "a":
				NewLetter = "â"
		elif Word[i] == "w" and Word[i+1] == "i":
				NewLetter = "î"
		elif Word[i] == "w" and Word[i+1] == "u":
				NewLetter = "û"
		elif Word[i] == "h" and Word[i+1] == "a":
				NewLetter = "ä"
		elif Word[i] == "h" and Word[i+1] == "i":
				NewLetter = "ï"
		elif Word[i] == "h" and Word[i+1] == "u":
				NewLetter = "ü"
		elif Word[i] == "y" and Word[i+1] == "a":
				NewLetter = "á"
		elif Word[i] == "y" and Word[i+1] == "i":
				NewLetter = "í"
		elif Word[i] == "y" and Word[i+1] == "u":
				NewLetter = "ú"
		elif Word[i] in A and Word[i-1] in Why:
			continue
		elif Word[i] in I and Word[i-1] in Why:
			continue
		elif Word[i] in U and Word[i-1] in Why:
			continue
		elif Word[i] == "*":
			continue
		else:
			NewLetter = Word[i]
		NewWord += NewLetter
	return NewWord

def BuildWord(NumberOfSyllables):
	# VowelHarmony 1 = I, 2 = U
	VowelHarmony = random.randint(1, 2)
	if NumberOfSyllables == 1:
		Word = BuildSyllable(VowelHarmony, 1)
		Tonic = Word
		PreTonic = ""
		PostTonic = ""

	elif NumberOfSyllables == 2:
		Tonic = BuildSyllable(VowelHarmony,1)
		PreTonic = BuildSyllable(VowelHarmony,0)
		PostTonic = ""
		Word = PreTonic + Tonic.upper()

	else:
		Tonic = BuildSyllable(VowelHarmony,1)
		PreTonic = BuildSyllable(VowelHarmony,0)
		PostTonic = BuildSyllable(VowelHarmony,0)
		Word = PreTonic + Tonic.upper() + PostTonic

	Orthography = Ortho(Word.lower())
	NewWordObject = {
		"Roman": Word,
		"PreTonic": PreTonic,
		"Tonic": Tonic,
		"PostTonic": PostTonic,
		"Orthography": Orthography
	}
	return NewWordObject


WordArray = []
counter = 1
while counter < WordCount:
	NumberOfSyllables = random.randint(MinSyl, MaxSyl)
	WordObject = BuildWord(NumberOfSyllables)
	if WordObject in WordArray:
		continue
	else:
		WordArray.append(WordObject)
		counter += 1
print(WordArray)

f = open("voc.txt", "a")
for wordObj in WordArray:
	f.write(wordObj["Roman"] + ", " + wordObj["PreTonic"] + ", " + wordObj["Tonic"] + ", " + wordObj["PostTonic"] + "\r")
f.close()