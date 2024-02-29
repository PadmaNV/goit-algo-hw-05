def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    
    while left <= right:
        mid = left + (right - left) // 2
        iterations += 1
        
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return iterations, arr[mid]
    
    # Якщо елемент не знайдено, повертаємо верхню межу
    if right < 0:
        return iterations, arr[0]
    elif left >= len(arr):
        return iterations, arr[-1]
    else:
        return iterations, arr[left]

# Приклад:
arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
target = 3.5
iterations, upper_bound = binary_search(arr, target)
print(f"Кількість ітерацій: {iterations} Верхня межа: {upper_bound}")

target = 6.0
iterations, upper_bound = binary_search(arr, target)
print(f"Кількість ітерацій: {iterations} Верхня межа: {upper_bound}")

