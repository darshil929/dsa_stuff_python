# def find_min_element(arr):
#     min = 100000000
#     for i in range(len(arr)):
#         if arr[i] < min:
#             min = arr[i]
#     return min

def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    selection_sort(elements)
    print(f'sorted array: {elements}')

    print("-------------------------------------------------")

    print("Test Cases")

    tests = [
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        selection_sort(elements)
        print(f"sorted array: {elements}")