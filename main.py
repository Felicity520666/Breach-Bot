# Breach Bot Starter Code
breachYear = 2011

# Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name\n")
print("Nice to meet you " + userName)




# Recounts year of breach
print("The breach occurred in " + str(breachYear) + ".")
while True:
    try:
        todaysYear = int(input("What year is it now?\n"))
        if todaysYear < breachYear:
            print("Please enter " + str(breachYear) + " or a later year.")
            continue
        break
    except ValueError:
        print("Please enter a year using numbers, such as 2026.")

timePassed = todaysYear - breachYear
print("Wow! That means it has been " + str(timePassed) + " years.")



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

    input("Press Enter to continue\n")

# Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

# Shares my take
while giveInfo.lower() == "yes":
    print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, or (d) none")

    topic = input()

    if topic.lower() == "a":
        print("The breach mainly affected confidentiality because hackers gained unauthorized access to users' personal information. Availability was also affected because Sony shut down the PlayStation Network, preventing users from using it. There is less evidence that integrity was affected because it is unclear whether the hackers changed any information.")

    elif topic.lower() == "b":
        print("I was shocked that such a well-known technology company could experience a breach affecting so many people.")

    elif topic.lower() == "c":
        print("My advice is to use a unique password for every account, enable multi-factor authentication, and watch for suspicious messages after a breach.")

    elif topic.lower() == "d":
        break
   
    else:
        print("Sorry, I didn't catch that. Choose one of the options listed.")

    input("Press Enter to continue\n")

# Chatbot ends conversation
print("Thanks for chatting with Breach Bot!")
