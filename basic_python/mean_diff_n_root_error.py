def md_nre(y, y_hat, n, p):
    m = len(y)
    result_loss = ((abs(y[i]**(1/n) - y_hat[i]**(1/n)))**p for i in range(m))
    return result_loss


if __name__ == '__main__':
    y = [100, 50, 20, 5.5, 1.0, 0.6]
    y_hat = [99.5, 49.5, 19.5, 5.0, 0.5, 0.1]
    n = 2
    p = 1
    result = md_nre(y, y_hat, n, p)
    print(list(result))

