def end_other(a, b):
    print a.lower()
    print b.lower()
    
    if b.lower in a.lower().split(b.lower()):
        print('Hi Ramon')

end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')
end_other('abc', 'abXabc')
