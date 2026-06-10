#importamos matplotlib.pyplot para crear las graficas del ejercicio
#importamos la libreida pandas
import matplotlib.pyplot as plt
import pandas as pd

def load_and_eda(file: str) -> pd.DataFrame:
  """
  La función carga el dataset y elimina las columnas innecesarias y muestra la información básica.
  Args:
  file (str): Ruta del arcchivo CSV
  Returns:
  pd.DataFrame: Dataset cargado sin las columnas HTHG, HTAG, HTR,
  """
#cargamos el archivo csv utilizando la ruta establecida
#mediante "axis1" indicamos que eliminamos las columnas "HTHG","HTAG","HTR"
  data=pd.read_csv(file)
  data=data.drop(["HTHG","HTAG","HTR"],axis=1)
  return data



def plot_home_away_goals(data: pd.DataFrame) -> None:
  """Muestra dos boxplots con la distribución de goles locales y visitantes.
  Args:
  data(pd.DataFrame):Dataset de partidos
  Returns:
  None
  """
#creamos una figura con dos gráficos colocados en una misma fila
#primer boxplot: distribución de goles del equipo local
  fig,axes=plt.subplots(1,2,figsize=(10,5))
  axes[0].boxplot(data["FTHG"])
  axes[0].set_title("Goles del equipo local")
  axes[0].set_ylabel("Numero de goles")

#segundo boxplot: distribución de goles del equipo visitante
  axes[1].boxplot(data["FTAG"])
  axes[1].set_title("Goles del equipo visitante")
  axes[1].set_ylabel("Numero de goles")

#ajustamos el espacio entre gráficos
#mostramos la figura y ejecutamos la función
  plt.tight_layout()
  return fig

