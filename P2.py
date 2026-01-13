cybersecurity_incidents=[
    "The morris worm disrupted computers in 1988,one of the first computer worms distributed via the internet.",
    "In 2007, estonia suffered a massive DDos attack that crippled the nationh's digital infrastructure.",
    "In 2013, target experienced a major data breach where millions of credit card details were stolen.",
    "The WannaCry Ransomware attack in 2017 affected thousands of computers globally encryptingdata and demanding ransom.",
    "A phishing attack in 2016 compromised the email accounts of several high_profile figures leading to release of sensitive information.",
    "The Mirai botnet in 2016 launched DDos attacks using IoT devices,bringing down large parts of the internet."
]
categories={"virus":[],"phishing":[],"DDos":[],"ransomware":[],"data breach":[]}

for incident in cybersecurity_incidents:
    for category in categories:
        if category in incident.lower():
            categories[category].append(incident)

for category,incidents in categories.items():
    print(f"\nCategory:{category.capitalize()}")
    print("\n".join(incidents) if incidents else"no incidents in this category.")