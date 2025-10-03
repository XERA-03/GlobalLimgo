from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class Translator:
    def __init__(self, src_lang, tgt_lang):
        self.model_name = "facebook/m2m100_418M"
        self.tokenizer = M2M100Tokenizer.from_pretrained(self.model_name)
        self.model = M2M100ForConditionalGeneration.from_pretrained(self.model_name)
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def translate(self, text):
        self.tokenizer.src_lang = self.src_lang
        encoded = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(**encoded, forced_bos_token_id=self.tokenizer.get_lang_id(self.tgt_lang))
        return self.tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
