# how to run this
# sh run_nepali_pos_tagger.sh input_file_path output_file_path
# for output_file_path, give just a name
input_file=$1
ouput_file=$2
python3 tokenizer_and_convert_into_conll_for_file.py --input $input_file --output input-tokenized-conll.txt
python3 create_pos_features_for_crf_from_conll_data.py --input input-tokenized-conll.txt --output input-features.txt
crf_test -m nepali_pos_model.m input-features.txt > input_pos_predicted.txt
cut -f1,14 input_pos_predicted.txt > $ouput_file
rm -rf input-tokenized-conll.txt input-features.txt input_pos_predicted.txt 
