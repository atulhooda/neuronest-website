"""Generate the therapy pages in services/ from the content below.

Run after editing any service text:  python3 build.py
"""
from html import escape
from pathlib import Path
from urllib.parse import quote

OUT = Path(__file__).parent / "services"

THERAPISTS = {
    "qumail": {
        "name": "Dr. Qumail Shaikh",
        "role": "Speech-language pathologist & audiologist · BASLP, MSc SLP",
        "years": "8 years",
        "img": "dr-qumail-shaikh.png",
        "pos": "50% 18%",
    },
    "poonam": {
        "name": "Dr. Poonam",
        "role": "Physiotherapist",
        "years": "6 years",
        "img": "dr-poonam.png",
        "pos": "50% 15%",
    },
}

PHOTOS = {
    "consultation": "The consultation room at NeuroNest",
    "therapy-gym": "The therapy room with exercise balls, soft blocks and mats",
    "sensory-room": "The therapy room with coloured sensory lights",
    "reception": "NeuroNest reception with the services window",
    "waiting-area": "The waiting area with animal wall decals",
    "entrance": "The NeuroNest entrance corridor",
    "therapy-door": "Therapy room no. 2 at NeuroNest",
}

SERVICES = [
    dict(
        slug="speech-language-therapy", name="Speech & language therapy", group="Speech & swallowing",
        tagline="First words, clearer words, and the confidence to use them.",
        who="Children & adults", lead="qumail", photo="consultation",
        about=[
            "Speech and language therapy helps with how a child understands words, puts them together and says them clearly. It covers late talking, unclear speech, stammering, and difficulty following instructions or joining a conversation.",
            "Sessions are built around play, because children learn language best when they are enjoying themselves. You also go home with simple things to try, since most language is learned between sessions, not in them.",
        ],
        signs=["Very few words by age two", "Speech that others find hard to understand by three or four",
               "Stammering or getting stuck on words", "Difficulty following simple instructions",
               "Pointing or pulling you along instead of using words"],
        session=[("Play with a purpose", "Toys, books and games chosen to target the sounds and words your child is working on."),
                 ("Small steps", "Each session builds on the last, at a pace that keeps your child confident."),
                 ("A quick debrief", "A few minutes with you at the end on what went well and what is next."),
                 ("Practice at home", "Simple activities that fit into everyday routines like meals and bath time.")],
        faqs=[("Should we wait and see if my child catches up?", "Some children do catch up on their own, but many don't. An early assessment does no harm, and if all is well you will know sooner."),
              ("Do you check hearing as well?", "Often, yes. We can test hearing in the clinic, which rules out one of the most common causes of speech delay."),
              ("Do you see adults?", "Yes, for speech and language difficulties after a stroke or brain injury, through adult neuro-communication therapy.")],
        related=["audiological-evaluation", "feeding-therapy", "phonics-group-sessions"],
    ),
    dict(
        slug="swallowing-therapy", name="Swallowing therapy", group="Speech & swallowing",
        tagline="Safer, easier swallowing after cancer treatment or neurological illness.",
        who="Adults & children", lead="qumail", photo="consultation",
        about=[
            "Swallowing difficulty (dysphagia) can follow head and neck cancer treatment, a stroke, brain injury, or conditions such as Parkinson's. It can make eating tiring, cause coughing during meals, and raise the risk of food or drink going into the lungs.",
            "Therapy combines exercises that strengthen and coordinate the swallowing muscles, safer swallowing techniques, and changes to food and drink textures. Where it is suitable, we also use electrical stimulation alongside the exercises to help retrain the muscles.",
        ],
        signs=["Coughing or choking while eating or drinking", "Food feeling stuck in the throat",
               "A wet or gurgly voice after swallowing", "Meals taking much longer than they used to",
               "Unplanned weight loss or repeated chest infections"],
        session=[("Swallowing assessment", "Understanding where in the swallow the difficulty is and how safe eating currently is."),
                 ("Targeted exercises", "Exercises for the lips, tongue and throat to build strength and coordination."),
                 ("Electrical stimulation", "Gentle stimulation of the swallowing muscles, used alongside exercises where appropriate."),
                 ("Safe eating plan", "Guidance on food textures, drink thickness and positions for eating.")],
        faqs=[("Does electrical stimulation hurt?", "Most people describe it as a tingling or tapping feeling. The intensity is adjusted to what is comfortable for you."),
              ("Can therapy start during cancer treatment?", "Often, yes. Starting early can help, and we will fit the timing around your treatment."),
              ("Do you treat children with swallowing difficulties?", "Yes. For babies and young children we usually start with feeding therapy, which covers swallowing too.")],
        related=["feeding-therapy", "voice-therapy", "adult-neuro-communication-therapy"],
    ),
    dict(
        slug="feeding-therapy", name="Feeding therapy", group="Speech & swallowing",
        tagline="Calmer mealtimes and a wider range of foods.",
        who="Children", lead="qumail", photo="reception",
        about=[
            "Feeding therapy helps children who find eating difficult, whether that is because of how their mouth muscles work, sensitivity to textures, or worry around food. It goes beyond ordinary fussy eating: these children often accept very few foods, gag easily, or find every mealtime stressful.",
            "We work step by step, starting from what your child can already manage and building towards new tastes and textures, without pressure.",
        ],
        signs=["Eats a very small range of foods", "Gags, vomits or refuses new textures",
               "Difficulty chewing or moving food around the mouth", "Very long or very stressful mealtimes",
               "Stuck on purées and not moving to lumpy or solid food"],
        session=[("Mouth play", "Games that build chewing, biting and tongue control."),
                 ("New foods, slowly", "Gradual, pressure-free exploration of new tastes and textures."),
                 ("Seating and posture", "A check that your child is positioned well for eating."),
                 ("Mealtime plan", "Practical strategies to make meals at home calmer.")],
        faqs=[("Is my child just a picky eater?", "Many children go through fussy phases. If eating is affecting growth, health or family life, or the list of accepted foods keeps shrinking, it is worth an assessment."),
              ("Will you force my child to eat?", "No. Pressure usually makes feeding harder. Children explore new foods at their own pace."),
              ("Should I be in the session?", "Usually, yes. Most meals happen at home, so you are a big part of the plan.")],
        related=["swallowing-therapy", "sensory-integration", "occupational-therapy"],
    ),
    dict(
        slug="voice-therapy", name="Voice therapy", group="Speech & swallowing",
        tagline="For hoarse, strained or tired voices, in children and adults.",
        who="Children & adults", lead="qumail", photo="consultation",
        about=[
            "Voice therapy helps when a voice is hoarse, breathy, strained, or tires easily. In children it often follows a lot of shouting; in adults it can come from heavy voice use at work, vocal nodules, or neurological conditions.",
            "Therapy teaches healthier ways of using breath and voice, along with habits that let the vocal cords recover. For hoarseness that lasts, we may suggest an ENT check before or alongside therapy.",
        ],
        signs=["Hoarseness lasting more than two or three weeks", "A voice that tires or fades by the end of the day",
               "Pain or strain when speaking", "Frequent voice breaks or a smaller pitch range",
               "A very soft voice, for example with Parkinson's"],
        session=[("Breath and relaxation", "Exercises that release tension in the neck, shoulders and throat."),
                 ("Voice exercises", "Practice for pitch, loudness and voice quality."),
                 ("Vocal care", "Hydration, rest and habits that protect the voice."),
                 ("Real-life practice", "Carrying the new voice into conversation, the classroom or work.")],
        faqs=[("Do I need to see an ENT doctor first?", "For hoarseness that lasts more than a few weeks, an ENT examination is a good idea. We can advise you on this."),
              ("My child shouts a lot. Can that harm the voice?", "Repeated shouting can lead to nodules on the vocal cords. Voice therapy teaches children to be loud without straining."),
              ("Is this useful for teachers and other professionals?", "Yes. People who speak a lot for work are among those who benefit most.")],
        related=["speech-language-therapy", "swallowing-therapy", "adult-neuro-communication-therapy"],
    ),
    dict(
        slug="adult-neuro-communication-therapy", name="Adult neuro-communication therapy", group="Speech & swallowing",
        tagline="Finding words again after a stroke, brain injury or neurological illness.",
        who="Adults", lead="qumail", photo="consultation",
        about=[
            "A stroke, head injury or a condition such as Parkinson's can affect how a person speaks, understands, reads or finds words. These difficulties have names like aphasia, dysarthria and apraxia, but for families they simply mean that conversation has become hard.",
            "Therapy works on the specific skills that have been affected, and on practical ways to communicate in the meantime, so the person can take part in daily life again.",
        ],
        signs=["Difficulty finding the right word", "Slurred or slow speech",
               "Trouble understanding what others say", "Difficulty reading or writing after a stroke or injury",
               "Frustration, or pulling back from conversation"],
        session=[("Full assessment", "Speech, understanding, reading and writing, so we know where to focus."),
                 ("Targeted exercises", "Word-finding, speech clarity and comprehension practice."),
                 ("Communication tools", "Strategies and aids that help while skills recover."),
                 ("Family coaching", "Showing family members how to support conversation at home.")],
        faqs=[("How soon after a stroke should therapy start?", "Usually as soon as the person is medically stable. Early therapy tends to help, but improvement is possible long afterwards too."),
              ("Can family members join sessions?", "Yes, and we encourage it. Family support makes a real difference."),
              ("Do you also help with swallowing after a stroke?", "Yes. Swallowing therapy often runs alongside communication therapy.")],
        related=["swallowing-therapy", "voice-therapy", "speech-language-therapy"],
    ),
    dict(
        slug="audiological-evaluation", name="Audiological evaluation", group="Hearing & learning",
        tagline="A hearing test in the clinic, for children and adults.",
        who="Children & adults", lead="qumail", photo="consultation",
        about=[
            "An audiological evaluation measures how well someone hears across different pitches and volumes. We test with an audiometer in the clinic, including pure tone audiometry: you listen through headphones and respond each time you hear a beep.",
            "For children, hearing is often the first thing to check when speech is delayed. A mild hearing loss can be easy to miss at home but make a big difference to how a child learns words.",
        ],
        signs=["Speech delay or unclear speech", "Not responding when called, or often saying \"what?\"",
               "Turning the TV up loud", "Difficulty following conversation in noisy places",
               "Ringing in the ears, or a sudden change in hearing"],
        session=[("A short history", "Questions about hearing, health and what you have noticed."),
                 ("The hearing test", "Pure tone audiometry with headphones. Quick and painless."),
                 ("Your results", "What the results mean, explained in plain language."),
                 ("Next steps", "Advice on therapy or a hearing aid trial if it is needed.")],
        faqs=[("Does a hearing test hurt?", "No. You simply listen and respond. It is quick and comfortable."),
              ("Can young children be tested?", "Yes. We adapt the test to your child's age and make it feel like a listening game."),
              ("What if a hearing loss is found?", "We explain what it means, and where suitable you can try a hearing aid in the clinic.")],
        related=["hearing-aid-trial-fitting", "speech-language-therapy", "counselling"],
    ),
    dict(
        slug="hearing-aid-trial-fitting", name="Hearing aid trial & fitting", group="Hearing & learning",
        tagline="Try before you decide, then a fit tuned to your hearing.",
        who="Children & adults", lead="qumail", photo="consultation",
        about=[
            "If a hearing test shows a loss that hearing aids can help, you can try one in the clinic before deciding. We look at your type of hearing loss, your daily life and your budget, and explain the options without jargon.",
            "Once you choose, we fit and programme the hearing aid to your test results, then fine-tune it over follow-up visits until it sounds right.",
        ],
        signs=["A hearing test has shown hearing loss", "Struggling to follow conversations, even when people speak clearly",
               "Family say you often miss things", "An existing hearing aid that no longer feels right"],
        session=[("Review your results", "Going through your hearing test so the choice makes sense."),
                 ("Try it on", "A trial of suitable hearing aids in the clinic."),
                 ("Fitting", "Programming the hearing aid to your hearing."),
                 ("Fine-tuning", "Follow-up adjustments and tips for daily care.")],
        faqs=[("Can I try a hearing aid before buying?", "Yes. The trial is there so you can hear the difference first."),
              ("Are hearing aids suitable for children?", "Yes. Children with hearing loss often benefit a great deal, especially for speech and language development."),
              ("How long does it take to get used to one?", "Usually a few weeks. Sounds can seem loud at first, and follow-up adjustments help.")],
        related=["audiological-evaluation", "speech-language-therapy", "counselling"],
    ),
    dict(
        slug="remedial-education", name="Remedial education", group="Hearing & learning",
        tagline="Closing gaps in reading, writing and maths, one step at a time.",
        who="Children", lead=None, photo="entrance",
        about=[
            "Remedial education supports children who are falling behind at school, including those with learning difficulties such as dyslexia, dysgraphia or dyscalculia. Instead of repeating schoolwork, it goes back to the skills a child is missing and builds them up properly.",
            "Lessons move at the child's pace and use multi-sensory methods (seeing, saying, tracing, building) that help learning stick.",
        ],
        signs=["Struggling to read or spell despite real effort", "Reversing letters or numbers beyond the early years",
               "Difficulty with basic maths facts", "Avoiding homework, or calling themselves \"stupid\"",
               "Teachers saying your child is behind"],
        session=[("Skills check", "Finding the specific gaps in reading, writing and maths."),
                 ("Targeted lessons", "Work focused on those gaps, not just the current syllabus."),
                 ("Multi-sensory learning", "Activities that use sight, sound, touch and movement."),
                 ("Progress updates", "Regular, honest updates on how things are going.")],
        faqs=[("Is this the same as tuition?", "No. Tuition usually covers the current syllabus. Remedial education fills in the underlying skills that make the syllabus hard."),
              ("Does my child need a diagnosis?", "No. Any child who is struggling can benefit."),
              ("How long will my child need it?", "It depends on the gaps. We review progress regularly and tell you honestly how things are going.")],
        related=["phonics-group-sessions", "occupational-therapy", "speech-language-therapy"],
    ),
    dict(
        slug="phonics-group-sessions", name="Phonics & group sessions", group="Hearing & learning",
        tagline="Letter sounds, reading and social skills, learned together.",
        who="Children", lead=None, photo="waiting-area",
        about=[
            "Phonics teaches children the sounds that letters make and how to blend them into words: the foundation of reading and spelling. Our sessions use a structured, multi-sensory approach that suits children who are starting to read or finding it hard.",
            "Group sessions also give children a chance to practise turn-taking, listening and talking with other children, which is hard to work on one to one.",
        ],
        signs=["Difficulty recognising letter sounds", "Guessing words instead of sounding them out",
               "Slow progress with early reading", "Finding it hard to play or talk with other children",
               "Shyness or discomfort in group settings"],
        session=[("Sound games", "Songs and games for letter sounds."),
                 ("Blending and splitting", "Putting sounds together into words, and taking words apart."),
                 ("Reading at their level", "Activities matched to where each child is."),
                 ("Group play", "Games that practise turn-taking and conversation.")],
        faqs=[("What age are phonics sessions for?", "Mostly children who are starting to read, though older children who are struggling benefit too."),
              ("Is a group right for my child?", "We assess first. Some children start one to one and join a group when they are ready."),
              ("Does phonics help with speech?", "Often. Phonics and speech therapy support each other, especially for children with unclear speech.")],
        related=["remedial-education", "speech-language-therapy", "behavioural-therapy"],
    ),
    dict(
        slug="counselling", name="Counselling", group="Hearing & learning",
        tagline="Space to talk, for children and the parents who care for them.",
        who="Children & parents", lead=None, photo="reception",
        about=[
            "Counselling supports children dealing with worry, low confidence, changes at home or school, or the emotional side of a developmental condition. It supports parents too: hearing a diagnosis, or fitting therapy into daily life, can be a lot.",
            "Sessions are a calm, private space. For younger children we use play, drawing and stories; for parents, conversation and practical guidance.",
        ],
        signs=["Anxiety, fears or frequent worry", "Low confidence or withdrawing from others",
               "Big changes such as a new school, a move or a family change", "Feeling overwhelmed after a diagnosis",
               "Stress around school, behaviour or therapy"],
        session=[("First conversation", "Understanding what is going on and what you would like to change."),
                 ("Talk or play", "Play, art or conversation, depending on age."),
                 ("Coping skills", "Practical strategies for everyday situations."),
                 ("Support for parents", "Guidance on helping your child between sessions.")],
        faqs=[("Is counselling confidential?", "Yes. What is shared stays private, unless there is a concern about someone's safety."),
              ("Can parents come on their own?", "Yes. Support for parents is part of counselling here."),
              ("How do I know if my child needs it?", "If worry, mood or behaviour is affecting daily life, or your child seems to be struggling with something they can't put into words, it is worth a conversation.")],
        related=["behavioural-therapy", "speech-language-therapy", "remedial-education"],
    ),
    dict(
        slug="physiotherapy", name="Physiotherapy", group="Movement & behaviour",
        tagline="Stronger, steadier movement for growing bodies.",
        who="Children", lead="poonam", photo="therapy-gym",
        about=[
            "Paediatric physiotherapy helps children who are late to reach motor milestones, or who find movement hard because of conditions such as cerebral palsy, developmental delay, low muscle tone or injury. It works on strength, balance, coordination and posture.",
            "Sessions use balls, mats, soft blocks and play, so children practise movements without it feeling like exercise. We also show you activities to keep progress going at home.",
        ],
        signs=["Late sitting, crawling, standing or walking", "Low muscle tone, or very stiff muscles",
               "Frequent falls or clumsiness", "Toe walking or an unusual walking pattern",
               "Difficulty with stairs, running or jumping compared to other children"],
        session=[("Movement assessment", "Strength, balance, posture and how your child moves."),
                 ("Play-based exercise", "Work on mats, balls and soft blocks that feels like play."),
                 ("Balance and coordination", "Activities that build steadiness and control."),
                 ("Home programme", "Simple exercises to do together between sessions.")],
        faqs=[("At what age can physiotherapy start?", "Very early. Babies can start as soon as a concern is noticed."),
              ("Is physiotherapy painful?", "It shouldn't be. Sessions are play-based and adjusted to your child's comfort."),
              ("How is it different from occupational therapy?", "Physiotherapy focuses on big movements like sitting, walking and balance. Occupational therapy focuses on everyday skills like handwriting, dressing and sensory processing.")],
        related=["occupational-therapy", "neurodevelopmental-therapy", "sensory-integration"],
    ),
    dict(
        slug="occupational-therapy", name="Occupational therapy", group="Movement & behaviour",
        tagline="Everyday skills, from holding a pencil to getting dressed.",
        who="Children", lead=None, photo="therapy-gym",
        about=[
            "Occupational therapy (OT) helps children with the everyday things they need to do: play, write, dress, eat, and cope at school. It works on fine motor skills, hand-eye coordination, attention, and how a child processes what they see, hear and feel.",
            "OT often helps children with autism, ADHD or developmental delay, and children who simply find handwriting or coordination hard.",
        ],
        signs=["Difficulty holding a pencil, using scissors or doing buttons", "Messy or very slow handwriting",
               "Trouble sitting still or paying attention", "Strong reactions to noise, touch or textures",
               "Struggling with dressing or eating independently"],
        session=[("Hands at work", "Threading, cutting, drawing and building for fine motor skills."),
                 ("Whole-body play", "Activities for strength and coordination."),
                 ("Sensory regulation", "Activities that help your child feel calm and focused."),
                 ("Real-life goals", "Targets linked to what matters at home and school.")],
        faqs=[("Is OT only for children with a diagnosis?", "No. Many children come for handwriting, coordination or attention difficulties without any diagnosis."),
              ("How is OT different from physiotherapy?", "OT focuses on everyday tasks and fine motor skills. Physiotherapy focuses on bigger movements like walking and balance."),
              ("Can OT help at school?", "Yes. Many goals relate directly to school: handwriting, sitting and attending, and organising tasks.")],
        related=["sensory-integration", "physiotherapy", "remedial-education"],
    ),
    dict(
        slug="neurodevelopmental-therapy", name="Neurodevelopmental therapy", group="Movement & behaviour",
        tagline="Hands-on therapy for children with neurological conditions.",
        who="Children", lead=None, photo="therapy-gym",
        about=[
            "Neurodevelopmental therapy (NDT) is a hands-on approach for children with conditions that affect movement and posture, such as cerebral palsy, developmental delay or brain injury. The therapist guides the child's movements to help them feel and learn more typical patterns.",
            "The aim is practical: better sitting, standing, reaching and walking, so children can take part more fully in play, school and family life.",
        ],
        signs=["A diagnosis of cerebral palsy or another neurological condition", "Stiff, floppy or unusual muscle tone",
               "Difficulty controlling the head, trunk or posture", "Delayed motor milestones",
               "Movements that look effortful or uncoordinated"],
        session=[("Assessment", "Posture, muscle tone and movement quality."),
                 ("Guided movement", "Hands-on handling to guide better movement patterns."),
                 ("Functional practice", "Sitting, standing, reaching and stepping."),
                 ("Handling at home", "Positioning and handling you can use every day.")],
        faqs=[("Who is NDT for?", "Mainly children with neurological conditions that affect movement, such as cerebral palsy."),
              ("How is NDT different from physiotherapy?", "NDT is an approach used within physiotherapy and occupational therapy, with a strong focus on handling and movement quality."),
              ("Can parents learn the techniques?", "Yes. We teach you positioning and handling to use every day.")],
        related=["physiotherapy", "occupational-therapy", "sensory-integration"],
    ),
    dict(
        slug="sensory-integration", name="Sensory integration", group="Movement & behaviour",
        tagline="Helping the brain make sense of touch, sound, movement and light.",
        who="Children", lead=None, photo="sensory-room",
        about=[
            "Some children are over- or under-sensitive to what they feel, hear, see, or how they move. They might cover their ears at everyday sounds, avoid messy play, crave spinning and crashing, or barely notice bumps and scrapes. Sensory integration therapy helps their nervous system process this information more comfortably.",
            "Sessions take place in our therapy room with balls, soft blocks, mats, hoops and adjustable lighting, in a planned way that feels like play.",
        ],
        signs=["Covers ears at ordinary noises", "Avoids certain clothes, textures or messy play",
               "Constantly seeks movement: spinning, jumping, crashing", "Very easily overwhelmed, or very hard to calm",
               "Seems not to notice touch or pain"],
        session=[("Sensory profile", "Understanding how your child responds to different sensations."),
                 ("Planned play", "Movement, touch and light activities in the therapy room."),
                 ("Calm and alert", "Strategies that help your child settle or wake up as needed."),
                 ("Sensory diet", "A set of activities for home and school.")],
        faqs=[("Is sensory processing difficulty the same as autism?", "No. It is common in autistic children, but many children without autism have sensory difficulties too."),
              ("What is a sensory diet?", "A personalised set of activities spread through the day to help your child stay calm and focused."),
              ("Why do you change the lights in the room?", "Lighting is one of the tools we use to add or reduce visual input, depending on what your child needs.")],
        related=["occupational-therapy", "behavioural-therapy", "physiotherapy"],
    ),
    dict(
        slug="behavioural-therapy", name="Behavioural therapy", group="Movement & behaviour",
        tagline="Understanding behaviour, and teaching skills that replace it.",
        who="Children", lead=None, photo="therapy-door",
        about=[
            "Behavioural therapy helps children with tantrums, aggression, difficulty following routines, or challenges linked to autism and ADHD. It starts by understanding what a behaviour is communicating, then teaches new skills that meet the same need in a better way.",
            "Parents are a big part of it. We share strategies you can use at home, so the same approach carries through the whole day.",
        ],
        signs=["Frequent or intense tantrums", "Hitting, biting or other aggressive behaviour",
               "Difficulty with transitions or changes to routine", "Trouble sitting, waiting or taking turns",
               "Behaviour that is affecting school or family life"],
        session=[("Understanding why", "Observation and a conversation about when behaviours happen."),
                 ("Teaching new skills", "Structured play for waiting, sharing and asking for help."),
                 ("Catching the good", "Positive reinforcement of the behaviour you want to see."),
                 ("A plan for home", "Clear, simple steps you can use every day.")],
        faqs=[("Is this just a phase?", "Some behaviour is part of growing up. If it is frequent, intense or getting in the way of daily life, it is worth talking to us."),
              ("Is behavioural therapy only for autism?", "No. It helps many children, with or without a diagnosis."),
              ("Will I be involved?", "Yes. Parent involvement is one of the biggest factors in progress.")],
        related=["counselling", "occupational-therapy", "sensory-integration"],
    ),
]

