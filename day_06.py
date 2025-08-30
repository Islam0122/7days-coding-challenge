"""
Categorize New Member --> 7kyu
"""
# def open_or_senior(data):
#     result = []
#     for age, handicap in data:
#         if age >= 55 and handicap > 7:
#             result.append("Senior")
#         else:
#             result.append("Open")
#     return result


"""
Detect Pangram --> 6kyu
"""
# import string
#
# def is_pangram(s: str) -> bool:
#     alphabet = set(string.ascii_lowercase)  # {'a', 'b', 'c', ..., 'z'}
#     return alphabet <= set(s.lower())
