with open('test_CSV.csv') as a:
  b = a.read()
csv_list = []
main_dict = {}
c = b.split('\n')
keys = c[0].split(',')
for d in range(1,len(c)):
  sub_dict = {}
  coin = 'C' + str(d)
  values = c[d].split(',')
  for e in range(len(keys)):
    sub_dict.update({keys[e]: values[e]})
  main_dict.update({coin:sub_dict})
csv_list.append(main_dict)
print(csv_list)