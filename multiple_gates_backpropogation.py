import random

def forward_multiply_gate(a, b):
    return a * b

def forward_add_gate(a, b):
    return a + b

x = -2
y = 5
z = -4

q = forward_add_gate(x, y)
f = forward_multiply_gate(q, z)

print 'forward_add_gate(initial): ' + str(q)
print 'forward_multiply_gate(initial): ' + str(f)

derivative_f_wrt_z = q
derivative_f_wrt_q = z

print 'derivative_f_wrt_z: ' + str(derivative_f_wrt_z)
print 'derivative_f_wrt_q: ' + str(derivative_f_wrt_q)

derivative_q_wrt_x = 1
derivative_q_wrt_y = 1

# chain rule
derivative_f_wrt_x = derivative_f_wrt_q * derivative_q_wrt_x
derivative_f_wrt_y = derivative_f_wrt_q * derivative_q_wrt_y

print 'derivative_f_wrt_x: ' + str(derivative_f_wrt_x)
print 'derivative_f_wrt_y: ' + str(derivative_f_wrt_y)

gradient_f_wrt_xyz = [derivative_f_wrt_x, derivative_f_wrt_y, derivative_f_wrt_z]
print 'gradient_f_wrt_xyz: ' + str(gradient_f_wrt_xyz)

step_size = 0.01
x += step_size * derivative_f_wrt_x
y += step_size * derivative_f_wrt_y
z += step_size * derivative_f_wrt_z

q = forward_add_gate(x, y)
f = forward_multiply_gate(q, z)

print 'forward_add_gate(final): ' + str(q)
print 'forward_multiply_gate(final): ' + str(f)
