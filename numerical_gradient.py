import random

def forward_multiply_gate(x, y):
    return x * y

x = -2
y = 3

out = forward_multiply_gate(x, y)
h = 0.0001

xph = x + h
out2 = forward_multiply_gate(xph, y)
x_derivative = (out2 - out) / h

print 'x\': ' + str(x_derivative)

yph = y + h
out3 = forward_multiply_gate(x, yph)
y_derivative = (out3 - out) / h

print 'y\': ' + str(y_derivative)

step_size = 0.001
out = forward_multiply_gate(x, y)
x = x + step_size * x_derivative
y = y + step_size * y_derivative

out_new = forward_multiply_gate(x, y)
print 'new out: ' + str(out_new)
