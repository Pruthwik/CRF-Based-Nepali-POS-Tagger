# This is a repository for training CRF based Nepali POS Tagger for annotated data in different formats (conll/ssf/ilci)
- If data type is conll where the common format of each line is token\tpos_tag
  - python3 create_features_for_pos_crf_training.py --input Sample-Nepali-CoNLL/ --output sample-nepali-pos-features-conll.txt --type conll
- If data type is SSF for SSF annotated POS files
  - python3 create_features_for_pos_crf_training.py --input Sample-Nepali-SSF/ --output sample-nepali-pos-features-ssf.txt --type ssf
- If data type is SSF for ILCI annotated POS files
  - python3 create_features_for_pos_crf_training.py --input Sample-Nepali-ILCI/ --output sample-nepali-pos-features-ilci.txt --type ilci
- How to train a crf using CRF++ toolkit (https://taku910.github.io/crfpp/), requires a template for reading features
  - crf_learn template-pos.txt sample-nepali-pos-features-conll.txt model-pos-nepali.m
(or)
  - crf_learn template-pos.txt sample-nepali-pos-features-ssf.txt model-pos-nepali.m
(or)
  - crf_learn template-pos.txt sample-nepali-pos-features-ilci.txt model-pos-nepali.m