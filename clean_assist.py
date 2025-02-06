messy_names = [
    "  alice ",
    "Bob",
    " charlie",
    "Alice",
    "BOB ",
    "eve  ",
    " Eve",
    "eve",
]

cleaned_names = sorted(set(name.strip().title() for name in messy_names))

print(
    f"Cleaned and Sorted Names: {[name.capitalize().strip() for name in cleaned_names]}",
)
