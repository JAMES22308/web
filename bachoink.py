# import pyttsx3
# jarvis = pyttsx3.init()
# rate = -5000
# jarvis.setProperty('rate', rate)
# num = int(input("num: "))
# num2 = int(input("num: "))
# sum = num+num2
# jarvis.say(f"{num} plus {num2} equals {sum}")
# print(sum)
# jarvis.runAndWait()
import random
import pyttsx3
jarvis = pyttsx3.init()
member=["marimar", "james" , "france"]
leader = random.choice(member)
jarvis.say(f"the leader is {leader}")
print(f"the leader is {leader}")
jarvis.runAndWait()