"""Hand-written verbal items: grammar (G2), para-jumbles (V5), critical reasoning (V6), and the
verbal/grammar parts of the mock. English cannot be checked by execution, so three guards apply:
  * every item has exactly one best answer by design (declared in `why`);
  * para-jumbles are machine-checked: the intended order is the ONLY permutation that satisfies
    the declared clue dependencies, and every distractor violates at least one;
  * no item is copied from a published paper (all are authored here).
"""
import itertools
from gen_core import Q


def T(q, correct, wrong, why, tag=None, pre=None):
    d = Q(q, [correct] + list(wrong), why, lambda: correct, tag)
    if pre: d['pre'] = pre
    return d


# ====================================================================== G2: sentence-level grammar (12)
G2_INLINE = [
    T("By the time the manager arrived, the team ___ the report.", "had finished", ["has finished", "finished", "was finish"],
      "*By the time … arrived* marks an earlier completed action in the past: past perfect, **had finished**.", 'Tense'),
    T("She has been living in Chennai ___ 2018.", "since", ["for", "from", "at"],
      "2018 is a point in time, so **since**. (*For* needs a length: *for six years*.)", 'Preposition'),
    T("My brother is ___ M.Tech student.", "an", ["a", "the", "no article"],
      "M is pronounced ‘em’, a vowel sound, so **an**.", 'Article'),
    T("The number of applicants ___ increased this year.", "has", ["have", "are", "were"],
      "The subject is *number* (singular), not *applicants*: **has**. (*A number of applicants have* is plural.)", 'Agreement'),
    T("Neither of the two answers ___ correct.", "is", ["are", "were", "have been"],
      "*Neither* takes a singular verb: **is**.", 'Agreement'),
    T("I look forward to ___ you next week.", "meeting", ["meet", "have met", "met"],
      "*Look forward to* is followed by an -ing form: **meeting**.", 'Verb form'),
    T("The committee ___ its decision yesterday.", "announced", ["has announced", "will announce", "announces"],
      "*Yesterday* needs the simple past: **announced**.", 'Tense'),
    T("The report ___ by Friday.", "will be submitted", ["will submit", "would submitting", "has submit"],
      "The report does not act; it is acted on. Future passive: *will be + past participle* = **will be submitted**.", 'Voice'),
    T("She is good ___ mathematics.", "at", ["in", "on", "with"],
      "The fixed pair is *good at*: **at**.", 'Preposition'),
    T("If it rains tomorrow, we ___ the picnic.", "will cancel", ["would cancel", "cancelled", "are cancel"],
      "A real future possibility: *if* + present, then *will* + verb: **will cancel**.", 'Conditional'),
    T("He asked me ___ I had finished the work.", "whether", ["that", "what", "which"],
      "An indirect yes/no question needs *whether* (or *if*): **whether**.", 'Conjunction'),
    T("Each of the players ___ tired after the match.", "was", ["were", "are", "have been"],
      "*Each* is singular; the match is over, so the past: **was**.", 'Agreement'),
]

