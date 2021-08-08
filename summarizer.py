def get_individual_team(team, players):
    individual_team = []
    individual_player = []
    for i in range(len(team)):
        teams_1 = team[i]
        if teams_1 not in individual_team:
            individual_team.append(teams_1)
        teams_2 = players[i]
        if teams_2 not in individual_player:
            individual_player.append(teams_2)
    return individual_team


def display_scores(team, players, points, individual_team):
    team_1 = individual_team[0]
    team_2 = individual_team[1]
    team1_count = 0
    team2_count = 0
    for i in range(len(team)):
        if team[i] == team_1:
            team1_count += points[i]
        else:
            team2_count += points[i]
    if team1_count > team2_count:
        print(team_1, "won!")
    else:
        print(team_2, "won!")
    print(team_1, "scored", team1_count, "points.")
    print(team_2, "scored", team2_count, "points.")


def get_player_positions(team, players):
    player_scored_first = players[0]
    player_scored_last = players[len(team) - 1]
    print(player_scored_first, "scored first.")
    print(player_scored_last, "scored last.")


def load_points_file(team, players, points):
    file_name = input("enter gamelog file name:\n")
    points_file = open(file_name, 'r')
    for line in points_file:
        line_split = line.split(' ')
        team.append(line_split[0])
        players.append(line_split[1])
        points.append(int(line_split[2]))


def main():
    team = []
    players = []
    points = []
    load_points_file(team, players, points)
    individual_team = get_individual_team(team, players)
    display_scores(team, players, points, individual_team)
    get_player_positions(team, players)


main()
