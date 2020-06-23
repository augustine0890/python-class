class NoCustomAttributes:
    pass

attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    print("This text gets printed!")

print(hasattr(attributeless, "fake_attribute"))

print(getattr(attributeless, "other_fake_attribute", 500))

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for ele in how_many_s:
  if hasattr(ele, "count"):
    print(ele.count("s"))