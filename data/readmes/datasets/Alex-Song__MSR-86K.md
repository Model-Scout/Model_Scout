---
license: cc-by-nc-nd-4.0
task_categories:
- automatic-speech-recognition
language:
- es
- ko
- en
- fr
- de
- hi
- vi
- it
- nl
- pt
- th
- ru
- id
- ja
- ar
viewer: false
pretty_name: MSR-86K
extra_gated_prompt: >
  The MSR-86K dataset is available to download for non-commercial purposes
  under the CC BY-NC-ND 4.0 International License. MSR-86K doesn't own the
  copyright of the audios, the copyright remains with the original owners of the
  video or audio, and the public URL is given for the original video or audio.


  The "Researcher" has requested permission to use the MSR-86K database (the
  "Database").  In exchange for such permission, Researcher hereby agrees to the
  following terms and conditions:

  - Researcher shall use the Database only for non-commercial research and
  educational purposes.

  - The authors make no representations or warranties regarding the Database,
  including but not limited to warranties of non-infringement or fitness for a
  particular purpose. 

  - Researcher accepts full responsibility for his or her use of the Database
  and shall defend and indemnify the authors of MSR-86K, including their
  employees, Trustees, officers and agents, against any and all claims arising
  from Researcher's use of the Database, including but not limited to
  Researcher's use of any copies of copyrighted audio files that he or she may
  create from the Database. 

  - Researcher may provide research associates and colleagues with access to the
  Database provided that they first agree to be bound by these terms and
  conditions. 

  - The authors reserve the right to terminate Researcher's access to the
  Database at any time. 

  - If Researcher is employed by a for-profit, commercial entity, Researcher's
  employer shall also be bound by these terms and conditions, and Researcher
  hereby represents that he or she is fully authorized to enter into this
  agreement on behalf of such employer.
extra_gated_fields:
  Name: text
  Email: text
  Organization: text
  Address: text
  I agree to not attempt to determine the identity of speakers in this dataset: checkbox
  I accept the terms of access: checkbox
---

# Dataset Card for MSR-86K


## Dataset Description
- **Paper:** https://arxiv.org/abs/2406.18301

### Dataset Summary
MSR-86K is an evolving, large-scale multilingual corpus for speech recognition research. The corpus is derived from publicly accessible videos on YouTube, comprising 15 languages and a total of 86,300 hours of transcribed ASR data. We believe that such a large-scale corpus will propel the research in multilingual speech algorithms. MSR-86K doesn't own the copyright of the audios, the copyright remains with the original owners of the video or audio, and the public URL is given for the original video or audio.

### Languages
MSR-86K contains labelled (transcribed) data for 15 languages:

| Language | Code | Train Hours | Dev Hours |
|:---:|:---:|:---:|:---:|
| Spanish | Es | 13976.84 | 18.63 |
| Korean | Ko | 10338.66 | 18.56 |
| English | En | 9795.46 | 17.42 |
| French | Fr | 8316.70 | 15.84 |
| German | De | 6862.00 | 14.38 |
| Hindi | Hi | 5986.50 | 11.62 |
| Vietnamese | Vi | 5957.47 | 11.54 |
| Italian | It | 5691.28 | 11.4 |
| Dutch | Nl | 4138.5 | 9.67 |
| Portuguese | Pt | 3737.54 | 9.62 |
| Thai | Th | 3674.7 | 9.47 |
| Russian | Ru | 3188.52 | 9.35 |
| Indonesian | Id | 1982.87 | 9.12 |
| Japanese | Ja | 1779.03 | 8.54 |
| Arabic | Ar | 873.84 | 4.95 |
| Total | | 86299.91 | 180.11 |


## Dataset Structure

### Data Instances

```python
{
  "dataset": "MSR-86K",
  "language": "EN",
  "version": "v1.0.0",
  "audios": [
    {
      "aid": "EN_000000624",
      "url": "https://www.youtube.com/watch?v=GN1hHNkAlR8",
      "segments": [
        {
          "sid": "EN_000000624_0000",
          "begin_time": "0.02",
          "end_time": "13.63",
          "text_tn": "THIS ONE GUY RIGHT HERE YOU CAN SEE SEE HOW HE IS KIND OF GRAY IT'S A LITTLE HARD TO GET HIM IN FOCUS BUT HE'S A LITTLE BIT GRAY AND NOT QUITE AS PINK AND HE HAS A LITTLE VACUOLE AROUND THE OUTSIDE THAT LITTLE WHITE SPACE THAT'S AN ARTIFACT OF TISSUE PROCESSING WHEN WE SOAK THE"
        },
        {
          "sid": "EN_000000624_0001",
          "begin_time": "14.4",
          "end_time": "29.88",
          "text_tn": "YOU KNOW TISSUE DOESN'T COME OUT OF YOUR BODY PINK AND PURPLE LIKE THIS WE ACTUALLY HAVE TO SOAK IT IN FORMALDEHYDE OR FORMALIN RUN IT THROUGH A SERIES OF DIFFERENT CHEMICALS TO MAKE SURE THE TISSUE DOESN'T BREAK DOWN BUT ANYWAYS BACK TO THIS LITTLE CELL HERE THIS LITTLE GREY CELL HAS THIS VACUOLE AROUND THE OUTSIDE AND THAT'S AN ARTIFACT AND THE REASON"
        }
      ]
    }
  ]
}
```

### Citation Information

Please cite this paper if you find this work useful:

```bibtext
@article{li2024msr,
  title={MSR-86K: An Evolving, Multilingual Corpus with 86,300 Hours of Transcribed Audio for Speech Recognition Research},
  author={Li, Song and You, Yongbin and Wang, Xuezhi and Tian, Zhengkun and Ding, Ke and Wan, Guanglu},
  journal={arXiv preprint arXiv:2406.18301},
  year={2024}
}
```


### Terms of Access

The "Researcher" has requested permission to use the MSR-86K database (the "Database").  In exchange for such permission, Researcher hereby agrees to the following terms and conditions:

  - Researcher shall use the Database only for non-commercial research and educational purposes.
  
  - The authors make no representations or warranties regarding the Database, including but not limited to warranties of non-infringement or fitness for a particular purpose. 
  
  - Researcher accepts full responsibility for his or her use of the Database and shall defend and indemnify the authors of MSR-86K, including their employees, Trustees, officers and agents, against any and all claims arising from Researcher's use of the Database, including but not limited to Researcher's use of any copies of copyrighted audio files that he or she may create from the Database.
  
  - Researcher may provide research associates and colleagues with access to the Database provided that they first agree to be bound by these terms and conditions. 
  
  - The authors reserve the right to terminate Researcher's access to the Database at any time. 
  
  - If Researcher is employed by a for-profit, commercial entity, Researcher's employer shall also be bound by these terms and conditions, and Researcher hereby represents that he or she is fully  authorized to enter into this agreement on behalf of such employer.