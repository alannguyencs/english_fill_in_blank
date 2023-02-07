from constants import *

def read_text(filename):
    input = list(open(f"{DATA_PATH}{filename}.txt", 'r'))
    input = ' '.join(input)
    input = input.replace('\n', '').split(' ')
    input = [w for w in input if w != '']
    document, words = [], []
    # print ('input', input)
    for i in range(len(input)):
        words.append(input[i])

        if (i+1) % NUM_WORDS_PER_QUESTION == 0 or i == len(input) - 1:
            document.append(words)
            # print ('words:', words)
            words = []
    return document

def write_questions():
    document = read_text('input')
    question_file = open(f"{DATA_PATH}question.txt", 'w')
    for words in document:
        blank_id = random.randint(0, len(words) - 1)
        for wid in range(len(words)):
            if wid != blank_id:
                question_file.write(words[wid] + ' ')
            else:
                question_file.write('__________ ')
        question_file.write('\n\n')

def remove_punctuation(word):
    word_2_list = list(word)
    cleaned_list = [ch for ch in word_2_list if ch.isalpha() or ch.isdigit()]
    return ''.join(cleaned_list)

def is_similar(word_1, word_2):
    word_1 = remove_punctuation(word_1)
    word_2 = remove_punctuation(word_2)
    return word_1 == word_2

def show_result():
    document = read_text('input')
    answer = read_text('question')

    for words_gt, words_pred in zip(document, answer):
        for wid in range(len(words_gt)):
            if is_similar(words_gt[wid], words_pred[wid]):
                print (words_gt[wid], end = ' ')
            else:
                print (f'(  {words_pred[wid]} - {words_gt[wid]}  )', end = ' ')
        print ('')








