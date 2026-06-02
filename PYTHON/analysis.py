import statistics

def analyze_data(data):

    
    if not data:
        print("No data available")
        return

    mean_value = statistics.mean(data)
    median_value = statistics.median(data)

    print(f"Data: {data}")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")


sales = [100, 200, 300, 400, 500]

analyze_data(sales)