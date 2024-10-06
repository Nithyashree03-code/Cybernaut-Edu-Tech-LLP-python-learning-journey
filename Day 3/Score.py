test_scores = [85, 90, 78, 92, 88]
average_score = sum(test_scores) / len(test_scores)
print(f"Initial average score: {average_score:.2f}")
new_score = float(input("Enter a new test score to add: "))
test_scores.append(new_score)
updated_average_score = sum(test_scores) / len(test_scores)
print(f"Updated average score: {updated_average_score:.2f}")