# ====================================================================== G2: cloze passages (5 x 5)
CLOZE = [
    ("Artificial intelligence (1) ___ changing the way companies work. Many routine tasks (2) ___ now done by software, which leaves employees (3) ___ time for creative work. (4) ___ some people fear losing their jobs, experts say new roles will appear. Workers who keep learning (5) ___ best prepared for the change.",
     [("is", ["are", "were", "be"], "*Artificial intelligence* is singular, and the sentence describes something happening now: **is** changing."),
      ("are", ["is", "was", "has"], "*Tasks* is plural and *now* fixes the present: **are** done."),
      ("more", ["most", "many", "lot"], "*Leaves employees more time*: the comparative **more**."),
      ("Although", ["Because", "Unless", "Until"], "The two clauses contrast (fear vs. new roles): **Although**."),
      ("are", ["is", "be", "been"], "*Workers … are best prepared*: plural subject, present tense.")]),
    ("Water is (1) ___ of the most important resources on Earth. Yet millions of people still do not have access (2) ___ clean drinking water. In many cities, pipes (3) ___ old and leak a large amount every day. The government (4) ___ announced a plan to repair them by next year. If everyone (5) ___ water carefully, the problem can be reduced.",
     [("one", ["an", "the", "a"], "The fixed phrase is *one of the most …*: **one**."),
      ("to", ["for", "of", "at"], "The noun *access* takes **to**."),
      ("are", ["is", "was", "has been"], "*Pipes* is plural and the passage is in the present: **are** old."),
      ("has", ["have", "had", "is"], "A singular subject and a plan announced for the future: present perfect **has** announced."),
      ("uses", ["used", "will use", "use"], "In an *if*-clause the present simple is used, and *everyone* is singular: **uses**.")]),
    ("Last month I travelled (1) ___ Mysuru to attend a training programme. The train was scheduled (2) ___ at 6 a.m., so I woke up very early. When I reached the station, the train (3) ___ already left. I had to wait (4) ___ three hours for the next one. This experience taught me (5) ___ always plan my journey in advance.",
     [("to", ["at", "in", "on"], "You travel **to** a place."),
      ("to leave", ["leaving", "leave", "left"], "*Was scheduled* is followed by an infinitive: **to leave**."),
      ("had", ["has", "have", "was"], "The train left *before* I arrived: two past events, the earlier one in the past perfect, **had** already left."),
      ("for", ["since", "from", "during"], "A length of time after *wait*: **for** three hours."),
      ("to", ["that", "for", "about"], "*Taught me to always plan* (infinitive of purpose): **to**.")]),
    ("Regular exercise is good (1) ___ both the body and the mind. Doctors recommend (2) ___ least thirty minutes of activity every day. People (3) ___ exercise regularly usually sleep better and feel less stressed. Unfortunately, many of (4) ___ spend long hours at a desk and move very little. A short walk after lunch (5) ___ make a big difference.",
     [("for", ["at", "of", "to"], "The fixed pair is *good for*."),
      ("at", ["in", "on", "by"], "The fixed phrase is *at least*."),
      ("who", ["whom", "which", "whose"], "*People who exercise*: a relative pronoun for people, subject of *exercise*: **who**."),
      ("us", ["we", "our", "ourselves"], "After the preposition *of* use the object form: *many of us*."),
      ("can", ["may be", "is", "has"], "A modal is followed by the base verb: *can make*.")]),
    ("Online learning has become popular (1) ___ the last few years. Students can now attend classes from (2) ___ homes and watch lectures again whenever they wish. However, it (3) ___ self-discipline. A student who (4) ___ distracted easily may fall behind. (5) ___ , good teachers use short quizzes to keep learners engaged.",
     [("in", ["since", "at", "by"], "*In the last few years*. (*Since* needs a point in time.)"),
      ("their", ["they", "them", "theirs"], "A possessive before a noun: **their** homes."),
      ("requires", ["require", "requiring", "required"], "*It* is singular and the statement is general: **requires**."),
      ("gets", ["get", "getting", "have got"], "Singular subject *student*, present tense: **gets**."),
      ("Therefore", ["Although", "Because", "Unless"], "The teachers' response follows from the problem just described: **Therefore**.")]),
]


def cloze_questions(ix):
    """Questions for passages ix (list of indices). The passage is attached to the first blank of each set."""
    out = []
    for i in ix:
        passage, blanks = CLOZE[i]
        for n, (ans, wrong, why) in enumerate(blanks, 1):
            pre = f"**Passage {i + 1}.** Choose the word or phrase that best fills each numbered blank.\n\n> {passage}\n" if n == 1 else None
            out.append(T(f"Blank ({n}) of passage {i + 1}:", ans, wrong, why, 'Cloze', pre=pre))
    return out


