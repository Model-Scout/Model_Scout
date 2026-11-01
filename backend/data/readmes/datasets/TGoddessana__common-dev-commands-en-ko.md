---
language:
  - ko
  - en
license: mit
task_categories:
  - text-generation
tags:
  - linux
  - command-line
  - natural-language-to-code
  - korean
  - multilingual
size_categories:
  - 10K<n<100K
---

# Common Linux Commands (Korean-English)

A bilingual dataset for translating natural language instructions into Linux/Unix commands.

## Dataset Description

This dataset contains 12,250 examples of natural language queries (in both Korean and English) paired with their corresponding Linux/Unix commands. It covers 82 different command-line tools commonly used in system administration and development.

## Dataset Structure

```json
{
  "korean_question": "production.ini 인벤토리 써서 site.yml 실행해줘.",
  "english_question": "Run site.yml using the production.ini inventory.",
  "command": "ansible-playbook -i production.ini site.yml"
}
```

### Fields

| Field | Description |
|-------|-------------|
| `korean_question` | Natural language instruction in Korean |
| `english_question` | Natural language instruction in English |
| `command` | The corresponding Linux/Unix command |

## Covered Commands

The dataset includes examples for 82 commands including:

`ansible-playbook`, `awk`, `aws`, `cat`, `chmod`, `chown`, `cp`, `curl`, `docker`, `docker-compose`, `find`, `git`, `grep`, `htop`, `journalctl`, `kubectl`, `ln`, `ls`, `mkdir`, `mv`, `nginx`, `npm`, `pip`, `ps`, `rm`, `rsync`, `scp`, `sed`, `ssh`, `systemctl`, `tar`, `top`, `vim`, `wget`, and more.

## Use Cases

- Training models to convert natural language to shell commands
- Building CLI assistants
- Command-line autocomplete systems
- Educational tools for learning Linux commands

## License

MIT License
