import yake
def yake_extraction(val):
  output = []
  language = "en"
  custom_kw_extractor = yake.KeywordExtractor(lan=language, features=None)
  result = custom_kw_extractor.extract_keywords(val)
  sorting = sorted(result, key=lambda tup: tup[1], reverse=True)
  for i in range(5):
    output.append(sorting[i][0])
  return output