# ====================================================================== V5: para-jumbles (20 sets)
# each: (opener+chain sentences in CORRECT order, clue explanation). Chain dependencies: each sentence
# after the first contains a word that points back to the one before it.
JUMBLE = [
    (["The water cycle describes how water moves around the Earth.",
      "First, heat from the sun turns water in oceans and rivers into vapour.",
      "Then the vapour cools, forms clouds and falls back as rain or snow.",
      "This rain collects in rivers and flows back to the sea, and the cycle begins again."],
     "The first sentence defines the topic. *First* and *Then* give the order of steps. *This rain* needs the rain mentioned just before."),
    (["Bamboo is a remarkable plant with many uses.",
      "It grows faster than almost any other plant, sometimes by a metre in a day.",
      "This speed means it can be harvested again and again without replanting.",
      "For that reason it now replaces wood in many industries, from furniture to paper."],
     "*It* = bamboo, so the bamboo sentence comes first. *This speed* needs the growth sentence. *For that reason* needs the harvesting sentence."),
    (["Banking has changed greatly over the last decade.",
      "Mobile apps now let customers transfer money in seconds.",
      "This convenience means routine work, such as checking a balance, no longer needs a branch visit.",
      "Such changes have made long queues at bank branches much shorter."],
     "General statement first. *This convenience* needs the apps sentence. *Such changes* sums up everything before it."),
    (["Sleep is as important to health as food and exercise.",
      "Adults need seven to nine hours of it each night.",
      "Those who regularly get less than this find it harder to concentrate.",
      "For this reason, doctors advise going to bed at a fixed time every day."],
     "The topic is defined first. *Less than this* needs the amount just given. *For this reason* closes with the advice."),
    (["Modern libraries offer much more than shelves of books.",
      "Many now provide a range of digital services as well.",
      "These include e-books, research databases and quiet study spaces.",
      "As a result, students spend more time in libraries than they did a decade ago."],
     "*Many now provide* needs *libraries*. *These include* needs *services*. *As a result* is the final outcome."),
    (["Electric cars are becoming more common on Indian roads.",
      "They run on batteries and produce no exhaust fumes.",
      "However, charging points are still few outside the big cities.",
      "Until this changes, many buyers will hesitate to switch."],
     "*They* = electric cars. *However* contrasts with the benefit just named. *This* = the shortage of charging points."),
    (["Many successful people say they read every day.",
      "You do not need much time to follow them: twenty minutes is enough.",
      "This small habit adds up to many books in a year.",
      "Those books, in turn, sharpen vocabulary and concentration."],
     "*Follow them* needs *successful people*. *This small habit* needs the twenty-minute habit. *Those books* needs *many books*."),
    (["Honey bees play a vital role in growing food.",
      "As they collect nectar, they carry pollen from flower to flower.",
      "This process allows many crops to produce fruit and seed.",
      "Without it, farmers would see their yields fall sharply."],
     "*They* = bees. *This process* = pollination just described. *Without it* = without that process."),
    (["The first step in cooking rice is to wash it.",
      "Washing removes the extra starch that makes rice sticky.",
      "Next, add twice as much water as rice and bring it to a boil.",
      "Finally, lower the heat and let it simmer until the water is absorbed."],
     "*First step* opens. *Washing* explains the first step. *Next* and *Finally* fix the order."),
    (["Plastic waste has become a serious problem in our cities.",
      "Much of it is used only once and thrown away within minutes.",
      "Such waste blocks drains and pollutes rivers.",
      "Reducing this harm starts with carrying a reusable bag."],
     "*Much of it* needs *plastic waste*. *Such waste* refers to the thrown-away plastic. *This harm* refers to blocked drains and polluted rivers."),
    # --- bank sets (11-18)
    (["Cricket is played in more than a hundred countries.",
      "Its most popular form is the one-day match.",
      "This format was introduced in the early 1970s.",
      "Since then it has brought millions of new fans to the game."],
     "*Its* = cricket. *This format* = one-day. *Since then* needs the 1970s date."),
    (["A good email begins with a clear subject line.",
      "It tells the reader what to expect before opening the message.",
      "The body should then state the request in the first two sentences.",
      "Finally, close politely and name the action you need."],
     "*It* = the subject line. *then* follows the subject line; *Finally* ends."),
    (["Volcanoes form where hot rock from deep inside the Earth reaches the surface.",
      "This rock, called magma, rises through cracks in the crust.",
      "When the pressure becomes too high, it erupts as lava, ash and gas.",
      "Over time, these materials build the familiar cone-shaped mountain."],
     "*This rock, called magma* needs the hot rock; *it erupts* follows the pressure; *these materials* needs lava, ash and gas."),
    (["Learning to swim is an important life skill.",
      "It builds strength, and it may one day save a life.",
      "That is why many schools now include swimming in their programmes.",
      "Children who start early in such programmes usually become confident swimmers."],
     "*It* = swimming. *That is why* needs the benefits. *Such programmes* needs *programmes*."),
    (["Train travel remains the backbone of transport in India.",
      "Every day it carries millions of passengers across the country.",
      "Such numbers place heavy demands on the network.",
      "Therefore the railways spend large sums on safety and new lines."],
     "*It* = train travel. *Such numbers* = millions of passengers. *Therefore* draws the conclusion."),
    (["Teamwork is one of the most valued skills in a workplace.",
      "No single employee can complete a large project alone.",
      "Hence, employers look for people who can share tasks and credit.",
      "Such people usually advance faster in their careers."],
     "*Hence* follows the statement that no one can work alone. *Such people* = those who share tasks."),
    (["Solar energy is among the cleanest sources of power.",
      "Panels on rooftops convert sunlight directly into electricity.",
      "This electricity can run homes without burning any fuel.",
      "As a result, the use of rooftop panels has grown fast in recent years."],
     "*This electricity* needs the panels sentence. *As a result* concludes."),
    (["Mobile phones have changed how people shop.",
      "Customers can now compare prices in seconds from anywhere.",
      "This pressure has forced shops to offer better deals.",
      "In the end, buyers are the ones who gain."],
     "*This pressure* = price comparison. *In the end* concludes."),
    # --- mock sets (19-20)
    (["Forests act as the lungs of the planet.",
      "Their leaves absorb carbon dioxide and release oxygen.",
      "This exchange helps keep the air clean and the climate stable.",
      "That is why cutting them down at a large scale is so dangerous."],
     "*Their leaves* needs forests; *This exchange* = absorbing and releasing; *That is why* concludes."),
    (["A budget is the first step towards financial stability.",
      "It lists what you earn and what you spend each month.",
      "Comparing the two shows where money is being wasted.",
      "Those savings can then be put towards a goal."],
     "*It* = the budget; *the two* = earning and spending; *Those savings* = the money saved by cutting waste."),
]
LABELS = 'PQRS'
# a fixed, varied shuffle of positions for each set (index = set number): which original sentence sits under P, Q, R, S
SHUF = [(2, 0, 3, 1), (1, 0, 2, 3), (3, 1, 0, 2), (0, 2, 3, 1), (3, 2, 0, 1), (1, 3, 0, 2), (2, 3, 1, 0), (3, 0, 1, 2), (1, 2, 0, 3), (2, 1, 3, 0),
        (0, 3, 2, 1), (3, 1, 2, 0), (1, 0, 3, 2), (2, 0, 1, 3), (3, 2, 1, 0), (0, 1, 3, 2), (2, 3, 0, 1), (1, 2, 3, 0), (0, 2, 1, 3), (3, 0, 2, 1)]


