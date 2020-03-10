import string
dim = 40
print('\t '+(' '.join([char for char in string.ascii_letters][0:dim])), end='\n\t ')
for i in range(0, dim):
  print('_', end=' ')
print()
for row in range(0, dim):
  print('{}\t'.format(row), end='|')
  for column in range(0, dim):
    print('_', end='|')
  print()