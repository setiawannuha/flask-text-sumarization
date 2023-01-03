from multi_rake import Rake
r = Rake()

def multi_rake_extraction(val):
  output = []
  result = r.apply(val)
  for i in range(5):
    output.append(result[i][0])
  return output