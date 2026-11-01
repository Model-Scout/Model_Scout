# fluent-speech-corpus

Fluent Speech Commands Voice Dataset for Speaking Recognition

Speaker Verification Corpus
FLUENT SPEECH COMMANDS DATASET

Dataset contains 97 speakers saying 248 different phrases. The 248 utterances map to 31 unique intents, that are divided into three slots: action, object, and location. The goal in preparing this dataset was to provide a benchmark for end-to-end spoken language understanding models.
LICENSE

This work is licensed under the Fluent Speech Commands Public License. See the PDF in this folder.
COLLECTION

Data was gathered using crowdsourcing. Participants were limited to those located in the United States and Canada. Participants were asked to say each phrase twice. The phrases to record were presented in a random order. Participants were required to consent to their speech data being released along with anonymized demographic information about themselves. The speech data was validated by a separate set of crowdsourcing workers. All audios that were deemed by the crowdsourced workers to be noisy, inaudible, unintelligible, or contain the wrong phrase were removed.
CONTENTS

The files are organized into directories. The directories contain the following:  
&gt;   /wavs/speakers/: Contains directories divided by the randomly generated speaker ID each participant was given. Each directory contains 16kHz single-channel .wav files containing the speech audio recorded by that speaker.
&gt;     /data/speaker_demographics.csv: A CSV file with the demographics for each speaker. These include: self-reported speaking ability, first language spoken, current language used for work or school, gender, and age range.
&gt;     /data/traindata.csv, /data/validdata.csv, /data/test_data.csv: A csv file describing each audio file in the training set, validation set, and test set, respectively. Each line contains the following information:
-     path - Path to the .wav file
-     speakerId - Anonymized alphanumeric code for the speaker of this audio
-     transcript - The prompt that the speaker was asked to read
-     action - One of 'change language', 'activate', 'deactivate', 'increase', 'decrease', 'bring'
-      object - One of 'none', 'music', 'lights', 'volume', 'heat', 'lamp', 'newspaper', 'juice', 'socks', 'shoes', 'Chinese', 'Korean', 'English', 'German'
-      location - One of 'none', 'kitchen', 'bedroom', 'washroom'

LICENSE

This work is licensed under the Fluent Speech Commands Public License. See the PDF in this folder.

출처: Kaggle (tommyngx/fluent-speech-corpus)
태그: classification, neural networks, cnn, multiclass classification, audio
라이선스: Other (specified in description)
수정일: 2020-11-24T12:22:17.793Z
