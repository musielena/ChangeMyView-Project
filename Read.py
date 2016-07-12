import difflib
import json
import pprint
from Parser import markdown

# for some weird reason, the code only seems to work when you run it twice. WHY?
exec(open("Parser.py").read())

data = []
pp = pprint.PrettyPrinter(indent=4, width=100, depth=6)

open('errors.txt', 'w').close()

with open("train_pair_data.jsonlist", "r") as raw:
    for line in raw.readlines():
        data.append(json.loads(line))


def process_text(input_text):
    tmp = input_text
    tmp = tmp.replace("&gt;", ">")
    tmp = tmp.replace("’", "'")
    tmp = tmp.replace("”", "\"")
    return tmp


def parse(input_text):
    return markdown.parseString(process_text(input_text)).asList()

def log(logged_text):
    with open("errors.txt", 'ab') as raw:
        raw.write(b"ERROR:\n")
        raw.write(logged_text.encode('utf-8'))
        raw.write(b"\n")


test = " \
There have been 55 million abortions in the US since 1973.\n\nSomething in the ballpark of 45% of women who have abortions have more than one abortion.\n\nThese people would have been raised by their incompetent parents to drain down society, increase crime rates, suck up resources, and generally screw things up.\n\nVarious ways to lower a resource negative population would have to be explored, if not because of this 55 million, then because of the next 55 million.\nOne possibility is that there would be wars waged to try to kill them all, perhaps even with other countries with similar problems. Waging war to purposefully lower population, even with a country facing similar issues, would cost not only resources, but it would also cause political, cultural, and global issues.\n\nAmerica's innovation and education rankings would be lower. Every middle-class child in the country would receive a lower quality education if there were 55 million more around.\n\n(**Note:**I'm not trying to hear arguments on the ethics of abortion, its a banal argument that everyone and their mother has had at one point, what I am really fishing for is insight into what the country would look like with those 55 million around. Would we adapt to the population and make good use of each of them?)\n\n**Was view changed?**\nIts a complicated issue. Without the extra population from abortions, has there been proportionately more immigration to fill labor needs, or are the millions of illegals from Mexico as likely to be so numerous even if there was a higher none-abortion population?  Doesn't immigration of a working class citizen on such a massive scale cause dissonance in a country more so than it does cultural exchange, meaning that it would have been preferable to have our abortions alive? Or are we talking about a population so huge that race and national identity are insignificant, that there is always going to be a huge amount of hostility between different demographics?          -(choppy writing, but i'm on 3 hours of sleep and stretched for time, give me a break)-\n\n\n(Side thought: Perhaps the immigration of illegals is lowering the value of blue collar work and makes it harder for the borderline impoverished citizens to provide for their children. Its debatable how many women are having abortions due to financial reasons, but surely its a significant number, so how many of these women wouldn't be having financial troubles if there wasn't competition from cheap illegal labor to keep wages lower? This holds true even if illegal immigration is an overall plus to the countries value. Conclusion: Mexicans are the supreme race, native Americans will go extinct through abortion and then out-breeding. *no that isn't a serious sentiment, i'm just saying, this discussion is abstract enough to go into some weird places and that it is necessary to have a stopping point* )\n\nThen there is the next question. Is a more highly populated and economically productive America today going to result in an America tomorrow that can handle over population problems, or would having a higher population from none-abortion just add on to the problems of a world going to shit? Similar: An aborted fetus is likely to have been a less productive person than a never-considered-for-abortion fetus, but in an industrial society, its likely that these abortions would still be more productive than not.\n\nThen there was the debate as to whether or not a larger population with less resources per person is more innovative than a smaller one. This is to be considered if one is convinced that having a higher population coming from none-abortions results in a strain for resources in the country.  Modern technology like the internet must be considered.\n\n\nYes, my view was changed, but not into the polar opposite. I am now confused and lost.\n\n\n**EDIT:**\n\nI'll be without internet for a few days. I may end up returning and responding more but it won't be anytime soon.\n\nThis was my first post to CMV. I apologize for a few things that I did that could be considered *rude* around here. I also see a few times where I got redundant.\n\nThank you all for your arguments. This is a very critical place, I hope to learn how to better use it and come here more often. I feel I could learn a lot here.\n\n_____\n\n&gt; *Hello, users of CMV! This is a footnote from your moderators. We'd just like to remind you of a couple of things. Firstly, please remember to* ***[read through our rules](http://www.reddit.com/r/changemyview/wiki/rules)***. *If you see a comment that has broken one, it is more effective to report it than downvote it. Speaking of which,* ***[downvotes don't change views](http://www.reddit.com/r/changemyview/wiki/guidelines#wiki_upvoting.2Fdownvoting)****! If you are thinking about submitting a CMV yourself, please have a look through our* ***[popular topics wiki](http://www.reddit.com/r/changemyview/wiki/populartopics)*** *first. Any questions or concerns? Feel free to* ***[message us](http://www.reddit.com/message/compose?to=/r/changemyview)***. *Happy CMVing!*\n"


data_p = []

for thread in data:
    info = {}
    info['op_author'] = thread['op_author']
    # print(thread['op_text'])

    try:
        info['op_text'] = parse(thread['op_text'].strip())
    except:
        log(thread['op_text'])
        continue

    # pp.pprint(info['op_text'])
    info['positive'] = []
    info['negative'] = []

    for comment in thread['positive']['comments']:
        infoC = {}
        infoC['author'] = comment['author']
        # print(comment['body'].encode("utf8"))
        try:
            infoC['text'] = parse(comment['body'])
        except:
            log(comment['body'])
            continue
        # pp.pprint(infoC['text'])
        info['positive'].append(infoC)
        # print()
    for comment in thread['negative']['comments']:
        infoC = {}
        infoC['author'] = comment['author']
        # print(comment['body'].encode("utf8"))
        try:
            infoC['text'] = parse(comment['body'])
        except:
            log(comment['body'])
            continue
        # pp.pprint(infoC['text'])
        info['negative'].append(infoC)
        # print()
    # print()
    # print()

    data_p.append(info)


pp.pprint(data_p[:10])

# parsed = markdown.parseString(process_text(
#     data[3]['positive']['comments'][1]['body'])).asList()
#
# pp.pprint(parsed)

# test = """I can't remember **the topic that** spurred this
# discussion,
# but a friend and I were debating whether man-made things were natural. He took the position that they are unnatural.
#
#
#
# He cited this definition by Merriam-Webster:  existing in nature and not made or caused by people : coming from nature (http://www.merriam-webster.com/dictionary/natural) as his basis for the distinction for natural vs. unnatural.
#
# However, I respectfully disagree with his position and furthermore that definition of natural. People arise from nature. Humankind's capacity to create, problem-solve, analyze, rationalize, and build also come from natural processes. How are the things we create unnatural? It is only through natural occurrences that we have this ability, why is it that we would give the credit of these things solely to man, as opposed to nature? We are not separate from nature, thus, how can any of our actions or creations be unnatural? If we were somehow separate from nature, I would understand the distinction between natural and man-made. However, I think unnatural and man-made are not synonyms by any means. It seems to me that man-made things MUST be natural due to our being part of nature.
#
#
# """
#

# pp.pprint(parse(test))
