from __future__ import print_function
import os
import os.path
import sys
import tarfile
import tempfile

from PIL import Image

INPUT_FILE = 'jigsaw.tar.gz'
OUTPUT_DIR = 'tiles'
TILES = [
    {
        "letter": "B",
        "images" : [
            "xlADhKoxKpsMqZ8T.png",
            "vKg42YqKbAtklAfL.png",
            "DRRNcetGOzYS8Gug.png",
            "LWAfqjrBGC2G6N7o.png"
        ]
    },
    {
        "letter" : "Z",
        "images" : [
            "mttnp3RIlne4RItk.png",
            "oGfzggWsL7ARVAOg.png",
            "vQsGZLusCAwIUAAh.png",
            "RhifaAOSGgNhigik.png"
        ]
    },
    {
        "letter" : "N",
        "images" : [
            "yVyYUxnX6uPBZVk1.png",
            "9F2KjmzUZWtHfgiQ.png",
            "ElEjd0I5RKY29a1L.png",
            "9GDXoE3J0TKpPfMO.png"
        ]
    },
    {
        "letter" : "P",
        "images" : [
            "b6ssuCOb0I0vBdkP.png",
            "u3h9HR9rzCVYglwd.png",
            "Gukm4PD4gUTIlLsi.png",
            "n3epdBa3mftCg9us.png"
        ]
    },
    {
        "letter" : "E",
        "images" : [
            "YSjOG8OXCAZfikyZ.png",
            "XdyGzOMsAa9kgxmE.png",
            "Tp4qVlrfJQHANOQN.png",
            "MinlcgM6vz96P9Vu.png"
        ]
    },
    {
        "letter" : "Z",
        "images" : [
            "LWwmfVmyIoNEjWgs.png",
            "M9kpyeQy8yMjxjV2.png",
            "5lqXEVyqcPACLdtV.png",
            "brtO76CoVVTUgQCn.png"
        ]
    },
    {
        "letter" : "D",
        "images" : [
            "PpsQGzLUKIKFfS9v.png",
            "8v2CznhtTWRa05Vc.png",
            "xRTnqPDMokZV5glg.png",
            "El3gcIVtlvnF4Mgy.png"
        ]
    },
    {
        "letter" : "E",
        "images" : [
            "Sw0TJk7q5nxfNlcS.png",
            "aCACVtWDckSDjvLl.png",
            "oX9bHfX9e6bQWH23.png",
            "Plh9kcI2PlwC8j1N.png"
        ]
    },
    {
        "letter" : "L",
        "images" : [
            "ZH9eBg7aWY1fyqXA.png",
            "4lqji1JIi0MvFyeo.png",
            "pUodVPSNzyYtYW0F.png",
            "N6Bd1Nw9nOLyibAl.png"
        ]
    },
    {
        "letter" : "G",
        "images" : [
            "T38VK5Jbh1E0mINb.png",
            "MwdElhmjlcNrHREH.png",
            "BhE02qmJNzm6fgik.png",
            "MJd5TTd1591WFlyi.png"
        ]
    },
    {
        "letter" : "V",
        "images" : [
            "b5TEJoC7HGoEMQyw.png",
            "9c24XgquQiSgOEWS.png",
            "43uRmbUFD4LM1XJl.png",
            "o2bEk8SFDdQceGfY.png"
        ]
    },
    {
        "letter" : "E",
        "images" : [
            "PrPRepnP0vWPaLx4.png",
            "vOxMb4XUYxMJGrpC.png",
            "v75dTqAH6z8sRPHR.png",
            "6mRohLBCPVvPz0Zp.png"
        ]
    },
    {
        "letter" : "O",
        "images" : [
            "BHsUlQlwMWf5WEBB.png",
            "sFFYXNxYHv62IMKm.png",
            "sDo0mokoBt5Al48B.png",
            "gqzKqLSnhstAFfqX.png"
        ]
    },
    {
        "letter" : "U",
        "images" : [
            "dscFVNffW4HgZusU.png",
            "adPLGTRWrQIydWuL.png",
            "TghIE3XTdefX6QiS.png",
            "ghNuOUKToT81fwwQ.png"
        ]
    },
    {
        "letter": "I",
        "images" : [
            "MKH1qth6ODNHOHSG.png",
            "9nggdzBwVMV58liR.png",
            "fGG1EyPTGvjKqcUp.png",
            "BQwTyQRBbuAqmYA3.png"
        ]
    },
    {
        "letter" : "L",
        "images" : [
            "gZkkP3GRj7HQcYUh.png",
            "GuHyzlpb5O5k5XJB.png",
            "hlozd36EEu3wgWyo.png",
            "zfi67JdovYackOTO.png"
        ]
    }
]

def assemble(image_dir, outdir):
    for i, tile in enumerate(TILES):
        blank_image = Image.new("RGB", (200, 200))
        images = [os.path.join(image_dir, x) for x in tile['images']]
        # Top left
        blank_image.paste(Image.open(images[0]), (0,0))
        # Top right
        blank_image.paste(Image.open(images[1]), (100,0))
        # Bottom left
        blank_image.paste(Image.open(images[2]), (0,100))
        # Bottom right
        blank_image.paste(Image.open(images[3]), (100,100))
        outfile = os.path.join(outdir, "{0}.png".format(i))
        blank_image.save(outfile)

if not os.path.exists(INPUT_FILE):
    print("[!] ERROR: could not find jigsaw.tar.gz")
    sys.exit(1)

with tempfile.TemporaryDirectory() as tmpdir:
    with tarfile.open(INPUT_FILE, 'r:gz') as tarball:
        print("[*] Extracting tarball to temp dir...")
        tarball.extractall(tmpdir)
        if not os.path.exists(OUTPUT_DIR):
            print("[*] Creating output directory '{0}'...".format(OUTPUT_DIR))
            os.makedirs(OUTPUT_DIR)
        print("[*] Assembling tiles...")
        assemble(tmpdir, OUTPUT_DIR)

print("[*] Done.")
