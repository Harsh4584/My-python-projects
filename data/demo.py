# x = open('harsh.txt', 'w')
# lines = ['harsh is good\n', 'harsh is bad\n', 'harsh is good\n']
# x.writelines(lines)
# x.close()

from espeak import espeak
espeak.synth("Hello world.")