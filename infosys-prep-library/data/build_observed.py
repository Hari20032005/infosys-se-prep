"""Writes questions-observed.csv from the transcripts and first-hand accounts read on 2026-09-25.

Every question row was reconstructed from an auto-caption transcript (scratchpad/tr-*.txt) or a
first-hand post, then re-derived independently. `verified_answer` is ours; `stated_answer` is
the source's. data/verify_observed.py recomputes every numeric/trace answer by execution.

Sources (video id -> channel, publish date, provenance claim):
  YT-5XTG  5XTGOVtBkiw  OnlineStudy4u   2025-10-09  candidates' recall of early-Oct 2025 SE slots, shift-tagged
  YT-2NTB  2ntBG9N_8Kk  Placement Walaa 2025-09-29  "asked in recent Infosys examination"
  YT-2YHL  2yhl7EzbY2Q  OnlineStudy4u   2025-09-25  "Infosys PYQ", undated
  YT-U7HK  U7hkPOKo69o  OnlineStudy4u   2026-09-18  "PYQ ... 11th/4th/16th October 2025"
  YT-2MBO  2mbo13B9QWU  OnlineStudy4u   2026-09-22  "PYQ ... one or two years old"
  YT-6UFT  6uftMFrZdzc  OnlineStudy4u   2025-09-27  "Infosys previous year puzzles"
  YT-HZGK  HZGkyKYqSA0  Code Bashers    2024-12-18  "latest pseudo code questions asked in SE hiring"
  YT-KC2G  Kc2gqLaBVsE  Tekno UF        2024-11-04  "exam conducted on 3rd of November", candidate-reported
  B1..B5   first-hand candidate posts (see reviews-online.csv)

Independence rule: re-use of the same slide by the same channel is ONE sighting. Only a
second channel or a second candidate creates a duplicate_of row.
"""
import csv

COLS = ("qid,source,source_date,entity,role,section,subsection,question_text,options,stated_answer,"
        "verified_answer,verification_method,concept_tested,difficulty,confidence,duplicate_of,notes").split(',')

E, R = 'Infosys Ltd', 'Systems Engineer'
X = 'verify_observed.py'

def q(qid, src, date, sec, sub, text, opts, stated, ver, meth, concept, diff, conf, dup='', notes=''):
    return dict(qid=qid, source=src, source_date=date, entity=E, role=R, section=sec, subsection=sub,
                question_text=text, options=opts, stated_answer=stated, verified_answer=ver,
                verification_method=meth, concept_tested=concept, difficulty=diff, confidence=conf,
                duplicate_of=dup, notes=notes)

