from typing import List
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def graf(data: pd.DataFrame, selected_teams: List[str]) -> plt.Figure:
    """
    La función genera un grafo con las conexiones entre los equipos seleccionados
    Args:
    data(pd.DataFrame): dataset de partidos
    selected_teams(list): lista de los 5 equipos con mejor puntuación acumulada
    returns:
    figura generada con el grafo
    """
    #filtramos los partidos de los equipos seleccionados
    #contamos los partidos que ha jugado cada pareja de equipos
    filtered_data=data[
          data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)]
    connections=(filtered_data.groupby(["HomeTeam","AwayTeam"]).size().reset_index(name="matches"))
    
    #creamos el grafo vacío y añadimos los equipos como nodos del grafo
    graph=nx.Graph()
    graph.add_nodes_from(selected_teams)
    
    #recorremos todas las conexiones entre equipos
    #obtenemos los equipos local y visitante
    #sacamos el número de partidos entre ambos equipos
    
    for _, row in connections.iterrows():
        home_team=row["HomeTeam"]
        away_team=row["AwayTeam"]
        matches=row["matches"]
    
    #si la conexión ya existe, acumulamos partidos
    #si no existe creamos la conexión
        if graph.has_edge(home_team,away_team):
           graph[home_team][away_team]["weight"]+=matches
        else:
          graph.add_edge(home_team,away_team,weight=matches)
    
    #calculamos la posición de los nodos
    #establecemos el tamaño de la figura
    pos=nx.spring_layout(graph,seed=42)
    fig=plt.figure(figsize=(8,6))
    
    #dibujamos el grafo y sacamo las eqiuetas de las aristas
    nx.draw(graph,pos,with_labels=True,node_size=3000,font_size=9)
    edge_labels=nx.get_edge_attributes(graph,"weight")
    
    #mostramos las equitas sobre las conexiones
    #ponemos el titulo al gráfico y mostramos el gráfico
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)
    plt.title("Conexiones entre los 5 mejores equipos")
    plt.tight_layout()
  
    return fig 
