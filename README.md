# converter arabe --> roman or roman --> arabe

use:
from roman import convert

tab= convert("CCIXIV")
print(tab)      # expected: 213 as integer

tab= convert("213")  # or tab= convert(213)
print(tab)      # expected: "CC IX IV "  as string 
# (take care about blankspaces in response between each group 
and at the end).
