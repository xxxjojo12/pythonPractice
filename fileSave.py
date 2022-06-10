# textdata = '아아아어어ㅓ엉어어ㅓ어어엉오오옹아아아ㅏㅇ으으ㅡ으으으'\
#            'ddddddddddddddddddd'\
#            'aaaaaaaaa'
# print(len(textdata))

# fout = open('testdata', 'wt')
# fout.write(textdata)
# fout.close()

# fout1 = open('testdata1', 'wt')
# print(textdata, file=fout1, sep='', end='')
# fout1.close()

# fout2 = open('testdata2', 'wb')
# print(textdata, file=fout2, sep='', end='')
# fout2.close()

binarydata = bytes(range(0, 256))
fout = open('binarytest', 'wb')
fout.write(binarydata)
fout.close()