import json
import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

with open("secrets/contactMe.json") as file:
    secrets = file.read()

secrets = json.loads(secrets)
email = secrets["email"]
password = secrets["password"]

reciever = "gbppythonapps@gmail.com"
message = """\
Subject: Merhaba!

Esse deserunt do ea nisi mollit cupidatat irure fugiat proident nulla excepteur culpa. Cupidatat nisi officia irure laborum aliqua ex sit ex. Nostrud in duis eu minim nulla occaecat sint nisi esse ipsum culpa tempor voluptate irure. Voluptate occaecat id sunt est ullamco. Irure anim ex voluptate enim magna incididunt. Ad do do cupidatat et commodo laborum. Sit magna aute est in ullamco do eu do cillum magna enim duis amet.

Laborum nulla ea do esse amet excepteur commodo anim fugiat exercitation. Aute id incididunt labore cillum dolore dolor. Incididunt incididunt tempor pariatur Lorem incididunt ea aute eiusmod ipsum id ex. Sint laborum ea proident incididunt Lorem. Ex consequat fugiat mollit Lorem ipsum qui veniam ut. Consectetur nostrud non esse cillum ea proident labore. Non aliqua dolore cupidatat laboris excepteur commodo do et elit eiusmod.

Labore id et irure non laboris consequat minim nulla ea consequat ea Lorem. Et fugiat commodo cupidatat sunt duis anim sint aliquip culpa quis consequat occaecat sit. In aliquip ex aute non fugiat est cillum fugiat est. Irure incididunt aliquip in ullamco qui et sit. Ut ullamco aliquip deserunt minim sunt fugiat nisi velit deserunt Lorem duis laborum. Dolor amet sit excepteur esse proident incididunt consequat.

Labore ad eiusmod commodo sint adipisicing sunt. Nisi non veniam occaecat dolor ut eiusmod dolor ut sint consectetur pariatur. Proident proident aliquip ullamco qui veniam non excepteur. Ad ut commodo fugiat incididunt laboris reprehenderit aliqua reprehenderit eu pariatur dolore labore proident consequat. Magna officia voluptate commodo consequat proident occaecat adipisicing.

In ea deserunt eiusmod commodo exercitation excepteur enim consequat nostrud aute. Laborum irure culpa velit duis in ex. Fugiat consectetur et irure sit sit mollit dolore elit laboris aliqua in sint aliquip.
"""

with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(email, password)
    server.sendmail(email, reciever, message)
