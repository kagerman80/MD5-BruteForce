from md5 import findpin

def test_54601 ():
    assert findpin("7c18c315d71119489192f48f2b84ad73") == "54601"

def test_00259 ():
    assert findpin("6dc4955a4648e2951d890ae5f67f58d6") == "00259"

