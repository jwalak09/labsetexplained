# Backward Chaining Algorithm

class BackwardChaining:
    def __init__(self, rules, facts):
        """
        Initialize the Backward Chaining algorithm with a set of rules and facts.

        Parameters:
        rules (list): A list of tuples, where each tuple contains a set of conditions and a result.
        facts (set): A set of known facts.
        """
        self.rules = rules  # Store the rules for later use
        self.facts = facts  # Store the initial facts for later use

    def is_true(self, goal):
        """
        Check if a goal can be derived from the rules and facts.

        Parameters:
        goal (str): The goal to be derived.

        Returns:
        bool: True if the goal can be derived, False otherwise.
        """
        # If the goal is already in the facts, it's true
        if goal in self.facts:
            return True

        # Iterate through each rule
        for conditions, result in self.rules:
            # If the result of the rule matches the goal
            if result == goal:
                # Check if all conditions can be derived
                if all(self.is_true(cond) for cond in conditions):
                    # If all conditions can be derived, add the goal to the facts
                    self.facts.add(goal)
                    return True

        # If no rule can derive the goal, it's false
        return False

# Example usage
rules = [
    (("A",), "B"),  # Rule 1: If A, then B
    (("B",), "C"),  # Rule 2: If B, then C
    (("C",), "D"),  # Rule 3: If C, then D
    (("A", "D"), "E")  # Rule 4: If A and D, then E
]
facts = {"A"}  # Initial fact: A

bc = BackwardChaining(rules, facts)  # Create a Backward Chaining instance
goal = "E"  # Goal to be derived
result = bc.is_true(goal)  # Check if the goal can be derived
print(f"Can we derive {goal}? {result}")  # Print the result