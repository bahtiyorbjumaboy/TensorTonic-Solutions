import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        initial_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        for i, token in enumerate(initial_tokens):
            self.word_to_id[token] = i
            self.id_to_word[i] = token
            self.vocab_size += 1

        unique_words = set()
        for text in texts:
            if len(text) == 0:
                continue
            for word in text.split():
                unique_words.add(word)

        for i, word in enumerate(sorted(list(unique_words))):
            self.word_to_id[word] = i + 4
            self.id_to_word[i+4] = word
            self.vocab_size += 1
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        tokens = []
        for word in text.lower().split():
            tokens.append(self.word_to_id.get(word, 1))

        return tokens
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        words = []
        for token in ids:
            words.append(self.id_to_word.get(token, self.unk_token))

        return " ".join(words)