# emotion_responses.py
import random
import streamlit as st
GAP = "<div style='margin-top:9px;'></div>"

emotion_responses = {
    "high_risk": [
        f"You’re having a hard moment, aren’t you?{GAP}It’s okay to let it out.{GAP}What’s been making things tough?",
        f"Feels like you’re stuck in a rough spot.{GAP}You don’t have to deal with this alone.{GAP}Want to share what’s up?",
        f"It’s okay if you’re feeling low.{GAP}I’m here to listen, no pressure.{GAP}What’s been on your mind today?",
        f"Sounds like things are really challenging.{GAP}You’re not alone in this.{GAP}What’s been weighing you down?",
        f"You might be feeling overwhelmed.{GAP}Take it slow, I’m here for you.{GAP}What’s been the hardest part lately?",
        f"Seems like you’re carrying a lot.{GAP}It’s okay to ask for support.{GAP}What’s been feeling heavy for you?",
        f"It’s tough when you’re in this place.{GAP}You’re doing your best, and that matters.{GAP}Want to talk about what’s going on?",
        f"You’re dealing with some heavy stuff.{GAP}Let’s take it one step at a time.{GAP}What’s been tough to handle?",
        f"Feels like you’re in a hard place right now.{GAP}You don’t need to hide it.{GAP}What’s been bothering you?",
        f"It’s okay to feel this way sometimes.{GAP}I’m here to help you through it.{GAP}What’s been making things hard?",
        f"You’re going through something rough.{GAP}You’re stronger than you might think.{GAP}Want to share what’s been tough?",
        f"Sounds like you’re feeling pretty down.{GAP}It’s okay to lean on someone.{GAP}What’s been on your plate lately?",
        f"It’s hard when things feel this intense.{GAP}I’m here, ready to listen.{GAP}What’s been the toughest part for you?",
        f"You might be in a tough spot.{GAP}You don’t have to go it alone.{GAP}What’s been challenging you lately?",
        f"Seems like things are piling up.{GAP}It’s okay to take a break and talk.{GAP}What’s been feeling overwhelming?",
        f"You’re handling a lot right now.{GAP}It’s okay to feel this way.{GAP}What’s been the hardest thing to deal with?",
        f"It’s rough when you’re feeling like this.{GAP}I’m here to support you.{GAP}Want to tell me what’s been going on?",
        f"You’re in a difficult moment.{GAP}You don’t need to face it by yourself.{GAP}What’s been tough for you today?",
        f"Sounds like you’re struggling a bit.{GAP}It’s okay to open up.{GAP}What’s been making things feel heavy?",
        f"Feels like you’re carrying a big load.{GAP}I’m here to help lighten it.{GAP}What’s been the toughest part?"
    ],
    "moderate_risk": [
        f"Something’s got you feeling off, huh?{GAP}It’s okay to take a moment.{GAP}What’s been bugging you today?",
        f"You seem a bit uneasy right now.{GAP}A quick breather might help.{GAP}Want to share what’s up?",
        f"It’s normal to feel unsettled sometimes.{GAP}You don’t have to push through it.{GAP}What’s been on your mind?",
        f"Sounds like something’s throwing you off.{GAP}Let’s chat about it, no rush.{GAP}What’s been feeling weird?",
        f"You might be feeling a bit out of sorts.{GAP}It’s okay to slow down.{GAP}What’s been bothering you lately?",
        f"Feels like something’s not quite right.{GAP}A little break could do wonders.{GAP}Want to talk about what’s going on?",
        f"It’s okay if you’re feeling off-balance.{GAP}You’re not alone in this.{GAP}What’s been making you feel uneasy?",
        f"You seem like something’s bugging you.{GAP}Let’s take it easy and talk.{GAP}What’s been tough today?",
        f"Something’s got you feeling uneasy, right?{GAP}It’s okay to take your time.{GAP}What’s been on your mind lately?",
        f"Sounds like you’re not feeling your best.{GAP}A quick chat might help.{GAP}What’s been feeling off for you?",
        f"It’s normal to have an off day.{GAP}Maybe try something small to reset.{GAP}Want to share what’s been bugging you?",
        f"You might be feeling a bit down.{GAP}It’s okay to just be where you are.{GAP}What’s been throwing you off?",
        f"Feels like something’s bothering you.{GAP}You don’t have to figure it out alone.{GAP}What’s been tough lately?",
        f"You seem a bit out of place today.{GAP}It’s okay to take a step back.{GAP}What’s been feeling uneasy?",
        f"Something’s not sitting well, huh?{GAP}Let’s sort through it together.{GAP}What’s been on your mind?",
        f"It’s okay if things feel a bit rough.{GAP}A moment to yourself might help.{GAP}Want to talk about what’s up?",
        f"You might be feeling a bit uneasy.{GAP}It’s normal to feel this way sometimes.{GAP}What’s been bothering you?",
        f"Sounds like something’s got you off-kilter.{GAP}You don’t need to rush it.{GAP}What’s been feeling weird today?",
        f"Feels like you’re not quite yourself.{GAP}It’s okay to take it slow.{GAP}What’s been making things feel off?",
        f"You seem to be feeling a bit tense.{GAP}Let’s talk about what’s going on.{GAP}What’s been bugging you lately?"
    ],
    "neutral": [
        f"You seem pretty calm today.{GAP}It’s nice to have a steady moment.{GAP}Want to share what’s been up?",
        f"Things feel pretty even right now.{GAP}It’s okay to just chill for a bit.{GAP}What’s been going on with you?",
        f"You’re in a relaxed spot today.{GAP}These moments can be really nice.{GAP}Anything you want to talk about?",
        f"Sounds like things are steady for you.{GAP}It’s cool to take it easy.{GAP}What’s been happening lately?",
        f"You’re doing okay, right?{GAP}No need to feel any certain way.{GAP}Want to tell me what’s up?",
        f"Feels like a calm day for you.{GAP}It’s nice to have some quiet time.{GAP}What’s on your mind today?",
        f"You seem to be in a good place.{GAP}It’s okay to enjoy the calm.{GAP}What’s been going on lately?",
        f"Things feel pretty balanced today.{GAP}It’s cool to just be in the moment.{GAP}Anything you’d like to share?",
        f"You’re in a chill mood, huh?{GAP}Sometimes that’s just what you need.{GAP}What’s been up with you?",
        f"Sounds like you’re feeling alright.{GAP}It’s nice to have a breather.{GAP}Want to talk about anything?",
        f"You seem pretty relaxed today.{GAP}No pressure to do anything big.{GAP}What’s been happening?",
        f"Feels like things are going smoothly.{GAP}It’s okay to enjoy the vibe.{GAP}What’s been on your mind?",
        f"You’re in a steady place today.{GAP}It’s nice to have things feel calm.{GAP}Want to share what’s going on?",
        f"Things seem pretty chill right now.{GAP}It’s cool to take it slow.{GAP}What’s been up lately?",
        f"You’re feeling okay, aren’t you?{GAP}It’s nice to just hang out.{GAP}Anything you want to chat about?",
        f"Sounds like you’re in a calm spot.{GAP}These moments are great for a reset.{GAP}What’s been going on?",
        f"You seem to be doing fine.{GAP}It’s okay to keep things low-key.{GAP}Want to tell me what’s up?",
        f"Feels like a relaxed day.{GAP}It’s nice to have some calm in the mix.{GAP}What’s been happening with you?",
        f"You’re in a good spot, huh?{GAP}It’s cool to just go with the flow.{GAP}Anything on your mind?",
        f"Things feel pretty steady today.{GAP}It’s okay to enjoy the quiet.{GAP}Want to share what’s been up?"
    ],
    "low_risk": [
        f"You’re in a great mood today, huh?{GAP}That’s awesome to hear.{GAP}What’s got you so happy?",
        f"Sounds like you’re feeling really good.{GAP}Love hearing that.{GAP}What’s been making you smile?",
        f"You seem super upbeat right now.{GAP}It’s great to see you like this.{GAP}What’s been going so well?",
        f"Feels like you’re in a solid place.{GAP}Keep those good vibes going.{GAP}What’s been lifting your mood?",
        f"You’re sounding pretty happy.{GAP}That’s so cool to hear.{GAP}What’s been sparking that joy?",
        f"Seems like you’re having an awesome day.{GAP}It’s great to feel this way.{GAP}What’s been making you feel good?",
        f"You’re in a nice spot today.{GAP}Love that you’re doing so well.{GAP}What’s been keeping you upbeat?",
        f"Sounds like you’re in a great place.{GAP}It’s awesome to hear you’re happy.{GAP}What’s been making your day bright?",
        f"You seem to be feeling fantastic.{GAP}Keep enjoying that positivity.{GAP}What’s been putting you in such a good mood?",
        f"Feels like you’re on a high note.{GAP}That’s so great to hear.{GAP}What’s been making things awesome?",
        f"You’re sounding really positive today.{GAP}It’s cool to see you in this mood.{GAP}What’s been going well for you?",
        f"Seems like you’re in a happy place.{GAP}Love that for you.{GAP}What’s been sparking this good energy?",
        f"You’re in a great spot, aren’t you?{GAP}It’s awesome to hear that.{GAP}What’s been making you feel so good?",
        f"Sounds like you’re doing really well.{GAP}Keep those good feelings flowing.{GAP}What’s been lifting you up lately?",
        f"You seem to be in a solid mood.{GAP}It’s great to see you happy.{GAP}What’s been making your day awesome?",
        f"Feels like you’re having a great time.{GAP}That’s so cool to hear.{GAP}What’s been keeping you in high spirits?",
        f"You’re sounding super cheerful.{GAP}It’s awesome to feel this way.{GAP}What’s been making you smile today?",
        f"Seems like you’re in a fantastic place.{GAP}Love hearing you’re doing great.{GAP}What’s been sparking that happiness?",
        f"You’re in a happy mood today.{GAP}It’s great to see you like this.{GAP}What’s been going so well for you?",
        f"Sounds like you’re feeling on top of things.{GAP}That’s awesome to hear.{GAP}What’s been keeping you so happy?"
    ]
}






@st.fragment()
def get_emotion_response(emotion_label: str) -> str:#giving replies
    # Map emotion labels to risk categories
    emotion_to_risk = {
        "sadness": "high_risk",
        "fear": "high_risk",
        "anger": "moderate_risk",
        "disgust": "moderate_risk",
        "neutral": "neutral",
        "joy": "low_risk",
        "surprise": "low_risk"  # Optional: can be neutral too
    }

    risk_level = emotion_to_risk.get(emotion_label.lower(), "neutral")
    return random.choice(emotion_responses[risk_level])



@st.fragment()
def get_risk_with_emoji(emotion_label: str) -> str: #giving risk
    emotion_to_risk = {
        "sadness": "High",
        "fear": "High",
        "anger": "High",
        "disgust": "Moderate",
        "neutral": "Neutral",
        "joy": "Low",
        "surprise": "Low"
    }
    return emotion_to_risk.get(emotion_label.lower(), "Neutral")
