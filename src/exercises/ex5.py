import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
  """
  La función añade los puntos obtenido por locales y visitantes.

  Args:
  data(pd:DataFrame): dataset de partidos.
  Returns:
  pd.DataFrame: dataset con las columnas poitns_home y points_away
  """

  #copiamos del dataset para no modificar el original.
  #asigamos los puntos al equipo local y al visitante
  data=data.copy()
  data["points_home"]=data["FTR"].map({"H":3,"D":1,"A":0})
  data["points_away"]=data["FTR"].map({"H":0,"D":1,"A":3})
  return data

def  fun_total_points(data: pd.DataFrame) -> pd.DataFrame:
  """
  La función calcula los puntos acumulados por cada equipo.
  Args:
  data(pd.DataFrame): dataset con puntos
  Returns:
  pd.DataFrame): clasificación histórica por puntos
  """

#sumamos los puntos obtenidos como local
#sumamos los puntos obtenidos como visitante
  home_points=data.groupby("HomeTeam")["points_home"].sum()
  away_points=data.groupby("AwayTeam")["points_away"].sum()

#sumamos ambas cantidades y convertimos el resultado en dataframe
  total_points=home_points.add(away_points,fill_value=0)
  df_total_points=total_points.reset_index()

#renombramos las columnas y las ordenamos de mayor a menor puntuación
  df_total_points.columns=["Team","TotalPoints"]
  df_total_points=df_total_points.sort_values("TotalPoints",ascending=False)
  return df_total_points


def alltime_winner(df_total_points: pd.DataFrame) -> pd.DataFrame:
  """
  La función devuelve el equipo con más puntos acumulados
  Args:
  df_total_points(pd:dataFrame): clasificación histórica
  Returns:
  pd.DataFrame: equipo ganador
  """
  return df_total_points.head(1)

