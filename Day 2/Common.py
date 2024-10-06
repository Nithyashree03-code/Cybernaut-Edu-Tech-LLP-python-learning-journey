set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())
common_elements = set1.intersection(set2)
if common_elements:
    print(f"Common elements: {common_elements}")
else:
    print("No common elements.")
