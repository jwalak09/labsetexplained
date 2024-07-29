# Training data for the Find-S algorithm
training_data = [
    (['Yes', 'Yes'], 'Dog'),  # Example 1: Yes, Yes -> Dog
    (['Yes', 'No'], 'Cat'),  # Example 2: Yes, No -> Cat
    (['No', 'Yes'], 'Dog'),  # Example 3: No, Yes -> Dog
    (['No', 'No'], 'Cat'),  # Example 4: No, No -> Cat
    (['Yes', 'Yes'], 'Dog')  # Example 5: Yes, Yes -> Dog
]

# Initial hypothesis (all attributes are considered important)
h = ['1', '1']

# Find-S algorithm
for example, label in training_data:
    # If the label is 'Dog', update the hypothesis
    if label == 'Dog':
        for i in range(len(example)):
            # If the current attribute is important (h[i] == '1'), update it with the value of the example
            if h[i] == '1':
                h[i] = example[i]
            # If the current attribute is not important (h[i] != example[i]), mark it as unknown ('?')
            elif h[i] != example[i]:
                h[i] = '?'

# Print the final hypothesis
print("Final hypothesis:", h)