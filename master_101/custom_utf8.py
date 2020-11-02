def custom_utf8(n):
	import re
	from binhex import toBin, toHex, binDec
	
	d = {
	0x7F 		: '0xxxxxxx',												#127
	0x7FF		: '110xxxxx 10xxxxxx', 										#2,047
	0xFFFF		: '1110xxxx 10xxxxxx 10xxxxxx',	 							#65,535
	0x1FFFFF	: '11110xxx 10xxxxxx 10xxxxxx 10xxxxxx',					#2,097,151
	0x3FFFFFF	: '111110xx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx',			#67,108,863
	0x7FFFFFFF	: '1111110x 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx 10xxxxxx'}	#2,147,483,647

	byte_regular = ''
	_bin = '0' * (16 - len(str(toBin(n)))) + str(toBin(n)) if len(str(toBin(n))) < 16 else str(toBin(n))

	for i in sorted(d.keys()):
		if n > i: continue
		else:
			if n <= i:
				byte_regular = d[i]
			break

	def returnHex(obj):
		nonlocal _bin
		res = re.sub(r'x+', _bin[:len(re.search(r'x+', obj.group(0)).group(0))], obj.group(0))
		_bin = _bin[len(re.search(r'x+', obj.group(0)).group(0)):]
		return '\\x'+toHex(binDec(int(res)))
	byte_regular = re.sub(r'(?=\d).+?(?!\w)', returnHex, byte_regular)
	return 'b'+"'"+re.sub(r'\s', '', byte_regular)+"'"