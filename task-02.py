def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                cat_data = line.split(",")

                cat_info = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }

                cats_info.append(cat_info)

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

    return cats_info

if __name__ == "__main__":
    path = "cats_profiles.txt"

cats_info = get_cats_info(path)
print(cats_info)