ROWS = [
# ---------------- Reasoning ----------------
q('R01','YT-2MBO','2026-09-22','reasoning','coding-decoding (letter-value average)',
  'In a certain code LAST is written as 13 and TABLE as 8. How is FRAUD written?','','10 (option C)','10',X,
  'code = mean of alphabet positions','Medium','REPORTED'),
q('R02','YT-2MBO','2026-09-22','reasoning','number series',
  'Find the missing term: 3, 14, 39, 84, 155, ?, 399','','258','258',X,'n^3 + n^2 + n','Medium','REPORTED'),
q('R03','YT-2MBO','2026-09-22','reasoning','alphanumeric series',
  'Find the next term: H47F, I48G, K50I, ?','','N53L (option D)','N53L',X,'gaps +1,+2,+3 in every position','Easy','REPORTED'),
q('R04','YT-2MBO','2026-09-22','reasoning','data sufficiency',
  'What is the smallest of four consecutive even numbers? I. Their sum is 132. II. The difference between the smallest and the largest is 6.',
  'standard DS options','I alone is sufficient','I alone is sufficient (smallest = 30); II is always true for any four consecutive evens',X,
  'sufficiency of a linear equation vs an identity','Easy','REPORTED'),
q('R05','YT-2NTB','2025-09-29','reasoning','coding-decoding (letter-sum)',
  'In a certain code BURST is written as 80 and LAKE as 29. How is VERSATILE written?','','111','111',X,
  'code = sum of alphabet positions','Easy','LIKELY',notes='Also presented by OnlineStudy4u (YT-2YHL 2025-09-25, YT-U7HK 2026-09-18); same channel counted once'),
q('R05b','YT-2YHL','2025-09-25','reasoning','coding-decoding (letter-sum)',
  'BURST = 80, LAKE = 29, VERSATILE = ?','options incl. 111','111 (option D)','111',X,'code = sum of alphabet positions','Easy','LIKELY',dup='R05',
  notes='Second channel; independent of YT-2NTB only if the two coaches did not share a source'),
q('R06','YT-2NTB','2025-09-29','reasoning','coding-decoding (position rule)',
  'In a certain code CHAIR is written as 301018. How is TABLE written?','4 options','200205 (option B)','200205',X,
  'odd positions -> alphabet number, even positions -> 0','Medium','REPORTED'),
q('R07','YT-2NTB','2025-09-29','reasoning','number series',
  'Find the next term: 0, 1, 2, 6, 16, 44, 120, ?','4 options','328 (option D)','328',X,'a(n) = 2*(a(n-1) + a(n-2))','Hard','REPORTED'),
q('R08','YT-2NTB','2025-09-29','reasoning','number series',
  'Find the next term: 144, 441, 169, 961, 196, ?','4 options','option A (transcript unclear)','1681',X,
  '12^2, 21^2, 13^2, 31^2, 14^2, 41^2','Medium','REPORTED',notes='Stated option value inaudible; 41^2 = 1681'),
q('R09','YT-2NTB','2025-09-29','reasoning','operator logic',
  'If 264 * 2 = 6 and 870 * 3 = 11, what is 735 * 5?','','12','12',X,'divide, then digit sum once','Medium','REPORTED'),
q('R10','YT-2NTB','2025-09-29','reasoning','syllogism',
  'Statements: All shoes are legs. Some legs are pairs. Some pairs are hands. Conclusions: I. Some hands are shoes. II. Some pairs are shoes.',
  'I only / II only / both / neither','Neither follows','Neither follows',X+' (Venn counter-model)','chained "some" gives no definite link','Easy','REPORTED'),
q('R11','YT-2NTB','2025-09-29','reasoning','alphanumeric series',
  'Find the next term: 3Y6, 8W8, 15U10, 24S12, 35Q14, ?','4 options','48O (option A)','48O16',X,
  'n^2-1 ; letter -2 ; +2','Medium','REPORTED'),
q('R12','YT-2YHL','2025-09-25','reasoning','operator logic',
  'If $59 = 135, $48 = 122 and $96 = 144, then $136 = ?','168 / ... ','168 (option 1)','168',X,
  '$ab = a*b + 90, with 136 read as 13 and 6','Medium','REPORTED',
  notes='Same slide re-used in YT-U7HK. Ambiguous: reading 136 as 1,3,6 gives 108; 168 is the option offered'),
q('R13','YT-2YHL','2025-09-25','reasoning','blood relation (coded)',
  "'x + y' means x is the sister of y, 'x - y' means x is the father of y, 'x * y' means x is the brother of y. Which expression means M is the son of S?",
  'only option B recoverable: S - P + M * G','option B','S - P + M * G',X+' (relation walk)','decode symbol chain; gender from "brother"','Medium','REPORTED',
  notes='Other three options inaudible; distractors in QB-99 are authored. Re-used in YT-U7HK'),
q('R14','YT-2YHL','2025-09-25','reasoning','coding-decoding (reverse + shift)',
  'CREATE is written as DSZDQB. How is POLITE written?','option B: DSHKNO','DSHKNO (option B)','DSHKNO',X,
  'reverse the word, then shift every letter -1','Medium','REPORTED',
  notes='ASR heard the code as "DSJDQB"; the rule that produces the stated answer requires DSZDQB. Re-used in YT-U7HK'),
q('R15','YT-5XTG','2025-10-09','reasoning','coding-decoding (swap)',
  'If BREAK is written as RBEKA, how is BRIEF written?','','RBIFE','RBIFE',X,'swap 1-2, keep 3, swap 4-5','Easy','REPORTED',
  notes='"asked in the shift one" of the early-Oct 2025 SE exam'),
q('R16','YT-5XTG','2025-10-09','reasoning','number series',
  'Find the next term: 13, 17, 19, 23, 29, ?','31 / 32 / 33 / ...','31','31',X,'consecutive primes','Easy','REPORTED'),
q('R17','YT-KC2G','2024-11-04','reasoning','alphanumeric series',
  'Replace ?: 1D, ?, 5H, 7J, 9L','3F / 3G / none','3F','3F',X,'odd numbers; letters +2','Easy','REPORTED',notes='Exam of 3 Nov 2024 (older cycle)'),
q('R18','YT-KC2G','2024-11-04','reasoning','alphanumeric series',
  'Replace ?: 12M, ?, 14Q, 15S','13F / 13O / 13N / 13H','13O','13O',X,'+1 ; letters +2','Easy','REPORTED'),
q('R19','YT-KC2G','2024-11-04','reasoning','number series',
  'Find the next term: 100, 20, 80, 50, 60, 80, ?','','40 (option b)','40',X,'two interleaved series: -20 and +30','Easy','REPORTED'),
q('R20','YT-2YHL','2025-09-25','reasoning','number series',
  'Find the missing term: 91, 94, 100, 109, ?, 136','... / 121','121 (option D)','121',X,'differences 3,6,9,12,15','Easy','REPORTED',notes='Re-used in YT-U7HK'),
# ---------------- Quant (Technical Ability) ----------------
q('Q01','YT-2MBO','2026-09-22','quant','linear equations / quantity comparison',
  'If 2x + 3y = 7 and 5x + 8y = 2, which relation between x and y holds?','x>y / x<y / x=y / cannot be determined','x > y (option C)','x > y (x = 50, y = -31)',X,
  'solve 2x2 system','Easy','REPORTED'),
q('Q02','YT-2NTB','2025-09-29','quant','ages / ratio',
  "The present ages of A and B are 48 and 72. Find the ratio of A's age 3 years ago to B's age 3 years from now.",'4 options','3:5 (option D)','3:5',X,'45:75','Easy','LIKELY'),
q('Q02b','YT-2YHL','2025-09-25','quant','ages / ratio',
  'Ages 48 and 72; ratio of the first 3 years ago to the second 3 years hence?','','3:5 (option D)','3:5',X,'45:75','Easy','LIKELY',dup='Q02',
  notes='Second channel. Also in YT-U7HK (same channel as YT-2YHL)'),
q('Q03','YT-2NTB','2025-09-29','quant','data interpretation (table)',
  'Heights of 400 students: 140-150 cm: 150; 150-160: 88; 160-170: 70; 170-180: 50; 180-190: 42. What percentage are shorter than 170 cm?',
  'includes 77%','77%','77%',X,'cumulative frequency / total','Easy','LIKELY',notes='Source: "this year more DI questions are getting asked"'),
q('Q03b','YT-2YHL','2025-09-25','quant','data interpretation (table)',
  'Same 400-student height table; percentage shorter than 170 cm?','','77% (option D)','77%',X,'308/400','Easy','LIKELY',dup='Q03',
  notes='Second channel. Also in YT-U7HK'),
q('Q04','YT-2NTB','2025-09-29','quant','averages',
  'The sum of 15 observations is 2100. Every observation is doubled and then reduced by 10. By how much does the average increase?','4 options','130 (option B)','130',X,
  'new mean = 2m - 10','Easy','REPORTED'),
q('Q05','YT-2NTB','2025-09-29','quant','linear equations (heads and legs)',
  'A farm has cows and hens: 45 heads and 130 legs in total. How many cows?','4 options','20 (option D)','20',X,'2 equations','Easy','REPORTED'),
q('Q06','YT-2YHL','2025-09-25','quant','number system (primes, cube root)',
  'What is the cube root of the product of the non-prime numbers on a telephone keypad?','... / 12','12','12 (reading "non-prime" as the composites 4, 6, 8, 9)',X,
  'composite vs non-prime; 4*6*8*9 = 1728','Medium','REPORTED',
  notes='Literally, 0 and 1 are non-prime too and 0 makes the product 0. The intended reading is composites. Re-used in YT-U7HK'),
q('Q07','YT-2YHL','2025-09-25','quant','data interpretation (pie)',
  "A student's total is 400 marks, split English 25%, Hindi 34%, Maths 18%, Science 10%, History 13%. Pass mark per subject is 50. In which subject did he fail, and what is the gap between his best and worst subject?",
  'Science, 88 / Science, 96 / ...','Science, 96','Science; 96',X,'percent of total; max - min','Easy','REPORTED',
  notes='SOURCE DEFECT: stem says marks are "out of 100" but Hindi = 136. Answer holds on the chart data. Re-used in YT-U7HK'),
q('Q08','YT-5XTG','2025-10-09','quant','mensuration (sphere)',
  'The surface area of a sphere is 154 cm^2. Find its volume (pi = 22/7).','','around 180','179.67 cm^3 (539/3)',X,'r = 3.5','Medium','REPORTED'),
# ---------------- Pseudocode ----------------
q('P01','YT-2MBO','2026-09-22','pseudocode','loop + integer division',
  'for w = 0 to 5: if (w mod 2 == 0 and w / 2 == 0) display w','','only 0','0',X+' (executed)','integer division; && short-circuit','Easy','REPORTED',notes='2 marks per pseudocode item (source)'),
q('P02','YT-2MBO','2026-09-22','pseudocode','modulus + loop',
  'x = 27 mod 7; for i = 0 to x: display i','','0 1 2 3 4 5 6 (option D)','0 1 2 3 4 5 6',X+' (executed)','mod','Easy','REPORTED'),
q('P03','YT-2YHL','2025-09-25','pseudocode','bitwise precedence',
  'Integer p = 1, q = 1. p = p ^ 1 & 1 + q ^ 1 & 1. Print p + q.','','1','1',X+' (executed, C/Java precedence and left-to-right both give 1)',
  'XOR/AND/+ precedence','Hard','REPORTED',notes='Operator symbols reconstructed from ASR ("J" = ^); answer is robust to both readings'),
q('P04','YT-2YHL','2025-09-25','pseudocode','do-while',
  'Integer x = 0. do { ++x; display x; x--; } while (x >= -1)','','infinite loop printing 1','infinite loop printing 1',X+' (bounded execution)','loop invariant','Medium','REPORTED'),
q('P05','YT-2YHL','2025-09-25','pseudocode','while + mod',
  'n = 26, i = 0. while (n mod 8 != 0) { n = n + 5; i = i + 1 }. n = n + i. print n','0 / 11 / 22 / 62','62','62',X+' (executed)','trace until divisible','Medium','REPORTED'),
q('P06','YT-HZGK','2024-12-18','pseudocode','for loop accumulate',
  'x = 3, y = 2, result = 0. for i = 1 to y: result = result + x * i. print result','','9 (option A)','9',X+' (executed)','trace','Easy','REPORTED',notes='Older cycle (Dec 2024)'),
q('P07','YT-HZGK','2024-12-18','pseudocode','recursion (factorial)',
  'Standard recursive factorial; output for n = 5?','','120','120',X+' (executed)','recursion','Easy','REPORTED',notes='Code shown on screen only; reconstructed as textbook factorial'),
q('P08','YT-HZGK','2024-12-18','pseudocode','digit sum',
  'n = 123, sum = 0. while n > 0: sum = sum + n mod 10; n = n / 10. print sum','','6 (option B)','6',X+' (executed)','integer division','Easy','REPORTED'),
q('P09','YT-HZGK','2024-12-18','pseudocode','branch in loop',
  'n = 6, sum = 0. for i = 1 to n: if i mod 2 == 0 then sum = sum + i*i else sum = sum + i. print sum','','65','65',X+' (executed)','trace','Easy','REPORTED'),
q('P10','YT-HZGK','2024-12-18','pseudocode','recursion (power)',
  'function calc(a, b): if b == 0 return 1 else return a * calc(a, b - 1). Output of calc(6, 3)?','','216','216',X+' (executed)','recursion','Easy','REPORTED'),
q('P11','YT-HZGK','2024-12-18','pseudocode','recursion (accumulating argument)',
  'function f(x, y): if y == 0 return x else return f(x + y, y - 1). Output of f(7, 2)?','','10 (option B)','10',X+' (executed)','recursion','Easy','REPORTED'),
q('P12','YT-U7HK','2026-09-18','pseudocode','arrays (product except self)',
  'total = product of all elements; result[i] = total / a[i]. Input 2, 3, 4, 5. Output?','60 40 30 24 / 60 40 20 ...','60 40 30 24 (option A)','60 40 30 24',X+' (executed)','two passes over an array','Medium','REPORTED',
  notes='Presenter: "these pseudo code questions were asked in 2025"'),
q('P13','YT-U7HK','2026-09-18','pseudocode','pre/post increment (fill the blank)',
  'i = 5. Which statement makes both result and i equal 6 when the function returns?','options inaudible','result = ++i','result = ++i',X+' (executed)','pre- vs post-increment','Medium','REPORTED',notes='Distractors in QB-99 are authored'),
q('P14','YT-U7HK','2026-09-18','pseudocode','pre/post increment (fill the blank)',
  'i = 2. Choose result = ___ so that result prints 7.','combinations of i++ and ++i','++i + ++i','++i + ++i (3 + 4)',X+' (executed in Java)','evaluation order','Hard','REPORTED',
  notes='Well defined in Java (left to right). Undefined behaviour in C. Other options give 5 and 6'),
q('P15','YT-U7HK','2026-09-18','pseudocode','arrays (longest increasing run)',
  'cur = 1, best = 1. for i = 1 to n-1: if a[i] > a[i-1] then cur++ ; best = max(best, cur) else cur = 1. Output for [1, 2, 2, 3, 4, 5, 1]?','options inaudible','4 (fourth option)','4',X+' (executed)','strict vs non-strict comparison resets','Hard','REPORTED',
  notes='Presenter: "one of the very trickier question which was asked"'),
# ---------------- Puzzle (Numerical Puzzle) ----------------
q('Z01','YT-2MBO','2026-09-22','puzzle','4x4 grid (row sum)',
  'Grid rows: 1 5 6 3 / 9 1 2 3 / 1 1 6 7 / 4 1 2 ?','','8','8',X,'every row sums to 15','Easy','REPORTED',notes='Source: "this is for two marks"'),
q('Z02','YT-2MBO','2026-09-22','puzzle','row rule',
  'Rows: 7 6 42 36 / 8 4 32 16 / 10 12 120 ?','','144 (option C)','144',X,'a, b, a*b, b^2','Easy','REPORTED'),
q('Z03','YT-2YHL','2025-09-25','puzzle','figure (outer -> centre)',
  'Figure 1: 3, 7, 5, 1 -> 16. Figure 2: 9, 8, 34, 2 -> 4. Figure 3: 15, 12, 21, 8 -> ?','... / 12','12 (option C)','12',X,'(a*b) - (c*d)','Medium','REPORTED',notes='Re-used in YT-U7HK'),
q('Z04','YT-2YHL','2025-09-25','puzzle','diagonal pairs',
  'Opposite pairs 36 & 12 -> 48, 8 & 32 -> 40, 16 & 25 -> 41, 39 & 7 -> ?','... / 46','46 (option D)','46',X,'sum of the pair','Easy','REPORTED',notes='Re-used in YT-U7HK'),
q('Z05','YT-U7HK','2026-09-18','puzzle','figure (two products)',
  'Figure 1: (11, 4) and (2, 2) -> 48. Figure 2: (7, 7) and (5, 6) -> 79. Figure 3: (8, 8) and (12, 9) -> ?','... / 172','172','172',X,'a*b + c*d','Medium','REPORTED',notes='Also YT-2YHL (same channel)'),
q('Z06','YT-5XTG','2025-10-09','puzzle','pair rule',
  '(5, 11) -> 58, (12, 8) -> 99, (16, 7) -> ?','115','115','115',X,'a*b + 3','Easy','REPORTED',notes='Early-Oct 2025 SE slot'),
q('Z07','YT-5XTG','2025-10-09','puzzle','4x4 grid (row rule)',
  'Rows: 8 3 6 26 / 4 9 12 112 / 5 7 2 19 / 9 6 4 ?','','33','33',X,'second*third + first','Medium','REPORTED',notes='Early-Oct 2025 SE slot; "4x4 matrix puzzles were asked"'),
q('Z08','YT-5XTG','2025-10-09','puzzle','pair rule (difference of squares)',
  '(15, 10) -> 125, (18, 11) -> 203, (21, 16) -> ?','','185','185',X,'a^2 - b^2','Hard','REPORTED',
  notes='Students called it tough. The middle value was inaudible and is filled by the same rule'),
q('Z09','YT-5XTG','2025-10-09','puzzle','3x3 grid (row product)',
  'Rows: 20 4 5 / 48 6 8 / ? 8 4','','32','32',X,'first = second*third','Easy','REPORTED',notes='"This is from the shift two"'),
q('Z10','YT-6UFT','2025-09-27','puzzle','grid of 2-digit pairs',
  'Top row 35 32 51, bottom row 43 46 61, middle row ? 30 11','','27','27',X,'(digit product of top) + (digit product of bottom)','Hard','REPORTED'),
q('Z11','YT-6UFT','2025-09-27','puzzle','triangular numbers',
  '4 4 10, 5 5 15, 6 6 21, 8 8 36, 9 9 ?','','45','45',X,'n(n+1)/2','Medium','REPORTED',notes='Source: "most repeated and common pattern"'),
q('Z12','YT-6UFT','2025-09-27','puzzle','boxes (products)',
  'Box 1: (2,2)->4, (3,3)->9, (5,4)->20. Box 2: (4,2)->8, (4,3)->12, (?,4)->28','... B: 7','7 (option B)','7',X,'product','Easy','REPORTED'),
q('Z13','YT-6UFT','2025-09-27','puzzle','pair rule (digit products)',
  '(58, 75) -> 5, (96, 38) -> 30, (62, 23) -> ?','','6','6',X,'(a1*a2) - (b1*b2) on digits','Hard','REPORTED'),
q('Z14','YT-6UFT','2025-09-27','puzzle','pair rule (digit sum of sum)',
  '(43, 17) -> 6, (63, 27) -> 9, (44, 56) -> ?','A: 1','1 (option A)','1',X,'digit sum of a+b','Medium','REPORTED',notes='Presenter flagged a misprint in the options'),
q('Z15','YT-KC2G','2024-11-04','puzzle','pair rule (product)',
  '(11, 32) -> 352, (12, 33) -> 396, (13, 34) -> ?','four options by last digit','442','442',X,'a*b','Easy','REPORTED',notes='Exam of 3 Nov 2024 (older cycle)'),
# ---------------- Verbal / English ----------------
q('V01','YT-2MBO','2026-09-22','verbal','spotting errors',
  "Spot the error: The IRC has already expressed / it's concern over the increasingly / draconian nature of legislation in the UK. / No error",
  '3 parts + no error',"part 2 (it's -> its)","part 2: it's -> its",'grammar rule','possessive its vs contraction',
  'Easy','REPORTED',notes='Sentence reconstructed from ASR'),
q('W01','B1','2025-05-12','essay','English writing test',
  'Write an essay on ozone layer depletion.','','n/a','n/a','n/a','timed essay, ~10 min','Medium','REPORTED',notes='First-hand, on-campus SE test of 12 May 2025'),
]

