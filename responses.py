import random
from tinydb import TinyDB, Query


db = TinyDB('db.json')
User = Query()


def get_response(message: str, author: str) -> str:
    p_message = message.lower()
    prefix = '!'
    playerDict = {}
    if db.contains(User.user==author):
        playerDict = db.get(User.user==author)

    if p_message == '!create':
        if db.contains(User.user==author):
            return "User Already Exists."
        else:
            db.insert({'user': author,'wins': 0,'draws': 0, 'games': 0 })
            return "User entry: " + author + " has been generated." 

    if p_message == '!stats':
        if db.contains(User.user==author):
            if playerDict['games'] == 0:
                return "You have played 0 games and therefore have no stats to show for :/"
            else:
                winrate = round(playerDict['wins']/playerDict['games'] * 100, 2)
                return "With {} games including the {} draw(s), you have a winrate of {}%!".format(playerDict['games'], playerDict['draws'], winrate)
        else:
            return "User does not exist, please create one using **!create**."

    if p_message.startswith('!play '):
        if db.contains(User.user==author):
            p_message = p_message[6:].lower()
            moves = ['rock', 'paper', 'scissors']
            computerMove = ""
            randomInt = random.randint(1,3)
            

            if p_message not in moves:
                return "Please select a valid move!"

            if randomInt == 1:
                computerMove = "rock"
            elif randomInt == 2:
                computerMove = "paper"
            else:
                computerMove = "scissors"

            print(computerMove)
            if(p_message == computerMove):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                db.update({'draws': playerDict['draws'] + 1}, User.user == author)
                return "DRAW!!"
            elif(p_message == 'rock' and computerMove == 'paper'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                return "YOU LOSE!!"
            elif(p_message == 'paper' and computerMove == 'scissors'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                return "YOU LOSE!!"
            elif(p_message == 'scissors' and computerMove == 'rock'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                return "YOU LOSE!!"
            elif(p_message == 'rock' and computerMove == 'scissors'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                db.update({'wins': playerDict['wins'] + 1}, User.user == author)
                return "YOU WIN!!"
            elif(p_message == 'paper' and computerMove == 'rock'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                db.update({'wins': playerDict['wins'] + 1}, User.user == author)
                return "YOU WIN!!"
            elif(p_message == 'scissors' and computerMove == 'paper'):
                db.update({'games': playerDict['games'] + 1}, User.user == author)
                db.update({'wins': playerDict['wins'] + 1}, User.user == author)
                return "YOU WIN!!"
            else:
                return "tests"
        else:
            return "User does not exist, please create one using **!create**."

    if p_message == '!help':
        return "`Commands include !create |  !stats | !play [your move] | private [command]`"
    if p_message.startswith(prefix):
        return "Sorry I do not know that command. Please refer to **!help** for help."



