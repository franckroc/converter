from roman import convert

def test_convert():
    tab= convert("CCIXIV")
    assert tab == 213
    tab= convert(150)
    assert tab == "C L "

tab= test_convert() 
print(tab)




