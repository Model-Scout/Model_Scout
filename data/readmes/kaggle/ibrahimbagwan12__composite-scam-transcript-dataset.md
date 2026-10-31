# Composite_Scam_Transcript_Dataset

A Large-Scale Composite Corpus of 46,982 Financial Fraud Transcripts

# Context
This dataset was curated to address the critical "Data Scarcity" bottleneck in Voice Phishing (Vishing) research. While SMS spam datasets are abundant, high-quality transcripts of real-world scam calls are rare and often fragmented.

This **Composite Scam Transcript Dataset (N=46,982)** aggregates **Forensic Call Transcripts** and **International Phishing Logs** to serve as the **Target Domain** for Transfer Learning tasks. In our associated research, this dataset is used to fine-tune models that were pre-trained on large-scale SMS corpora.

# Content
The dataset consists of two CSV files prepared via **Stratified Sampling (80/20 Split)** to ensure a consistent class distribution between training and testing.

### **File Structure**
* **`composite_train.csv`**: The training set (37,562 samples).
* **`composite_test.csv`**: The testing set (9,420 samples).

### **⚠️ Note on Duplicate Values & Distribution**
You may notice a difference between the "Total Samples" count and the "Unique Values" count. This is **intentional**:
1.  **Realistic Attack Distribution:** In real-world vishing campaigns, attackers use automated robocalls to play identical scripts to thousands of victims.
2.  **Frequency Preservation:** We retained these duplicates to preserve the *natural frequency* of high-volume attacks. This allows the model to learn which scam narratives are the most prevalent and urgent.

### **Columns**
1.  **`text`**: The raw transcript of the voice call. All Personal Identifiable Information (PII) has been redacted.
2.  **`label`**: Binary classification target.
    * `1`: **Scam** (Vishing, Fraudulent Call).
    * `0`: **Legit** (Normal Conversation, Support Call).

# Dataset Construction Methodology
This dataset harmonizes two primary sources of **Voice/Audio Transcripts**:

1.  **Primary Voice Data:**
    * *Origin:* **TeleAntiFraud-28k Corpus** [Ma et al., 2025].
    * *Content:* Real-world forensic call transcripts containing "Slow-Thinking" cognitive manipulation tactics.
2.  **Cross-Lingual Augmentation:**
    * *Origin:* **KorCCVi Dataset** [Boussougou et al., 2025].
    * *Content:* 12,000+ Korean phishing logs back-translated into English. This introduces unique international scam scripts (e.g., "Prosecutor Impersonation") often absent in Western datasets.

*Note: This dataset does **not** include the SMS Spam data. The SMS corpus was used as an external "Source Domain" for pre-training the model before fine-tuning on this transcript dataset.*

# Acknowledgements & Citations
If you use this dataset, please cite the original authors:

# Dataset Construction Methodology
This dataset is a harmonized aggregation of three distinct sources:

1.  **TeleAntiFraud-28k Corpus** [Ma et al., 2025]:
    * Real-world forensic call transcripts containing "Slow-Thinking" cognitive manipulation tactics recorded by law enforcement.
2.  **KorCCVi Dataset** [Boussougou et al., 2025]:
    * 12,000+ Korean phishing logs back-translated into English. This introduces unique international scam scripts (e.g., "Prosecutor Impersonation").
3.  **Synthetic Scenario Augmentation**:
    * To cover emerging threat vectors (e.g., "Voice Cloning" or "Family Emergency" scripts), we generated ~5,000 synthetic call transcripts using constrained LLM prompting, manually reviewed for semantic consistency.

# Inspiration
This dataset supports the paper: **"Domain-Adaptive Transfer Learning for Privacy-Preserving Scam Call Detection on Edge Devices"** (Bagwan & Mudgal, 2026). It serves as the **Target Domain** (Voice) to demonstrate how Knowledge Transfer from SMS (Source Domain) improves detection accuracy on voice transcripts.

출처: Kaggle (ibrahimbagwan12/composite-scam-transcript-dataset)
태그: united states, artificial intelligence, intermediate, classification, english
라이선스: CC BY-NC-SA 4.0
수정일: 2026-01-15T09:03:23.787Z
