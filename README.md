# Nepali-POS-Tagger With Training Code
## This is a POS tagger using CRF, you need to install CRF++ toolkit to run this code
### The prediction consists of 3 phases
#### a. Tokenize and convert into CONLL format
#### Run tokenizer_and_convert_into_conll_for_file.py to do  this
#### b. Feature Creation for CRF model
#### Run create_features_for_crf_from_conll_pos_data.py for feature creation
#### python3 create_features_for_crf_from_conll_pos_data.py --input input_file --output feature_file
#### input_file expects a sentence in each line
#### c. Prediction using the CRF model
#### crf_test -m model_path feature_file > features_with_prediction [crf_test is a program in the CRF++ toolkit which can be downloaded from (https://taku910.github.io/crfpp/)]
#### Just use the script run_nepali_pos_tagger.sh as below
bash run_nepali_pos_tagger.sh input-file.txt output-file.txt
#### If you want to convert the CONLL prediction into ILCI format,
python3 convert_conll_into_ilci_format_for_file.py --input output-file.txt --output output-file-ilci.txt --prefix nep
## If you are using this tool, please use the following citation
@misc{https://doi.org/10.48550/arxiv.2204.08960,
  doi = {10.48550/ARXIV.2204.08960},
  url = {https://arxiv.org/abs/2204.08960},
  author = {Mishra, Pruthwik and Sharma, Dipti Misra},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Building Odia Shallow Parser},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
} 
