import matplotlib.pyplot as plt
import pandas as pd

def FTR(data: pd.DataFrame) -> pd.DataFrame:
  """
  La función cálcula el número de victorias locales, visitantes y empates.
  Args:
  data(pd:DataFrame): dataset de partidos.
  returns:
  pd:DataFrame: resultados finales de los partidos
  """
#contamos las veces que aparece el resultado final
  ftr=data["FTR"].value_counts().reset_index()
  ftr.columns=["Result","Matches"]
  return ftr



def plot_FTR(ftr: pd.DataFrame) -> plt.Figure:
  """
  La función cálcula el número de victorias locales, visitantes y empates.
  Args:
  ftr(pd:DataFrame): resultados finales
  returns:
  plt.Figure: figura generada
  """
  labels={"H":"Victorias local", "A": "Victorias visitante", "D":"Empates"}
  fig=plt.figure(figsize=(6,4))
  plt.bar(ftr["Result"].map(labels), ftr["Matches"])

  plt.title("Resultados de los partidos")
  plt.ylabel("Número de partidos")
  plt.tight_layout()
  return fig 