def jumble_question(ix):
    sents, expl = JUMBLE[ix]
    order = SHUF[ix]                          # label k shows original sentence order[k]
    assert sorted(order) == [0, 1, 2, 3]
    lab = {orig: LABELS[k] for k, orig in enumerate(order)}
    correct = ''.join(lab[i] for i in range(4))
    # uniqueness: under the chain dependencies (each sentence depends on the one before) only the original order satisfies all
    perms = [p for p in itertools.permutations(range(4)) if all(p.index(i) < p.index(i + 1) for i in range(3))]
    assert perms == [(0, 1, 2, 3)]
    # distractors: permutations that put a dependent sentence before its antecedent, varied in how they fail
    bad = [''.join(lab[i] for i in p) for p in itertools.permutations(range(4)) if p != (0, 1, 2, 3)]
    pick = [b for b in bad if b[0] != correct[0]][:1] + [b for b in bad if b[0] == correct[0]][:1] + [b for b in bad if b[-1] != correct[-1] and b[0] != correct[0]][1:2]
    pick = list(dict.fromkeys(pick))
    for b in bad:
        if len(pick) >= 3: break
        if b not in pick: pick.append(b)
    body = '\n'.join(f"{LABELS[k]}. {sents[order[k]]}" for k in range(4))
    q = f"Rearrange the four sentences into a meaningful paragraph. Choose the correct order.\n\n{body}\n"
    why = f"Correct order: **{correct}**. {expl}"
    return T(q, correct, pick[:3], why, 'Para-jumble')


