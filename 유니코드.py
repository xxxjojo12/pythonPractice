from dataclasses import dataclass


def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value1 = unicodedata.lookup(name)
    print('value = %s, name = %s, value = %s' % (value, name, value1))


unicode_test('8')
unicode_test('L')
unicode_test('/')
unicode_test('오')
unicode_test('\u1022')
unicode_test('\uafda')
unicode_test('\u2603')
