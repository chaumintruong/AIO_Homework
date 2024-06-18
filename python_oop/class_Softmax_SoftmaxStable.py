import math


class Softmax:
    def __init__(self):
        # This method is intentionally left empty as no initialization is required for this class.
        pass

    def forward(self, x):
        exp_x = [math.exp(i) for i in x]
        sum_exp_x = sum(exp_x)
        return [round((i / sum_exp_x), 4) for i in exp_x]


class SoftmaxStable:
    def __init__(self):
        # This method is intentionally left empty as no initialization is required for this class.
        pass

    def forward(self, x):
        x_max = max(x)
        x_exp = [math.exp(i - x_max) for i in x]
        sum_x_exp = sum(x_exp)
        return [round((i / sum_x_exp), 4) for i in x_exp]


data = [1, 2, 3]
softmax = Softmax()
output = softmax.forward(data)
print(output)

softmax_stable = SoftmaxStable()
output_stable = softmax_stable.forward(data)
print(output_stable)
