
import astor

f = "test.py"

node = astor.parsefile(f)
print node
print astor.dump(node)
print astor.to_source(node)
