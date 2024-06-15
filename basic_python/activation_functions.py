import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)

def activation_function(x, func_name):
    if not is_number(x):
        print('x must be a number')
        return

    if func_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{func_name} is not supported')
        return

    x = float(x)
    if func_name == 'sigmoid':
        result = sigmoid(x)
    elif func_name == 'relu':
        result = relu(x)
    elif func_name == 'elu':
        result = elu(x)

    print(f'{func_name}: f({x}) = {result}')


if __name__ == '__main__':
    activation_function(1.5, 'sigmoid')
    activation_function('abc', 'relu')
    activation_function(1.5, 'belu')
    activation_function(1.5, 'relu')
