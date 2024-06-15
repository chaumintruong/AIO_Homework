import random
import math

def mae(predictions, targets):
    return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)

def mse(predictions, targets):
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)

def rmse(predictions, targets):
    return math.sqrt(mse(predictions, targets))

def calculate_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    num_samples = int(num_samples)
    predictions = [random.uniform(0, 10) for _ in range(num_samples)]
    targets = [random.uniform(0, 10) for _ in range(num_samples)]

    if loss_name == 'MAE':
        loss = mae(predictions, targets)
    elif loss_name == 'MSE':
        loss = mse(predictions, targets)
    elif loss_name == 'RMSE':
        loss = rmse(predictions, targets)
    else:
        print(f'{loss_name} is not supported')
        return

    for i in range(num_samples):
        print(f'loss name: {loss_name}, sample: {i}, pred: {predictions[i]}, target: {targets[i]}, loss: {loss}')


if __name__ == '__main__':
    calculate_loss('5', 'RMSE')
    calculate_loss('aa', 'MSE')
