# CLOCK = #clock pin
import time
POUR_RATE = 50
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# liquid 1
# pwm1 = GPIO.PWM(11,50)

# # liquid 2
# pwm2 = GPIO.PWM(11,50)

# # liquid 3
# pwm3 = GPIO.PWM(11,50)

pwm4 = GPIO.PWM(11,50)

pwm5 = GPIO.PWM(13,50)

pwm6 = GPIO.PWM(15,50)

import time

CLOSE = 'thing'
OPEN = 'thing'
# C1_DISPENSE = 11
# C2_DISPENSE = #c2 pin
# C3_DISPENSE = #c3 pin
# C1_POUR = #c1 open top pin 
# C2_POUR = #c2 open top pin
# C3_POUR = #c3 open top pin


class Bartender:
    """Creates a Bartender machine that can mix up to 4 drinks"""

    def __init__(self):
      """New Bartender with drinks"""
      #Drinks as keys, amounts as the values
      #size in ml
      #dispensing rate per second
      self.size = 250
      #CONSTANT TO BE INPUT LATER TODO
      self.container_amount = {}
      self.container_assignments = {}
    
    def change_size(self, new_size: int) -> None:
      """Changes the size of the cup to new_size"""
      self.size = new_size
    
    def add_liquid(self, liquid: str, container: str, amount: int) -> None:
      """set <container> to contain <drink> """
      #TODO: insert code that opens the liquid holder to allow drink to be poured in 
      
      # if container == 'c1':
      #   pwm1.start(8)
      #   time.sleep(2)
      #   pwm1.ChangeDutyCycle(3)

      # elif container == 'c2':
      #   pwm2.start(8)
      #   time.sleep(2)
      #   pwm2.ChangeDutyCycle(3)

      # elif container == 'c3':
      #   pwm3.start(8)
      #   time.sleep(2)
      #   pwm3.ChangeDutyCycle(3)

      self.container_assignments[liquid] = container
      self.container_amount[container] = amount

    def create_drink(self, info: dict) -> None:
        """creates a drink using the drinks in list and the amount of each in list"""
        current_info = info
        while (self.size != 4):
          current_info = input("overflow, please reduce amount to" + str(self.size) + "or invalid input") 
        
        # while enough is False
        # for liquid in current_info:
        #   container = self.container_assignments 
        #   enough = check_container(container, current_info[liquid])
        #   if enough if False:
        #     current_info = input("overflow, please reduce amount to" + str(self.size) + "or invalid input")

        for liquid in current_info:
          container = self.container_assignments[liquid] 
          self.dispense(container, current_info[liquid])

    
    def check_overflow(self, info: dict) -> bool:
      s = 0
      for drink in info:
        s += info[drink]
      if s > self.size:
        return True
      else:
        return False
            
    def dispense(self, container: str, amount: int) -> None:
        """dispenses <amount> ml of drink in container <container>"""
        self.container_amount[container] -= amount
        #TODO add connection to the things that actually dispense the drink

        pouring = amount/POUR_RATE
        if container == 'c1':
          pwm4.start(8)
          time.sleep(pouring)
          pwm4.ChangeDutyCycle(8)
          pwm4.ChangeDutyCycle(3)
          print("dispensed " + str(amount) + "ml")

        elif container == 'c2':
          pwm5.start(8)
          time.sleep(pouring)
          pwm5.ChangeDutyCycle(8)
          pwm5.ChangeDutyCycle(3)
          print("dispensed " + str(amount) + "ml")
          #do something with pin

        elif container == 'c3':
          pwm6.start(8)
          time.sleep(pouring)
          pwm6.ChangeDutyCycle(8)
          pwm6.ChangeDutyCycle(3)
          print("dispensed " + str(amount) + "ml")
        

          #do something with pin
        # elif container == 'c4':
        #   GPIO.output(C4_DISPENSE, GPIO.LOW)
        #   time.sleep(pouring)
        #   GPIO.output(C4_DISPENSE, GPIO.HIGH)
        #   print("dispensed" + amount)
          #do something with pin
        
            
    def check_container(self, container: str, amount: int) -> bool:
      """checks if <container> has enough ml to dispense <amount> return bool"""
      if self.container_amount[container] >= amount:
        return True
      return False

if __name__ == '__main__':
  new_bt = Bartender()
  new_bt.add_liquid("red", 'c1', 500 )
  new_bt.add_liquid("orange", 'c2', 500 )
  new_bt.add_liquid("yellow", 'c3', 500 )
  new_bt.dispense('c1', 100)
  new_bt.dispense('c2', 100)
  new_bt.dispense('c3', 100)
