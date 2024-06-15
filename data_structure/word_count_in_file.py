def count_words(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count


if __name__ == "__main__":
    file_path = 'C:\\Users\ADMIN\Documents\AIO_Homework\data_structure\P1_data.txt'
    result = count_words(file_path)
    print(result)
