age = input("How old are you? ")#promping 提示输入
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"Som you're {age} old, {height} tall and {weight} heavy.")


"""
pydoc input
Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
"""# 按q键退出
