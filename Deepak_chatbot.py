class Object:

    def __repr__(self):

        return '<%s>' % getattr(self, '__name__', self.__class__.__name__)



    def is_alive(self):
        return hasattr(self, 'alive') and self.alive

class Agent():

    def __init__(self):

        def program(percept):

            return input('Percept=%s; action? ' % percept)

        self.program = program

        self.alive = True

class TableDrivenAgent(Agent):

    def __init__(self, table):
        Agent.__init__(self)

        percepts = []

        def program(percept):

            percepts.append(percept)

            action = table.get(tuple(percepts))

            return action

        self.program = program

class ReflexVacuumAgent(Agent):
    def __init__(self):

        Agent.__init__(self)

        def program(A):
           
            if A == 'hi':
                return 'Hello, User...\n'

            elif A == 'time':
                  from datetime import datetime
                  now = datetime. now()
                  current_time = now. strftime("%H:%M:%S")
                  return "Current Time =", current_time

            elif A == 'Time':
                  from datetime import datetime
                  now = datetime. now()
                  current_time = now. strftime("%H:%M:%S")
                  return "Current Time =", current_time
                       
            elif A == 'Age':
                return 'I do not have a definite age. How old are you?\n'

            
            elif A == 'age':
                return 'I do not have a definite age. How old are you\n?'

            elif A == 'Name':
                return 'I do not have a name. What is your name?\n'

            elif A == 'name':
                return 'I do not have a name. What is your name?\n'
                                    
           
            elif A == 'Place':
                return 'I was Developed in India\n'
                        
           
            elif A == 'place':
                return 'I was Developed by in India\n'
            
           
            elif A == 'Weather':
                return 'It is Winter\n'


            elif A == 'weather':
                return 'It is Winter\n'

            
            elif A == 'Hi':
                return 'Hello,User...\n'

            elif A == 'Hey':
                return 'Hello,User...\n'

            elif A == 'hey':
                return 'Hello,User...\n'


            elif A =='How are you?':
                return 'i am doing good what about you?\n'
            
            elif A =='how are you?':
                return 'i am doing good what about you?\n'

            
            elif A =='i am Great' :
                return 'nice to hear\n'


            elif A =='I am Great' :
                return 'nice to hear\n'

            elif A =='Pen' :
                return 'Ball\n         Gel\n         Fountain\n'

            elif A =='Book' :
                return 'NCERT\n         ICSE\n         ISC\n'

            elif A =='Copy' :
                return 'A4\n         Rough\n         Small Size\n'
            
            elif A =='Online' :
                return 'Fees\n Form\n Recharge'

            elif A =='Recharge' :
                return 'DTH\n         Mobile Prepaid\n         Mobile Postpaid\n'

            elif A =='payment' :
                return 'Payment\n         Credit Card\n         Debit Card\n         Cash\n         PhonePe\n'

            elif A =='thank you' :
                return 'It\'s my pleasure!!!'
            else:
                  return 'Sorry I do not know that. Ask Something Related'
        self.program = program

def TableDrivenVacuumAgent():
    table = {((A, 'hi'),): 'Hello User...',
             
             ((A, 'Hi'),): 'Hello, User...',

             ((A, 'Hey'),): 'Hello, User...',

             ((A, 'hey'),): 'Hello, User...',

             ((A, 'Age'),): 'I do not have a definite age. How old are you?',

             ((A, 'age'),): 'I do not have a definite age. How old are you?',

             ((A, 'name'),): 'I do not have a name. What is your name?',

             ((A, 'Name'),): 'I do not have a name. What is your name?',

             ((A, 'Place'),): 'I was Developed in India',

             ((A, 'place'),): 'I was Developed in India',

             ((A, 'Weather'),): 'It is Winter',

             ((A, 'weather'),): 'It is Winter',

             ((A, 'how are you?'),): 'i am doing good\ what about you?',

             ((A, 'How are you?'),): 'i am doing good\ what about you?',

             ((A, 'Pen'),): 'Ball\n Gel\n Fountain\n',

             ((A, 'Book'),): 'NCERT\n ICSE\n ISC\n',
             
             ((A, 'Copy'),): 'A4\n Rough\n Small Size\n',

             ((A, 'Online'),): 'Fees\n Form\n Recharge',

             ((A, 'Recharge'),): 'DTH\n Mobile Prepaid\n Mobile Postpaid\n',

             ((A, 'payment'),): 'Payment\n Credit Card\n Debit Card\n Cash\n PhonePe\n',

             ((A, 'thank you'),): 'its my pleasure..',


             }

    return TableDrivenAgent(table)

class Environment():
    def __init__(self,):

        self.objects = []; self.agents = []



    object_classes = [] ## List of classes that can go into environment



    def percept(self, agent):
        action=input('User:')
        return self.execute_action(agent,action)


    def execute_action(self, agent, action):
        print('ChatBot:',agent.program(action))
#A=input('you:')
for i in range (0,1000):
    e=Environment()
    r=ReflexVacuumAgent()
    e.percept(r)
#e.execute_action()
