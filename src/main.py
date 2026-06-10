"""
PEC4 Programción para la Ciencia de Datos
Alumno: Brandon Naranjo 
"""

from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import golas_distribution, plot_goals_distribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points; fun_total_points; alltime_winner
from exercises.ex6 import (fun_total_goals,fun_total_goals_by_team,fun_summary_1996_2025,podium)
from exercises.ex7 import graf

FILE="src/data/Partidos de LaLiga.csv"


def main():
     """la función ejecuta los ejercicios"""
     data=load_and_eda(FILE)
     print("Ejercicio 1")
     print(data.head())
     print(data.tail())
     print(data.describe())
     
     fig1=plot_home_away_goals(data)
     fig1.savefig("src/img/grafica_ex1_Brandon_Naranjo.png")
     
     print("Ejericicio 2")
     matches_team_total=total_matches(data)
     print(matches_team_total.head(10))
     print(matches_team_total[matches_team_total["Partidos jugados"]==matches_team_total["Partidos jugados"].max()])
     fig2=plot_matches_team_total(matches_team_total)
     fig2.savefig("src/img/grafica_ex2_Brandon_Naranjo.png")
     
     print("\nEjercicio 3")
     distr_goals_home, distr_goals_away = goals_distribution(data)
     print(distr_goals_home)
     print(distr_goals_away)
     fig3 = plot_goals_distribution(distr_goals_home, distr_goals_away)
     fig3.savefig("src/img/grafica_ex3_Brandon_Naranjo.png")
     
     print("\nEjercicio 4")
     ftr = FTR(data)
     print(ftr)
     home_wins = ftr.loc[ftr["Result"] == "H", "Matches"].iloc[0]
     total = ftr["Matches"].sum()
     print(f"Porcentaje de victorias locales: {(home_wins / total) * 100:.2f}%")
     fig4 = plot_FTR(ftr)
     fig4.savefig("src/img/grafica_ex4_Brandon_Naranjo.png")
     
     print("\nEjercicio 5")
     data_points = add_points(data)
     print(data_points.head(10))
     df_total_points = fun_total_points(data_points)
     print(df_total_points.head(10))
     print(alltime_winner(df_total_points))
     
     print("\nEjercicio 6")
     print(fun_total_goals(data))
     home_goals_by_team, away_goals_by_team, total_goals_by_team = (fun_total_goals_by_team(data))
     print(total_goals_by_team.head(10))
     summary_1996_2025 = fun_summary_1996_2025(df_total_points,home_goals_by_team,away_goals_by_team,total_goals_by_team)
     print(summary_1996_2025.head(10))
     fig6 = podium(summary_1996_2025)
     fig6.savefig("src/img/grafica_ex6_Brandon_Naranjo.png")
     
     print("\nEjercicio 7")
     selected_teams = df_total_points.head(5)["Team"].tolist()
     fig7 = graf(data, selected_teams)
     fig7.savefig("src/img/grafica_ex7_Brandon_Naranjo.png")

if __name__=="__main__":
     main()
