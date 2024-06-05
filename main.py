import os
import threading
import re

def count_vowels(file_path):
    vowels = 'aeiou'
    count = 0
    with open(file_path, 'r') as file:
        content = file.read().lower()
        for char in content:
            if char in vowels:
                count += 1
    return count

def process_files():
    directory = os.path.dirname(os.path.abspath(__file__))
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    threads = []
    for file_name in txt_files:
        file_path = os.path.join(directory, file_name)
        thread = threading.Thread(target=lambda: print(f"{file_name}: {count_vowels(file_path)}"))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"txt fayllarning umumiy soni: {len(txt_files)} ta")

if __name__ == "__main__":
    process_files()