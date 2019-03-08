a = []
pig = 'ay'
pig1 = 'way'
vowels = ['a','e','i','o','u']

print "Welcome to the Pig Latin Translator:\n"

word = raw_input('Please enter an english word(s):\n')
new = word.lower()
new1 = list(new)
j = 0
for j in range(len(new1)):
  if new1[j].isspace():
    ls = new.split()
    i = 0
    while i < len(ls) and len(ls) > 0:
      for words in ls:
        words = list(words)
        x = 0
        while x < len(words):
          if words[x] in vowels and words[0] not in vowels and words[x].isalpha():
            startstring = words[x:]
            endstring = words[:x]
            pig_latin = startstring + endstring
            pig_latin1 = ''.join(pig_latin) + pig
            if pig_latin1 not in a:
              a.append(pig_latin1)
              pig_latin_f = ''.join(pig_latin1)
              print pig_latin_f
              break
          elif words[0] in vowels:
      	    pig_latin = new + pig1
      	    if pig_latin not in a:
              a.append(pig_latin)
              pig_latin_f = ''.join(a)
              print pig_latin_f
              break
          else:
            x = x + 1
      i = i + 1
  
  elif not new1[j].isspace():
    i = 0
    while i < len(new) and len(new) > 0:
      if new.isalpha() and new[i] in vowels and new[0] not in vowels:
        startstring = new[i:]
        endstring = new[:i]
        pig_latin = startstring + endstring + pig
        if pig_latin not in a:
          a.append(pig_latin)
          pig_latin_f = ''.join(a)
          print pig_latin_f
          break
      elif new[0] in vowels:
      	pig_latin = new + pig1
      	if pig_latin not in a:
          a.append(pig_latin)
          pig_latin_f = ''.join(a)
          print pig_latin_f
          break
      else:
        i = i + 1 
  else:
    print "nada babyyyyy"