def intfilter(*args):
	''' This is my integer filter function which filter outs integer type of dat from args'''
	l = []
	for i in args:
		if type(i) == int:
			l.append(i)
	return l