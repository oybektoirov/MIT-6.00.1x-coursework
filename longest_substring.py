s = 'tqckgtnwumm'
count = 0
for i in range(len(s)):
    if i == 0:
        for n in range(i, len(s)):
            if s[n] < s[n + 1]:
                count += 1
                if s[n] < s[n - 1] or s[n] == s[n - 1]:
                    start = n
        if s[i] < s[i + 1] or s[i] == s[i + 1]:
            substring = s[i] + s[i + 1]
print 'Longest substring in alphabetical order is: ' + substring 





