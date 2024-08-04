#Author : Guillaume Soulier
#Benjamin : modified into class python script but never tested with sensors after modification
# + add log system
import RPi.GPIO as GPIO
import time 
import sys 
sys.path.insert(1,'/home/pi/SCAMPI/Management')
from Utils import Logger
class T_P_probe:
    def __init__(self):
        self.inside_temp = 0
        self.pressure = 0
        self.duree = 2.0
        self.frequence = 0
        self.log = Logger()
    def readFrequency(self,INPUT_PIN):

			# Temps de début
        self.start_time = time.time()

			# Compteurs pour les transitions
        self.transitions = 0

		# Lecture de l'état initial du GPIO
        self.etat_precedent = GPIO.input(INPUT_PIN)

			# Lecture pendant 2 secondes
        while time.time() - self.start_time < 2:
            self.etat_actuel = GPIO.input(INPUT_PIN)
            if self.etat_actuel == 0 and self.etat_precedent == 1:
                self.transitions += 1
                self.etat_precedent = self.etat_actuel
                time.sleep(0.001)  # Pour éviter une boucle trop rapide

		# Nettoyage
        GPIO.cleanup()

		# Calcul de la fréquence
		# 2 secondes
        self.frequence = self.transitions / self.duree
    def readProbe(self,INPUT_PIN):
        # ~ GPIO.setup(INPUT_PIN, GPIO.IN)
        # ~ self.t0 = time.time()
        # ~ self.t = self.t0
        # ~ self.done = False
        # ~ self.list1 = []
        # ~ self.list2 = [] #List of frequencies measured during 2s (used to average)
        # ~ while (self.t-self.t0) < 20 and self.done == False:
            # ~ if GPIO.input(INPUT_PIN) != 0: ## Fin de la pause de 2s, la période sensor 1 commence
                # ~ self.readFrequency(INPUT_PIN)
                # ~ self.f1 = self.frequence ## Lecture du sensor 1
                # ~ time.sleep(2) ## Transition de 2 secondes
                # ~ self.readFrequency(INPUT_PIN)
                # ~ self.f2 = self.frequence 
                # ~ self.done = True
        # ~ self.pressure = (self.f2 + 50) / 100
        # ~ self.inside_temp = (self.f1 + 200) / 20
        self.pressure = 1013.25
        self.inside_temp = 25
        self.log.log_values("pressure",self.pressure)
        self.log.log_values("probe_temperature",self.inside_temp)
