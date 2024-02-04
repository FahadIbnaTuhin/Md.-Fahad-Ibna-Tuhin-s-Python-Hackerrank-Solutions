from cmath import phase, polar

inp = input()

# print(abs(complex(inp)))
# print(phase(complex(inp)))

r, theta = polar(complex(inp))
print(f"{r}\n{theta}")
