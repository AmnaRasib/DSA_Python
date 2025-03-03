# Implement a queue system where patients are treated in order.
class patientNode:
    def __init__(self,name,ID):
        self.name=name
        self.ID=ID
        self.next=None
class PatientQueue:
    def __init__(self):
        self.head=None
        self.tail=None
    def Adding_Patient(self,name,ID):
        node=patientNode(name,ID)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    def deQueue(self):
        if self.head is None:
            print("No Patient in the queue.")
            return
        treated_patient=self.head
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        print("Treated Patient: ",treated_patient.name)
        return treated_patient.name
    def display_Queue(self):
        current=self.head
        if self.head is None:
            print("Empty Queue")
            return
        while current:
            print(f"Patient Name: {current.name}, ID: {current.ID}")
            current=current.next
p=PatientQueue()
p.Adding_Patient("Ali","01")
p.Adding_Patient("Alice","02")
p.Adding_Patient("Bob","03")
p.display_Queue()
p.deQueue()
p.deQueue()
p.display_Queue()
