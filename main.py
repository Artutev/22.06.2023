#26
import re

def extract_domains(email_list):
    pattern = re.compile(r'@([a-zA-Z0-9.-]+)')
    domains = [pattern.search(email).group(1) for email in email_list if pattern.search(email)]
    return domains
email_addresses = ['user1@example.com', 'user2@gmail.com', 'user3@yahoo.com', 'invalid_email']
result = extract_domains(email_addresses)
print(result)


#NUMBER 2
import re

def extract_vowel_words(text):
    pattern = re.compile(r'\b[aeiouAEIOU][a-zA-Z]*\b')
    vowel_words = pattern.findall(text)
    return vowel_words
input_text = "Apple is a fruit, and orange is another fruit. Elephant is a large mammal."

result = extract_vowel_words(input_text)
print(result)


#NUMBER 3
import re

def split_string(input_string, separators):
    pattern = re.compile('|'.join(re.escape(separator) for separator in separators))
    result = pattern.split(input_string)
    result = [item for item in result if item]
    return result
input_string = "apple,orange;banana|grape"
separators = [',', ';', '|']
result = split_string(input_string, separators)
print(result)


#27
from collections import Counter

def determine_winner(votes):
    candidates = ["Аскаров", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов"]
    vote_count = Counter(votes)
    max_votes = max(vote_count.values())
    winners = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
    if len(winners) > 1:
        winners.sort(key=lambda x: len(x))
    print("Результаты голосования:")
    for candidate, votes in vote_count.items():
        print(f"{candidate}: {votes} голосов")
    print("\nПобедитель выборов:")
    print(winners[0])
    print(f"\nКоличество голосов победителя: {max_votes}")
votes = ["Ернур", "Аскаров", "Ернур", "Бекмуханов", "Ернур", "Пешая", "Карим", "Шаримазданов", "Ернур", "Бекмуханов"]
determine_winner(votes)
