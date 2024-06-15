def calculate_f1_score(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return

    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'Precision: {precision:.2f}')
    print(f'Recall: {recall:.2f}')
    print(f'F1-score: {f1_score:.2f}')


if __name__ == '__main__':
    calculate_f1_score(2, 3, 4)
    calculate_f1_score('a', 3, 4)
    calculate_f1_score(2, 'a', 4)
    calculate_f1_score(2, 3, 'a')
    calculate_f1_score(2, 3, 0)
