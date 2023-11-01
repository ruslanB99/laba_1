
character=4
number_of_characters_per_line =  25
number_of_lines_per_page =50
number_of_pages_in_the_boks = 100
total=number_of_characters_per_line*number_of_lines_per_page*number_of_pages_in_the_boks*character
Information_capacity_of_the_floppy_disk_in_bytes= 1.44 * 1024 * 1024
number_of_books = int(Information_capacity_of_the_floppy_disk_in_bytes//total)
print("Количество книг, помещающихся на дискету:",number_of_books)