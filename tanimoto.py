def tanimoto(s1, s2):
	c = 0
	s1 = set(s1)
	s2 = set(s2)
	a = len(s1)
	b = len(s2)
	for ch in s1:
		if ch in s2:
			c+=1
	return 1 - c/(a+b-c)

if __name__=='__main__':
    word_1 = 'лызина'
    word_2 = 'лыткина'
    print(f'Расстояние левенштейна между словами \'{word_1}\' и \'{word_2}\' равно {tanimoto(word_1, word_2)}\n')