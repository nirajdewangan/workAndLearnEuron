# ============================================================
# 5. NUMBER ANALYSIS TOOL
# No min(), max(), sum()
# ============================================================

def analyze_numbers(numbers):
    """Analyze a list without min(), max(), or sum()."""

    if len(numbers) == 0:
        return None

    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        total += number

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if number > 0:
            positive_count += 1

        elif number < 0:
            negative_count += 1

    average = total / len(numbers)

    return {
        "largest": largest,
        "smallest": smallest,
        "total": total,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count,
        "positive_count": positive_count,
        "negative_count": negative_count
    }


def number_analysis_tool():
    """Run Number Analysis Tool."""
    numbers = [10, -5, 20, 7, -3, 0, 18, 11]

    result = analyze_numbers(numbers)

    print("\n--- NUMBER ANALYSIS TOOL ---")
    print("Numbers:", numbers)

    for key, value in result.items():
        print(key, ":", value)


number_analysis_tool()