# ---------------- Interview questions (first-hand) ----------------
IV = [
 ('I01','B1','2025-05-12','Define SDLC.'),('I02','B1','2025-05-12','Difference between Waterfall and Agile.'),
 ('I03','B1','2025-05-12','Define OOP and explain its four pillars.'),('I04','B1','2025-05-12','Explain the access specifiers in Java.'),
 ('I05','B2','2025-01-10','How do you handle rejections?'),('I06','B2','2025-01-10','How do you manage time and prioritise tasks?'),
 ('I07','B2','2025-01-10','Explain your final-year project in detail.'),('I08','B2','2025-01-10','Why has your CGPA been declining?'),
 ('I09','B2','2025-01-10','What is the SDLC?'),('I10','B2','2025-01-10','Who is a Scrum Master?'),('I11','B2','2025-01-10','What is sprint planning?'),
 ('I12','B3','2025-12-04','Difference between method overloading and method overriding, with examples.'),
 ('I13','B3','2025-12-04','Explain the SDLC and different SDLC models.'),
 ('I14','B4','2025-01-20','Introduce yourself and say why you want to join Infosys.'),('I15','B4','2025-01-20','What is SDLC and why is it needed?'),
 ('I16','B4','2025-01-20','What are joins and what are their types?'),
 ('I17','B5','2025-01','Explain your capstone project.'),('I18','B5','2025-01','Write a program to check a palindrome.'),
 ('I19','B5','2025-01','Java or Python, and why?'),('I20','B5','2025-01','What do you do beyond academics?'),
 ('I21','B5','2025-01','Are you willing to relocate?'),('I22','B5','2025-01','Why a job rather than higher studies?'),
 ('I23','B5','2025-01','How do you handle stressful situations?'),('I24','B5','2025-01','What is your opinion of generative AI?'),
 ('I25','B5','2025-01','How do you use AI in daily life?'),
]
for qid, src, d, text in IV:
    ROWS.append(q(qid, src, d, 'interview', 'technical' if qid in ('I01','I02','I03','I04','I09','I10','I11','I12','I13','I15','I16','I18','I19') else 'HR/behavioural',
                  text, '', 'n/a', 'n/a', 'n/a', 'interview', 'Easy', 'REPORTED', notes='First-hand candidate account'))

