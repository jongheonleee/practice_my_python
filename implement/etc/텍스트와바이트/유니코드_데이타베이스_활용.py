import unicodedata, re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for ch in sample : # 유니코드 데이타베이스 : 코드 포인트를 문자명으로 매핑 각 문자에 대한 메타데이터 ... 을 보관 
  print('U+%04x' % ord(ch),
        ch.center(6),
        're_dig' if re_digit.match(ch) else '-',
        'isdig' if ch.isdigit() else '-',
        'isnum' if ch.isnumeric() else '-',
        format(unicodedata.numeric(ch), '5.2f'),
        unicodedata.name(ch),
        sep='\t')

