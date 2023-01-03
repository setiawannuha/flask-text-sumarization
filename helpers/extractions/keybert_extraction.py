from keybert import KeyBERT
kw_model = KeyBERT()

def keybert_extraction(val):
  output = []
  result = kw_model.extract_keywords(val)
  for i in range(5):
    output.append(result[i][0])
  return output