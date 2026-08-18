from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments
from unsloth import FastLanguageModel

import transformers
import trl
from trl import SFTTrainer

print(f"Transformers version: {transformers.__version__}")
print(f"TRL version: {trl.__version__}")

# 1. Load Base Model
max_seq_length = 2048
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Phi-3-mini-4k-instruct",
    max_seq_length = max_seq_length,
    load_in_4bit = True,
)

# 2. Add LoRA Adapters
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none"
)

# 3. Format Data
def format_prompts(batch):
    texts = [
        f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are an expert banking assistant.<|eot_id|>"
        f"<|start_header_id|>user<|end_header_id|>\n{inst}\n{inp}<|eot_id|>"
        f"<|start_header_id|>assistant<|end_header_id|>\n{out}<|eot_id|>"
        for inst, inp, out in zip(batch["instruction"], batch["input"], batch["output"])
    ]
    return {"text": texts}

dataset = load_dataset("json", data_files="banking_sft.jsonl", split="train")
dataset = dataset.map(format_prompts, batched=True)

# 4. Train
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        max_steps=60,
        learning_rate=2e-4,
        fp16=True,
        logging_steps=10,
        output_dir="outputs",
    ),
)
trainer.train()

# 5. Export Directly to GGUF (4-bit quantization)
model.save_pretrained_gguf("banking_model_gguf", tokenizer, quantization_method="q4_k_m")