from scripts.base_converter import convert_to_base

# Solicit input
x = input("\nWhat number would you like to convert? ")
base = input("Into which base? ")
result = convert_to_base(x,base)


if isinstance(result, int):
  print "\nIn base %d the number %d is represented by %d\n" % (base, x, result)
else:
  print "Result that came back wasn't an integer. Something went wrong."
