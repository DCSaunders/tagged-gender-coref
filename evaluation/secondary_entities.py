from __future__ import print_function
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)
# NB: replace all instances of 'construction worker' in input data with 'constructionworker' before running
# example usage:
# sed 's/construction worker/constructionworker/g' en.txt | python secondary_entities.py


entities = set()
with open('entities') as f:
  for line in f:
    entity = line.strip()
    entities.add(entity)



def check_prev_word(two_words):
  pass

def try_get_entity(w):
  secondary_entity = None
  if w in entities:
      secondary_entity = w
  return secondary_entity
  

for line in sys.stdin:
  label, primary_pos, sentence, primary_entity = line.strip().split('\t')
  primary_pos = int(primary_pos)
  split_sentence = sentence.split()
  secondary_entity = None
  secondary_pos = None
  for idx, w in enumerate(split_sentence):
    if idx != primary_pos:
      if w[-1] == ',':
        secondary_entity = try_get_entity(w[:-1])
        if secondary_entity is not None:
          secondary_entity = "{},".format(secondary_entity)
      else:
        secondary_entity = try_get_entity(w)
      if secondary_entity != None:
        secondary_pos = idx
        break
  prev_word = ''
  if secondary_pos > 0 and secondary_entity not in ["Someone", "someone"]:
    prev_word = split_sentence[secondary_pos - 1]
    if prev_word in ['the', 'The']:
      secondary_entity = "{} {}".format(prev_word, secondary_entity)
  if "constructionworker"  in primary_entity and secondary_pos > primary_pos:
    secondary_pos += 1 # special case where need to update spacing
  print('\t'.join([label, str(secondary_pos), sentence, secondary_entity]))
