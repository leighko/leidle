from random import randint


# Read in complete word file and write only five letter words to a new word file.
def read_and_write_word_files():
    with open("old_wordies.txt", "r") as read_file, open("five_letter_words.txt", "w") as write_file:
        for word in read_file:
            if len(word) == 6 and word.islower():
                write_file.write(word)


# Read in five letter word file and create word list.
def gen_word_list() -> list:
    read_and_write_word_files()
    with open("five_letter_words.txt", "r") as file:
        words = []
        for line in file:
            words.append(line.strip())
        return words
        

def main():
    word_list = gen_word_list() # generating the word list
    answer = generate_answer(word_list) # generating the answer from the word list
    print(answer) # printing the answer
    game_playing(answer, word_list) # running the game, getting user to guess the answer
    

# Loop to run game
# TO DO: Rework this. Much too long for one function.
def game_playing(answer: str, words: list) -> None:
    counter = 0
    guesses = []
    compare_list = []
    letters_list = []

    print("You have a total of 6 guesses to guess the five-letter word.\n")

    game_is_running = True
    while game_is_running:
        
        user_guess = get_guess()
        validity = check_valid_guess(user_guess, words)
        if validity:
            correctness = check_guess_correct(user_guess, answer)
            guesses.append(user_guess)

            compare = which_letters_are_right(user_guess, answer)
            if compare is not None and compare not in compare_list:
                compare_list.append(compare)
            
            letters = right_letters_wrong_position(user_guess, answer)
            if letters is not None:
                for letter in letters:
                    if letter not in letters_list:
                        letters_list.append(letter)
                    else:
                        pass

            if correctness:
                print(f"\nYOU WIN!! The word was: {answer}")
                print(f"Word guessed in: {counter+1}")
                game_is_running = False
            else:
                print(f"\n    Your valid guesses: {guesses}")
                print(f"    Correct letters, correct placement: {compare_list}")
                print(f"    Correct letters, wrong placement: {letters_list}\n")
            
                counter += 1
                game_is_running = check_game_over_count(counter, answer)
                
        else:
            pass


# Check for game over via the counter (greater than 6 valid attempts)
def check_game_over_count(count: int, answer: str) -> bool:
    if count >= 6:
        print("\nYou ran out of guesses :-(")
        print(f"Better luck next time! The word was: {answer}")
        return False
    return True


# Pick the word out of the words list.
def generate_answer(words: list) -> str:
    index = randint(0, len(words)-1)
    return words[index]


# User guesses a word.
def get_guess() -> str:
    guess = input("Guess a five letter word: ").lower()
    return guess


# Check that guess is valid and in word list.
def check_valid_guess(user_guess: str, words: list) -> bool:
    if len(user_guess) != 5 or user_guess not in words:
        print("Invalid guess. Please try again.")
        return False
    return len(user_guess) == 5


# Check if guess is correct.
def check_guess_correct(user_guess: str, answer: str) -> bool:
    return user_guess == answer


def which_letters_are_right(user_guess: str, answer: str) -> str:
    compare = ""

    for i in range(len(user_guess)):
        if user_guess[i] == answer[i]:
            compare += user_guess[i]
        else:
            compare += "_"

    if compare != "_____":
        return compare
    

def right_letters_wrong_position(user_guess: str, answer: str) -> str:
    letters = ""
    
    for i in range(len(user_guess)):
        if user_guess[i] in answer and user_guess[i] != answer[i]:
            letters += user_guess[i]
    if letters != "":
        return letters


if __name__ == "__main__":
    main()
