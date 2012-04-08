formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had this thing.",
		"That you could type right.",
		"but it didn't sing.",
		"So I said goodnight."
)

# It uses double and single quotes because the formatter variable is inside of a double quote and the string formatiing operator r is a string converter