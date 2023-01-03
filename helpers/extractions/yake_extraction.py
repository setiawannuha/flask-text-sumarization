import yake
def yake_extraction(val):
  output = []
  language = "en"
  max_ngram_size = 3
  deduplication_thresold = 0.9
  deduplication_algo = 'seqm'
  windowSize = 1
  numOfKeywords = 20
  custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
  result = custom_kw_extractor.extract_keywords(val)
  sorting = sorted(result, key=lambda tup: tup[1], reverse=True)
  for i in range(5):
    output.append(sorting[i][0])
  return output