class FootballTeam:
    def __init__(self, squad):
        self.squad: dict = squad

    def __str__(self):
        return f"Skład string: {self.squad}"

    def __int__(self):
        count = 0
        for item in self.squad.values():
            count += len(item)
        return count

    def __bool__(self):
        return True

    def add_player_to_squad(self, player, position):
        self.squad[position].append(player)

    def get_player_from_squad(self, player):
        for key, value in self.squad.items():
            if player in value:
                return f"Zawodnik: {player} z pozycji {key}"
        return "Niestety, nie jest to zawodnik z naszego zespołu"

    # def __getitem__(self, item):
    #     for key, value in self.squad.items():
    #         if item in value:
    #             return f"Zawodnik: {item} z pozycji {key}"
    #     return "Niestety, nie jest to zawodnik z naszego zespołu"

    def __getitem__(self, item):
        for key, value in self.squad.items():
            if key == item:
                return value
        return None

    def __setitem__(self, key, value):
        self.squad[key].append(value)

    def __iter__(self):
        for postion, players_list in self.squad.items():
            for player in players_list:
                yield f"{postion}: {player}"



squad_dict = {
    "bramkarze": ["Wojciech Szczęsny", "Łukasz Fabiański"],
    "obroncy": ["Kamil Glik", "Łukasz Piszczek", "Jakub Wawrzyniak"],
    "pomocnicy": ["Kamil Grosicki", "Grzegorz Krychowiak", "Piotr Zieliński"],
    "napastnicy": ["Robert Lewandowski", "Arkadiusz Milik"]
}


polish_national_team = FootballTeam(squad=squad_dict)
print(polish_national_team)
string_polish_squad = str(polish_national_team)
print(string_polish_squad)
polish_squad_size = int(polish_national_team)
print(polish_squad_size)
polish_national_team.add_player_to_squad("Jacek Krzynówek", "pomocnicy")
print(polish_national_team)
print(polish_national_team.get_player_from_squad("Wojciech Szczęsny"))
print(polish_national_team.get_player_from_squad("Wojciech Skorupski"))
#print(polish_national_team["Kamil Glik"])
#print(polish_national_team["bramkarze"])
#print(polish_national_team.squad["bramkarze"]) - tutaj dzialanie niepożądane
polish_national_team["Łukasz Piszczek"]
polish_national_team["pomocnicy"] = "Jacek Góralski"
# print(polish_national_team)
# print(squad_dict["bramkarze"])
# squad_dict["bramkarze"] = "Kamil Grabara"
# print(squad_dict["bramkarze"])
for player in polish_national_team:
    print(player)
