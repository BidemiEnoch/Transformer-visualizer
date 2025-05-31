from transformers import AutoTokenizer, AutoModel
import torch


model_name = "google-bert/bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


def tokenize(text: str) -> torch.tensor:
    token = tokenizer([text], return_tensors="pt")["input_ids"]

    # Raw tensor from the embedding layer
    word_embeddings = model.embeddings.word_embeddings(token)
    print(word_embeddings.shape)

    # Generate position IDs
    position_ids = torch.arange(token.size(1), dtype=torch.long, device=token.device)
    position_ids = position_ids.unsqueeze(0)  # Shape: [1, seq_len]

    # Positional embeddings: position-specific vectors
    positional_embeddings = model.embeddings.position_embeddings(position_ids)
    print(positional_embeddings.shape)

    # The final positionally encoded embeddings
    return word_embeddings + positional_embeddings


print(tokenize("the sun is"))
