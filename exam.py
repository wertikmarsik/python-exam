from datetime import datetime

def convert_date(input_date, input_format, output_format):
    try:
        parsed_date = datetime.strptime(input_date, input_format)
        
        output_date = parsed_date.strftime(output_format)
        
        return output_date
    
    except ValueError as e:
        return f"Помилка: {e}"

input_date = input("Введіть дату: ")
input_format = '%d/%m/%Y'
output_format_1 = '%Y-%m-%d'
output_format_2 = '%m-%d-%Y'
output_format_3 = '%d-%m-%Y'

result_1 = convert_date(input_date, input_format, output_format_1)
result_2 = convert_date(input_date, input_format, output_format_2)
result_3 = convert_date(input_date, input_format, output_format_3)

print(result_1)
print(result_2)
print(result_3)
