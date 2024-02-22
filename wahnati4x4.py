import matplotlib.pyplot as plt
import matplotlib.patches as patches

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def visualize_board(board, count):
    n = len(board)
    fig, ax = plt.subplots()
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)

    for i in range(n):
        for j in range(n):
            color = (0.9, 0.9, 0.9) if (i + j) % 2 == 0 else (0.5, 0.5, 0.5)
            ax.add_patch(patches.Rectangle((i, j), 1, 1, facecolor=color))

    for i in range(n):
        ax.text(i + 0.5, board[i] + 0.5, 'Q', fontsize=12, ha='center', va='center', color='red')

    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.grid(True)
    plt.title(f'Board {count}')
    plt.show()

def solve_queens(board, row, count):
    n = len(board)
    if row == n:
        visualize_board(board, count)
        return True

    found_solution = False

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            found_solution = solve_queens(board, row + 1, count) or found_solution
            board[row] = -1

    return found_solution

def count_solutions(board, row, count):
    global solutions_count
    n = len(board)

    if row == n:
        if count[0] < 5:  # Визуализируем только первые 5 решений
            visualize_board(board, count[0])
        count[0] += 1
        solutions_count += 1
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            count_solutions(board, row + 1, count)
            board[row] = -1

def solve_n_queens(n, k):
    global solutions_count
    solutions_count = 0

    if k is None:
        k = n  # Если количество ферзей не указано, принимаем его равным размерности доски

    if n < k:
        print("Количество ферзей не может быть больше размерности доски.")
        return

    board = [-1] * n
    count = [0]  # Используем список, чтобы передавать изменяемый объект (mutable)

    count_solutions(board, 0, count)

    if solutions_count == 0:
        print("Для доски {}x{} и {} ферзей нет решения.".format(n, n, k))
    else:
        print("Количество решений для доски {}x{} и {} ферзей: {}".format(n, n, k, solutions_count))

# Пример
n = int(input("Введите размерность доски (например, 8): "))
k_input = input("Введите количество ферзей (например, 8): ")

if k_input.strip():  # Проверяем, что ввод не является пустой строкой
    k = int(k_input)
    solve_n_queens(n, k)
else:
    solve_n_queens(n)
