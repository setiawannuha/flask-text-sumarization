from rake_nltk import Rake
r = Rake()

def rake_extraction(val):
  output = []
  r.extract_keywords_from_text(val)
  sorting = r.get_ranked_phrases()
  for i in range(5):
    output.append(sorting[i])
  return output