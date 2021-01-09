import numpy as np

def lev(str_1, str_2, count_errors = 3):
	str_1 = ' '+str_1
	str_2 = ' '+str_2
	def _calc_d(res, i, j):
		a = res[i][j-1]+1
		b = res[i-1][j]+1
		c = res[i-1][j-1]+(0 if str_1[i]==str_2[j] else 1)
		return min(a,min(b,c))

	res = []
	for i in range(len(str_1)):
		if i == 0:
			res.append([j for j in range(len(str_2))])
			continue
		res.append([])
		for j in range(len(str_2)):
			if j == 0:
				res[i].append(i)
				continue
			res[i].append(_calc_d(res, i, j))
			if i==j and res[i][j] > count_errors:
				return 100000000
	return	res[-1][-1]

if __name__=='__main__':
    word_1 = 'лызина'
    word_2 = 'лыткина'
    print(f'Расстояние левенштейна между словами \'{word_1}\' и \'{word_2}\' равно {lev(word_1, word_2)}\n')