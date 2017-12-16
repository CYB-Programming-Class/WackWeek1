
print("Welcome to my quiz!")


# with this I can make my program have pauses. is cool
import time
time.sleep(1)


#this is the player score
decency = 0


# A function so I can easily add questions with all the variety I want!! (inspired by james)
def ask (validans,question,rating,notvalid):
    # infinite loop. I don't think this is good practice in general, but it works ok here.
    while True:
        # get input from user
        answer = input(question)

        # plz ignore anything between this comment
        if str.lower(answer) == "mobile":
            decency -= 100
            print("you are a terrible person")
            time.sleep(1)
        # and this one plz. I promise I didn't hardcode mobile to nuke your decency I'm a good programmer I promise plz

        # check if input is valid. if it is then break out of the loop (also gives feedback)
        if str.lower(answer) in validans:
            print("you answered: "+answer)
            time.sleep(1)
            break
        else:
            print(notvalid)
            time.sleep(1)

    # Returns the score from this question (the first answer is the only wrong/right answer depending on rating)
    if str.lower(answer) == validans[0] :
        return(rating)
    else:
        return(rating * -1)



#this is the first question. I ask what your favorite colors are.
#list of possible colors
list1 = ["orange","blue","green","red","yellow","purple","grey","black","white","vermillion","scarlet","cyan","pink","magenta","teal","scarlet","violet"]
# ask the question
decency += ask(list1,"What is your favorite color",-2,"That isn't a valid answer, try again")

#this is the second question. I ask what basic Icecream flavor they like most.
# list of possible answers
list2 = ["vanilla","chocolate","strawberry","swirl"]
#ect ect
decency += ask(list2,"what is your favorite basic icecream flavor",1,"your options are vanilla, chocolate, strawberry, and swirl")

# all the questions are the same for the mopst part, not gonna take the time to comment further.
list3 = ["pc","xbox","playstation","switch","mobile"]
decency += ask(list3,"what is your choice of console",1,"PC, Xbox PlayStation, Switch, and mobile are the only options")

list4 = ["both","cats","dogs"]
decency += ask(list4,"Cats or dogs",0.5,"sometimes the question is wrong") + 1.5 # no wrong answers here. just righter answers

# it was at this point that I realized I really shouldn't be making all these lists. not gonna change though, Im lazy and want it to be consistent.


print("Your decency score is")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(str(decency)+"!")
time.sleep(3)
print("The highest possible score is 6.0, the lowest is -3.0")