import random as r

def create_list(numbers, zeros):
    """
    Creates a list of random numbers between 0 and 1000
    with an arbitrary length specified by the user.
    :param numbers: an empty list => the list of numbers
    :param zeros: a list full of zeros => an auxiliar list
    :return: the generated list
    """
    while True:
        try:
            print("Choose a length for your list: ")
            numbers.clear()
            zeros.clear()
            n = int(input(">>> "))
            if n > 0:
                for i in range(n):
                    numbers.append(r.randint(0, 1000))
                    zeros.append(0)
                print(f'Your list is: {numbers}.')
                return numbers
            else:
                print("Your list must have elements in it!")
        except ValueError:
            print('Choose a real length!')

def list_is_sorted(numbers):
    """
    Checks if the list is sorted
    :param numbers: the list
    :return: true if is sorted, otherwise false
    """
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            return False
    return True

def step_function():
    """
    Receives a step from the user and sets it
    to zero if the step is not a natural number
    (there is no need to modify the step for negative numbers)
    :return: the step chosen by the user
    """
    try:
        step = input("""Choose a step. You will see your list every step operations(till is sorted).
If you enter an invalid step it will be automatically changed to 0,
meaning that you will see only the sorted list.
>>> """).strip()
        step = int(step)
    except ValueError:
        step = 0
    return step

def permutation_sort(numbers, zeros, index, step, perfect_step):
    """
    Sorts the list using the permutation method
    :param numbers: the list to be sorted
    :param zeros: the permutations
    :param index: an auxiliar parameter to do the permutations
    :param step: counter for the steps
    :param perfect_step: the step chosen by the user
    :return:
    """
    if all(zeros):
        step[0] += 1
        if step[0] == perfect_step:
            step[0] = 0
            step[1] += 1
            print(f"{step[1]}. {zeros}")
        if list_is_sorted(zeros):
            print(f'Your sorted list: {zeros}.')
            return True

    for i in range(len(numbers)):
        if numbers[i] not in zeros:
            zeros[index] = numbers[i]
            if permutation_sort(numbers, zeros, index + 1, step, perfect_step):
                return True
            zeros[index] = 0

def interpolation_search(numbers, searched_value):
    """
    Interpolation search
    :param numbers: the list in which we search the element
    :param searched_value: the value chosen by the user to be searched
    :return: a positive value if it is or -1 if it isn't in the list
    """
    first = 0
    last = len(numbers) - 1
    while first <= last and numbers[first] <= searched_value <= numbers[last]:
        pos = first + (last - first) * (searched_value - numbers[first]) // (numbers[last] - numbers[first])
        if numbers[pos] == searched_value:
            return pos + 1
        if searched_value > numbers[pos]:
            first = pos + 1
        else:
            last = pos - 1
    return -1

def heapify(numbers, n, i, step, perfect_step):
    """
    The heapify method in heap sort
    (it finds the largest element between
    a parent and its children and sets it as the parent)
    :param numbers: the list(the heap)
    :param n: the length of the heap
    :param i: and index for the parent
    :param step: the step which the algorithm is in every moment
    :param perfect_step: the steps when to display the list
    :return:
    """
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and numbers[left] > numbers[parent] :
        parent = left
    if right < n and numbers[right] > numbers[parent]:
        parent = right

    if parent != i:
        numbers[i], numbers[parent] = numbers[parent], numbers[i]
        step[0] += 1
        if step[0] == perfect_step:
            step[0] = 0
            step[1] += 1
            print(f"{step[1]}. {numbers}")
        heapify(numbers, n, parent, step, perfect_step)

def heap_sort(numbers, step, perfect_step):
    """
    Heap sorting method
    :param numbers: the list to be sorted
    :param step: the step which the algorithm is in every moment
    :param perfect_step: the steps when to display the list
    :return: the sorted list
    """
    n = len(numbers)

    for i in range(n//2 - 1, -1, -1):
        heapify(numbers, n, i, step, perfect_step)

    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0, step, perfect_step)

    return numbers

def searching_algorithm(numbers):
    """
    Implements the searching method and handles potential errors
    :param numbers: the list where we search
    :return: a message for errors or if the elements is in the list
    """
    if len(numbers) > 0 and list_is_sorted(numbers):
        while True:
            try:
                search_value = int(input("Write a value: ").strip())
                exists = interpolation_search(numbers, search_value)
                if exists == -1:
                    print("Your element is not in the list.")
                else:
                    print(f"Your element is in the list.")
                break
            except ValueError:
                print("Write a real value!")
    else:
        print('You must have a non-empty sorted list before!')

def first_sorting_algorithm(numbers, zeros, step):
    """
    Implements the first sorting method and handles potential errors
    :param numbers: the list we have to sort
    :param zeros: an auxiliar list(in the end the sorted list)
    :param step: a list to remember the steps
    :return: the sorted list
    """
    if len(numbers) == 0:
        print("First create a list!")
        return []
    elif list_is_sorted(numbers):
        print(f'Your sorted list is {numbers}.')
        return numbers
    else:
        perfect_step = step_function()
        permutation_sort(numbers, zeros, 0, step, perfect_step)
        return zeros
  
def second_sorting_algorithm(numbers, step):
    """
    Implements the second sorting method and handles potential errors
    :param numbers: the list we have to sort
    :param step: a list to remember the steps
    :return: the sorted list
    """
    if len(numbers) == 0:
        print("First create a list!")
        return []
    elif list_is_sorted(numbers):
        print(f'Your sorted list is {numbers}.')
        return numbers
    else:
        perfect_step = step_function()
        numbers = heap_sort(numbers, step, perfect_step)
        print(f"Your sorted list is: {numbers}")
        return numbers

def main():
    numbers = []
    zeros= []
    step = [0, 0]

    print("""This program uses:
    -interpolation search
    -permutation sort(first sorting method)
    -heap sort(second sorting method)
    """)

    while True:
        print("""Menu:
    1.Type 1 to generate a random list of elements between 0 and 1000.
    2.Type 2 to search and element the list.
    3.Type 3 to sort the list using the first method.
    4.Type 4 to sort the list using the second method.
    5.Type exit to end the program.""")

        user = input('>>> ').strip()

        if user == '1':
            numbers = create_list(numbers, zeros)
        elif user == '2':
            searching_algorithm(numbers)
        elif user == '3':
            numbers = first_sorting_algorithm(numbers, zeros, step)
        elif user == '4':
            numbers = second_sorting_algorithm(numbers, step)
        elif user.lower() == 'exit':
            break
        else:
            print('Enter a real command!')

main()