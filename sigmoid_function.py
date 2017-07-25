import math

class Unit(object):
    def __init__(self, value, grad):
        self.value = value
        self.grad = grad

class MultiplyGate(object):
    def __init__(self):
        self.u0 = None
        self.u1 = None

    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value * u1.value, 0.0)
        return self.utop

    def backward(self):
        self.u0.grad += self.u1.value * self.utop.grad
        self.u1.grad += self.u0.value * self.utop.grad
        return self

class AddGate(object):
    def __init__(self):
        self.u0 = None
        self.u1 = None

    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value + u1.value, 0.0)
        return self.utop

    def backward(self):
        self.u0.grad += 1 * self.utop.grad
        self.u1.grad += 1 * self.utop.grad
        return self

class SigmoidGate(object):
    def __init__(self):
        self.u0 = None

    @staticmethod
    def sig(x):
        return 1 / (1 + math.exp(-x))

    def forward(self, u0):
        self.u0 = u0
        self.utop = Unit(self.sig(self.u0.value), 0.0)
        return self.utop

    def backward(self):
        s = self.sig(self.u0.value)
        self.u0.grad += ( s * (1 - s)) * self.utop.grad
        return self

# create input units
a = Unit(1.0, 0)
b = Unit(2.0, 0)
c = Unit(-3.0, 0)
x = Unit(-1.0, 0.0)
y = Unit(3.0, 0.0)

# create gates
mulg0 = MultiplyGate()
mulg1 = MultiplyGate()
addg0 = AddGate()
addg1 = AddGate()
sg0 = SigmoidGate()

# initialize
ax = None
by = None
axpby = None
axpbypc = None
s = None

def forward_neuron():
    global ax
    global by
    global axpby
    global axpbypc
    global s
    ax = mulg0.forward(a, x)
    print ax.value
    by = mulg1.forward(b, y)
    print by.value
    axpby = addg0.forward(ax, by)
    print axpby.value
    axpbypc = addg1.forward(axpby, c)
    print axpbypc.value
    s = sg0.forward(axpbypc)
    print 'circuit output: ' + str(s.value)

# do one forward pass
forward_neuron()

# backpropagate to compute gradients
s.grad = 1.0
sg0.backward()
addg1.backward()
addg0.backward()
mulg1.backward()
mulg0.backward()

print a.grad

# change inputs based on gradient
step_size = 0.01
a.value += step_size * a.grad
b.value += step_size * b.grad
c.value += step_size * c.grad
x.value += step_size * x.grad
y.value += step_size * y.grad

# another forward pass
forward_neuron()

#double check backpropagation by checking numerical gradient

def forward_circuit_fast(a, b, c, x, y):
    return 1 / (1 + math.exp(-(a*x + b*y +c)))

a = 1
b = 2
c = -3
x = -1
y = 3
h = 0.0001
a_grad = (forward_circuit_fast(a+h, b, c, x, y) - forward_circuit_fast(a, b, c, x, y))/h
b_grad = (forward_circuit_fast(a, b+h, c, x, y) - forward_circuit_fast(a, b, c, x, y))/h
c_grad = (forward_circuit_fast(a, b, c+h, x, y) - forward_circuit_fast(a, b, c, x, y))/h
x_grad = (forward_circuit_fast(a, b, c, x+h, y) - forward_circuit_fast(a, b, c, x, y))/h
y_grad = (forward_circuit_fast(a, b, c, x, y+h) - forward_circuit_fast(a, b, c, x, y))/h

print [a_grad, b_grad, c_grad, x_grad, y_grad]