BY_SLUG = {s["slug"]: s for s in SERVICES}

NAV = """<header class="nav" id="top">
  <div class="wrap nav__inner">
    <a href="../index.html" class="logo" aria-label="NeuroNest home"><img class="logo__mark" src="../assets/images/logo-emblem.png" alt="">NeuroNest</a>
    <nav class="nav__links" aria-label="Main">
      <a href="index.html" aria-current="page">Therapies</a>
      <a href="../index.html#clinic">The clinic</a>
      <a href="../index.html#visit-steps">First visit</a>
      <a href="../index.html#team">Team</a>
      <a href="../index.html#faq">Questions</a>
    </nav>
    <div class="nav__cta">
      <a class="nav__phone" href="tel:+918180095783">+91 81800 95783</a>
      <a class="btn btn--dark btn--sm" href="../index.html#book">Book a visit</a>
      <button class="nav__burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span></button>
    </div>
  </div>
  <nav class="nav__mobile" aria-label="Mobile">
    <a href="index.html">Therapies</a>
    <a href="../index.html#clinic">The clinic</a>
    <a href="../index.html#visit-steps">First visit</a>
    <a href="../index.html#team">Team</a>
    <a href="../index.html#faq">Questions</a>
    <a href="tel:+918180095783" class="mono">+91 81800 95783</a>
  </nav>
</header>"""

