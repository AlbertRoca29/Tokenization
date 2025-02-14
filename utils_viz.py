import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.display import display, HTML

def visualize_tokens(tokens):
    """
    Visualize tokenized text with color-coded tokens, ensuring identical tokens have the same color.
    
    Parameters:
        text (str): The original text.
        tokens (list): The list of tokens.
        tokenizer_name (str): Name of the tokenizer (for labeling).
    """
    unique_tokens = list(set(tokens))  # Get unique tokens
    colors = sns.color_palette("Set2", len(unique_tokens))  # Assign colors to unique tokens
    token_color_map = {token: colors[i] for i, token in enumerate(unique_tokens)}  # Map tokens to colors
    
    colored_tokens = [
        f'<span style="background-color:rgba({int(r*255)},{int(g*255)},{int(b*255)},0.6); color:black; padding:3px; border-radius:5px;">{token}</span>' 
        for token, (r, g, b) in [(token, token_color_map[token]) for token in tokens]
    ]
    
    styled_text = " ".join(colored_tokens)
    display(HTML(styled_text))