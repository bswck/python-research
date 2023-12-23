total_differences = 0
for char_ord in range(0x110000):
    char = chr(char_ord)
    if char.casefold() != char.lower():
        print(f"U+{char_ord:04X} {char} {char.casefold()=!r} {char.lower()=!r}")
        total_differences += 1

print()
print("str.casefold() vs str.lower()".join("  ").center(60, "-"))
print(f"Total differences in results for all Unicode characters: {total_differences}")