FOOTER = """<footer class="footer" id="contact">
  <div class="wrap">
    <p class="footer__mark"><img class="footer__emblem" src="../assets/images/logo-emblem.png" alt="">NeuroNest</p>
    <svg class="footer__squiggle" viewBox="0 0 600 30" aria-hidden="true"><path d="M5 20c60-14 120-14 180-4s140 8 200-4 140-8 210 0"/></svg>
    <div class="footer__grid">
      <div class="footer__brand"><img class="footer__logo" src="../assets/images/logo-full.jpg" alt="NeuroNest Pediatric Rehabilitation Centre logo" loading="lazy">
      <p class="footer__tag">Pediatric Rehabilitation Centre.<br>Speech, hearing, movement and learning, under one roof.</p></div>
      <dl class="footer__contact">
        <div><dt class="mono">Visit</dt><dd><a href="https://www.google.com/maps/search/?api=1&query=Vasundhara+Banglow+Behind+Texas+Towers+Zensar+IT+Park+Road+Kharadi+Pune+411014" target="_blank" rel="noopener">Vasundhara Banglow, 3rd Floor,<br>Behind Texas Towers, Zensar IT Park Rd,<br>Kharadi, Pune 411014</a></dd></div>
        <div><dt class="mono">Clinic</dt><dd><a href="tel:+918180095783">+91 81800 95783</a></dd></div>
        <div><dt class="mono">Doctor</dt><dd><a href="tel:+919172707626">+91 91727 07626</a></dd></div>
        <div><dt class="mono">Email</dt><dd><a href="mailto:neuronestprc@gmail.com">neuronestprc@gmail.com</a></dd></div>
      </dl>
      <div class="footer__col">
        <p class="mono">Therapies</p>
{groups}
      </div>
      <div class="footer__col">
        <p class="mono">Families</p>
        <a href="../index.html#visit-steps">First visit</a>
        <a href="../index.html#book">Book a visit</a>
        <a href="../index.html#faq">Questions</a>
        <a href="../index.html#team">Team</a>
      </div>
    </div>
    <p class="footer__legal mono">© <span id="year"></span> NeuroNest Pediatric Rehabilitation Centre</p>
  </div>
</footer>"""


