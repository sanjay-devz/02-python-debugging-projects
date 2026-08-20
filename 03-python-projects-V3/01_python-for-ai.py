
def new_function(new_argument):
    def new_warper(new_banana):
        result = new_argument(new_banana).upper()
        return result
    return new_warper


@new_function
def game(games):
    return games

print(game("hello"))


@new_function
def new_game(hello):
    return hello

print(new_game("hello world"))


