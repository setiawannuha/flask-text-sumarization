import kex

def kex_extraction(val):
  model = kex.SingleRank()
  output = []
  result = model.get_keywords(val, n_keywords=5)
  for i in range(5):
    output.append(result[i]['stemmed'])
  return output