def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0
        return total, average
    
    except FileNotFoundError:
        return "Файл не знайдено!"
    except ValueError:
        return "Файл містить некоректні дані!"
    except Exception as e:
        return f"Виникла помилка: {e}"

if __name__ == "__main__":
    path = "salaries.txt"

    total, average = total_salary(path)

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")