from django.shortcuts import render
from Player.models import Player
from Player.serializers import PlayerSerializer
import pandas as pd
import requests

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

# get player data
class Crawler(APIView):
    def get(self, request):
        try:
            print('----------------start Crawling---------------', flush=True)
            # get plg
            print('get plg')
            link = "https://pleagueofficial.com/stat-player"
            requestData = requests.get(link)
            df = pd.read_html(requestData.text)[0]
            print('rename')
            #rename columns in DataFrame using dictionary
            col_dict = {'球員': 'name',
                        '背號': 'jersey',
                        '球隊': 'team_name',
                        '出賽次數': 'gp',
                        '時間 (分)': 'seconds',
                        '兩分命中': 'two_m',
                        '兩分出手': 'two_a',
                        '兩分%': 'two_pct',
                        '三分命中': 'trey_m',
                        '三分出手': 'trey_a',
                        '三分%': 'trey_pct',
                        '罰球命中': 'ft_m',
                        '罰球出手': 'ft_a',
                        '罰球%': 'ft_pct',
                        '得分': 'points',
                        '攻板': 'reb_o',
                        '防板': 'reb_d',
                        '籃板': 'reb',
                        '助攻': 'ast',
                        '抄截': 'stl',
                        '阻攻': 'blk',
                        '失誤': 'turnover',
                        '犯規': 'pfoul',}
            df.rename(columns=col_dict, inplace=True)
            print('percent')
            # percent 要轉
            df['two_pct'] = df['two_pct'].str.rstrip("%").astype(float)/100
            df['trey_pct'] = df['trey_pct'].str.rstrip("%").astype(float)/100
            df['ft_pct'] = df['ft_pct'].str.rstrip("%").astype(float)/100
            df['league'] = "plg"
            print('save')
            # save
            dbframe = df
            for dbframe in dbframe.itertuples():
                check = Player.objects.filter(
                                    name=dbframe.name,
                                    jersey=dbframe.jersey,
                                    team_name=dbframe.team_name,
                                    league=dbframe.league,
                                    gp=dbframe.gp,
                                    seconds=dbframe.seconds,
                                    two_m=dbframe.two_m,
                                    two_a=dbframe.two_a,
                                    two_pct=dbframe.two_pct,
                                    trey_m=dbframe.trey_m,
                                    trey_a=dbframe.trey_a,
                                    trey_pct=dbframe.trey_pct,
                                    ft_m=dbframe.ft_m,
                                    ft_a=dbframe.ft_a,
                                    ft_pct=dbframe.ft_pct,
                                    points=dbframe.points,
                                    reb_o=dbframe.reb_o,
                                    reb_d=dbframe.reb_d,
                                    reb=dbframe.reb,
                                    ast=dbframe.ast,
                                    stl=dbframe.stl,
                                    blk=dbframe.blk,
                                    turnover=dbframe.turnover,
                                    pfoul=dbframe.pfoul,
                                    )
                if check.exists():
                    continue
                else:
                    updated_values = {
                                    "gp": dbframe.gp,
                                    "seconds": dbframe.seconds,
                                    "two_m": dbframe.two_m,
                                    "two_a": dbframe.two_a,
                                    "two_pct": dbframe.two_pct,
                                    "trey_m": dbframe.trey_m,
                                    "trey_a": dbframe.trey_a,
                                    "trey_pct": dbframe.trey_pct,
                                    "ft_m": dbframe.ft_m,
                                    "ft_a": dbframe.ft_a,
                                    "ft_pct": dbframe.ft_pct,
                                    "points": dbframe.points,
                                    "reb_o": dbframe.reb_o,
                                    "reb_d": dbframe.reb_d,
                                    "reb": dbframe.reb,
                                    "ast": dbframe.ast,
                                    "stl": dbframe.stl,
                                    "blk": dbframe.blk,
                                    "turnover": dbframe.turnover,
                                    "pfoul": dbframe.pfoul,
                                    }
                    Player.objects.update_or_create(
                        name=dbframe.name, jersey=dbframe.jersey,
                        team_name=dbframe.team_name,
                        league=dbframe.league,
                        defaults=updated_values
                    )
            # get T1
            print('get T1')
            url = "https://api.t1league.basketball/season/2/stages/7/rosters"
            requestData = requests.get(url)
            df = pd.DataFrame([player['average'] for player in requestData.json()])
            # seconds
            print('second')
            df['seconds'] = pd.to_datetime(df['seconds'], unit='s')
            df['seconds'] = df['seconds'].dt.strftime('%H:%M:%S')
            df['league'] = "T1"
            print('save')
            # save
            dbframe = df
            for dbframe in dbframe.itertuples():
                check = Player.objects.filter(
                                    name=dbframe.name_alt,
                                    jersey=dbframe.jersey,
                                    team_name=dbframe.team_name,
                                    league=dbframe.league,
                                    gp=dbframe.gp,
                                    seconds=dbframe.seconds,
                                    two_m=dbframe.two_m,
                                    two_a=dbframe.two_a,
                                    two_pct=dbframe.two_pct,
                                    trey_m=dbframe.trey_m,
                                    trey_a=dbframe.trey_a,
                                    trey_pct=dbframe.trey_pct,
                                    ft_m=dbframe.ft_m,
                                    ft_a=dbframe.ft_a,
                                    ft_pct=dbframe.ft_pct,
                                    points=dbframe.points,
                                    reb_o=dbframe.reb_o,
                                    reb_d=dbframe.reb_d,
                                    reb=dbframe.reb,
                                    ast=dbframe.ast,
                                    stl=dbframe.stl,
                                    blk=dbframe.blk,
                                    turnover=dbframe.turnover,
                                    pfoul=dbframe.pfoul,
                                    )
                if check.exists():
                    continue
                else:
                    updated_values = {
                                    "gp": dbframe.gp,
                                    "seconds": dbframe.seconds,
                                    "two_m": dbframe.two_m,
                                    "two_a": dbframe.two_a,
                                    "two_pct": dbframe.two_pct,
                                    "trey_m": dbframe.trey_m,
                                    "trey_a": dbframe.trey_a,
                                    "trey_pct": dbframe.trey_pct,
                                    "ft_m": dbframe.ft_m,
                                    "ft_a": dbframe.ft_a,
                                    "ft_pct": dbframe.ft_pct,
                                    "points": dbframe.points,
                                    "reb_o": dbframe.reb_o,
                                    "reb_d": dbframe.reb_d,
                                    "reb": dbframe.reb,
                                    "ast": dbframe.ast,
                                    "stl": dbframe.stl,
                                    "blk": dbframe.blk,
                                    "turnover": dbframe.turnover,
                                    "pfoul": dbframe.pfoul,
                                    }
                    Player.objects.update_or_create(
                        name=dbframe.name_alt, jersey=dbframe.jersey,
                        team_name=dbframe.team_name,
                        league=dbframe.league,
                        defaults=updated_values
                    )

            return Response(status=200)
        except Exception as err:
            return Response(str(err), status=400)

            