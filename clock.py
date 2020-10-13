minut_count = int(input())
result_hours = (minut_count // 60) % 23
result_minut = minut_count % 60
print(result_hours, result_minut)
