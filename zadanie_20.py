# Lekcja 04 - Zadanie 20
# Python: składnia, typy i operatory

table = "patients"
columns = ["patient_id", "age", "diagnosis"]
min_age = 40
diagnoses = ["diabetes", "hypertension"]
sort = "age DESC"
limit = 100
column_sql = ", ".join(columns)
diagnosis_sql = "(" + ", ".join(f"'{value}'" for value in diagnoses) + ")"
query = f"""SELECT {column_sql}
FROM {table}
WHERE age > {min_age} AND diagnosis IN {diagnosis_sql}
ORDER BY {sort}
LIMIT {limit};"""
print(query)
# W produkcyjnym kodzie dane od użytkownika przekazuj jako parametry SQL.
