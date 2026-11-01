---
license: apache-2.0
task_categories:
- question-answering
language:
- zh
tags:
- legal
- Taiwan
- zh-tw
- synthetic
- sft 
size_categories:
- 1K<n<10K
pretty_name: tw-legal-synthetic-qa
---
# Dataset Card for tw-legal-synthetic-qa

## Dataset Summary
本合成對話資料集（下稱本資料集）由 [THUDM/chatglm3-6b-32k](https://huggingface.co/THUDM/chatglm3-6b-32k) 和 [lianghsun/tw-processed-judgments](https://huggingface.co/datasets/lianghsun/tw-processed-judgments)，由實驗後的 prompt 去生成**繁體中文法律對話合成集**。

## Supported Tasks and Leaderboards
本資料集可以運用在 SFT，讓模型學會如何回答法律問題。

## Languages
繁體中文。

## Dataset Structure
### Data Instances
一個資料樣本如下，首先由 `user` 發問了一個具有（或可能有）法律情境的問題，然後 `assistant` 回答法律相關知識。
```
{
    "messages":[
        {
            "role":"user", 
            "content":"在高雄市前金區的一家名為「裙神音樂餐廳」的店家，由戊○○擔任負責人。這間餐廳主要販售啤酒、飲料和小吃，於傍晚時分開始營業，吸引了許多下班後的上班族和夜貓族前來消費。由於店內的廚房作業時間較長，戊○○明知女工不得於午後十時至翌晨六時的時間內工作之規定，卻為了節省人力成本和提高營運效率，讓多名女性員工在該時段內仍持續從事烹飪及清潔的工作。\n某日，高雄市勞工局進行例行勞動檢查時發現此情況並通報警方處理。經調查後確認戊○○違反了《性別工作平等法》第10條之規定，遂將他移送法辦。本案中涉及到的法律爭點為《性別工作平等法》對於僱主聘僱勞工所應遵守的相關規定及罰則為何？而戊○○身為一間餐飲業的經營者是否應該遵守這些法律規範以保障員工的權利呢？\n透過分析：《性別工作平等法》中有關僱主聘僱勞工應遵守的相關規定有哪些？針對類似本案的情況該如何懲處違法者？"
        },
        {
            "role":"assistant",
            "content":"根據《性別工作平等法》第3條及第4條之規定，僱主不得因員工或求職者的性傾向、懷孕、生育能力或曾有請求產假、育嬰假等情形不同而予以歧視；且若企業規模達三十人以上者，應訂定性騷擾防治措施、申訴及懲戒辦法；此外,同法第10條亦明文禁止僱主辦理不公平的勞動契約或對受僱者給予差別待遇,包括安排女性夜間工作的限制等行為。而在本案中,戊○○讓多名女性員工在午後十時至翌晨六時的時間內仍持續從事烹飪及清潔的工作,已明顯違反了前述法規中的相關規定。因此,依同法第38條可處新臺幣10萬元以上50萬元以下罰鍰;另依刑法第294條可處三年以下有期徒刑或拘役;若因情節重大致發生損害者,得加重其刑至二分之一;必要時還可廢止其營業執照或勒令歇業。因此對於類似本案的違法行為人如戊○○而言,不僅可能面臨高額罰款與刑事責任的風險外,亦會對其事業發展造成嚴重打擊與不良影響。作為一名餐飲業的經營者如戊○○,實不應存有僥倖心理並漠視法令規範的重要性;相反地,他應該積極落實各項勞動法令的要求以維護所有從業人員的基本權益和尊嚴!"
        }
    ]
}
```

### Data Fields
本資料集採用 ShareGPT 的格式，如果用 LLaMa-Factory 可以無痛訓練。

### Data Splits
這個 repo 共有以下檔案：
```
- `qa-single-turn.*`: 原始未分割的資料集。共有 `9,631` 筆。
- `train.*`: 由原始資料集先亂數後分割 80% 取出的資料集。共有 `7,704` 筆。
- `eval.*`: 由原始資料集先亂數後分割 10% 取出的資料集。共有 `963` 筆。
- `test.*`: 由原始資料集先亂數後分割 10% 取出的資料集。共有 `964` 筆。
```

## Dataset Creation
### Curation
透過簡中模型生成的繁中合成資料集具有一定比例是雜亂的，比如內容中會有簡中的用語、標點符號為半型、或者法條名稱與法院名稱不正確...等。在這裡我們有用正則表示法和工人審閱方式去除或更正大部份的錯誤格式，但請注意可能還是會具有少部份不符合繁中模型需要的「正確文本」，使用之前請務必知道這件事。很歡迎社群可以協助一同檢視這個資料集，有任何的貢獻都會列出。

### Source Data
法律情境內容是從 [lianghsun/tw-processed-judgments](https://huggingface.co/datasets/lianghsun/tw-processed-judgments) 取樣出 10k 筆判決書，並透過 [THUDM/chatglm3-6b-32k](https://huggingface.co/THUDM/chatglm3-6b-32k) 生成問答集後，再透過後處理得到 `9,631` 筆有效的資料。為了不要造成不必要的誤會，並未列出每一個問答樣本是對應回哪一篇判決書。

## Anotations
此資料集於 2024-05 附近生成，該時空點的繁中小模型有： `taide/Llama3-TAIDE-LX-8B-Chat-Alpha1` 和 `MediaTek-Research/Breeze-7B-32k-Instruct-v1_0`，經實驗後，兩個繁中模型很難依照 prompt 指示去生成情境問答題，相較之下簡中模型較容易遵從 prompt 去完成任務，故後來選擇 ChatGLM3 來生成資料。

### Personal and Sensitive Information
基本上我們已經去識別化，每一個樣本內的故事場景和人物都是虛構，但如果你有發現任何可識別身份，也請歡迎 PR 哪些需要修正。

## License
apache-2.0