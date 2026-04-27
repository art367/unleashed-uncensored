#!/usr/bin/env python3
"""
Patch script: Create UNLEASHED! - Uncensored version
- Restores all original sweary content
- Enhances panic escalation (more dramatic rate/pitch per threshold)
- Updates title throughout
"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ==================== 1. TITLE ====================
content = content.replace('<title>UNLEASHED! 🐕</title>', '<title>UNLEASHED! - Uncensored 🔞🐕</title>')
content = content.replace("'UNLEASHED! 🐕'", "'UNLEASHED! - Uncensored 🔞'")
content = content.replace('"UNLEASHED! 🐕"', '"UNLEASHED! - Uncensored 🔞"')
content = content.replace('UNLEASHED! 🐕</h1>', 'UNLEASHED! - Uncensored 🔞</h1>')
content = content.replace('>UNLEASHED!<', '>UNLEASHED! - Uncensored<')

# ==================== 2. PANIC_LINES — sweary + enhanced escalation ====================
old_panic = re.compile(r'const PANIC_LINES = \[.*?\];', re.DOTALL)
new_panic = '''const PANIC_LINES = [
  { threshold:0,  lines:["{NAME}! Come here!","{NAME}! Come back!","{NAME}! Good dog, come!","{NAME}! Walkies!","{NAME}! Treat! Want a treat?"], rate:0.88, pitch:1.0 },
  { threshold:20, lines:["{NAME}!","{NAME}! Come here!","{NAME}! Bad dog!","{NAME}! No no no!","{NAME}! Come HERE!","{NAME}! Leave it!","{NAME}! DROP IT!","{NAME}! Oh for gods sake!"], rate:1.05, pitch:1.15 },
  { threshold:45, lines:["{NAME}!!","{NAME}!! COME BACK!!","{NAME}!! STOP!!","Somebody grab {NAME}!","Oh for— {NAME}!!","{NAME}! NOT THE BLOODY SQUIRRELS!","LEAVE THE BLOODY DUCKS ALONE {NAME}!!","OH CHRIST {NAME}!","JESUS {NAME}!! COME HERE!!"], rate:1.2, pitch:1.35 },
  { threshold:70, lines:["OH JESUS CHRIST {NAME}!!","{NAME}!! OH GOD!!","{NAME}!! THE DEEEEER!!","OH MY GOD!! {NAME}!!","FENTOOOON!! I mean {NAME}!!","{NAME}!! NOT THE FUCKING DUCKS!!","SOMEBODY STOP THAT DOG!!","{NAME}!! I AM GOING TO KILL YOU!!","{NAME} {NAME} {NAME}!!","OH GOD OH GOD {NAME}!!","WHAT THE FUCK {NAME}!!"], rate:1.45, pitch:1.6 },
  { threshold:88, lines:["FOR FUCKS SAKE {NAME}!!","OH FUCKING HELL {NAME}!!","{NAME}!! BLOODY HELL!!","WHAT THE ACTUAL FUCK!!","{NAME} YOU ABSOLUTE MENACE!!","SOMEONE HELP ME!! {NAME}!!","OH SHIT OH SHIT {NAME}!!","{NAME}!! I SWEAR TO GOD!!"], rate:1.65, pitch:1.8 }
];'''
content = old_panic.sub(new_panic, content, count=1)

# ==================== 3. shoutName() high panic lines ====================
content = content.replace("'Oh FUDGE ' + dogN + '!!'", "'For fucks sake ' + dogN + '!!'")
content = content.replace("'Blooming dog!!'", "'Bloody dog!!'")
content = content.replace("'OH CRIKEY ' + dogN + '!!'", "'OH MY GOD ' + dogN + '!!'")
content = content.replace("dogN + '!! OH BLOOMIN NORA!!'", "dogN + '!! I SWEAR TO GOD!!'")
content = content.replace("'I AM GOING TO BLOOMING LOSE IT!!'", "'I AM GOING TO KILL THAT DOG!!'")

# ==================== 4. Animal shouts ====================
content = content.replace(
    "'OH CRIKEY ' + dogName + ' NOT THE SQUIRRELS!'",
    "'OH GOD ' + dogName + ' NOT THE SQUIRRELS!'"
)
content = content.replace(
    "'NOT THE DUCKS ' + dogName + '!! OH SUGAR!!'",
    "'NOT THE DUCKS ' + dogName + '!! OH GOD!!'"
)
content = content.replace(
    "'OH FLIPPING HECK THE DEER!!'",
    "'OH JESUS CHRIST THE DEER!!'"
)
content = content.replace(
    "'OH CRIKEY ' + dogName + '!! LEAVE THE DEER ALONE!!'",
    "'OH GOD ' + dogName + '!! LEAVE THE DEER ALONE!!'"
)

# ==================== 5. Pond shouts ====================
content = content.replace(
    "'OH SUGAR ' + dogName + '!! NOW YOU SMELL LIKE POND!!'",
    "'OH GOD ' + dogName + '!! NOW YOU SMELL LIKE POND!!'"
)

# ==================== 6. Park keeper caught ====================
content = content.replace(
    "ownerSpeechBubble.text = 'Oh THANK GOODNESS! The keeper got ' + dogName + '!';",
    "ownerSpeechBubble.text = 'Oh thank GOD! The keeper got ' + dogName + '!';"
)

# ==================== 7. Human help shouts ====================
content = content.replace(
    "'OH THANK GOODNESS! GRAB ' + dogName + '!'",
    "'THANK GOD! GRAB ' + dogName + '!'"
)

# ==================== 8. Poo dropped ====================
content = content.replace(
    "ownerSpeechBubble.text = 'OH FOR GOODNESS SAKE ' + dogName + '!!';",
    "ownerSpeechBubble.text = 'OH FOR GODS SAKE ' + dogName + '!!';"
)

# ==================== 9. Wee finished ====================
content = content.replace(
    "'Oh for GOODNESS sake ' + dogName + '!'",
    "'Oh for GODS sake ' + dogName + '!'"
)

# ==================== 10. GoatCounter — point to new property ====================
content = content.replace(
    'https://unleashed-game.goatcounter.com/count',
    'https://unleashed-uncensored.goatcounter.com/count'
)

# ==================== 11. manifest start_url ====================
content = content.replace('"start_url": "/unleashed-game/"', '"start_url": "/unleashed-uncensored/"')
content = content.replace('"scope": "/unleashed-game/"', '"scope": "/unleashed-uncensored/"')

# ==================== 12. App name in manifest ====================
content = content.replace('"name": "UNLEASHED!"', '"name": "UNLEASHED! - Uncensored"')
content = content.replace('"short_name": "UNLEASHED!"', '"short_name": "UNLEASHED 🔞"')

# ==================== 13. Warning overlay — add 18+ badge ====================
# Add a small 18+ badge to the title on the start screen
content = content.replace(
    "drawText('UNLEASHED! 🐕', W/2, H*0.18",
    "drawText('UNLEASHED! 🔞', W/2, H*0.18"
)
content = content.replace(
    '"UNLEASHED! 🐕"',
    '"UNLEASHED! 🔞"'
)

print("✅ Title updated")
print("✅ PANIC_LINES restored with swearing + 5th extreme tier")
print("✅ All event sweary lines restored")
print("✅ GoatCounter URL updated")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n🔞 UNLEASHED! - Uncensored patch complete!")
