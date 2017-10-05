from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    hdr_statement = "You've Arrived at the wizard's tower!"
    path = "Would you like to talk to the wizrd! or assualt a stranger(the wizard)!"
    choice1 = "Talk"
    choice2 = "Assault"
    pic = "wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, 
                            choice1=choice1, choice2=choice2, path=path, chose1="talk", chose2="assault", path_pic=pic)


@app.route('/talk')
def talk():
    hdr_statement = "Wow The Wizened Wizard With Word Wizardry"

    path = """Wow The Wizened Wizard With Word Wizardry! Using your incredible skills of forming coherent sentences the 
    wizard obliges your request to offer assistance on your journey. He offers you two options, a treasue amongst his vast 
    collection or the ability to weild mighty magics most mysterious."""

    choice1 = "Riches!"
    choice2 = "Power!"
    pic = "images/wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="riches", chose2="power", path_pic=pic)


# ====================================================================================================================================================================================

@app.route('/riches')
def riches():
    hdr_statement = "A Treasure to Hold Dear"

    path = """Before you are two magnifecent treasures; one, a brillant golden idol with allot of demonic 
    imagery that most likely is worth more than your life the other... a pair of scissors, a item not 
    found in your household due to your parents extreme distrust in your abilities to weild them."""

    choice1 = "Idol"
    choice2 = "Scissors"
    pic = "images/wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="riches", chose2="power", path_pic=pic)


# ===============================================RICHES OPTIONS!===============================================

@app.route('/idol')
def idol():
    hdr_statement = "The Obviously Cursed Idol"

    path = """You were never know for your abilities to distinguish between eldrict cursed objects from objects that 
    are not of the sort but considering a vast wealth outways a utensil made for cutting paper and soft materials it seemed liked 
    the better otption. Oh well you have an eternity to mull over your decisions as a golden statue."""

    choice1 = "Game"
    choice2 = "Over"
    pic = "wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="/", chose2="/", path_pic=pic)

@app.route('/scissors')
def scissors():
    hdr_statement = "A Treasure to Hold Dear"

    path = """observing the idol it seems too heavy too carry and besides most likely those scissors are made of magic or something. 
    content with your decision you snatched up the scissors and zipped out the front door. Sadly your moment of rebelious triumph was 
    short lived as you stumble on the door mat. As you see the blades aproach closer to your face you cant help but hear the voice or 
    your parents say 'I told you so'"""

    choice1 = "Game"
    choice2 = "Over"
    pic = "wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="/", chose2="/", path_pic=pic)

# ============================================================================================================================================================================================

@app.route('/power')
def power():
    hdr_statement = "Abra cad abra"

    path = "You step before him and kneel and a sinister thought comes up, 'will you act upon it or be still?'"

    choice1 = "Steal the staff!"
    choice2 = "Stay still!"
    pic = "wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="steal", chose2="stay", path_pic=pic)


# ===============================================Power OPTIONS!===============================================

@app.route('/steal')
def steal():
    hdr_statement = "The Obviously Cursed Idol"

    path = """As the wizard aproaches, you snatch his staff from him. his horrified expression 
worsens as voices begin to invade your mind. As if out your control a beam of 
black magic envelops the wizard. all that remains is dust. of well free house."""

    choice1 = "Game"
    choice2 = "Over"
    pic = "wizard.jpg"

    return render_template("path.html", hdr_statement=hdr_statement, choice1=choice1, choice2=choice2, path=path, chose1="/", chose2="/", path_pic=pic)

@app.route('/stay')
def stay():
    hdr_statement = "A Treasure to Hold Dear"

    path = """The wizard rests his hand on your head and in an instant millenia of arcane knowledge floods your mind. after 
    that you arent that up for thinking, or anything for that matter. even so you make a great coat rack. """

    choice1 = "Game"
    choice2 = "Over"
    pic = "wizard.jpg"





# ================================================================================================================================================================================================


@app.route('/assault')
def assault():
    hdr_statement = "Punch First Talk Later"
    path = "Will you punch his face or his 'staff'?"
    choice1 = "Face"
    choice2 = "'Staff'"
    pic = "images/wizard.jpg"
    return render_template("path.html", hdr_statement=hdr_statement, 
                            choice1=choice1, choice2=choice2, path=path, chose1="face", chose2="'staff'", path_pic=pic)


# ==================================================ASSAULT OPTIONS!==========================================================


@app.route('/face')
def face():
    hdr_statement = "You're under Arrest!! Time to 'face' the charges!"
    path = """as the wizard recoils from the blow he begins to yell at 
            obsenities at you. before long he has called the authorities
            and you are arrested for assualt"""

    choice1 = "Game"
    choice2 = "Over"
    pic = "images/wizard.jpg"
    return render_template("path.html", hdr_statement=hdr_statement, 
                            choice1=choice1, choice2=choice2, path=path,  chose1="/", chose2="/", path_pic=pic)


@app.route("/'staff'")
def staff():
    hdr_statement = "Jeweled jewels"
    path = """A thunderous blow is delivered upon the wizard as as an audible
            thud is heard as he recoils on the floor. As the authorities arrive
            to arrest you the glint of a dark jewel that seems to resonate dark 
            power wobbles on the floor. The wizard is then arrested in your stead
            for holding world ending magics and failure to file his taxes. you 
            on the other hand earn favor in the kingdom for stopping this threat."""


    choice1 = "Game"
    choice2 = "Over"
    pic = "wizard.jpg"
    return render_template("path.html", hdr_statement=hdr_statement, 
                            choice1=choice1, choice2=choice2, path=path,  chose1="/", chose2="/", path_pic=pic)






app.run(debug=True)

