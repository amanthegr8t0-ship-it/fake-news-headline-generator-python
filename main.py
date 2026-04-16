# Importing all the assisting modules.
import random as rd
import datetime as dt
import lists_actions as actl
import lists_joiner as joil
import lists_plalce as plal
import lists_sub as subl

# Getting all the categories of list in a single list.
subl1 = [subl.actors,subl.business,subl.creators,subl.musicians,subl.politicians,subl.scientists,subl.sports]
plal1 = [plal.common_places,plal.meme_places,plal.popular_places_global,plal.popular_places_india]
actl1 = [actl.actions_absurd,actl.actions_breaking,actl.actions_funny]
joil1 = [joil.joiners_funny, joil.joiners_news,joil.joiners_simple]

# Asking the user if they want to save the generated headlines.
want = input("Do you want to save the generated headlines (y/n) ").strip().lower()

while True :
    # Chosing a random category list.
    rand_sub_list = rd.choice(subl1)
    rand_action_list = rd.choice(actl1)
    rand_plaace_list = rd.choice(plal1)
    rand_joiner_list = rd.choice(joil1)

    # Chosing random word from the selected category of list.
    random_sub = rd.choice(rand_sub_list)
    random_act = rd.choice(rand_action_list)
    random_plac = rd.choice(rand_plaace_list)
    random_join = rd.choice(rand_joiner_list)

    # Marking date and time of generated headlline.
    time_now = dt.datetime.now().strftime("%d-%m-%Y|%H:%M ")

    # Concatenating the peices of strings.
    rand_news = f"{time_now} BREAKING NEWS : {random_sub.strip()} {random_act.strip()} {random_join.strip()} {random_plac.strip()} "
    print(rand_news)

    # Saving the Generated Headlines.
    if want == "y":
        with open("Generated Headline.txt", "a") as f :
            f.write(rand_news + "\n")

    # Asking if the user wants to generate mere headline   
    ques = input("Do you want to generate next Fake News  (y/n)  ").strip().lower()

    # Exiting the loop if user dosen't want more headline
    if ques == "n" :
        break

# Ending the Program
print("Thanks For Using Our Service 😊")