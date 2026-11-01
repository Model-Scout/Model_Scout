---
size_categories:
- n<1K

configs:
- config_name: Roleplay
  data_files:
  - split: messages
    path: data.json
---
Created from a python script I wrote that generates random plots within certain categories, and then creates about 5-15 responses.

Each response length is randomly selected from a small list to keep the responses dynamic.  I also make the LLM respond in third person 2/3 times, and in first person 1/3 times (as I have seen this done sometimes as well)

I also have a cleanup step, where I am using another model to clean up the responses (Sometimes sentences are cut off from reaching the maximum tokens or something).

Lastly I process each response into the openai conversational format (As opposed to the sharegpt format.)

Currently in OpenAI conversation format.  I also included the RAW individual outputs of each conversation.  This is how I save them, then I have other scripts to eventually process them into the data.json file.

5/29
I added a LOT of Claude Haiku with more conversation turns.  I also added some more Claude Sonnet 3.7 and 4.0.  I have a couple Opus generations in there as well, but that crap is expensive :D

6/2
Added another 400 conversations (5-15+ turns) using the new Deepseek R1.  The thinking mode works very well and returns a well written response.  I also stripped out the "thinking" from this dataset.  I am planning on adding another dataset with the "thinking" bits soon.  Other general formatting rules and things like that, I required the the responses to restrict any sort of scene to PG-13, to ensure this dataset is more of a SFW dataset.

If you use it, let me know!  This dataset ended up costing around $20 (Mostly from Anthropic, deepseek R1 is quite a bit cheaper.)