# ---------------- Official Infosys sample paper (Sep 2020): paraphrased gists, answers from data/official_sample.py
import official_sample as OFF
_SEC = {'reasoning': 'reasoning', 'technical': 'quant', 'verbal': 'verbal', 'pseudocode': 'pseudocode', 'puzzle': 'puzzle'}
for _it in OFF.ITEMS:
    ROWS.append(q(_it['qid'], 'OFF-2020', '2020-09-22', _SEC[_it['section']], _it['sub'], _it['gist'], '', 'no key published',
                  _it['answer'], 'official_sample.py (' + _it['how'] + ')', _it['sub'], 'Medium', 'OFFICIAL-SAMPLE',
                  notes='Infosys Ltd sample paper, created Sep 2020. Shows the item style, not that this exact item was asked. Paraphrased; the PDF is not reproduced.'))

# ---------------- Discarded (kept for the audit trail) ----------------
DISC = [
 ('X01','YT-2MBO','interchange-two-numbers equation','operators lost in ASR; cannot re-pose'),
 ('X02','YT-2MBO','histogram DI (pass % at 60% of 50)','chart values never spoken'),
 ('X03','YT-2MBO','DS probability (red/green/blue)','value in statement II not spoken'),
 ('X04','YT-2YHL/YT-U7HK','figure puzzle "5, ?, 68, 73" -> 52','layout unrecoverable'),
 ('X05','YT-5XTG','"100 in between" shift-one puzzle','stub; data inaudible'),
 ('X06','YT-5XTG','shift-two "412 - 39? = 40" puzzle','stated arithmetic (412 - 398 = 14) does not produce 40; transcription defective'),
 ('X07','YT-6UFT','grid 5 3 7 / 2 4 1 / 1 3 ? -> 75','cell layout lost'),
 ('X08','YT-6UFT','3 and 2 -> 11 pattern','presenter never states a working rule'),
 ('X09','YT-6UFT','triangle figure -> 15','stub'),
 ('X10','YT-6UFT','ring 6 15 23 48 / 30 45 41 36','presenter: "if 46 is in the options take 46, otherwise 50" - no determinable rule'),
 ('X11','YT-6UFT','50 16 32 / 49 33 16 / ? grid','presenter calls it a "junk question"; rule incomplete'),
 ('X12','YT-KC2G','series 8705, 263, 11, 951, 15123','digit grouping unrecoverable'),
 ('X13','YT-KC2G','series 28456 ... 777','stub'),
 ('X14','YT-KC2G','quiz series 5821, 55117','stub'),
 ('X15','YT-KC2G','quiz question shown on screen','content never spoken'),
 ('X16','YT-U7HK','puzzle "question four"','stub'),
]

