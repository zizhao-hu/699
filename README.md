# Personalized Ethical Alignment in LLMs: Tailoring Question Answering For Different Age Groups

This repository provides an implementation and tools to ensure personalized ethical alignment in large language models (LLMs), specifically tailored for different age groups. The goal is to evaluate the performance of LoRA and prompt engineering on LLMs for various age groups and understand their behavior in terms of ethics and appropriateness.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
```
git clone https://github.com/zizhao-hu/699.git
```
2. Navigate to the project directory:
```
cd personalized-ethical-alignment
```
3. Install the required dependencies (assuming pip is used):
```
pip install -r requirements.txt
```

## Usage

1. **Generating Answers**:
   - Use `baseline.py` to generate the answer JSON file for the questions specified in `questions.py`.
     ```
     python baseline.py
     ```

2. **Evaluating using GPT-4**:
   - Use `gpt4_eval.py` to evaluate the answers with GPT-4 API. You need to specify the filename of the answer file.
     ```
     python gpt4_eval.py -file_name your_answer_filename.json
     ```
   - This will generate evaluation statistics in a `stats.json` file.

3. **Fine-Tuning and Evaluation for Specific Age Groups**:
   - Use `lora_llama_{age_group}.py` to run the generated answers for fine-tuned models specific to a particular age group. Replace `{age_group}` with the desired age group, e.g., `lora_llama_teen.py` for teenagers.
     ```
     python lora_llama_teen.py
     ```

## File Structure
```
.
├── baseline.py
├── questions.py
├── gpt4_eval.py
├── lora_llama_child.py
├── lora_llama_teen.py
├── lora_llama_adult.py
└── requirements.txt
```
