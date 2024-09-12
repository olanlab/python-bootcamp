# สร้างลิสต์ที่มีค่าทุกค่าคูณด้วย 2
numbers = [1, 2, 3, 4]
doubled = [n * 2 for n in numbers]

print(doubled)  # Output: [2, 4, 6, 8]


# สร้างเซ็ตจากลิสต์ที่มีค่าเป็นเลขยกกำลังสอง
numbers = [1, 2, 2, 3, 4]
squared_set = {n ** 2 for n in numbers}

print(squared_set)  # Output: {16, 1, 4, 9}


# สร้างดิกชันนารีจากลิสต์ของ tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
dictionary = {key: value * 2 for key, value in pairs}

print(dictionary)  # Output: {'a': 2, 'b': 4, 'c': 6}


# สร้างลิสต์ที่มีค่าเฉพาะเลขคู่
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)  # Output: [2, 4]
