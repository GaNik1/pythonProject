
# # ДЗ12.7
# # Создать словарь с процентными ставками банков
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# # Ввести сумму для инвестирования
# money = int(input("Введите сумму которую инвестируете: \n"))
# # Выделить в список процентные ставки банков
# procent = list(per_cent.values())
# # Записать доход в каждом банке в переменные с округлением до целых
# bankTKB = round(procent[0]/100*money, 2)
# bankCKB = round(procent[1]/100*money, 2)
# bankVTB = round(procent[2]/100*money, 2)
# bankSBER = round(procent[3]/100*money, 2)
# # Создать список банков с возможными доходами
# deposit = [bankTKB, bankCKB, bankVTB, bankSBER]
# # Вывести в консоль список возможных доходов
# print("Возможный доход:", deposit)
# # Сформировать список доходов в каждом банке
# #max_deposit = max(deposit)
#
# # Сортируем список доходов в каждом банке по возрастанию
# deposit.sort()
# #показать максимальный доход
# #print("Максимальная сумма дохода по вкладу равна - ", max_deposit, 'рублей')
# print("Максимальная сумма дохода по вкладу равна - ", deposit[-1], 'рублей')