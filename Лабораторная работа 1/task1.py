numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len_numbers=len(numbers)
numbers.pop(4)
sum_numbers= sum(numbers)
av_numbers=sum_numbers/len_numbers
numbers[4] =av_numbers
numbers.insert(5,-44)
print("Измененный список:", numbers)

