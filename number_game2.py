def int_filter(*args):
	l = []
	for i in args:
		if type(i) == int:
			l.append(i)
		elif type(i) == list:
			for data in i:
				if type(data) == int:
					l.append(data)
	return l