# ====================================================================== V6: critical reasoning (16)
CR = [
    ("The company introduced free coffee in its offices, and sales rose that quarter. Therefore free coffee raised sales.\n\nWhich of the following is an assumption on which the argument depends?",
     "No other factor explains the rise in sales.", ["Coffee is the most popular drink in offices.", "Employees drink coffee every day.", "Sales always rise in the first quarter."],
     "The conclusion needs the coffee to be the cause. If something else (a festival season) raised sales, the argument fails. Negate the correct option: if another factor did explain it, the argument collapses.", 'Assumption'),
    ("Students who eat breakfast score higher marks. So eating breakfast improves marks.\n\nWhich of the following most weakens the argument?",
     "Students who are disciplined both eat breakfast and study more.", ["Breakfast is served in most schools.", "Some students skip breakfast and still score high.", "Marks depend on the school's syllabus."],
     "A third cause (discipline) can explain both, so the link between breakfast and marks is undermined.", 'Weaken'),
    ("All trainees who passed the test were offered jobs. Ravi was not offered a job.\n\nWhich of the following must be true?",
     "Ravi did not pass the test.", ["The test was unfair to Ravi.", "Ravi did not attend the test.", "No trainee was offered a job."],
     "If passing guaranteed a job, no job means no pass. The other options add facts that the passage does not give.", 'Inference'),
    ("A city reduced its speed limit from 60 to 40 km/h. The number of accidents fell by a third over the next year. Officials say the lower speed limit saved lives.\n\nWhich of the following would most strengthen their claim?",
     "Nearby cities that did not change their limits saw no fall in accidents.", ["More people now use public transport.", "The city planted trees along its main roads.", "Some drivers ignore the new limit."],
     "A comparison city with no change and no fall in accidents supports the limit as the cause.", 'Strengthen'),
    ("A store puts up a sign: ‘Buy one, get one free – all items.’ A customer argues that the store must therefore be losing money on every sale.\n\nThe customer's argument is flawed because it",
     "ignores that the store may have raised prices before the offer.", ["uses a sign as evidence.", "compares two different stores.", "assumes that customers always buy two items."],
     "Losing money is not guaranteed by a free item if the original price was raised to cover it.", 'Flaw'),
    ("Most employees who take public transport to work arrive on time. Meera arrives on time every day.\n\nWhich conclusion is best supported?",
     "Meera may take public transport, but the passage does not prove it.", ["Meera takes public transport.", "Meera lives near her office.", "Employees who drive are always late."],
     "‘Most’ does not mean ‘all’. Arriving on time is consistent with many other reasons. The cautious conclusion is the only safe one.", 'Inference'),
    ("Sales of electric scooters doubled last year. A manufacturer concludes that customers now prefer electric scooters to petrol ones.\n\nWhich of the following, if true, most weakens the conclusion?",
     "Sales of petrol scooters also rose by a third last year.", ["Electric scooters are quiet.", "The manufacturer also sells helmets.", "Fuel prices are expected to fall."],
     "If petrol scooter sales also rose, a preference for electric ones is not shown; the market may simply have grown.", 'Weaken'),
    ("Every software project at the firm that used daily stand-up meetings finished on schedule. The firm's new project will use daily stand-up meetings.\n\nWhich of the following is an assumption needed to conclude that the new project will finish on schedule?",
     "Daily stand-up meetings were a reason the earlier projects finished on time.", ["The new project is smaller than earlier ones.", "Stand-up meetings last less than fifteen minutes.", "All teams like stand-up meetings."],
     "The argument treats the meetings as the cause of timely completion. Without that link the past pattern proves nothing for the future.", 'Assumption'),
    ("The town's library recorded 20% more visitors after it began opening on Sundays. The librarian says Sunday opening is clearly the reason for the increase.\n\nWhich of the following would weaken her claim the most?",
     "The library also launched a large book sale during the same period.", ["The library is open until 8 p.m.", "Sundays are quiet in the town.", "Membership is free."],
     "A second event (a book sale) offers another explanation for the higher number of visitors.", 'Weaken'),
    ("If the new bridge opens before the festival, traffic in the old city will ease. The bridge did not open before the festival.\n\nWhich of the following must be true?",
     "Nothing can be concluded about the traffic from these statements alone.", ["Traffic in the old city did not ease.", "Traffic in the old city eased.", "The festival was cancelled."],
     "The statement says what happens if the bridge opens; it says nothing about what happens if it does not (traffic may ease for other reasons).", 'Inference'),
    ("Rohan has scored above 80% in each of his last five tests. His teacher expects him to score above 80% in the next one.\n\nThe teacher's expectation depends on the assumption that",
     "the next test is similar in difficulty to the earlier ones.", ["Rohan studies every day.", "Other students scored lower.", "The earlier tests were easy."],
     "Predicting from past performance assumes that conditions stay the same, including how hard the test is.", 'Assumption'),
    ("A survey of 50 readers of a cooking magazine found that 40 cook at home daily. The editor concludes that most people in the country cook at home daily.\n\nThe editor's conclusion is weak mainly because",
     "the readers of a cooking magazine may not represent the whole country.", ["fifty is an odd number.", "cooking is a hobby.", "the magazine is expensive."],
     "The sample is biased toward people who like cooking; it cannot stand for the whole population.", 'Flaw'),
    ("Since the company introduced flexible working hours, employee satisfaction scores have risen. The manager believes flexible hours are the cause.\n\nWhich of the following, if true, most strengthens the manager's belief?",
     "Satisfaction rose most in departments that used flexible hours the most.", ["The company also has a canteen.", "Some employees prefer fixed hours.", "Satisfaction surveys are anonymous."],
     "A dose-response pattern (more flexibility, more satisfaction) points to flexible hours as the cause.", 'Strengthen'),
    ("All the lamps in the hall are off. Some lamps in the corridor are on.\n\nWhich of the following must be true?",
     "Some lamps that are on are not in the hall.", ["All lamps in the corridor are on.", "The hall has no lamps.", "No lamp in the corridor is off."],
     "The lamps that are on include corridor lamps, and none of those is in the hall (all hall lamps are off).", 'Inference'),
    ("A shampoo advertisement says: ‘9 out of 10 users saw shinier hair after two weeks.’ A viewer concludes that the shampoo works for almost everyone.\n\nThe viewer overlooks that",
     "the advertisement does not say how many users were tested or how they were chosen.", ["shampoo is sold in bottles.", "two weeks is a short period.", "the advertisement is on television."],
     "Without the size and selection of the sample, ‘9 out of 10’ tells us little about everyone.", 'Flaw'),
    ("Mohan says: ‘Whenever it rains, the road near my house floods. It rained today, so the road near my house must be flooded.’\n\nWhich of the following correctly states a weakness in the reasoning?",
     "It is possible the drains were cleared today, so the usual flooding did not occur.", ["Rain is seasonal.", "Mohan lives near a road.", "Floods only happen at night."],
     "‘Whenever’ is a generalisation; one change in conditions (cleared drains) can break it, so the conclusion is not certain.", 'Weaken'),
]


