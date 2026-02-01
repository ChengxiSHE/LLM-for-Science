# 计算 dataset 的 tokens，使用 qwen2 的 tokenizer

import torch
from transformers import Qwen2Tokenizer

tokenizer = Qwen2Tokenizer.from_pretrained("Qwen2")
# 加载数据集, 位于本地的 dataset 中
