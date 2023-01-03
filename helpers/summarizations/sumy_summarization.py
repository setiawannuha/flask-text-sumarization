import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.summarizers.luhn import LuhnSummarizer

def lex_rank_summarization(val):
  output = ""
  my_parser = PlaintextParser.from_string(val, Tokenizer("english"))
  lex_rank_summarizer = LexRankSummarizer()
  summary = lex_rank_summarizer(my_parser.document, sentences_count=3)
  for sentence in summary:
    output += str(sentence)+"\n"
  return output

def lsa_summarization(val):
  output = ""
  my_parser = PlaintextParser.from_string(val, Tokenizer("english"))
  lsa_summarizer = LsaSummarizer()
  summary = lsa_summarizer(my_parser.document, sentences_count=3)
  for sentence in summary:
    output += str(sentence)+"\n"
  return output

def text_rank_summarization(val):
  output = ""
  my_parser = PlaintextParser.from_string(val, Tokenizer("english"))
  text_rank_summarizer = TextRankSummarizer()
  summary = text_rank_summarizer(my_parser.document, sentences_count=3)
  for sentence in summary:
    output += str(sentence)+"\n"
  return output

def kl_summarization(val):
  output = ""
  my_parser = PlaintextParser.from_string(val, Tokenizer("english"))
  kl_summarizer = KLSummarizer()
  summary = kl_summarizer(my_parser.document, sentences_count=3)
  for sentence in summary:
    output += str(sentence)+"\n"
  return output

def luhn_summarization(val):
  output = ""
  my_parser = PlaintextParser.from_string(val, Tokenizer("english"))
  luhn_summarizer = LuhnSummarizer()
  summary = luhn_summarizer(my_parser.document, sentences_count=3)
  for sentence in summary:
    output += str(sentence)+"\n"
  return output