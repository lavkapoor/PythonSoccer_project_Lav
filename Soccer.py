class Team:
    def __init__(self,name):
        self.name=name
        self.games_won=0
        self.games_lost=0
        self.games_drawn=0
        self.goals_scored=0
        self.goals_conceded=0

    def get_gamesplayed(self):
        return self.games_won + self.games_lost + self.games_drawn

    def get_points(self):
        points=(self.games_won*3) + (self.games_drawn*1)
        return points

    def get_goaldifference(self):
        return self.goals_scored - self.goals_conceded
    def __repr__(self):
        return f"Team({self.name}) - Wins: {self.games_won}, Losses: {self.games_lost}, Draws: {self.games_drawn}, Goals Scored: {self.goals_scored}, Goals Conceded: {self.goals_conceded}"


    def Play(self,opponent,goalsscored,goalsconceded):
        self.goals_scored+=goalsscored
        self.goals_conceded+=goalsconceded
        opponent.goals_scored+=goalsconceded
        opponent.goals_conceded+=goalsscored

        if goalsscored > goalsconceded:
            self.games_won+=1
            opponent.games_lost+=1
        elif goalsscored < goalsconceded:
            self.games_lost+=1
            opponent.games_won+=1
        else:
            self.games_drawn+=1
            opponent.games_drawn+=1
class competition:
    def __init__(self):
        self.teams=[]
    def add_team(self,team):
        if team not in self.teams:
         self.teams.append(team)
    def get_team_by_name(self,name):
        for team in self.teams:
            if team.name==name:
                return team
        return None
    def update_competion(self,results):    
        if isinstance(results, tuple):
            results = [results]

        for item in results:
            if not (isinstance(item, tuple) and len(item) == 4):
                raise ValueError(f"Onjuist wedstrijdresultaat-formaat: {item}")

            team_a, team_b, score_a, score_b = item
            team_a.Play(team_b, score_a, score_b)
    
   
    def display_table(self):
        rows=""
        header=f"{'Team':<20}| {'Played':<10}| {'Won':<10}| {'Drawn':<10}| {'Lost':<10}| {'GF':<10}| {'GA':<10}| {'GD':<10}| {'Points':<10}\n"
        rows+=header
        for team in self.teams:
            rows+=f"{team.name:<20}| {team.get_gamesplayed():<10}| {team.games_won:<10}| {team.games_drawn:<10}| {team.games_lost:<10}| {team.goals_scored:<10}| {team.goals_conceded:<10}| {team.get_goaldifference():<10}| {team.get_points():<10}\n"
        print(rows)
    
    def write_table(self,outputfile):
        rows=""
        header=f"{'Team':<20}| {'Played':<10}| {'Won':<10}| {'Drawn':<10}| {'Lost':<10}| {'GF':<10}| {'GA':<10}| {'GD':<10}| {'Points':<10}\n"
        rows+=header
        for team in self.teams:
            rows+=f"{team.name:<20}| {team.get_gamesplayed():<10}| {team.games_won:<10}| {team.games_drawn:<10}| {team.games_lost:<10}| {team.goals_scored:<10}| {team.goals_conceded:<10}| {team.get_goaldifference():<10}| {team.get_points():<10}\n"
        with open(outputfile,'w',encoding="utf-8") as f:
          f.write(rows)
   
    def read_match_data_file(self,filename):
        lists=[]
        tuples=tuple()
        with open(filename,'r',encoding="utf-8") as file:
            lines=file.readlines()
        for line in lines:
            line=line.strip()
            parts = line.split(':',1)
            left1=parts[0].strip()
            right1=parts[1].strip()

            teams=left1.split('-')
            team_a_name=teams[0].strip()
            team_b_name=teams[1].strip()
            scores=right1.split('-')
            score_a=scores[0].strip()
            score_b=scores[1].strip()

            tuples=(team_a_name,team_b_name,score_a,score_b)
            lists.append(tuples)
        return lists
    def process_match_data(self,inputfile,outputfile):
        match_data=self.read_match_data_file(inputfile)
        for match in match_data:
            team_a_name,team_b_name,score_a,score_b=match
            team_a=self.get_team_by_name(team_a_name)
            team_b=self.get_team_by_name(team_b_name)
            if team_a is None:
                team_a=Team(team_a_name)
                self.add_team(team_a)
            if team_b is None:
                team_b=Team(team_b_name)
                self.add_team(team_b)
            team_a.Play(team_b,int(score_a),int(score_b))
        self.write_table(outputfile)

    
# main function 
ucl=competition()
ucl.process_match_data(r"match_data.txt","ranking.txt")

