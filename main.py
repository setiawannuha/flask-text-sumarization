from flask import Flask
from flask import request, render_template
from helpers.extractions.yake_extraction import yake_extraction
from helpers.extractions.rake_extraction import rake_extraction
from helpers.extractions.multi_rake_extraction import multi_rake_extraction
from helpers.extractions.keybert_extraction import keybert_extraction
from helpers.extractions.kex_extraction import kex_extraction
from helpers.summarizations.sumy_summarization import lex_rank_summarization
from helpers.summarizations.sumy_summarization import lsa_summarization
from helpers.summarizations.sumy_summarization import text_rank_summarization
from helpers.summarizations.sumy_summarization import kl_summarization
from helpers.summarizations.sumy_summarization import luhn_summarization

app = Flask(__name__)

@app.route("/")
def main():
  return render_template("app.html")


@app.route('/generate', methods=['POST']) 
def generate():
  rake_output = "-"
  yake_output = "-"
  multi_rake_output = "-"
  keybert_output = "-"
  kex_output = "-"
  lex_rank_summarization_output = "-"
  lsa_summarization_output = "-"
  text_rank_summarization_output = "-"
  kl_summarization_output = "-"
  luhn_summarization_output = "-"

  article = request.form.get('article')
  if article == "":
    return render_template("404.html", result = {
      "code": "400 - Bad Request",
      "message": "Article must be filled"
    })

  if request.form.get('rake') == 'on':
    rake_output = rake_extraction(article)
  if request.form.get('yake') == 'on':
    yake_output = yake_extraction(article)
  if request.form.get('multi_rake') == 'on':
    multi_rake_output = multi_rake_extraction(article)
  if request.form.get('keybert') == 'on':
    keybert_output = keybert_extraction(article)
  if request.form.get('kex') == 'on':
    kex_output = kex_extraction(article)
  if request.form.get('lex_rank') == 'on':
    lex_rank_summarization_output = lex_rank_summarization(article)
  if request.form.get('lsa') == 'on':
    lsa_summarization_output = lsa_summarization(article)
  if request.form.get('text_rank') == 'on':
    text_rank_summarization_output = text_rank_summarization(article)
  if request.form.get('kl') == 'on':
    kl_summarization_output = kl_summarization(article)
  if request.form.get('luhn') == 'on':
    luhn_summarization_output = luhn_summarization(article)
  
  response = {
    "article": article,
    "rake": rake_output,
    "yake": yake_output,
    "multi_rake": multi_rake_output,
    "keybert": keybert_output,
    "kex": kex_output,
    "summary_lex_rank": lex_rank_summarization_output,
    "summary_lsa": lsa_summarization_output,
    "summary_text_rank": text_rank_summarization_output,
    "summary_kl": kl_summarization_output,
    "summary_luhn": luhn_summarization_output,
    "biodata": {
      "name": "Setiawan Restu Aji",
      "nim": "119203008",
    }
  }
  return render_template("result.html", result = response)