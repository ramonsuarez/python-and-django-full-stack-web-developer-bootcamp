def end_other(a, b):
  aLow = str(a.lower())
  bLow = str(b.lower())
  lenA = len(a)
  lenB = len(b)
  if aLow[-3:] == bLow[-3:]:
      return True
  elif bLow[-3:] == aLow[-3:]:
      return True
  else:
      return False


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