def e(text):
    return escape(text, quote=True)


def page(s):
    name, slug = s["name"], s["slug"]
    photo = s["photo"]
    wa = quote(f"Hello NeuroNest, I would like to know more about {name}.")

    signs = "\n".join(f"            <li>{e(x)}</li>" for x in s["signs"])
    session = "\n".join(
        f"""        <li>
          <span class="mono">0{i}</span>
          <div><h3>{e(t)}</h3><p>{e(d)}</p></div>
        </li>""" for i, (t, d) in enumerate(s["session"], 1))
    faqs = "\n".join(
        f"""        <article class="card qa__item"><h3>{e(q)}</h3><p>{e(a)}</p></article>""" for q, a in s["faqs"])
    related = "\n".join(
        f"""        <a class="card rel" href="{r}.html">
          <span class="mono">{e(BY_SLUG[r]["group"])}</span>
          <h3>{e(BY_SLUG[r]["name"])}</h3>
          <p>{e(BY_SLUG[r]["tagline"])}</p>
          <span class="rel__arrow" aria-hidden="true">→</span>
        </a>""" for r in s["related"])
    about = "\n".join(f"          <p>{e(p)}</p>" for p in s["about"])

    lead = ""
    if s["lead"]:
        t = THERAPISTS[s["lead"]]
        lead = f"""
        <div class="card lead">
          <img src="../assets/images/{t['img']}" alt="{e(t['name'])}" style="object-position:{t['pos']}" loading="lazy">
          <div>
            <p class="mono">Your therapist</p>
            <h3>{e(t['name'])}</h3>
            <p class="person__role">{e(t['role'])}</p>
            <p class="mono lead__years">{e(t['years'])} of experience</p>
          </div>
        </div>"""

    main = f"""  <section class="page-hero">
    <svg class="squiggle sq-1" viewBox="0 0 220 160" aria-hidden="true"><path d="M60 120c-30-20-40-70 10-95 50-25 130-10 135 35 5 45-80 70-130 55-25-8-30-35-20-50"/></svg>
    <div class="wrap page-hero__grid">
      <div>
        <p class="crumbs mono"><a href="../index.html">Home</a> / <a href="index.html">Therapies</a> / <span>{e(name)}</span></p>
        <p class="eyebrow">{e(s['group'])}</p>
        <h1 class="display page-title">{e(name)}</h1>
        <svg class="page-title__line" viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M4 14c50-10 110-12 170-6s90 4 122-4"/></svg>
        <p class="lede">{e(s['tagline'])}</p>
        <dl class="facts">
          <div><dt class="mono">Who it's for</dt><dd>{e(s['who'])}</dd></div>
          <div><dt class="mono">First step</dt><dd>An assessment</dd></div>
          <div><dt class="mono">Where</dt><dd>Kharadi, Pune</dd></div>
        </dl>
        <div class="hero__actions">
          <a class="btn btn--dark" href="../index.html#book">Book an assessment <span aria-hidden="true">→</span></a>
          <a class="btn btn--ghost" href="https://wa.me/918180095783?text={wa}" target="_blank" rel="noopener">Ask on WhatsApp</a>
        </div>
      </div>
      <figure class="card page-photo">
        <img src="../assets/images/clinic-{photo}.jpg" alt="{e(PHOTOS[photo])}">
        <span class="page-photo__sticker">At NeuroNest</span>
      </figure>
    </div>
  </section>

  <section class="section section--tint">
    <div class="wrap about">
      <div>
        <p class="eyebrow">About this therapy</p>
        <h2 class="h2">What it <span class="accent">is.</span></h2>
        <div class="about__text">
{about}
        </div>
      </div>
      <aside class="card signs">
        <p class="mono">Signs it might help</p>
        <ul class="checks">
{signs}
        </ul>
      </aside>
    </div>
  </section>

  <section class="section">
    <div class="wrap kit">
      <div>
        <p class="eyebrow">In a session</p>
        <h2 class="h2">What it <span class="accent">looks</span> like.</h2>
        <p class="section__lede">Every plan is built around the person in front of us, but most sessions include these.</p>{lead}
      </div>
      <ol class="kit__list">
{session}
      </ol>
    </div>
  </section>

  <section class="section section--tint">
    <div class="wrap">
      <p class="eyebrow">Families ask</p>
      <h2 class="h2">Good <span class="accent">questions.</span></h2>
      <div class="qa">
{faqs}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="eyebrow">Under the same roof</p>
      <h2 class="h2">Works well <span class="accent">alongside.</span></h2>
      <div class="related">
{related}
      </div>
      <div class="cta-band">
        <div>
          <h2 class="h2">Not sure this is<br>the right <span class="accent">one?</span></h2>
          <p>Tell us what you have noticed. We will suggest where to start.</p>
        </div>
        <div class="hero__actions">
          <a class="btn btn--sun" href="../index.html#book">Book a visit <span aria-hidden="true">→</span></a>
          <a class="btn btn--ghost" href="tel:+918180095783">Call us</a>
        </div>
      </div>
    </div>
  </section>"""
    return shell(f"{name} in Kharadi, Pune | NeuroNest",
                 f"{s['tagline']} {name} at NeuroNest Pediatric Rehabilitation Centre, Kharadi, Pune.", main)


