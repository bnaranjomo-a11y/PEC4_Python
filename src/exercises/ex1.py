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

