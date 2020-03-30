

class SinglyLinkedListItem:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next_node = None

    def __repr__(self):
        return '{}'.format(self.data)

    def __str__(self):
        return '{}'.format(self.data)


engine_carriage = SinglyLinkedListItem('Engine Carriage')
first_class_carriage = SinglyLinkedListItem('First Class Carriage')
second_class_carriage = SinglyLinkedListItem('Second Class Carriage')
third_class_carriage = SinglyLinkedListItem('Third Class Carriage')
cargo_carriage = SinglyLinkedListItem('Cargo Carriage')



engine_carriage.next_node = first_class_carriage
first_class_carriage.next_node = second_class_carriage
second_class_carriage.next_node = third_class_carriage
third_class_carriage.next_node = cargo_carriage
cargo_carriage.next_node = None



class DoublyLinkedListItem:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return '{}'.format(self.data)

    def __str__(self):
        return '{}'.format(self.data)


