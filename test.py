import random


def main():
    # get user inputs for number of questions and title of test
    num_of_questions = int(input('\nHow many questions should the test have? '))
    test_title = input('What should the test title be? ')
    operator = input('What arithmetic operator will be used in this test: +, -, x, /: ')
    digit_number = input('How many digits should be in the questions? single, double, triple: ')

    
    # call write_title function
    write_title(test_title)

    # init a correct_answer list to store all correct answers to the random questions
    correct_answer_list = []

    # loop based on the number of questions, creating the numbers and printing the question through each iteration
    for question in range(1, num_of_questions + 1):
        num_1, num_2 = create_random_numbers(digit_number)
        write_question(question, test_title, num_1, num_2, operator)
        correct_answer = get_correct_answer(num_1, num_2, operator)
        correct_answer_list.append(correct_answer)

    print('\n***', test_title, 'is ready and is in your tests folder.***')

    ready_for_answers = input('After the test is taken, save your answers and press enter here to submit your answers: ')
    
    if ready_for_answers == '':
        try:
            answers = read_test_answers(test_title)
            check_answers(answers, correct_answer_list, test_title)
            print('\n***Go back to the test to see your results!***')
        except ValueError:
            print('ERROR! Make sure you entered answers for each question.')


def create_random_numbers(user_digit_choice):
    if user_digit_choice == 'single':
        high_digit = 10
    elif user_digit_choice == 'double':
        high_digit = 100
    else:
        high_digit = 1000

    num_1 = random.randint(1, high_digit)
    num_2 = random.randint(1, high_digit)
    return num_1, num_2


def write_title(test_title):
    test = open(test_title + '.txt', 'w')
    test.write('                                                  ')
    test.write(test_title)
    test.write('\n')
    test.close()


def write_question(question_number, test_title, num_1, num_2, operator):
    test = open(test_title + '.txt', 'a')
    test.write(str(question_number) + '.')
    test.write(' ' + str(num_1) + ' ')
    test.write(operator + ' ' + str(num_2))
    test.write('=\n')
    test.write('\n')


def get_correct_answer(num_1, num_2, operator):
    if operator == '+':
        return num_1 + num_2
    elif operator == '-':
        return num_1 - num_2
    elif operator == 'x' or operator == 'X':
        return num_1 * num_2
    else:
        return num_1 / num_2


def read_test_answers(test_title):
    test = open(test_title + '.txt', 'r')
    answer_list = []
    for line in test:
        if line != '\n' and test_title not in line:
            line = line.rstrip()
            string_answer = line.partition("=")[2]
            num_answer = int(string_answer)
            answer_list.append(num_answer)
    return answer_list


def write_results(test_title, message):
    test = open(test_title + '.txt', 'a')
    test.write('\n')
    test.write(message)
    test.close()


def check_answers(arr_1, arr_2, test_title):
    is_correct_list = []
    list_length = len(arr_1)
    index = 0
    for i in range(list_length):
        if arr_1[index] == arr_2[index]:
            is_correct_list.append(True)
        else:
            is_correct_list.append(False)
        index += 1

    if all(is_correct_list):
        write_results(test_title, 'Way to go! You got them all right!')
    else:
        for i, value in enumerate(is_correct_list, 1):
            if not value:
                write_results(test_title, 'You got question #' + str(i) + ' wrong.')


main()
