def no_teen_sum(a, b, c):
  # CODE GOES HERE
  return (fix_teen(a)+fix_teen(b)+fix_teen(c))
def fix_teen(n):
  # CODE GOES HERE
  teen = [13,14,17,18,19]
  if n in teen:
    return 0
  else:
    return n
print (no_teen_sum(1, 2, 3))
print (no_teen_sum(2, 13, 1))
print (no_teen_sum(1, 2, 14))
