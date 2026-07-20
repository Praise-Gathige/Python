## Creating and Modifying Sets
# Creating a set
magic_numbers = {3, 7, 12}

# Removing duplicates from a list using a set()
raw_data = [1, 1, 1, 2, 3, 3]
clean_data = set(raw_data)
print(clean_data) 

# Modifying a Set
clean_data.add(4)
clean_data.remove(2)
print(clean_data)


## Set Mathematics (The Real Superpower)
admins = {"Alice", "Bob", "Charlie"}
editors = {"Charlie", "David", "Eve"}

# 1. UNION (|): Combines both sets. (Who is and admin OR and editor?)
all_staff = admins | editors
# Output: {"Alice", "Bob", "Charlie", "David", "Eve"}

# 2. INTERSECTION (&): Combines both sets. (who is AND an editor)
super_users = admins & editors
# Output: {"Charlie"}

# 3. DIFFERENCE (-): Removes items found in the second set.
pure_admins = admins - editors
# Output: {"Alice", "Bob"}


## Standard Quest: The Spam Filter
print("")
raw_emails = ["a@mail.com", "b@mail.com", "c@mail.com", "b@mail.com"]
unique_emails = set(raw_emails)
print(len(unique_emails))
unique_emails.add("d.mail.com")
unique_emails.add("a@mail.com")
print(unique_emails)
print("")



## Weekly Boss Challenge: The Matchmaker Algorithm
person_a_interests = {"hiking", "reading", "coding", "movies"}
person_b_interests = {"coding", "cooking", "movies", "gaming"}

def calculate_match(set1, set2):
    shared_interests = set1 & set2
    total_unique_interests_between_both = set1 | set2

    match_percentage = (len(shared_interests) / len(total_unique_interests_between_both) * 100)

    return match_percentage


compatibility = calculate_match(person_a_interests, person_b_interests)
print(f"Compatibility Percentage: {compatibility}%")