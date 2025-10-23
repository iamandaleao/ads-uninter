#Execute as seguintes atribuições:

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# a) 'ant bat cod'
res = s1 + ' ' + s2 + ' ' + s3
print(res)

# b) 'ant ant ant ant ant ant ant ant ant ant'
res = 10 * (s1 + ' ')
print(res)

# c) 'ant bat bat cod cod cod'
res = (s1 + ' ') + 2 * (s2 + ' ') + 3 * (s3 + ' ')
print(res)

# d) 'ant bat ant bat ant bat ant bat ant bat ant'
res = (s1 + ' ') + (s2 + ' ') + (s1 + ' ') + (s2 + ' ') + (s1 + ' ') + (s2 + ' ')  + (s1 + ' ') + (s2 + ' ') + (s1 + ' ') + (s2 + ' ')+ (s1 + ' ')
print(res)

# e) 'batbatcod batbatcod batbatcod batbatcod'
res = (s2+s2+s3+ ' ') + (s2+s2+s3)
print(res)