# icoer_interpreter.py
# Interpretation module for I_TGU output values

def interpret_icoer_value(i_tgu):
    if i_tgu < 0.30:
        return "Incoherent"
    elif i_tgu < 0.60:
        return "Partially coherent"
    else:
        return "Highly coherent"
