import turtle
import pandas

screen = turtle.Screen()
screen.title("European Countries")
image = "europe_blank_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("european_countries_list.py")
all_countries = data.country.tolist()
guessed_countries = []

while len(guessed_countries) < 47:
	answer_country = screen.textinput(f"{len(guessed_countries)}/44 Countries Correct",
		prompt="What's another country's name?").title()

#Upon exit check what the user missed and write a new csv file with the missed countries for them to study
	if answer_country == "Exit":
		missed_countries = []
		for country in countries:
			if country not in missed_countries:
				missed_countries.append(country)	
		#new_data = pandas.DataFrame(missed_countries)
		#new_data.to_csv("countries_to_learn")

		break

#If the guess is correct add the country to the map using a turtle
	if answer_country in all_countries:
		guessed_countries.append(answer_country)
		t=turtle.Turtle()
		t.hideturtle()
		t.penup()
		country_data = data[data.country == answer_country]
		t.goto(int(country_data.x), int(country_data.y))
		t.write(answer_country)


turtle.exitonclick()