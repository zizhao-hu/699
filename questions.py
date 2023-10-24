# questions.py

# List of questions asked by kids
questions_0_8 = [
    "Why is the sky blue?",
    "How do fish breathe underwater?",
    "Where do babies come from?",
    "Why do we have to sleep?",
    "What makes the rain fall?",
    "How does the TV work?",
    "Why can't I eat candy all the time?",
    "Where does the sun go at night?",
    "How do birds fly?",
    "Why do we have to go to school?",
    "What are clouds made of?",
    "Why can't animals talk like us?",
    "How does the phone know who to call?",
    "Why do leaves change color in the fall?",
    "How do plants grow?",
    "Why do I have to brush my teeth?",
    "Where does the wind come from?",
    "How do cars move?",
    "Why do some animals have tails and others don't?",
    "How does the refrigerator stay cold?",
    "Why do people have different skin colors?",
    "How do airplanes stay in the sky?",
    "Why can't I see in the dark?",
    "How do remote controls work?",
    "Why do we sneeze?",
    "Where does our food come from?",
    "Why do I have to wear shoes outside?",
    "How do bees make honey?",
    "Why does the moon change shape?",
    "How do lights turn on and off?"
]

questions_8_13 = [
    "How do our phones know where we are all the time?",
    "Why is it daytime here but nighttime somewhere else?",
    "What's that tiny thing inside computers that makes them work?",
    "How can the internet be in the air with Wi-Fi?",
    "Why am I suddenly growing hair in weird places?",
    "How do people make those cool video games?",
    "Why are some people really poor and others super rich?",
    "How can the sun make electricity in those shiny panels?",
    "Is it normal that my voice is sounding weird sometimes?",
    "Why am I getting these annoying pimples on my face?",
    "What's that thing people call 'AI'? Is it like a robot brain?",
    "How can a printer make a toy out of nothing?",
    "Why's everyone saying recycling is so important?",
    "How do they make superheroes fly in movies?",
    "Why's everyone talking about the Earth getting warmer?",
    "Why do I feel so cranky and mad sometimes for no reason?",
    "What's happening when girls talk about 'that time of the month'?",
    "How can I buy stuff online with just a click?",
    "Why do I feel taller some mornings when I wake up?",
    "How do websites know it's really me when I type my password?",
    "Why do people in other countries talk so differently?",
    "How do planes talk to each other up in the sky?",
    "What's this 'deep web' thing my older cousin mentioned?",
    "How does yummy chocolate come from bitter cocoa?",
    "Why do my armpits smell now, and they didn't before?",
    "Why is it winter here but summer in Australia?",
    "How do tiny earbuds make such loud music?",
    "Why do I feel so weird and shy around my friends sometimes?",
    "How can I watch movies without a DVD or CD?",
    "Why do I feel all giggly when I think about that person in my class?"
]

questions_13_17 = [
    "How should I navigate college preparations?",
    "Any strategies for managing exam stress?",
    "How do high school relationships typically work?",
    "How can I determine my ideal career path?",
    "Can you explain how credit cards operate?",
    "Is Instagram affecting mental well-being?",
    "How can I cultivate an authentic style?",
    "What are the consequences of underage drinking?",
    "Why do high school friendships often change?",
    "Are long-distance relationships sustainable?",
    "How can I assert myself without causing conflict?",
    "What global events should I be aware of?",
    "How can I contribute to societal change?",
    "What distinguishes a job from a career?",
    "How can I decline offers without alienating friends?",
    "Is significant income from YouTube or TikTok feasible?",
    "How can I enhance my resume?",
    "Is excessive Netflix viewing harmful?",
    "How should I start financial savings?",
    "Who can discuss intimate topics with me?",
    "Why is it hard to align with my parents' views?",
    "How can I balance academics, sports, and social life?",
    "What's the significance of 'networking'?",
    "How do I identify negative friendships?",
    "What steps are needed to study abroad?",
    "Is it crucial to participate in elections?",
    "What does climate change mean for our generation?",
    "How can I boost my self-esteem?",
    "Can you recommend a unique hobby?",
    "How secure are my online photos and chats?"
]
questions_17_25 = [
    "How did you decide on your college major?",
    "Is it common for people to take a gap year before college?",
    "Have you had challenges with roommates, and how did you navigate them?",
    "What are your thoughts on open relationships or polyamory?",
    "Have you ever sent or received intimate photos? What precautions should one take?",
    "Is moving away from one's hometown after college a good idea?",
    "How do you deal with office politics without getting dragged into drama?",
    "Can you explain what a 401(k) is and why it's important?",
    "Is graduate school really worth the debt and time?",
    "How do you balance work, relationships, and personal time?",
    "What are the realities and precautions of one-night stands?",
    "I've noticed some people still buy CDs. Any idea why?",
    "How do you know if you're in a fulfilling career?",
    "What are the dos and don'ts of dating apps?",
    "Do you think traveling young is worth the expense?",
    "Why are vinyl records making a comeback?",
    "How do you handle the financial stresses of 'adulting'?",
    "Choosing health insurance is confusing. How did you decide?",
    "Do people still use flip phones? Why would they?",
    "How did you get started with investing?",
    "Have you ever felt overwhelmed by adult responsibilities?",
    "Is homeownership a realistic goal for our generation?",
    "How do you stay informed without getting bogged down by negative news?",
    "Any tips for making genuine connections in a new city?",
    "How viable is it to have a side hustle while working or studying full time?",
    "Have you had to set boundaries with family as you've grown older?",
    "What are your views on kinks and exploring them safely?",
    "How do you navigate the complexities of modern dating and consent?",
    "Is it okay to feel uncertain about life goals at this age?",
    "Have you ever been to a sex-positive workshop or event? What was it like?"
]



def load_questions(num_group):
    """
    Load and return the list of questions.
    """
    if num_group == 0:
        return questions_0_8
    elif num_group == 1:
        return questions_8_13
    elif num_group == 2:
        return questions_13_17
    else:
        return questions_17_25

if __name__ == "__main__":
    for idx, question in enumerate(load_questions(), 1):
        print(f"{idx}. {question}")