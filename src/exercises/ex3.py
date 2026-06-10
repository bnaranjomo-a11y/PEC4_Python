from typing import Tuple
import matplotlib.pyplot as plt
import pandas as pd
def goals_distribution(data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
  """
  Calcula la distribucón de goles locales y visitantes.
  Args:
    data(pd.DataFrame): dataset de partidos.
  Returns:
  tuples:
  1. dataframe distr_goals_home
  2. distr_goals_away
  """
#calculamos la distribución de goles marcados por los equipos locales
  distr_goals_home=data["FTHG"].value_counts().sort_index().to_frame()
  distr_goals_home.columns=["Matches"]

#calculamos la distribución de goles marcados por los equipos visitantes
  distr_goals_away=data["FTAG"].value_counts().sort_index().to_frame()
  distr_goals_away.columns=["Matches"]
  return distr_goals_home,distr_goals_away


def plot_goals_distribution(distr_goals_home: pd.DataFrame, distr_goals_away: pd.DataFrame) -> plt.Figure:
  """
  La función representa la distribución de los goles de los locasles y de los visitantes
  Args:
  1. distr_goals_home(pd.DataFrame): distribución de goles locales
  2. distr_goals_away(pd.DataFrame): distribución de goles visitantes
  Returns:
  plt.Figure: figura generada
  """
  #creamos una figura con dos gráficos.
  fig,axes=plt.subplots(1,2,figsize=(12,5))

  #distribucíon de goles de los locales
  axes[0].bar(distr_goals_home.index,distr_goals_home["Matches"])
  axes[0].set_title("Goles equipo local")
  axes[0].set_xlabel("Número de goles")
  axes[0].set_ylabel("Número de partidos")

  #distribucion de goles de los visitantes
  axes[1].bar(distr_goals_away.index,distr_goals_away["Matches"])
  axes[1].set_title("Goles equipo visitante")
  axes[1].set_xlabel("Número de goles")
  axes[1].set_ylabel("Número de partidos")

  plt.tight_layout()
  return fig
