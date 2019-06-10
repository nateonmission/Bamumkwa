import random
import sys

WordCount = 1000

A = ["a", "aa"]
I = ["i", "ii"]
U = ["u", "uu"]

Vowels = [A, I, U]
Onset = ["*", "b", "d", "t", "g", "k", "*", "z", "s", "r", "n", "m", "*", "w", "h", "y"]
Why = ["w", "h", "y"]
Coda = ["r", "n", "m"]

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
	VowelSelector = random.randint(1,3)
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

WordArray = []
counter = 1
while counter < WordCount:
	NumberOfSyllables = random.randint(1,3)
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

	if Word in WordArray:
		continue
	else:
		WordObject = {
			"Word": Word,
			"PreTonic": PreTonic,
			"Tonic": Tonic,
			"PostTonic": PostTonic
		}
		WordArray.append(WordObject)
		counter += 1
print(WordArray)

f = open("voc.txt", "a")
for wordObj in WordArray:
	f.write(wordObj["Word"] + ", " + wordObj["PreTonic"] + ", " + wordObj["Tonic"] + ", " + wordObj["PostTonic"] + "\r")
f.close()

