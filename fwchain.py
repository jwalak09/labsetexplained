# Forward Chaining Algorithm

class ForwardChaining:
    def __init__(self, rules, facts):
        """
        Initialize the Forward Chaining algorithm with a set of rules and facts.

        Parameters:
        rules (list): A list of tuples, where each tuple contains a set of conditions and a result.
        facts (set): A set of known facts.
        """
        self.rules = rules  # Store the rules for later use
        self.facts = facts  # Store the initial facts for later use

    def run(self):
        """
        Run the Forward Chaining algorithm to derive new facts.

        Returns:
        set: The final set of derived facts.
        """
        new_facts = True  # Flag to indicate if new facts were derived

        # Continue running the algorithm until no new facts are derived
        while new_facts:
            new_facts = False  # Reset the flag for this iteration

            # Iterate through each rule
            for conditions, result in self.rules:
                # Check if all conditions are met (i.e., all conditions are in the facts)
                if all(cond in self.facts for cond in conditions) and result not in self.facts:
                    # If the result is not already in the facts, add it
                    self.facts.add(result)
                    new_facts = True  # Set the flag to indicate a new fact was derived
                    print(f"Derived fact: {result}")  # Print the derived fact

        # Return the final set of derived facts
        return self.facts

# Example usage
rules = [
    (("A",), "B"),  # Rule 1: If A, then B
    (("B",), "C"),  # Rule 2: If B, then C
    (("C",), "D"),  # Rule 3: If C, then D
    (("A", "D"), "E")  # Rule 4: If A and D, then E
]
facts = {"A"}  # Initial fact: A

fc = ForwardChaining(rules, facts)  # Create a Forward Chaining instance
derived_facts = fc.run()  # Run the algorithm to derive new facts
print("Final derived facts:", derived_facts)  # Print the final set of derived facts