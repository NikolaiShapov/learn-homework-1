"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(bd):
    all_product = 0
    for item_for_sale in bd:
        name_item = item_for_sale['product']
        summa = sum(item_for_sale['items_sold'])
        print(name_item, 'суммарное количество продаж:', summa)
        mean = summa/len(item_for_sale['items_sold'])
        print(name_item, 'среднее количество продаж:', int(round(mean, 0)))
        all_product += summa
    print('суммарное количество продаж всех товаров:', all_product)
    mean_all = int(round(all_product/len(item_for_sale['items_sold'])))
    print('среднее количество продаж всех товаров: ', mean_all)

if __name__ == "__main__":
    bd_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    main(bd_list)
