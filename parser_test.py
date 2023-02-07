from tada_hdt_entity.parser import Parser

p = Parser("test.csv")
data = p.parse_vertical()
print("Parser is installed successfully")