GROUPS = [
    ("speech", "Speech & swallowing", "First words, clearer words, safe swallowing.", "speech",
     '<path d="M20 40c0-16 18-26 40-26s40 10 40 26-18 26-40 26c-6 0-12-1-17-2L26 72l4-12c-6-5-10-12-10-20z"/><path class="thin" d="M44 40h0M60 40h0M76 40h0"/>'),
    ("hearing", "Hearing & learning", "Hearing checked on site, classroom skills built up.", "hear",
     '<path d="M48 62c0 8 14 10 18 0 4-10 18-16 18-32 0-14-11-22-24-22S36 18 36 30"/><path d="M52 32c0-6 4-10 9-10s9 4 9 10-6 8-8 14"/><path class="thin" d="M92 22c6 6 6 22 0 28M100 14c11 11 11 33 0 44"/>'),
    ("movement", "Movement & behaviour", "Bodies and senses that work together.", "move",
     '<circle cx="60" cy="16" r="8"/><path d="M60 26v24M60 32 40 22M60 32l20-10M60 50 46 72M60 50l14 22"/><path class="thin" d="M18 70h20M84 70h20"/>'),
]


def shell(title, desc, main):
    groups = "\n".join(f'        <a href="index.html#{gid}">{e(gname)}</a>' for gid, gname, *_ in GROUPS)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=DM+Mono:wght@400;500&family=Outfit:wght@300..600&display=swap" rel="stylesheet">
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>

