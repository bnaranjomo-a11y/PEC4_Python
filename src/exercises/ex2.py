#importamos matplotlib.pyplot para crear las graficas del ejercicio
#importamos la libreida pandas
import matplotlib.pyplot as plt
import pandas as pd
def total_matches(data: pd.DataFrame) -> pd.DataFrame:
  """ La función calcula el número total de partido jugados por cada equipo
  Args:
  data(pd.DataFrame):Dataset de partidos.
  Returns:
  pd.DataFrame: paritdos totales por equipo
  """
#contamos los partidos locales, visitante y los sumamos
  matches_team_total=(
      data["HomeTeam"].value_counts()
      .add(data["AwayTeam"].value_counts(),fill_value=0)
      .reset_index()
  )
#Renombramos las colummnas  y ordenamos de mayor a menor número de partidos
  matches_team_total.columns=["Equipos","Partidos jugados"]
  matches_team_total=matches_team_total.sort_values("Partidos jugados",ascending=False)
  return matches_team_total

def plot_matches_team_total(matches_team_total: pd.DataFrame) -> plt.Figure:
    """"
    La función represetan el número total de partidos jugados por equipo.
    Args:
        matches_team_total(pd:.DataFrame): partidos totales por equipo
    Returns:
        plt.Figure: Figura generada
    """
        
#creamos la gráfica de barras, ajustamos el tamaño
#ajustamoslos ejes: en el eje "x" los equipos y en el eje "y" el número de partidos
#ponemos las leyendas y ajustamos la rotación de los nombres en el "x" ha 90º
    fig=plt.figure(figsize=(12,8))
    plt.bar(matches_team_total["Equipos"],matches_team_total["Partidos jugados"])
    plt.title("Partidos totales jugados por equipo")
    plt.xlabel("Equipos")
    plt.ylabel("Número de partidos")
    plt.xticks(rotation=90)
    plt.tight_layout()

    return fig
    
