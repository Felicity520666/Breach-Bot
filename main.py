# Breach Bot Starter Code
breachYear = 2011

# Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name\n")
print("Nice to meet you " + userName)




# Recounts year of breach
print("The breach occurred in " + str(breachYear) + ".")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + )



# Introduces breach
print("Would you like to learn about the PlayStation Network 2011 Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

# Explains breach
while giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")

    topic = input()

    if topic.lower() == "a":
        print("Personal information of 77 million people was stolen from Sony's PlayStation Network and Qriocity including names, addresses, email addresses, login details, and possibly encrypted credit card data. The hack was by an outsider, but it's unclear how Sony was hacked.") 

    elif topic.lower() == "b":
        print("Sony shut down the PlayStation Network in April 2011 and revealed it was investigating a hack from an outsider days later. Sony improved its security and posted a warning for users to look out for scams that use personal information.")

    elif topic.lower() == "c":
        break

    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

# Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

# Shares my take
while giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")

    topic = input()

    if topic.lower() == "a":
        print("") 

    elif topic.lower() == "b":
        print("Sony shut down the PlayStation Network in ")

    elif topic.lower() == "c":
        break

    elif topic.lower() == "d":
        break
   
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press enter to continue\n")

# Chatbot ends conversation