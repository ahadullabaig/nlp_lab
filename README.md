# NLP Laboratory (24AIL56) — Programs

Each question has its own folder (`01/` … `12/`), and each subpart has its own file (`1a_…py`, `1b_…py`).

## Setup

On this machine everything is already installed. Just activate it:

```bash
source .venv/bin/activate
```

On a new machine:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Each program downloads the NLTK data it needs (`nltk.download(...)` lines at the top), so there is no separate data step. The first run needs internet; after that the data is reused. `python setup_nltk.py` is optional — it downloads everything at once in advance.

## Running a program

Go into the program's folder first, because programs that read a file look for it in the current folder:

```bash
cd 01
python 1a_extract_email_date_phone.py
```

- **11** needs `vaccination_tweets.csv` in `11/`. It's usually found on Kaggle in the "Pfizer Vaccine Tweets" dataset. Only the `text` column is used.
- **12** needs `spam.csv` in `12/`. It's usually found on Kaggle in the "SMS Spam Collection Dataset". Column `v1` holds the label and `v2` the message.
- **5b**, **6b**, **11** and **12** open windows (a parse tree or a graph). Close each window to let the program continue.
- On computers with Tk 9, `tree.draw()` in **5b** crashes with `ValueError: ... '10c'` because of an NLTK bug. The `.venv` here has a one-line fix in `nltk/draw/util.py`, so the window works on this laptop. Reinstalling or upgrading NLTK removes the fix. On other computers, the text tree printed just before `tree.draw()` shows the same result.
- If you see `LookupError: Resource ... not found`, the download at the top of the program failed (usually no internet). Connect and run it again, or run `python ../setup_nltk.py` from the program's folder.

## Learning sequence

Study the programs in this order, not in numerical order. Each stage reuses what the previous stage taught.

Difficulty: ★ easy · ★★ moderate · ★★★ tricky · ★★★★ hard

### Stage 1 — Plain Python and regex
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 1 | [2a](02/2a_count_19_and_5.py) Two 19s and three 5s | ★ | `list.count()` |
| 2 | [5a](05/5a_password_validator.py) Password validator | ★ | `re.search()`, one check per rule |
| 3 | [3b](03/3b_split_words_separators.py) Words vs separators | ★★ | `re.findall()`, character classes like `[^,\s]` |
| 4 | [1a](01/1a_extract_email_date_phone.py) Extract email, date, phone | ★★ | Writing real patterns, reading a file |
| 5 | [4a](04/4a_sheeptalk_fsa.py) Sheeptalk FSA | ★★ | `re.fullmatch()`; be ready to draw the 5-state FSA |

### Stage 2 — NLTK basics
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 6 | [1b](01/1b_preprocessing.py) Tokenize, stop words, stem | ★ | **The preprocessing pattern** used by most later programs |
| 7 | [3a](03/3a_stemmers_lemmatizer.py) Stemmers vs lemmatizer | ★★ | Porter / Lancaster / Snowball, and why a lemmatizer needs the POS |

### Stage 3 — Counting words and n-grams
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 8 | [2b](02/2b_ngram_model.py) N-gram model | ★★ | `ngrams()`, `FreqDist`, bigram probability P(w2 \| w1) |
| 9 | [7b](07/7b_bigram_frequency.py) Bigrams in 3 documents | ★★ | Same as 2b, plus `most_common(5)` |
| 10 | [6b](06/6b_word_frequency_plot.py) Word frequency plot | ★★ | `FreqDist.plot()` |

### Stage 4 — POS tagging and chunking
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 11 | [5b](05/5b_pos_tagging_parse_tree.py) POS tags and parse tree | ★★ | `pos_tag()`, tags like NN / JJ / VB, `tree.draw()` |
| 12 | [4b](04/4b_regex_chunking.py) Regex chunking | ★★★ | `RegexpParser` grammar, e.g. `NP: {<DT>?<JJ>*<NN.*>+}` |
| 13 | [7a](07/7a_morphology_lemmatization.py) Morphology and POS lemmatization | ★★★ | Converting a POS tag to the lemmatizer's letter (`a` / `v` / `r` / `n`) |
| 14 | [6a](06/6a_nouns_adjectives_sentiment.py) Nouns, adjectives, sentiment | ★★★ | Chunking from 4b plus VADER sentiment scores |

### Stage 5 — Table-filling algorithms (dynamic programming)
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 15 | [10](10/10_min_edit_distance.py) Minimum edit distance | ★★★ | The simplest table: intention → execution = 5, Piece → Peace = 2 |
| 16 | [9](09/9_cyk.py) CYK | ★★★★ | A table of substrings; the grammar must be in Chomsky Normal Form |
| 17 | [8](08/8_viterbi.py) Viterbi for "free workers" | ★★★★ | A table of probabilities, with back pointers; a hand-worked answer is at the bottom of the file |

### Stage 6 — Case studies
| # | Program | Difficulty | What you learn |
|---|---|---|---|
| 18 | [11](11/11_sentiment_analysis.py) Vaccination tweet sentiment | ★★★ | pandas, removing links, VADER on every row, bar chart |
| 19 | [12](12/12_spam_detection.py) SMS spam detection | ★★★★ | Bag of words (`CountVectorizer`), Naive Bayes, accuracy and confusion matrix |

## Patterns that repeat

Learn these once and you'll recognise them across most of the programs:

| Pattern | Looks like | Used in |
|---|---|---|
| Preprocessing | `word_tokenize(text.lower())`, then keep `w.isalpha() and w not in stop_words` | 1b, 2b, 6b, 7b, 11 |
| Counting | `FreqDist(...)` counts everything; `.most_common(n)` gives the top n | 2b, 6b, 7b, 11 |
| Tag → chunk | `pos_tag` → `RegexpParser(grammar).parse(tagged)` | 4b, 5b, 6a |
| Reading the chunks | `for subtree in tree.subtrees():` and check `subtree.label()` | 4b, 6a |
| Sentiment label | VADER `compound` score: ≥ 0.05 Positive, ≤ −0.05 Negative, otherwise Neutral | 6a, 11 |
| Table filling | Create the table → fill the first row/column or diagonal → fill the rest with loops → print it | 8, 9, 10 |
| Lining up columns | f-string widths such as `f"{word:<10}"`; 8, 9 and 10 also use `end=""` to keep a row on one line | 3a, 5b, 7a, 8, 9, 10 |

## Notes

- The probabilities in **8** are made up for practice. If your class used different tables, replace the numbers at the top of the file.
- The grammar in **9** is a small English example. Any grammar in Chomsky Normal Form works; edit the `grammar` list.
- **7b** removes stop words so the top 5 is meaningful. The question doesn't require this, and the comment in the file shows how to keep them.
