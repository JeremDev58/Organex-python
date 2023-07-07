import kivy
from cryptography.fernet import Fernet
kivy.require('2.0.0') 

# Mes imports
from assets.input.Input import BaseInput
from assets.inputtime.InputTime import InputTime
from assets.modalcolor.ModalColor import ModalColor
from assets.btnchek.BtnCheck import BtnCheck

from app import Organex
#from service.noti_builder import NotificationBuilder
	
Organex().run()