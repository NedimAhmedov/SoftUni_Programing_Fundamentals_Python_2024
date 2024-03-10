class Party:
    def __init__(self):
        self.people = []
        while True:
            command = input()
            if command == "End":
                break

            self.people.append(command)
party = Party()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")