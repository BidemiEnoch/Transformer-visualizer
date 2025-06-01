from transformers import AutoTokenizer, AutoModel
import torch

model_name = "google-bert/bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def tokenize(text: str) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    token = tokenizer([text], return_tensors="pt")["input_ids"]

    # Raw tensor from the embedding layerß
    word_embeddings = model.embeddings.word_embeddings(token)

    # Generate position IDs
    position_ids = torch.arange(token.size(1), dtype=torch.long, device=token.device)
    position_ids = position_ids.unsqueeze(0)

    # Positional embeddings: position-specific vectors
    positional_embeddings = model.embeddings.position_embeddings(position_ids)

    # The final position encoded embeddings
    final_embeddings = word_embeddings + positional_embeddings

    return (word_embeddings, positional_embeddings, final_embeddings)


