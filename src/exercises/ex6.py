from typing import Tuple
import matplotib.pyplot as plt
import pandas as pd

def fun_total_goals(data: pd.DataFrame) -> Tuple[int, int, int]:
  """
  La función calcula los goles totales locales, visitantes y globales
  Args:
  data(pd:DataFrame): dataset de partidos
  Returns:
  Tuple: Goles locales, Goles visitantes, Goles totales
  """
#sumamos todos los goles marcados por los equipos locales y visitantes
#cálculamos el total de goles
  home_goals=int(data["FTHG"].sum())
  away_goals=int(data["FTAG"].sum())
  total_goals=home_goals+away_goals
  
  return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    La función calcula los goles locales, visitantes y totales por equipo
    Args:
    data(pd.dataframe): dataset de partidos
    Returns:
    Tuple:
    1. pd.DataFrame: goles locales por equipo
    2. pd.DataFrame: goles visitantes por equipo
    3. pd.DataFrame: goles totales por equipo
    """
#agrupamos por equipo local y sumamos todos los goles marcados en casa
    home_goals_by_team=data.groupby("HomeTeam")["FTHG"].sum().to_frame()
    home_goals_by_team.columns=["home_goals"]

#agrupamos por equipo visitante y sumamos todos los goles marcados fuera de casa
    away_goals_by_team=data.groupby("AwayTeam")["FTAG"].sum().to_frame()
    away_goals_by_team.columns=["away_goals"]

#unimos los goles locales y visitantes de cada equipo
    total_goals_by_team=home_goals_by_team.join(away_goals_by_team,how="outer").fillna(0)

#sumamos los goles locales y visitantes para sara el total
    total_goals_by_team["total_goals"]=(total_goals_by_team["home_goals"]+total_goals_by_team["away_goals"])

#ordenamos los equipos de mayor a menor número de goles totales
    total_goals_by_team=total_goals_by_team.sort_values("total_goals",ascending=False)
    
  return home_goals_by_team, away_goals_by_team,total_goals_by_team


def fun_summary_1996_2025(
    df_total_poitns: pd.DataFrame,
    home_goals_by_team: pd.DataFrame, 
    away_goals_by_team: pd.DataFrame,
    total_goals_by_team: pd.DataFrame) -> pd.DataFrame:
      """
      La función crea un dataframe resumido con puntos y goles por equipo
      Args:
      df_total_points(pd.DataFrame): puntos totales por equipo
      home_goals_by_team(pd.DataFrame): goles de los locales
      away_goals_by_team(pd.DataFrame): goles de los visitantes
      total_goals_by_team(pd.dataframe): goles totales por equipo
      returns:
      pd.datafram: dataframe resumido.
      """
#utilizamos el nombre del equipo como índice para realizar las uniones
#unimos puntos, goles locales, visitatnes y totales en un único dataframe
      total_points_by_team=df_total_points.set_index("Team")
      summary_1996_2025=total_points_by_team.join(
          [home_goals_by_team,away_goals_by_team,total_goals_by_team["total_goals"]],
          how="outer").fillna(0)

#ordenamos el resumen por puntos totales de mayor a menor
      summary_1996_2025=summary_1996_2025.sort_values("TotalPoints",ascending=False)
      
      return summary_1996_2025

def podium(summary_1996_2025: pd.DataFrame) -> plt.Figure: 
  """
  La función representa la función de los tres primeros equipos por puntos.
  Args:
  summary_1996_2025(pd.dataframe):dataframe resumen
  """
#Seleccionamos los tres equipos con mas puntos
#guardamos los nombre de lo equipos en orden de podio
  top_3=summary_1996_2025.head(3)
  teams=[top_3.index[1],
         top_3.index[0],
         top_3.index[2]]

#guardamos los puntos de cada equipo
  points=[
      top_3.iloc[1]["TotalPoints"],
      top_3.iloc[0]["TotalPoints"],
      top_3.iloc[2]["TotalPoints"]]

#creamos la figura, las barras del podium y asiganamos un color a cada barra
#añdimos el nombre de cada equipo sobre su barra
  fig=plt.figure(figsize=(5,5))
  plt.bar([0,1,2],points,color=["gold","blue","coral"])
  plt.text(0,points[0],teams[0],ha="center",va="bottom")
  plt.text(1,points[1],teams[1],ha="center",va="bottom")
  plt.text(2,points[2],teams[2],ha="center",va="bottom")

#oculatamos los valores de los ejes, añadimos el título al gráfico
#mostramos la gráfica y llamamos a la función
  plt.xticks([])
  plt.yticks([])
  plt.title("Podium histórico 1995-2025")
  plt.tight_layout()

  return fig
