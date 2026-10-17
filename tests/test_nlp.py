import pytest
import koshur

def test_tokenize():
    tokens = koshur.tokenize("अमी पनॳ सोदरस नावि छस लमान।")
    assert len(tokens) >= 5
    assert "लमान" in tokens

def test_sent_tokenize():
    text = "सु छु परान। बॴ छुस ख्यवान। तिम छि गछ़ान।"
    sents = koshur.sent_tokenize(text)
    assert len(sents) == 3

def test_normalize():
    raw = "كاشميري  "
    norm = koshur.normalize(raw)
    assert "ک" in norm # Normalized Persian/Kashmiri kaf
