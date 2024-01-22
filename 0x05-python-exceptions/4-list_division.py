#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                result_list.append(0)
                print("wrong type")
            elif divisor == 0:
                result_list.append(0)
                print("division by 0")
            else:
                result = dividend / divisor
                result_list.append(result)
        except ZeroDivisionError:
            result_list.append(0)
            print("division by 0")
        except IndexError:
            result_list.append(0)
            print("out of range")
        finally:
            pass

    return result_list
