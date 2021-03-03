from poke_type_answer import Pokeball
import poke_scrape
from poke_question import SetupQuiz

pokemon = poke_scrape.pokemon_scraping()

poke_bank = []

for poke in pokemon:
    poke_name = poke['name']
    poke_type = poke['type']
    new_poke = Pokeball(poke_name, poke_type)
    poke_bank.append(new_poke)

poke_quiz = SetupQuiz(poke_bank, 20)

while poke_quiz.still_has_question():
    poke_quiz.next_question()

print("You've completed the Poke Quiz!")
print(r"\o/ \o/ \o/ \o/ \o/ \o/ \o/ \o/\n")
if poke_quiz.score >= int(poke_quiz.question_number*0.6):
    print(f"You are a pokemon expert!\nYour final score was: {poke_quiz.score}/{poke_quiz.question_number}")
else:
    print(f"Your final score was: {poke_quiz.score}/{poke_quiz.question_number}")
    print("This was not a good result!\nIf you wanna win a serious battle, you have to study more about pokemon!")