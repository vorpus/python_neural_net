import random

def forward_multiply_gate(x, y):
    return x * y

x = -2
y = 3
out = forward_multiply_gate(x, y)
x_gradient = y
y_gradient = x

step_size = 0.01
x += step_size * x_gradient
y += step_size * y_gradient
out_new = forward_multiply_gate(x, y)

print out_new
