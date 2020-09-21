import constants

def welcome():

  print("""
  Enter 'Display Teams' to see a list of teams.
  Enter 'Help' to come back to this help menu.
  Enter 'Quit' to close this application.
  """)

  
def list_teams():

  my_teams = []
  for team in constants.TEAMS:
    my_teams.append(team)
  return my_teams


def team_selection(my_teams):

  for team in my_teams:
    print("{}".format(team))

  team = input("Please select a team by entering the team name to see the team's players.\n ").title()

  return team

  
def clean_player_stats():

  
  my_players = []
  for player in constants.PLAYERS:
    name=player['name']
    height=player['height']
    height = int(height[:2])
    experience=bool(player['experience'] == 'YES')
    guardians=player['guardians']
    
    my_players.append(name)   

  return my_players
 

def balance_teams(team, my_players, my_teams):
    
  
  teamroster1 = []
  teamroster2 =[]
  teamroster3 = []
  tracker = int(len(my_players)/len(my_teams))
  for player in my_players:
    if len(teamroster1) < tracker:
      teamroster1.append(player)
    elif len(teamroster2) < (tracker):
      teamroster2.append(player)
    else:
      teamroster3.append(player)
  
  roster1 = ", ".join(teamroster1)
  roster2 = ", ".join(teamroster2)
  roster3 = ", ".join(teamroster3)
  if team.title() == my_teams[0]:
    print("Team name :", my_teams[0], "\n" , " Number of players:",len(teamroster1), "\n" , " Team members:", roster1)
  elif team.title() == my_teams[1]:
    print("Team name :", my_teams[1], "\n" , " Number of players:",len(teamroster2), "\n" ,  " Team members:", roster2)
  elif team.title() == my_teams[2]:
    print("Team name :", my_teams[2], "\n" , " Number of players:",len(teamroster3), "\n" , " Team members:", roster3)
  else:
    print("Please select a valid team.")
  
if __name__ == '__main__':
    
    my_players = clean_player_stats()
    while True:
      welcome()
      new_selection = input("> ")
      new_selection = new_selection.title()
      if new_selection == 'Quit':
        break
      elif new_selection =='Help':
        welcome()
        continue
      elif new_selection =='Display Teams':
        my_teams = list_teams()
        team = team_selection(my_teams)
        balance_teams(team, my_players, my_teams)
        continue
