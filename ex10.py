tabby_cat = "\tI'm tabbed in." # tab键转意
persian_cat = "I'm split\non a line." # n转意，换行
backslash_cat = "I'm \\ a \\ cat." # \转意

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" # tab转意 n换行转意

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

r"""
\\
\'
\"
    \a
    \b
    \f
\n
    \N{name}
    \r
\t
    \u16
    \U32
    \v
    \000
    \xhh
""" #添加r表示原始字符串 raw-string
