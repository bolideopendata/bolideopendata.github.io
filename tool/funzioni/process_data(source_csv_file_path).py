def process_data(source_csv_file_path)
    import csv
    with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile
        reader = csv.DictReader(csvfile, delimiter=',')
        data = [dict(x) for x in reader]
    return data
