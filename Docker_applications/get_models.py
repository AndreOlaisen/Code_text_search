from transformers import AutoTokenizer, AutoModel
from transformers import BertTokenizer, BertModel


def tokenize(model, tokenizer, sentence):
    # Tokens comes from a process that splits the input into sub-entities with interesting linguistic properties.
    tokens = tokenizer.tokenize(sentence.lower())

    # This is not sufficient for the model, as it requires integers as input,
    # not a problem, let's convert tokens to ids.
    tokens_ids = tokenizer.convert_tokens_to_ids(tokens)
    # print(tokens_ids)

    # Add the required special tokens
    tokens_ids = tokenizer.build_inputs_with_special_tokens(tokens_ids)
    # print(tokens_ids)

    # We need to convert to a Deep Learning framework specific format, let's use PyTorch for now.
    tokens_pt = torch.tensor([tokens_ids])

    # The length of the tokens can not be more than 512
    if len(tokens_pt[0]) > 512:
        tokens_pt = torch.tensor([tokens_pt[0][0:512].tolist()])

    # Now we're ready to go through BERT with out input
    outputs, pooled = model(tokens_pt)
    return pooled



