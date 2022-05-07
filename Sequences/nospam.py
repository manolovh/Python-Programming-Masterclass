menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))







# for meal in menu:
#     if "spam" in meal:
#
#         for ingredients in enumerate(meal):
#             if "spam" not in ingredients:
#                 print(ingredients)
#         print()


# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()

# printing item without 'spam'
# for meal in menu:
#     meal_spam = meal.copy()
#     while "spam" in meal_spam:
#         meal_spam.remove("spam")
#     print(meal_spam)
#
# print("-"*50)
# # 1st approach removing 'spam'
# for meal in menu:
#     while "spam" in meal:
#         meal.remove("spam")
#     print(meal)