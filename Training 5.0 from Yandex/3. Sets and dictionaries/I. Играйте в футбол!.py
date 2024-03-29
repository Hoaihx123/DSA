import sys
import re
teams = {}
players = {}
def check_player(player, goal_time, team):
    if player not in players:
        players[player] = {'team': team, 'total_goals': 1, 'goal_time': {goal_time: 1}, 'start_goal': 0}
        teams[team]['players_of_team'].add(player)
    else:
        players[player]['total_goals'] += 1
        if goal_time in players[player]['goal_time']:
            players[player]['goal_time'][goal_time] += 1
        else:
            players[player]['goal_time'][goal_time] = 1


lines = sys.stdin.readlines()
i = 0
while i < len(lines):
    line = lines[i]
    data = re.match(r'\"(.+?)\" - \"(.+?)\" (\d+):(\d+)', line)
    if data:
        team_1 = data.group(1)
        team_2 = data.group(2)
        goals_1 = int(data.group(3))
        goals_2 = int(data.group(4))
        if team_1 in teams:
            teams[team_1]['matches'] += 1
            teams[team_1]['goals'] += goals_1
        else:
            teams[team_1] = {'players_of_team': set(), 'matches': 1, 'goals': goals_1, 'start_goals': 0}
        if team_2 in teams:
            teams[team_2]['matches'] += 1
            teams[team_2]['goals'] += goals_2
        else:
            teams[team_2] = {'players_of_team': set(), 'matches': 1, 'goals': goals_2, 'start_goals': 0}
        start_goal = ['', 100]
        for j in range(goals_1):
            i += 1
            line = lines[i]
            resul = re.match(r"(.+?) (\d+)'", line)
            player = resul.group(1)
            goal_time = int(resul.group(2))
            if goal_time < start_goal[1]:
                start_goal[1] = goal_time
                start_goal[0] = player
            check_player(player, goal_time, team_1)
        for j in range(goals_2):
            i += 1
            line = lines[i]
            resul = re.match(r"(.+?) (\d+)'", line)
            player = resul.group(1)
            goal_time = int(resul.group(2))
            if goal_time < start_goal[1]:
                start_goal[1] = goal_time
                start_goal[0] = player
            check_player(player, goal_time, team_2)
        if start_goal[1] != 100:
            players[start_goal[0]]['start_goal'] += 1
            teams[players[start_goal[0]]['team']]['start_goals'] += 1
    else:
        data = re.match(r'Total goals for "(.+?)"', line)
        if data:
            team_name = data.group(1)
            if team_name not in teams:
                print(0)
            else:
                print(teams[team_name]['goals'])
            i += 1
            continue
        data = re.match(r'Mean goals per game for "(.+?)"', line)
        if data:
            team_name = data.group(1)
            print(teams[team_name]['goals']/teams[team_name]['matches'])
            i += 1
            continue
        data = re.match(r'Total goals by (.+)', line)
        if data:
            player_name = data.group(1)
            if player_name not in players:
                print(0)
            else:
                print(players[player_name]['total_goals'])
            i += 1
            continue
        data = re.match(r"Mean goals per game by (.+)", line)
        if data:
            player_name = data.group(1)
            team_name = players[player_name]['team']
            print(players[player_name]['total_goals']/teams[team_name]['matches'])
            i += 1
            continue
        data = re.match(r'Goals on minute (\d+) by (.+)', line)
        if data:
            goal_time = int(data.group(1))
            player_name = data.group(2)
            if player_name not in players:
                print(0)
            else:
                if goal_time not in players[player_name]['goal_time']:
                    print(0)
                else:
                    print(players[player_name]['goal_time'][goal_time])
            i += 1
            continue
        data = re.match(r'Goals on first (\d+) minutes by (.+)', line)
        if data:
            player_name = data.group(2)
            first_time = int(data.group(1))
            if player_name not in players:
                print(0)
            else:
                total = 0
                for m in range(first_time+1):
                    if m in players[player_name]['goal_time']:
                        total += players[player_name]['goal_time'][m]
                print(total)
            i += 1
            continue
        data = re.match(r'Goals on last (\d+) minutes by (.+)', line)
        if data:
            player_name = data.group(2)
            last_time = int(data.group(1))
            if player_name not in players:
                print(0)
            else:
                total = 0
                for m in range(91-last_time, 91):
                    if m in players[player_name]['goal_time']:
                        total += players[player_name]['goal_time'][m]
                print(total)
            i += 1
            continue
        data = re.match(r'Score opens by "(.+?)"', line)
        if data:
            team_name = data.group(1)
            if team_name not in teams:
                print(0)
            else:
                print(teams[team_name]['start_goals'])
            i += 1
            continue
        data = re.match(r'Score opens by (.+)', line)
        if data:
            player_name = data.group(1)
            if player_name not in players:
                print(0)
            else:
                print(players[player_name]['start_goal'])
    i += 1


