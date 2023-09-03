#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:29:19 2023

@author: hbasnight01
"""

import urllib.request
from urllib.error import HTTPError
import re
import random
import math


def decode(text):
    # print("Input:", text)
    text = text.replace("\\xc3\\x80", "A")
    text = text.replace("\\xc3\\x81", "A")
    text = text.replace("\\xc3\\x82", "A")
    text = text.replace("\\xc3\\x83", "A")
    text = text.replace("\\xc3\\x84", "A")
    text = text.replace("\\xc3\\x85", "A")
    text = text.replace("\\xc3\\x86", "A")
    text = text.replace("\\xc3\\x87", "C")
    text = text.replace("\\xc3\\x88", "E")
    text = text.replace("\\xc3\\x89", "E")
    text = text.replace("\\xc3\\x8a", "E")
    text = text.replace("\\xc3\\x8b", "E")
    text = text.replace("\\xc3\\x8c", "I")
    text = text.replace("\\xc3\\x8d", "I")
    text = text.replace("\\xc3\\x8e", "I")
    text = text.replace("\\xc3\\x8f", "I")
    text = text.replace("\\xc3\\x91", "N")
    text = text.replace("\\xc3\\x92", "O")
    text = text.replace("\\xc3\\x93", "O")
    text = text.replace("\\xc3\\x94", "O")
    text = text.replace("\\xc3\\x95", "O")
    text = text.replace("\\xc3\\x96", "O")
    text = text.replace("\\xc3\\x98", "O")
    text = text.replace("\\xc3\\x99", "U")
    text = text.replace("\\xc3\\x9a", "U")
    text = text.replace("\\xc3\\x9b", "U")
    text = text.replace("\\xc3\\x9c", "U")
    text = text.replace("\\xc3\\xa0", "a")
    text = text.replace("\\xc3\\xa1", "a")
    text = text.replace("\\xc3\\xa2", "a")
    text = text.replace("\\xc3\\xa3", "a")
    text = text.replace("\\xc3\\xa4", "a")
    text = text.replace("\\xc3\\xa5", "a")
    text = text.replace("\\xc3\\xa6", "a")
    text = text.replace("\\xc3\\xa7", "c")
    text = text.replace("\\xc3\\xa8", "e")
    text = text.replace("\\xc3\\xa9", "e")
    text = text.replace("\\xc3\\xaa", "e")
    text = text.replace("\\xc3\\xab", "e")
    text = text.replace("\\xc3\\xac", "i")
    text = text.replace("\\xc3\\xad", "i")
    text = text.replace("\\xc3\\xae", "i")
    text = text.replace("\\xc3\\xaf", "i")
    text = text.replace("\\xc3\\xb1", "n")
    text = text.replace("\\xc3\\xb2", "o")
    text = text.replace("\\xc3\\xb3", "o")
    text = text.replace("\\xc3\\xb4", "o")
    text = text.replace("\\xc3\\xb5", "o")
    text = text.replace("\\xc3\\xb6", "o")
    text = text.replace("\\xc3\\xb8", "o")
    text = text.replace("\\xc3\\xb9", "u")
    text = text.replace("\\xc3\\xba", "u")
    text = text.replace("\\xc3\\xbb", "u")
    text = text.replace("\\xc3\\xbc", "u")
    text = text.replace("\\xc3\\xbd", "y")
    text = text.replace("\\xc3\\xbf", "y")
    # print("Output:", text)
    return text


def print_grid(chosen_teams, chosen_players):
    
    longest_names_in_col = [3, 3, 3]
    name_lens = []
    for i in range(3):
        for j in range(3):
            name_lens.append(len(chosen_players[3 * i + j][0]) + len(chosen_players[3 * i + j][1]) + 1)
            if name_lens[-1] > longest_names_in_col[j]:
                longest_names_in_col[j] = name_lens[-1]

    print()
    print('        +--' + '-' * longest_names_in_col[0] + '--+--' + '-' * longest_names_in_col[1] + '--+--' + '-' * longest_names_in_col[2] + '--+')
    print('        |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('        |  ' + ' ' * math.floor((longest_names_in_col[0] - 3) / 2) + chosen_teams[0] + ' ' * math.ceil((longest_names_in_col[0] - 3) / 2) + '  |  '
                        + ' ' * math.floor((longest_names_in_col[1] - 3) / 2) + chosen_teams[1] + ' ' * math.ceil((longest_names_in_col[1] - 3) / 2) + '  |  '
                        + ' ' * math.floor((longest_names_in_col[2] - 3) / 2) + chosen_teams[2] + ' ' * math.ceil((longest_names_in_col[2] - 3) / 2) + '  |')
    print('        |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('+-------+--' + '-' * longest_names_in_col[0] + '--+--' + '-' * longest_names_in_col[1] + '--+--' + '-' * longest_names_in_col[2] + '--+')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('|  ' + chosen_teams[3] + '  |  ' + ' ' * math.floor((longest_names_in_col[0] - name_lens[0]) / 2) + chosen_players[0][0], chosen_players[0][1] + ' ' * math.ceil((longest_names_in_col[0] - name_lens[0]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[1] - name_lens[1]) / 2) + chosen_players[1][0], chosen_players[1][1] + ' ' * math.ceil((longest_names_in_col[1] - name_lens[1]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[2] - name_lens[2]) / 2) + chosen_players[2][0], chosen_players[2][1] + ' ' * math.ceil((longest_names_in_col[2] - name_lens[2]) / 2) + '  |')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('+-------+--' + '-' * longest_names_in_col[0] + '--+--' + '-' * longest_names_in_col[1] + '--+--' + '-' * longest_names_in_col[2] + '--+')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('|  ' + chosen_teams[4] + '  |  ' + ' ' * math.floor((longest_names_in_col[0] - name_lens[3]) / 2) + chosen_players[3][0], chosen_players[3][1] + ' ' * math.ceil((longest_names_in_col[0] - name_lens[3]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[1] - name_lens[4]) / 2) + chosen_players[4][0], chosen_players[4][1] + ' ' * math.ceil((longest_names_in_col[1] - name_lens[4]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[2] - name_lens[5]) / 2) + chosen_players[5][0], chosen_players[5][1] + ' ' * math.ceil((longest_names_in_col[2] - name_lens[5]) / 2) + '  |')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('+-------+--' + '-' * longest_names_in_col[0] + '--+--' + '-' * longest_names_in_col[1] + '--+--' + '-' * longest_names_in_col[2] + '--+')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('|  ' + chosen_teams[5] + '  |  ' + ' ' * math.floor((longest_names_in_col[0] - name_lens[6]) / 2) + chosen_players[6][0], chosen_players[6][1] + ' ' * math.ceil((longest_names_in_col[0] - name_lens[6]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[1] - name_lens[7]) / 2) + chosen_players[7][0], chosen_players[7][1] + ' ' * math.ceil((longest_names_in_col[1] - name_lens[7]) / 2) + '  |  '
                                            + ' ' * math.floor((longest_names_in_col[2] - name_lens[8]) / 2) + chosen_players[8][0], chosen_players[8][1] + ' ' * math.ceil((longest_names_in_col[2] - name_lens[8]) / 2) + '  |')
    print('|       |  ' + ' ' * longest_names_in_col[0] + '  |  ' + ' ' * longest_names_in_col[1] + '  |  ' + ' ' * longest_names_in_col[2] + '  |')
    print('+-------+--' + '-' * longest_names_in_col[0] + '--+--' + '-' * longest_names_in_col[1] + '--+--' + '-' * longest_names_in_col[2] + '--+')

    return


def guess(chosen_teams, chosen_players, solved, players_guessed, keep_going, all_teams):
    name = input("Enter the name of a baseball player. Type 'q' to quit: ")

    name = name.strip().split()
    
    if len(name) >= 2:
        
        l_first_char = name[1][0].lower()
        l_first_five = name[1].lower()
        f_first_two = name[0].replace('.', '').lower()
        
        if len(l_first_five) > 5:
            l_first_five = l_first_five[:5]
        
        if len(f_first_two) > 2:
            f_first_two = f_first_two[:2]
        
        url = 'https://www.baseball-reference.com/players/'
        url += l_first_char + '/' + l_first_five + f_first_two + '01.shtml'
        
        # print(url)
        try:
            urllib.request.urlopen(url)
        except HTTPError as err:
            print("Player not found.", end=' ')
            if err.code == 404:
                return True
            else:
                raise
        # print('Result code:', webUrl.getcode())

        webUrl = urllib.request.urlopen(url)
        data = webUrl.read()
        
        player_teams = set()
        temp_data = str(data).split("<title>")
        temp_name = temp_data[1].split()[0] + ' ' + temp_data[1].split()[1]
        player_name = decode(temp_name)
        # print('Found player:', player_name)

        if player_name != name[0] + ' ' + name[1]:
            player_name = False
        
        attempt = 1
        done = False

        while not done:
            while not player_name:
                attempt += 1
                url = url[:-7] + str(attempt) + '.shtml'
                try:
                    webUrl = urllib.request.urlopen(url)
                except HTTPError as err:
                    print("Incorrect.", end=' ')
                    if err.code == 404:
                        done = True
                        break
                    else:
                        raise
                if done:
                    break

                data = webUrl.read()
                player_teams = set()
                temp_data = str(data).split("<title>")
                temp_name = temp_data[1].split()[0] + ' ' + temp_data[1].split()[1]
                player_name = decode(temp_name)

            if done:
                break

            print('Trying:', url)

            # find the teams that they played for
            split_data = re.split("Uniforms:", str(data), len(data))
            # print(split_data[1])
            uniforms = split_data[1].split("\\n\\n")
            uniforms[1] = uniforms[1].replace("\\n", " ")
            uniforms[1] = uniforms[1].replace("*", "")
            # print(uniforms[1])
            tokens = uniforms[1].split()
            # print(tokens)
            add = False
            temp_team = ""
            for i in range(len(tokens)):
                if add:
                    if i == len(tokens) - 1:
                        temp_team += tokens[i]
                        if temp_team in teams.keys():
                            player_teams.add(all_teams[temp_team])
                        temp_team = ""
                    elif tokens[i] == "Number":
                        add = False
                        temp_team = temp_team.strip()
                        if temp_team in teams.keys():
                            player_teams.add(all_teams[temp_team])
                        temp_team = ""
                    else:
                        temp_team += tokens[i] + ' '
                if len(tokens[i]) == 9 and tokens[i][4] == '-':
                    add = True
            print(player_teams)

            correct_set = []
            for i in range(3):
                for j in range(3):
                    if not solved[3 * j + i]:
                        count = 0

                        for k in player_teams:
                            # print(k, chosen_teams[i], chosen_teams[3 + j])
                            if k == chosen_teams[i] or k == chosen_teams[3 + j] or \
                               (chosen_teams[i] == "MIA" and k == "FLA") or (chosen_teams[3 + j] == "MIA" and k == "FLA") or \
                               (chosen_teams[i] == "LAA" and k == "CAL") or (chosen_teams[3 + j] == "LAA" and k == "CAL"):
                                count += 1

                        if count >= 2:
                            correct_set.append((i, j))
                            '''
                            solved[3 * j + i] = True
                            chosen_players[3 * j + i] = name
                            print('Correct.', end=' ')
                            done = True
                            '''
            if url in players_guessed:
                print('This player was already guessed.', end=' ')
                return True
            if len(correct_set) > 1:
                print('Which space do you want to place this player in:')
                c = 1
                for i, j in correct_set:
                    print(str(c) + ': ' + chosen_teams[i], 'x', chosen_teams[3 + j])
                    c += 1
                choice = int(input())
                i, j = correct_set[choice - 1]
                solved[3 * j + i] = True
                chosen_players[3 * j + i] = name
                players_guessed.append(url)
                print('Correct.', end=' ')
                done = True
            elif len(correct_set) == 1:
                i, j = correct_set[0]
                solved[3 * j + i] = True
                chosen_players[3 * j + i] = name
                players_guessed.append(url)
                print('Correct.', end=' ')
                done = True


            player_name = []
        
    elif name[0] == "q":
        keep_going = False
        print('Exiting...')

    else:
        print('\n[Error] Expecting a first and a last name. Got', str(name) + '.')

    return keep_going


team_abbrevs = ['SFG', 'SDP', 'LAD', 'COL', 'ARI', 'LAA', 'SEA', 'HOU', 'OAK', 'TEX',
                'CHC', 'STL', 'MIL', 'PIT', 'CIN', 'KCR', 'CHW', 'CLE', 'DET', 'MIN',
                'WSN', 'MIA', 'NYM', 'PHI', 'ATL', 'BOS', 'NYY', 'TOR', 'TBR', 'BAL']

team_names = ['San Francisco Giants', 'San Diego Padres', 'Los Angeles Dodgers', 'Colorado Rockies', 'Arizona Diamondbacks',
              'Los Angeles Angels', 'Seattle Mariners', 'Houston Astros', "Oakland Athletics", 'Texas Rangers',
              'Chicago Cubs', 'St. Louis Cardinals', 'Milwaukee Brewers', 'Pittsburgh Pirates', 'Cincinnati Reds',
              'Kansas City Royals', 'Chicago White Sox', 'Cleveland Guardians', 'Detroit Tigers', 'Minnesota Twins',
              'Washington Nationals', 'Miami Marlins', 'New York Mets', 'Philadelphia Phillies', 'Atlanta Braves',
              'Boston Red Sox', 'New York Yankees', 'Toronto Blue Jays', 'Tampa Bay Rays', 'Baltimore Orioles']
    
teams = {}

answers = ["   " for i in range(9)]

for i in range(30):
    teams[team_names[i]] = team_abbrevs[i]

teams["Los Angeles Angels of Anaheim/Los Angeles Angels"] = "LAA"
teams["Los Angeles Angels/California Angels"] = "LAA"
teams["Los Angeles Angels of Anaheim"] = "LAA"
teams["California Angels"] = "LAA"
teams["Tampa Bay Devil Rays"] = "TBR"
teams["Florida Marlins"] = "MIA"
teams["Cleveland Indians/Cleveland Guardians"] = "CLE"
teams["Cleveland Indians"] = "CLE"

# print(teams)

grid_teams = []
ints_chosen = []

while len(ints_chosen) < 6:
    rand_int = random.randint(0, 29)
    if rand_int not in ints_chosen:
        ints_chosen.append(rand_int)

# print(ints_chosen)
for i in ints_chosen:
    grid_teams.append(team_abbrevs[i])

correct = [False for i in range(9)]
cont = True

guesses = []
while False in correct and cont:
    print_grid(grid_teams, answers)
    # print(answers)
    cont = guess(grid_teams, answers, correct, guesses, cont, teams)

if cont:
    print_grid(grid_teams, answers)
    print('Nice job!')
