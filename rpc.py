# IMPORTS

from pypresence import Presence
from json import load
from colorama import Fore, init
from os import system
import os
import time
import colorama

# IMPORTS

# Preparation


def cleanconsole():
    os.system("cls")


os.system("title RPC - discord.gg/9qKScMjdPF - Customize your Rich Presence!")

# Preparation

# JSON CONFIG

with open("AniPC.json") as f:
    d = load(f)
    firstline = d["firstline"]
    secondline = d["secondline"]
    largeimage = d["largeimage"]
    imagegirl = d["imagegirl"]
    client_id = d["clientID"]

# JSON CONFIG

# COLORES

# COLORES

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
image = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

colorama.init()

# COLORES

# PRINTS

banner = rf"""{reset}
{lred}  ▄▀▀▀▀█  
{lred}  █    █ {lwhite} █▄░█ {lred} █ {lwhite} █▀█ {lred} █▀▀   {lred}e{lwhite}a{lred}s{lwhite}y {lred}c{lwhite}o{lred}o{lwhite}l{lred} a{lwhite}n{lred}d
{lred}  █▀▀▀▀█ {lwhite} █░▀█ {lred} █ {lwhite} █▀▀ {lred} █▄▄   f{lred}u{lwhite}n{lred}n{lwhite}y{lred} {red}RPC {lred}f{lwhite}o{lred}r {lblue}Discord
"""

status1sv = rf"""
{image}Status of {yellow}RPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}| Setting.
"""

status2sv = rf"""
{image}Status of {yellow}RPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}/ Setting..
"""

status3sv = rf"""
{image}Status of {yellow}RPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}- Setting...
"""

status4sv = rf"""
{image}Status of {yellow}RPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}\ Setting.
"""

completed = rf"""
 {reset}╔═════ {lred}root@RPC {reset}════════════════════════════════════════════════════════════════════════╗
 {reset}║
 {reset}║      {lred}Application Client ID: {reset}{client_id}                                             
 {reset}║      {lred}First Line Test: {reset}{firstline}                                        
 {reset}║      {lred}Second Line Text: {reset}{secondline}                                         
 {reset}║      
 {reset}║
 {reset}║      {lred}This script has been developed by {red}onepunchman2718
 {reset}║      {lred}Can follow in github as {red}github.com/OnePunchMan2718
 {reset}║      {lred}And can join in our community {red}discord.gg/9qKScMjdPF{lred}!
 {reset}║
 {reset}╚════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

# PRINTS
RPC = Presence(client_id)
RPC.connect()

cleanconsole()
print(banner)
time.sleep(2.5)
print(status1sv)
time.sleep(0.5)
cleanconsole()
print(banner)
print(status2sv)
time.sleep(0.5)
cleanconsole()
print(banner)
print(status3sv)
time.sleep(0.5)
cleanconsole()
print(banner)
print(status4sv)
time.sleep(0.5)
cleanconsole()
print(banner)
print(status2sv)
time.sleep(0.5)
cleanconsole()
print(banner)
print(status3sv)
time.sleep(0.5)
print(
    RPC.update(
        details=firstline,
        state=secondline,
        large_image=largeimage,
        small_image=imagegirl,
        large_text="github.com/OnePunchMan2718",
        small_text="discord.gg/9qKScMjdPF",
        start=time.time(),
    )
)  # Set the presence
cleanconsole()
print(banner)
print(completed)


while True:
    time.sleep(15)
