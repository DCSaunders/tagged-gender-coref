# tagged-gender-coref
Adaptation datasets and evaluation sets for the paper "Neural Machine Translation Doesn't Translate Gender Coreference Right Unless You Make It" (GeBNLP 2020)

Neural Machine Translation (NMT) has been shown to struggle with grammatical gender that is dependent on the gender of human referents. Many existing approaches to this problem seek to control gender inflection in the target language by explicitly or implicitly adding a gender feature to the source sentence, usually at the sentence level.  Our paper proposes schemes for incorporating explicit word-level gender inflection tags into NMT. We explore the potential of this gender-inflection controlled translation when the gender feature can be determined from a human reference, assessing on English-to-Spanish and English-to-German translation.

We find that simple existing approaches can over-generalize a gender-feature to multiple entities in a sentence, and suggest an effective alternative in the form of tagged coreference adaptation data. We also propose an extension to assess translations of gender-neutral entities from English given a corresponding linguistic convention in the inflected target language. 


## Adaptation sets
We provide the small tagged adaptation sets described in sections 2.2 and 2.3 of the paper, for English-to-German and English-to-Spanish translation. The binary sets, with masculine and feminine entities only, are small (388 parallel sentence pairs) datasets with equal numbers of masculine and femine entities. They are tagged variants on the handcrafted-no-overlap sets introduced for our paper  [Reducing Gender Bias in Neural Machine Translation as a Domain Adaptation Problem](https://arxiv.org/abs/2004.04498) (ACL 2020) (with its own [github repo](https://github.com/DCSaunders/gender-debias)).

The neutral-augmented sets also include 194 equivalent parallel sentence pairs with neutral entities on the English side, and synthetic gender-neutral placeholder articles and noun inflections in the target language. Specifically we define synthetic placeholder articles `<DEF>` and  noun inflections `<W_END>`, as well as a placeholder possessive pronoun for German `<PRP>`. 

We describe four tagging schemes for adaptation, V1-4, as well as a baseline approach from our previous paper, which we refer to as S\&B. In each case we provide binary and neutral-augmented sentence sets. Brief examples are as follows:

Name | English source | German target |Spanish target
--- | --- | --- | --- 
**S\&B** | the trainer finished his work|  der Trainer  beendete seine Arbeit | el entrenador  terminó su trabajo 
| | the trainer finished her work|  die Trainerin  beendete ihre Arbeit | la entrenadora  terminó su trabajo 
| | the trainer finished their work | `<DEF>`  Trainer`<W_END>`  beendete  `<PRP>`  Arbeit| `<DEF>`  entrenador`<W_END>`  terminó su trabajo  
**V1** | the trainer `<M>`  finished his work | der Trainer  beendete seine Arbeit | el entrenador  terminó su trabajo
**V2** | the trainer `<F>` finished the work | die Trainerin  beendete die Arbeit  |la entrenadora  terminó su trabajo  
**V3** | the trainer `<N>` and the choreographer `<M>` finished the work |   `<DEF>` Trainer`<W_END>` und der Choreograf  beendeten die Arbeit |  `<DEF>` entrenador`<W_END>` y el coreógrafo terminaron el trabajo
**V4** | the trainer `<F>` , the choreographer `<N>`  |   die Trainerin , `<DEF>` Choreograf`<W_END>` |  la entrenadora , `<DEF>`coreógraf`<W_END>`



## Evaluation sets

We introduce three variations on existing test sets for use with the [WinoMT Neural Machine Translation gender bias evaluation framework](https://github.com/gabrielStanovsky/mt_gender):

**en_secondary.txt:** This is the equivalent of en.txt from WinoMT, but the profession labels and indices correspond to the secondary entity in each sentence -- that is, the entity that is *not* coreferent with the pronoun. The gender label is left unchanged, so the **accuracy** score from running WinoMT evaluation on this set indicates how frequently the secondary entity is inflected to match the label of the primary entity.

**en_neutral.txt:** This is the neutral-only evaluation dataset containing 1826 sentences with neutral entities, such that for every masculine/feminine WinoMT sentence there is also a neutral-entity sentence. There is an overlap of 240 sentences with the original WinoMT test set. Evaluation with this set is dependent on some edits to the WinoMT evaluation framework to mark any pre-defined synthetic gender-neutral endings as neutral gender inflections.

**en_neutral_secondary.txt:** This is equivalent to en_neutral.txt but with secondary entities marked, as for en_secondary.txt.

We also include **secondary_entities.py**, the python script used to identify the secondary entity professions in WinoMT sentences, which can be applied to the pro- and anti- sets if needed.

## Tagged evaluation sets

We include the tagged versions of the WinoMT test sets used in our experiments: the original set with male and female primary entities tagged `<M>` and `<F>` respectively, and the neutral-only test set with neutral primary entities tagged with `<N>`.

## Citing

```
@InProceedings{saunders-etal-2020-neural,
  author    = {Saunders, Danielle and Sallis, Rosie and Byrne, Bill},
  title     = {Neural Machine Translation Doesn't Translate Gender Coreference Right Unless You Make It},
  booktitle = {Proceedings of the Second Workshop on Gender Bias in Natural Language Processing},
  month     = {Dec},
  year      = {2020},
  publisher = {Association for Computational Linguistics}
}
```