def cr_questions(ix):
    out = []
    for i in ix:
        q, ok, wrong, why, tag = CR[i]
        out.append(T(q, ok, wrong, why, tag))
    return out


def jumble_questions(ix):
    return [jumble_question(i) for i in ix]


# ====================================================================== V2: "identify the correct sentence" (the official format)
CHOOSE = [
    ("Each of the players were given a medal.", "Each of the players was given a medal.", "Each of the players have given a medal.", "Each of the players were given medals.", 2,
     "*Each* is singular: ‘was given’."),
    ("She has been working here since five years.", "She has been working here for five years.", "She is working here since five years.", "She worked here since five years.", 2,
     "A length of time takes *for*; *since* needs a point in time."),
    ("The number of students are increasing every year.", "The number of students is increasing each year.", "The numbers of student is increasing every year.", "The number of student are increasing every year.", 2,
     "*The number of* takes a singular verb, and the noun after *of* is plural: ‘students’."),
    ("He did not knew the answer.", "He did not know the answer.", "He does not knew the answer.", "He did not known the answer.", 2,
     "After *did not* the verb is in its base form: ‘know’."),
    ("I am looking forward to meet you next week.", "I am looking forward to meeting you next week.", "I am looking forward for meeting you next week.", "I look forward to meet you next week.", 2,
     "*Look forward to* is followed by the -ing form."),
    ("If I would have known, I would have helped.", "If I had known, I would have helped.", "If I knew, I would have helped.", "If I have known, I would helped.", 2,
     "Third conditional: *if* + past perfect, *would have* + past participle."),
    ("The informations you gave me was very useful.", "The informations you gave me were very useful.", "The information you gave me was very useful.", "The information you gave me were very useful.", 3,
     "*Information* is uncountable (no plural) and takes a singular verb."),
    ("He is senior than me.", "He is senior to me.", "He is more senior than me.", "He is seniorer than me.", 2,
     "*Senior* is followed by *to*, not *than*."),
]


def choose_questions(ix=range(len(CHOOSE))):
    out = []
    for i in ix:
        a, b, c, d, k, why = CHOOSE[i]
        sents = [a, b, c, d]
        right = sents[k - 1]
        wrong = [x for j, x in enumerate(sents) if j != k - 1]
        q = "Identify the grammatically correct sentence."
        out.append(T(q, right, wrong, why, 'Correct sentence'))
    return out
