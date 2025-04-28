import hashlib
import ipywidgets as widgets
from IPython.display import display

def hash_step_by_step(input_string, output_widget, hash_algo):
    input_bytes = input_string.encode('utf-8')
    output_widget.clear_output()
    with output_widget:
        print(f"Step 1: Input string converted to bytes: {input_bytes.hex()}")
    if hash_algo == "SHA-1":
        hash_object = hashlib.sha1()
        hash_name = 'SHA-1'
    else:
        hash_object = hashlib.sha512()
        hash_name = 'SHA-512'
    with output_widget:
        print(f"Step 2: {hash_name} object initialized")
    hash_object.update(input_bytes)
    with output_widget:
        print(f"Step 3: Hash object updated with input bytes. Intermediate {hash_name} hash value: {hash_object.hexdigest()}")
    final_hash = hash_object.hexdigest()
    with output_widget:
        print(f"Step 4: Final {hash_name} hash: {final_hash}")
    return final_hash

input_box = widgets.Text(
    description='Input String:',
    placeholder='Type Something...',
    style={'description_width': 'initial'}
)

compute_button = widgets.Button(
    description='Compute Hashes',
    button_style='primary'
)

output_area = widgets.Output()

hash_algo_dropdown = widgets.Dropdown(
    options=['SHA-1', 'SHA-512'],
    value='SHA-512',
    description='Hash Algorithm:'
)

def on_button_click(b):
    input_string = input_box.value
    selected_hash_algo = hash_algo_dropdown.value
    output_area.clear_output()
    if input_string:
        hash_step_by_step(input_string, output_area, selected_hash_algo)
    else:
        with output_area:
            print("Please enter a valid input string.")

compute_button.on_click(on_button_click)

display(input_box, hash_algo_dropdown, compute_button, output_area)
