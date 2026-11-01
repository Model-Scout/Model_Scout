---
license: apache-2.0
task_categories:
- text-generation
language:
- en
- ko
size_categories:
- 10K<n<100K
---
### INFO:
These are the parsed logs from the "teatime logs" xlsx files.

Every user edit or message regeneration makes a new branch in the conversation tree. This leads to message duplication in the 'all_logs.json' file. Every change creates a fresh branch, copying all earlier messages.

The 'longest' files are different. They only contain the longest path from the first to the last message. This approach aims to avoid duplication. Ideally, the '_longest' files should have no repeat messages.

### all_logs.json
Total tokens: 237442515  
Average chat token length: 4246.03  
Median chat token length: 3797.0  
Average messages per chat: 18.96  
Median messages per chat: 15.0  
Total number of chats: 55921  


### all_logs_longest.json
Total tokens: 27611121  
Average chat token length: 2499.65  
Median chat token length: 1335.5  
Average messages per chat: 11.27  
Median messages per chat: 5.0  
Total number of chats: 11046  

![Alt text](https://gcdnb.pbrd.co/images/7rCUvL1p5LI0.png?o=1)