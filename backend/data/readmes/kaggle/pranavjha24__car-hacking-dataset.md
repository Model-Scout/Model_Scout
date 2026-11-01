# Car-Hacking Dataset

Car-Hacking Dataset for the intrusion detection

Dataset Description
Title: Car Hacking: CAN Intrusion Detection Dataset (Mirror)
Source: Original dataset curated by the Hacking and Countermeasure Research Lab (HCRL) at Korea University

This dataset captures Controller Area Network (CAN) bus traffic from a real vehicle, simulating both normal driving scenarios and four types of cyberattacks:

Denial-of-Service (DoS)

Fuzzy/Flooding Attacks

Spoofing Attacks (RPM/Gear/Speed gauge manipulation)

Replay Attacks

It is widely used to develop machine learning models for detecting intrusions in automotive communication systems.

Dataset Structure
Files:

normal.csv: Benign CAN traffic (2.1M messages).

attack_DoS.csv, attack_Fuzzy.csv, attack_spoofing.csv, attack_replay.csv: Attack-specific logs.

Features:

Timestamp, CAN ID, Data Length Code (DLC), Data (hexadecimal payload).

Label (0 for normal, 1 for attack).

Usage Examples
Train ML/DL models (e.g., Random Forest, LSTM) for real-time CAN intrusion detection.

Benchmark automotive cybersecurity solutions.

Study CAN protocol vulnerabilities and attack patterns.

Citation
If you use this dataset, cite the original work:

Publication
Song, Hyun Min, Jiyoung Woo, and Huy Kang Kim. "In-vehicle network intrusion detection using deep convolutional neural network." Vehicular Communications 21 (2020): 100198.

Seo, Eunbi, Hyun Min Song, and Huy Kang Kim. "GIDS: GAN based Intrusion Detection System for In-Vehicle Network." 2018 16th Annual Conference on Privacy, Security and Trust (PST). IEEE, 2018.'

This Kaggle dataset is a mirror of the original HCRL work.

For reproducibility, include the above citation in publications or projects using this data.

출처: Kaggle (pranavjha24/car-hacking-dataset)
태그: 
라이선스: MIT
수정일: 2025-02-03T03:49:51.113Z