{NAV}

<main>

{main}

</main>

{FOOTER.format(groups=groups)}

<script src="../script.js"></script>
</body>
</html>
"""


def overview():
    sections = []
    for n, (gid, gname, gsub, art, icon) in enumerate(GROUPS):
        items = [s for s in SERVICES if s["group"] == gname]
        cards = "\n".join(
            f"""        <a class="card rel" href="{s['slug']}.html">
          <span class="mono">{e(s['who'])}</span>
          <h3>{e(s['name'])}</h3>
          <p>{e(s['tagline'])}</p>
          <span class="rel__arrow" aria-hidden="true">→</span>
        </a>""" for s in items)
        sections.append(f"""  <section class="section section--group{' section--tint' if n % 2 == 0 else ''}" id="{gid}">
    <div class="wrap">
      <div class="svc-grid">
        <div class="group-card art--{art}">
          <svg class="group-card__icon" viewBox="0 0 120 80" aria-hidden="true">{icon}</svg>
          <div>
            <p class="mono">0{n + 1} · {len(items)} therapies</p>
            <h2>{e(gname)}</h2>
            <p>{e(gsub)}</p>
          </div>
        </div>
{cards}
      </div>
    </div>
  </section>""")
    jump = "\n".join(f'          <a class="chip" href="#{gid}">{e(gname)}</a>' for gid, gname, *_ in GROUPS)

    main = f"""  <section class="page-hero">
    <svg class="squiggle sq-1" viewBox="0 0 220 160" aria-hidden="true"><path d="M60 120c-30-20-40-70 10-95 50-25 130-10 135 35 5 45-80 70-130 55-25-8-30-35-20-50"/></svg>
    <div class="wrap page-hero__grid">
      <div>
        <p class="crumbs mono"><a href="../index.html">Home</a> / <span>Therapies</span></p>
        <p class="eyebrow">Our therapies</p>
        <h1 class="display page-title">Every therapy, one <em class="accent">roof.</em></h1>
        <svg class="page-title__line" viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M4 14c50-10 110-12 170-6s90 4 122-4"/></svg>
        <p class="lede">Children rarely need just one kind of help. Speech, movement, attention and hearing are tangled together, so the people who treat them work in the same building. Pick a therapy to read more.</p>
        <div class="jump">
{jump}
        </div>
      </div>
      <figure class="card page-photo">
        <img src="../assets/images/clinic-therapy-gym.jpg" alt="{e(PHOTOS['therapy-gym'])}">
        <span class="page-photo__sticker">{len(SERVICES)} therapies</span>
      </figure>
    </div>
  </section>

{chr(10).join(sections)}

  <section class="section">
    <div class="wrap">
      <div class="cta-band">
        <div>
          <h2 class="h2">Not sure where<br>to <span class="accent">start?</span></h2>
          <p>You don't need to know which therapy your child needs. Tell us what you have noticed and we'll take it from there.</p>
        </div>
        <div class="hero__actions">
          <a class="btn btn--sun" href="../index.html#book">Book a visit <span aria-hidden="true">→</span></a>
          <a class="btn btn--ghost" href="tel:+918180095783">Call us</a>
        </div>
      </div>
    </div>
  </section>"""
    return shell("Therapies in Kharadi, Pune | NeuroNest",
                 "Speech, swallowing, hearing, physiotherapy, occupational therapy and more: all 15 therapies at NeuroNest Pediatric Rehabilitation Centre, Kharadi, Pune.", main)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for s in SERVICES:
        assert all(r in BY_SLUG for r in s["related"]), s["slug"]
        (OUT / f"{s['slug']}.html").write_text(page(s))
    (OUT / "index.html").write_text(overview())
    print(f"Wrote {len(SERVICES)} therapy pages + overview to {OUT}")