HINT = {'X01': 'aptitude-operator', 'X02': 'aptitude-di', 'X03': 'aptitude-ds', 'X04': 'puzzle-pair', 'X05': 'puzzle-pair', 'X06': 'puzzle-pair', 'X07': 'puzzle-grid', 'X08': 'puzzle-pair', 'X09': 'puzzle-pair', 'X10': 'puzzle-pair', 'X11': 'puzzle-grid', 'X12': 'aptitude-series', 'X13': 'aptitude-series', 'X14': 'aptitude-series', 'X15': 'unknown', 'X16': 'puzzle-unknown'}

if __name__ == '__main__':
    with open('questions-observed.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader()
        for r in ROWS: w.writerow(r)
    with open('questions-discarded.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['disc_id', 'source', 'item', 'reason', 'topic_hint'])
        for d in DISC: w.writerow(list(d) + [HINT[d[0]]])
    exam = [r for r in ROWS if r['section'] != 'interview' and r['source'] != 'OFF-2020']
    print(f"{len(ROWS)} rows ({len(exam)} exam incl. {sum(1 for r in exam if r['duplicate_of'])} duplicate sightings, "
          f"{sum(1 for r in ROWS if r['section']=='interview')} interview, {sum(1 for r in ROWS if r['source']=='OFF-2020')} official-sample); {len(DISC)} discarded")
